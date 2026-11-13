# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/01-SelfBilledInvoice.xml`, Git blob `aee01edf4f4e0c209dc01462389e7115dcceae7c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/01#F1 · High · Payment due date contradicts the due date, the terms and the later prepayment record
- XPath: `/SelfBilledInvoice/cbc:DueDate` = `2026-01-13`
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27`
- XPath: `/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `Paid on issue by transfer. …`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-01-13`
- Why: `DueDate` ("The date on which Invoice is due") and the payment terms say the advance is paid on the issue date, and the final self-billed invoice records the prepayment as paid on 2026-01-13. `PaymentMeans/PaymentDueDate` ("The date on which payment is due for this means of payment") puts the payment six weeks later, on 2026-02-27. One payment cannot be due on both dates.
- Condition: `PaymentMeans/PaymentDueDate` is absent or equal to `DueDate`, and both agree with the terms note and with the `PaidDate` in 04.
- Options: (preferred) drop `PaymentMeans/PaymentDueDate` or set it to 2026-01-13, because the note and 04 both say paid on issue; or, if the advance was really due later, change `DueDate`, the note and 04's `PaidDate` together.
- Needs decision: no

### cotton/01#F2 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: in UN/EDIFACT 5305 code `O` is "Services outside scope of tax" (taxes not applicable to the services). The line is seed cotton, a supply of goods, and the same tax category says so with `SupplyTypeCode` `GOODS`. EN 16931 uses `O` for any supply outside the scope of VAT, but the repository's rule of semantic conformance makes the code's own meaning decisive; that practice does not lower the severity. The same code is used for goods in 17 examples of the world (`grep -rl --include='*.xml' 'schemeID="UN/EDIFACT EDED 5305">O<'`).
- Condition: the tax category of the seed-cotton line and its subtotal carries a code whose meaning covers goods outside the scope of tax, or the difference is recorded as a finding of the repository and the example states which meaning it uses.
- Options: (preferred) decide once, for the whole world, how a supply of goods outside any sales tax is coded (another 5305 code such as `Z`/`E` only if the tax story supports it, or a regional list), because the same choice affects 17 examples; or keep `O` and record it as a deliberate EN 16931-style deviation.
- Needs decision: yes

### cotton/01#F3 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxTotal` is "The total amount of a specific type of tax" and `TaxScheme` "The taxation scheme within which this tax category is defined". "No general sales tax" is not a taxation scheme but the absence of one, and the scheme has no `ID`, so a receiver cannot tell which tax the zero total is for. Nine examples of the world use this name (`grep -rl --include='*.xml' '<cbc:Name>No general sales tax</cbc:Name>'`).
- Condition: either the zero tax total names a real tax scheme of Lisavu that the supply is outside of, or the example carries no tax total for a tax that does not exist.
- Options: (preferred) name the Lisavan tax (if any) that the supply falls outside, with its scheme ID; or leave the tax total out, if the world's tax story says Lisavu has no sales tax at all and the billing customization does not require a tax total.
- Needs decision: yes

### cotton/01#F4 · Low · The ginnery's contact in its buying role is its sales desk
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: in this document the ginnery is the accounting customer that buys seed cotton and writes the self-billed invoice. A question about it goes to its purchasing or farm-payments desk (the later self-billed invoice routes it to "Farm payments", `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`), not to the desk that sells lint.
- Condition: the accounting customer's contact is a function that handles seed-cotton purchases or farm payments.
- Options: (preferred) give the ginnery a purchasing / farm-payments contact for its buyer role; or leave the contact out.
- Needs decision: no

### cotton/01#F5 · Low · Address lines repeat the structured address and mix languages
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[2]/cbc:Line` = `Farm track off Plantation Road at kilometre 4, past the cotton fields.`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[3]/cbc:Line` = `North coast`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the four address lines repeat `StreetName`, `Description`, `District` and `CityName` of the same address. `Line` "may be repeated only to provide the same content in multiple natural languages", yet lines 1 and 4 put the Lisavan and English forms in one text without `languageID`. The lines add nothing the structured parts do not already say.
- Condition: the farm's postal address states each part once, and any language-specific rendering carries its `languageID`.
- Options: (preferred) drop the address lines and keep the structured parts; or keep only lines that add information not in the structured parts, one language per `Line` with `languageID`.
- Needs decision: no

### cotton/01#F6 · Low · Expiry date on a commercial-register entry
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)". The registration described is the farm's entry in the island companies register, which normally does not expire. A registration that does expire at year end would rather be the farm registration the later invoice refers to (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AdditionalDocumentReference/cbc:ID` = `XL-FARM-REG-0412`), which is not the company registration.
- Condition: the expiry date belongs to a registration that expires, and that registration is the one described in this `PartyLegalEntity`.
- Options: (preferred) drop the expiry date from the company registration; or, if Lisavan sole proprietorships really register for one year at a time, keep it and make the world's register rules say so.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 4500 kg × 0.226 XLC/kg = 1017.000 XLC = line, line extension, tax-exclusive, tax-inclusive and payable amount; tax amounts 0.000.
- Check digits: RF reference `RF61SCGSBI260191` and account `XL67BSEL0020004817534` pass (`check_ids.py`).
- The final self-billed invoice deducts this advance: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BillingReference/cac:SelfBilledInvoiceDocumentReference/cbc:ID` = `SCG-SBI-26-0191`, with issue date 2026-01-13 and prepaid amount 1017.000 XLC, as the note here says.
- The payee account is the same farm account in 04 and in the remittance advice 06.
- Parties: ginnery and farm are described the same way (identifiers, register, legal form, addresses) as in 03, 04 and 05.

## Considered and refuted
- `/SelfBilledInvoice/cac:PayeeParty`: payee equal to the seller looked redundant — refuted because the UBL definition ("The Party who receives the Payment") has no "if different" condition, and naming the payee avoids implying it by absence (IND6).
- `/SelfBilledInvoice/cbc:InvoiceTypeCode`: prepayment code 386 in a self-billed invoice instead of 389 — refuted: the document is a prepayment, the self-billing is carried by the document type itself, and 04 deducts it as a prepayment.
- `/SelfBilledInvoice/cbc:AccountingCost`: the buyer's cost centre in an invoice — refuted: in self-billing the issuer is the buyer, and the definition does not restrict the code to the supplier.
- `/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID`: refers to no example — refuted: the season agreement is an external contract, not a document of the flow.
- `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a small advance — refuted: plausible for a same-day payment on issue.
