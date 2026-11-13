# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/05-SelfBilledCreditNote.xml`, Git blob `ae986b70b136e1ac8647dd8051159b9d408be29a` (committed)
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

### cotton/05#F1 · Medium · A customs broker as tax representative of a domestic farm purchase
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID` = `IC41585`
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `cac:TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Self Billed Credit Note." A tax representative acts for a party that is not established in the taxing country. Here supplier (the farm) and customer (the ginnery) are both Lisavan and registered in the island companies register, the supply is outside the scope of a general sales tax, and the presumptive tax is withheld by the ginnery itself. Tevaro Customs Brokers appears nowhere else in the flow; in the only other example that names it, it is a customs agent (`sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`). The role has no party to represent, and the first self-billed document of the same season (01-SelfBilledInvoice.xml) has no tax representative.
- Condition: `cac:TaxRepresentativeParty` is present only if a party to the document needs a tax representative in Lisavu, and then names a party whose role in the world is tax representation.
- Options: (a, preferred) drop the tax representative; (b) if the story wants one, make the represented party non-resident and give the representative a tax role in the world.
- Needs decision: yes

### cotton/05#F2 · Medium · The farm as payee of a credit note that is set off
- XPath: `/SelfBilledCreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`
- XPath: `/SelfBilledCreditNote/cac:PaymentTerms/cbc:Note` = `Set off against the payment of the self-billed invoice.`
- Why: `cac:PayeeParty` is "The Party who receives the Payment." A self-billed credit note reduces what the ginnery owes the farm: the amount credited flows from the farm to the ginnery, here by clearing it against the payment of 04-SelfBilledInvoice.xml (06-RemittanceAdvice.xml shows it as a credit line). The farm receives nothing under this credit note, so it is not its payee; if anyone, the ginnery is. The value is the farm as in the self-billed invoice, apparently carried over.
- Condition: The credit note names no payee, or names the party that receives the credited amount.
- Options: (a, preferred) drop `cac:PayeeParty`, since the amount is set off and nothing is paid; (b) name the ginnery.
- Needs decision: no

### cotton/05#F3 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the debtor writing a self-billed credit note for below-grade seed cotton; its contact for this is purchasing or farm payments, as `/SelfBilledCreditNote/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments` shows.
- Condition: The ginnery's contact in this role is seed cotton purchasing or farm payments, or the contact is left out.
- Options: (a, preferred) use a contact for seed cotton purchasing or farm payments; (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/05#F4 · Low · A customer service officer in the sales department of a one-person farm
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: The farm is a sole proprietorship and a micro enterprise, owned and run by one person. A job title `Customer service officer` in a department `Sales` describes a company with a sales organisation; it does not fit the farm, whose contact is called `Farm office`.
- Condition: The farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) drop JobTitle and Department; (b) a job title such as Farmer or Owner.
- Needs decision: no

### cotton/05#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/05#F6 · Low · Party master data the document does not use
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Section 4.8 (presence): the ginnery's customs trader number and the farm's physical location (the fields, with coordinates) are present. A credit for below-grade domestic seed cotton involves neither customs nor the place of the fields; the credit note does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- The cotton fund levy's beneficiary is the Selanu Chamber of Commerce (`IC42133`), as in 04.
- Accounting parties, buyer, seller and signatory agree with 01, 03 and 04; the farm's and the ginnery's full descriptions are identical to those in 01 and 04 (compared block by block).

## Considered and refuted
- Missing originator and beneficiary (04 names the mill in both roles): not a finding of this example — the inconsistency is recorded in the reviews of 03 and 04, where the roles are present.
