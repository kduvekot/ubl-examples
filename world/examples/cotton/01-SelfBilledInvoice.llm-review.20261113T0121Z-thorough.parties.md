# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

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

### cotton/01#F1 · Low · Payee named although it is the seller itself
- XPath: `/SelfBilledInvoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- Why: `cac:PayeeParty` is "The Party who receives the Payment." It is the farm, which is already the accounting supplier and the seller, and the payee account `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Lisavu Cotton Farm` already says where the money goes. A separate payee role carries information only when someone other than the supplier is paid (a factor, a collecting agent); here it adds a role without a party behind it.
- Condition: `cac:PayeeParty` is present only if a party other than the accounting supplier receives the payment.
- Options: (a, preferred) drop `cac:PayeeParty`; (b) keep it only if the story has a different payee (e.g. a cooperative or a lender).
- Needs decision: no

### cotton/01#F2 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the buyer of seed cotton and the accounting customer of a self-billed prepayment it writes and pays itself; its contact for this is its purchasing or accounts payable side (the self-billed invoice 04-SelfBilledInvoice.xml routes the same farm invoices to `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`).
- Condition: The ginnery's contact in this role is seed cotton purchasing or farm payments, or the contact is left out.
- Options: (a, preferred) use a contact for seed cotton purchasing or farm payments; (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/01#F3 · Low · A customer service officer in the sales department of a one-person farm
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: The farm is a sole proprietorship and a micro enterprise, owned and run by one person. A job title `Customer service officer` in a department `Sales` describes a company with a sales organisation; it does not fit the farm, whose contact is called `Farm office`.
- Condition: The farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) drop JobTitle and Department; (b) a job title such as Farmer or Owner.
- Needs decision: no

### cotton/01#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/01#F5 · Low · Party master data the document does not use
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Section 4.8 (presence): the ginnery's customs trader number and the farm's physical location (the fields, with coordinates and the farm's website as `InformationURI`) are present. A domestic self-billed prepayment between two Lisavan parties involves no customs and no place of delivery, and the farm's postal address already locates it; the self-billed invoice does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- Both parties carry the same register identifiers in `PartyIdentification`, `PartyLegalEntity/cbc:CompanyID`, `SignatoryParty` and `ElectronicAddressID` (`IC42681`, `IC42544`), and the same full descriptions as in 03, 04, 05 and 06 (compared block by block).
- The signatory is the ginnery, which writes the self-billed invoice; buyer and seller repeat the accounting parties, which states the roles explicitly.
- The payee account `XL67BSEL0020004817534` is held at the Bank of Selanu and named after the farm, as in 04 and 06.

## Considered and refuted
- `/SelfBilledInvoice/cac:BuyerCustomerParty` and `/SelfBilledInvoice/cac:SellerSupplierParty`: suspected as duplicates of the accounting parties without a reason — refuted because stating the buyer and seller explicitly is how a self-billed invoice shows that the customer writes it, and nothing may be implied by absence (IND6).
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`: suspected as two languages in one line without languageID — kept out because it is an unstructured rendering of the structured parts in the same address and the Lisavu address format may print both names on one line; recorded for whoever checks the address format.
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`: suspected as an expiry on a permanent company registration — refuted because 04 refers to a farm registration (`XL-FARM-REG-0412`) and a farm registration renewed each season is a plausible reading of a registration with an expiry date.
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Lisavu Cotton Farm`: suspected because a sole proprietorship is usually registered under the owner's name — refuted, a trade name in the register is possible and the world's register is fictional.
