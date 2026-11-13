# LLM review: 06-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/06-RemittanceAdvice.xml`, Git blob `e26eebc8bac0997744bbae65cf8d2aa86a65b428` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### cotton/06#F1 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the payer reporting its payment to the farm; the contact for a remittance is its accounts payable side (04-SelfBilledInvoice.xml routes these payments to `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`).
- Condition: The ginnery's contact in this role is farm payments (accounts payable), or the contact is left out.
- Options: (a, preferred) use a contact for farm payments (accounts payable); (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/06#F2 · Low · A customer service officer in the sales department of a one-person farm
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: The farm is a sole proprietorship and a micro enterprise, owned and run by one person. A job title `Customer service officer` in a department `Sales` describes a company with a sales organisation; it does not fit the farm, whose contact is called `Farm office`.
- Condition: The farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) drop JobTitle and Department; (b) a job title such as Farmer or Owner.
- Needs decision: no

### cotton/06#F3 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/06#F4 · Low · Party master data the document does not use
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Section 4.8 (presence): the ginnery's customs trader number and the farm's physical location (the fields, with coordinates) are present. A remittance advice for a domestic payment uses neither, and does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- Payer account `XL31BSEL0020004922263` is named `Selanu Cotton Ginnery Ltd`, the ginnery's registration name, and is the same account the ginnery gives as payee in 16 and 18; the payee account is the farm's account from 01 and 04.
- Accounting customer and supplier are the same parties, with the same full descriptions, as in 04 and 05 (compared block by block).
