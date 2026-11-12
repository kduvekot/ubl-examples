# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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

### utilities/02#F1 · High · "30 days net" contradicts the due date 21 days after issue
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- Why: The note states a net term of 30 days, which from the issue date 2026-04-02 gives 2026-05-02. The structured due dates (invoice DueDate, PaymentTerms and PaymentMeans PaymentDueDate) are 2026-04-23, 21 days after issue. The discount part agrees (SettlementPeriod 2026-04-02 to 2026-04-12, 10 days). The free text contradicts the structured value next to it.
- Condition: The net term in the note and the due dates give the same date.
- Options: (a) change the note to 21 days net; (b) move the due dates to 2026-05-02. Preferred: whichever matches the term agreed in Ferrano's contract; the other utilities invoices of the flow use 2026-04-23 as well, so (a) keeps the flow aligned.
- Needs decision: no

### utilities/02#F2 · High · Excise per-unit rates do not produce the excise amounts, and both tiers show the same rate
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TierRange` = `The first 50,000 kWh of the month`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TierRange` = `Above 50,000 kWh: the industrial rate`
- Why: PerUnitAmount is "Where a tax is applied at a certain rate per unit, the rate per unit applied", with BaseUnitMeasure 1 kWh. At 1 XUF/kWh the first tier (50000 kWh) gives 50000, not 60000; the amounts imply 60000 / 50000 = 1.2 XUF/kWh. The second tier covers the rest of the electricity, (412800 + 18600) − 50000 = 381400 kWh, and 228840 / 381400 = 0.6 XUF/kWh. The second tier is described as "the industrial rate", i.e. a different rate, but carries the same PerUnitAmount as the first. The values look rounded to whole Ferra (the document's other amounts are whole numbers), which a per-unit rate is not bound to.
- Condition: For each tier, PerUnitAmount × the tier's quantity = the tier's TaxAmount, and the two tiers' rates differ as their TierRange says.
- Options: (a, preferred) PerUnitAmount 1.2 and 0.6 in both TaxSubtotal and TaxCategory.
- Needs decision: no

### utilities/02#F3 · Medium · Excise TaxableAmount holds the tax, not the taxable base
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `228840`
- Why: TaxableAmount is "The net amount to which the tax percent (rate) is applied to calculate the tax amount." In both excise subtotals it equals the TaxAmount, so it is the tax itself, not the net amount of the electricity on which the excise is charged. For a per-unit tax the base is the quantity (BaseUnitMeasure, TierRange); a TaxableAmount, if given, would be the net amount of the electricity in that tier.
- Condition: The excise subtotals' TaxableAmount is the net amount of the supply taxed in that tier, or is absent.
- Options: (a, preferred) leave TaxableAmount out of the per-unit subtotals and let BaseUnitMeasure, PerUnitAmount and TierRange carry the calculation; (b) give the net amount of the electricity of each tier.
- Needs decision: no

### utilities/02#F4 · Medium · OriginatorParty used for the warehouse occupant
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Castrano Logistics warehouse, Ferrano`
- Why: InvoiceLine/OriginatorParty is "The Party who originates the Order to which the Invoice is related." There is no order in this flow; electricity is supplied under Valdara's supply contract FE-C-0047120, and Castrano Logistics is the party at whose warehouse the electricity is consumed (`03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`). The role the line wants to express is the receiver of the supply at that point, for which the line's Delivery (DeliveryParty) exists.
- Condition: Castrano Logistics appears on line 2 in a role whose definition fits (the party to which the electricity is delivered), not as the originator of an order.
- Options: (a, preferred) Delivery/DeliveryParty on line 2; (b) leave it to the line's PurchaseReference and AccountingCost, which already name the warehouse.
- Needs decision: no

### utilities/02#F5 · Low · Billing reference to February's invoice line without a stated purpose
- XPath: `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0211`
- XPath: `/Invoice/cac:BillingReference/cac:BillingReferenceLine/cbc:ID` = `2`
- Why: BillingReference is "A reference to a billing document associated with this document." This March invoice is an ordinary commercial invoice (380) and nothing in it says why February's invoice, line 2, is associated with it; no example of the flow carries FE-INV-26-0211. The likely reason is the February estimate for the warehouse meter that `03-UtilityStatement.xml` corrects ("February's estimate of 17,200 kWh was 750 kWh too high"), but this invoice bills line 2 at 18600 × 27.3 = 507780 without any correction, so the reference is not used either.
- Condition: The reference is there only if the invoice does something with the referenced line (e.g. bills a correction of it), and then the line or a note says so.
- Options: (a) remove the reference; (b) keep it together with a correction line or note that uses it. Which one depends on how the estimate correction of `03-UtilityStatement.xml` is to be settled.
- Needs decision: yes

### utilities/02#F6 · Low · Buyer's accounting cost "Raw materials and parts" for electricity and gas
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCost is the buyer's accounting cost code for the invoice. Electricity and gas for the factory are energy or overhead costs, not raw materials and parts; the code is also Valdara's ISIC class 3100. The same text occurs in 12 examples (counted with `grep -rl --include='*.xml' 'Raw materials and parts' world/examples | wc -l`), Valdara's purchasing default.
- Condition: The header cost centre fits energy for the factory, or is absent.
- Options: (a, preferred) an energy or factory-overhead cost centre.
- Needs decision: no

### utilities/02#F7 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: An energy invoice to Valdara has no use for its listed shares, its logistics service provider, its customs trader number or its sales order desk as contact. They look copied from master data.
- Condition: The customer carries what the invoice uses, and a contact that handles energy invoices.
- Options: (a, preferred) remove them; use an accounts payable contact.
- Needs decision: no

### utilities/02#F8 · Low · Electricity and gas classified as services for VAT
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." (Own knowledge.) In VAT systems modelled on the EU VAT Directive, electricity and gas are treated as goods (Art. 15(1)); the item descriptions sell "Electricity supply, per kilowatt hour" and "Natural gas supply", i.e. the energy itself, with network charges included. Unless Urvanian VAT law says otherwise, the code does not fit.
- Condition: The supply type follows Urvania's VAT treatment of energy supplies, stated in the world's tax story.
- Options: (a) GOODS for the energy lines; (b) keep SERVICES if the world's VAT law treats energy supply as a service, recorded there.
- Needs decision: yes

## Checked and consistent
- Lines: 412800 × 27.3 = 11269440; 18600 × 27.3 = 507780; 61200 × 8.4 = 514080; sum 12291300 = LineExtensionAmount = TaxExclusiveAmount. LineCountNumeric 3.
- Excise total 60000 + 228840 = 288840; VAT base 12291300 + 288840 = 12580140; 20 % = 2516028; TaxInclusiveAmount 12291300 + 288840 + 2516028 = 15096168 = PayableAmount.
- Settlement discount 2 % × 15096168 = 301923.36 → 301923; used by `04-RemittanceAdvice.xml`, which pays on 2026-04-10, within the settlement period ending 2026-04-12.
- Gas conversion (own knowledge): 1350 m³ at 4 bar absolute ≈ 5400 m³ at standard conditions; × about 11.3 kWh/m³ ≈ 61000 kWh, consistent with 61200 kWh.
- Statements `01-UtilityStatement.xml` (line 1) and `03-UtilityStatement.xml` (line 2) match lines 1 and 2 in quantity, price and amount; issued after this invoice.
- PaymentID RF58FEINV260313: check digits OK (check_ids.py); the same reference is used in `04-RemittanceAdvice.xml`.

## Considered and refuted
- `/Invoice/cac:PurchaseReference/cbc:ID`: a supply contract in PurchaseReference rather than a contract document reference — refuted because PurchaseReference names "a subscription number" as an example of its object, and a utility supply contract number is the subscription.
- `/Invoice/cac:BuyerCustomerParty`, `/Invoice/cac:SellerSupplierParty`: repeat the accounting parties — refuted because neither definition ("The buyer.", "The seller.") has an "if different" condition.
- `/Invoice/cac:InvoiceLine[3]/cbc:Note`: gas conversion stated in a note — refuted because no structured element of the line holds the volume and pressure, and the note agrees with the quantity.
- `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID`: category S for an excise — refuted because UNCL 5305 S is "standard rate" without being limited to VAT, and the excise has a standard (tiered) rate.
