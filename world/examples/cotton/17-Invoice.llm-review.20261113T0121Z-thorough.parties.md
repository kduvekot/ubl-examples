# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
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

### cotton/17#F1 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/17#F2 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the accounting customer of a freight invoice; a purchasing or accounts payable contact fits the role, the job title and department do not. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/17#F3 · Low · The forwarder's export operations desk as the contact of its invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- Why: As accounting supplier Bayforth bills the mill for sea freight; the contact a customer needs for an invoice is the forwarder's billing or accounts receivable side, while the export operations desk is the contact for the bookings in 09 and 13.
- Condition: The supplier's contact on the invoice is one for billing questions, or is absent.
- Options: (a, preferred) a billing or accounts receivable contact; (b) drop the contact.
- Needs decision: no

### cotton/17#F4 · Low · Party master data the document does not use
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: Section 4.8 (presence): the carrier Tidewell Ocean Lines is described in full (legal entity with share capital, tax registration, address, contact) inside the delivery of a freight invoice, and the mill carries its customs trader number. The invoice needs only to identify the carrier the freight was booked with, and does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

### cotton/17#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Supplier and seller are Bayforth Forwarding (`20411644`), the forwarder of 08, 09 and 13; customer and buyer the mill, which as FOB buyer pays the sea freight (13: freight collect).
- Payee account `XB40BLUM38020502618225` is named `Bayforth Forwarding Ltd`, its registration name, at the Bank of Lumeport.
- Bayforth's, the mill's and Tidewell's full descriptions are identical to 09/13, 08/16 and 12/13/14 (compared block by block).
