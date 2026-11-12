# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/02-Invoice.xml`, Git blob `b2993194ed77fe144060459952d69428ed29f5bc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/02#F1 · High · Excise per-unit amounts do not produce the excise amounts, and the tier range does not match the taxable amount
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TierRange` = `The first 50,000 kWh of the month`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `228840`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- Why: PerUnitAmount is "Where a tax is applied at a certain rate per unit, the rate per unit applied", with BaseUnitMeasure 1 kWh. The first tier is "The first 50,000 kWh of the month"; at 1 XUF per kWh it would be 50000 XUF, not 60000. Both tiers give the same rate (1 XUF/kWh), although the second is called "the industrial rate", so the tiering would be meaningless. The amounts fit a different calculation: the invoice's electricity is 412800 + 18600 = 431400 kWh (lines 1 and 2); 50000 kWh × 1.2 = 60000 and (431400 − 50000) = 381400 kWh × 0.6 = 228840, total 288840. The per-unit amounts are therefore wrong (1.2 and 0.6 would be right), and TaxableAmount ("The net amount to which the tax percent (rate) is applied") repeats the tax amount instead of the base. Nothing in the invoice says that the excise applies to the electricity lines only and not to the gas of line 3, which the arithmetic implies.
- Condition: For each excise tier, PerUnitAmount (in subtotal and category) × the taxed quantity of the tier = TaxAmount; the quantity of the first tier is the one named in TierRange; TaxableAmount is either absent or the net amount the tax is based on, not a copy of the tax amount; it is recognisable which lines the excise is levied on.
- Options: (a, preferred) rates 1.2 and 0.6 XUF/kWh, TaxableAmount left out (the tax is per unit, not a percentage) or set to the line amounts of the taxed quantity, and the taxed quantity made visible (e.g. in TierRange "50,000 kWh of 431,400 kWh of electricity"); (b) if the world's energy tax is meant to be 1 XUF/kWh, recompute the amounts (and then 288840 elsewhere, e.g. 01-UtilityStatement.xml, too).
- Needs decision: no

### utilities/02#F2 · High · Due date contradicts "30 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- Why: The invoice is issued on 2026-04-02 (`/Invoice/cbc:IssueDate` = `2026-04-02`). 30 days net gives 2026-05-02; the due date given is 21 days after issue (and 23 days after the end of the invoice period, 2026-03-31). The settlement period (2026-04-02 to 2026-04-12) does match the 10 days of the discount, so the note is applied for the discount but not for the net term.
- Condition: The due dates and the payment terms note state the same term.
- Options: (a) set the due date to 2026-05-02; (b) change the note to the 21-day term actually used. Preference: (b) if the world's utility terms are shorter than the general "XU-STD" terms (then the terms ID should not be the standard one either), otherwise (a).
- Needs decision: no

### utilities/02#F3 · Medium · Castrano Logistics as OriginatorParty of an order that does not exist
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: InvoiceLine/OriginatorParty is "The Party who originates the Order to which the Invoice is related." There is no order in this flow; the supply runs under Valdara's contract (`/Invoice/cac:PurchaseReference/cbc:ID` = `FE-C-0047120`). Castrano Logistics is the party consuming at the warehouse meter (it is the subscriber and receiver of 03-UtilityStatement.xml), not the originator of an order. The element is used for the consumer of the line.
- Condition: Castrano's role in line 2 is expressed by an element whose definition is the party at whose site the supply is delivered or consumed (e.g. Delivery/DeliveryParty), or by the line's accounting cost alone, not by OriginatorParty.
- Options: (a, preferred) Delivery/DeliveryParty with Castrano Logistics, next to the delivery location already there; (b) leave the party out and keep the cost centre text.
- Needs decision: no

### utilities/02#F4 · Medium · Province in Region
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country, for which UBL has CountrySubentity. The Bayvarran examples of this flow put their states in CountrySubentity. The same value is in Region in 104 examples (`grep -l --include='*.xml' -r '<cbc:Region>Province of'`).
- Condition: Urvanian provinces are given in CountrySubentity, not in Region.
- Options: (a, preferred) CountrySubentity (with a code where a list exists).
- Needs decision: no

### utilities/02#F5 · Low · Reference to a previous invoice line with no purpose in this invoice
- XPath: `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0211`
- XPath: `/Invoice/cac:BillingReference/cac:BillingReferenceLine/cbc:ID` = `2`
- Why: BillingReference is "A reference to a billing document associated with this document." This is a normal commercial invoice (380) for March 2026; nothing in it corrects, settles or continues FE-INV-26-0211 or its line 2 (no note, no amount, no line referring to it). The referenced invoice is not an example of the flow (flow_index: `-> ?`). Without a stated reason the reference is a filler, or a story element that is not told (e.g. a correction of last month's warehouse line).
- Condition: Either the invoice shows what it does with FE-INV-26-0211 line 2 (e.g. a corrected amount or a note), or the reference is absent.
- Options: (a) remove the reference; (b) give it a reason in the story (e.g. a meter correction of February's warehouse line, then with an amount in this invoice). Preference: (a) unless the story needs (b).
- Needs decision: yes

### utilities/02#F6 · Low · Electricity and gas booked as "Raw materials and parts"
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". Electricity and gas are energy costs, not raw materials and parts; the same code and text are used for Valdara's purchases of goods in 12 examples (`grep -l --include='*.xml' -r 'Raw materials and parts'`), and 3100 equals Valdara's ISIC code (`/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`). Line 2 shows that Valdara uses separate cost centres (`/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`).
- Condition: The invoice-level accounting cost is Valdara's energy cost account.
- Options: (a, preferred) an energy cost account; (b) leave it out at document level and give cost centres per line.
- Needs decision: no

### utilities/02#F7 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: A domestic energy invoice uses neither the customs trader number nor the stock-exchange listing of the customer; both look copied from master data. The customer contact is the "Order desk" in Sales, while the invoice concerns energy supply under a contract and is paid by accounts payable. (The ServiceProviderParty Castrano Logistics does have a reason here, since line 2 is its warehouse.)
- Condition: The customer carries only data the invoice uses, and its contact handles energy invoices.
- Options: (a, preferred) drop the customs trader ID and the security listing, and give an accounts-payable or energy contact.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 412800 × 27.3 = 11269440; 18600 × 27.3 = 507780; 61200 × 8.4 = 514080; sum 12291300 = LineExtensionAmount = TaxExclusiveAmount.
- Tax: excise total 60000 + 228840 = 288840; VAT base 12291300 + 288840 = 12580140; × 20 % = 2516028; TaxInclusiveAmount 12291300 + 288840 + 2516028 = 15096168 = PayableAmount; CalculationSequenceNumeric 1 (excise) before 2 (VAT) agrees with VAT on the excise.
- Settlement discount: 2 % of 15096168 = 301923.36, given as 301923; settlement period 2026-04-02 to 2026-04-12 = 10 days.
- Gas conversion (line 3 note): 61200 kWh / 1350 m³ = 45.3 kWh per operating m³; at 4 bar absolute and about 15 °C that is about 5100 Nm³ at about 11.9 kWh/Nm³, at 4 bar gauge about 6400 Nm³ at 9.6 kWh/Nm³; natural gas has about 10–11.5 kWh/Nm³ (own knowledge), so the figure is within a plausible range.
- Lines 1 and 2 agree with 01-UtilityStatement.xml and 03-UtilityStatement.xml (quantities, amounts, prices, meters FE-M-881204 and FE-M-881377, line IDs 1 and 2 as ParentDocumentLineReferenceID).
- 04-RemittanceAdvice.xml refers to this invoice by ID.
- check_ids.py: RF58FEINV260313 (ISO 11649), IBAN-like account XU080351041600000004084431 and ISIN XU0001042501 have correct check digits; BIC-like CREVXUFR uses the user-assigned country code XU and cannot be a real BIC.
- LineCountNumeric 3 = number of lines; PaymentPurposeCode ELEC/GASB are ISO 20022 ExternalPurpose1Code values for electricity and gas bills.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: electricity and gas classified as services, whereas EU VAT law treats them as goods (own knowledge) — refuted because the world's VAT law is fictional and the classification is consistent across all three lines; EU practice does not apply.
- `/Invoice/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID`: seller repeats the accounting supplier — refuted because UBL defines SellerSupplierParty simply as "The seller", without a condition "if different".
- `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID`: category S (standard rate) used for an excise — refuted because UNCL 5305 is a duty, tax or fee category list and S applies to excise as well.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a routine utility payment — refuted, for an amount of about 15 million XUF from a large company a real-time gross settlement payment is plausible.
- `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate`: previous invoice issued on a Sunday (2026-03-01) — refuted, invoices can be issued automatically on any day; not material.

## Outside this review
- 01-UtilityStatement.xml reports the whole excise of this invoice (288840) as the energy tax of one consumption point; belongs to that example's review.
