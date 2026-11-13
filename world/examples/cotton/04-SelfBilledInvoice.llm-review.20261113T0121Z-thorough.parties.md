# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/04-SelfBilledInvoice.xml`, Git blob `7ff28661ff5e42f702b07e4477e9454c7a6c7ebb` (committed)
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

### cotton/04#F1 · Medium · A customs broker as tax representative of a domestic farm purchase
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID` = `IC41585`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `cac:TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Self Billed Invoice." A tax representative acts for a party that is not established in the taxing country. Here supplier (the farm) and customer (the ginnery) are both Lisavan and registered in the island companies register, the supply is outside the scope of a general sales tax, and the presumptive tax is withheld by the ginnery itself. Tevaro Customs Brokers appears nowhere else in the flow; in the only other example that names it, it is a customs agent (`sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`). The role has no party to represent, and the first self-billed document of the same season (01-SelfBilledInvoice.xml) has no tax representative.
- Condition: `cac:TaxRepresentativeParty` is present only if a party to the document needs a tax representative in Lisavu, and then names a party whose role in the world is tax representation.
- Options: (a, preferred) drop the tax representative; (b) if the story wants one, make the represented party non-resident and give the representative a tax role in the world.
- Needs decision: yes

### cotton/04#F2 · Low · The textile mill as originator and beneficiary of a seed cotton purchase from the farm
- XPath: `/SelfBilledInvoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- XPath: `/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- Why: `cac:OriginatorCustomerParty` is defined here as "The Party who originated the Order to which this Invoice is related." and `cac:BeneficiaryParty` as "A Party for whom the associated transaction is ultimately intended or who derives benefit from it." The transaction is the ginnery's purchase of seed cotton from the farm, called off under the ginnery's own season agreement (an order reference assigned by the buyer, the ginnery). The mill buys lint from the ginnery later and separately (08-Order.xml, `08-Order.xml:/Order/cbc:ID` = `LTM-PO-26-0198`); it neither originated this call-off nor is the seed cotton intended for it, since the ginnery gins and sells the lint on its own account. The originator document `LTM-SEASON-2026` (a mill season agreement) exists in no example, so nothing links the mill to this order. The other documents of the same purchase, 01-SelfBilledInvoice.xml and 05-SelfBilledCreditNote.xml, name no originator or beneficiary, so the flow is not consistent either. A reading in which the mill's season agreement drives the ginnery's purchases is possible, but the documents do not show it.
- Condition: The mill appears as originator or beneficiary of the farm-to-ginnery documents only if the story makes it the party that requested, or the party for whom, the seed cotton is bought, and then in every document of that purchase.
- Options: (a, preferred) drop both roles from the farm-to-ginnery documents; (b) if the mill finances or pre-buys the farm's crop, say so in the story and name it the same way in 01, 03, 04 and 05.
- Needs decision: yes

### cotton/04#F3 · Low · Payee named although it is the seller itself
- XPath: `/SelfBilledInvoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- Why: `cac:PayeeParty` is "The Party who receives the Payment." It is the farm, which is already the accounting supplier and the seller, and the payee account in the payment means already names the farm. A separate payee role carries information only when someone other than the supplier is paid.
- Condition: `cac:PayeeParty` is present only if a party other than the accounting supplier receives the payment.
- Options: (a, preferred) drop `cac:PayeeParty`; (b) keep it only if the story has a different payee.
- Needs decision: no

### cotton/04#F4 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the buyer of seed cotton and the accounting customer of a self-billed invoice it writes and pays; the same document routes it internally to `/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`.
- Condition: The ginnery's contact in this role is seed cotton purchasing or farm payments, or the contact is left out.
- Options: (a, preferred) use a contact for seed cotton purchasing or farm payments; (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/04#F5 · Low · A customer service officer in the sales department of a one-person farm
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: The farm is a sole proprietorship and a micro enterprise, owned and run by one person. A job title `Customer service officer` in a department `Sales` describes a company with a sales organisation; it does not fit the farm, whose contact is called `Farm office`.
- Condition: The farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) drop JobTitle and Department; (b) a job title such as Farmer or Owner.
- Needs decision: no

### cotton/04#F6 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/04#F7 · Low · Party master data the document does not use
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Section 4.8 (presence): the ginnery's customs trader number and the farm's physical location (the fields, with coordinates and the website as `InformationURI`) are present. The purchase is domestic and the delivery place is given in `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`; the self-billed invoice does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- The cotton fund levy's beneficiary is the Selanu Chamber of Commerce (`IC42133`), which the line note names as the fund's holder; a collection line with a beneficiary fits the definition "an item or amount collected on behalf of a third party".
- Accounting parties, buyer, seller and signatory agree with 01, 03 and 05; the full descriptions of farm and ginnery are identical to those in 01 (compared block by block).
- The payee account `XL67BSEL0020004817534` is the same farm account as in 01 and 06.

## Considered and refuted
- `/SelfBilledInvoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu Cotton Ginnery, weighbridge`: suspected as a company name in a location name — refuted, it names a facility (the gin's weighbridge) by its operator, which identifies the place, and the ginnery's address is in the same document.
- `/SelfBilledInvoice/cac:CollectionInvoiceLine/cbc:Note` = `Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.`: suspected as contradicting a document written by the ginnery — refuted, a collection line is the supplier's (the farm's) collection on behalf of a third party, also when the customer writes the invoice.
