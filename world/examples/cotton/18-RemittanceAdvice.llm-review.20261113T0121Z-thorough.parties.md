# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
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

### cotton/18#F1 · Medium · Language code in `LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/18#F2 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the payer reporting a payment; an accounts payable contact fits the role, the job title and department do not. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/18#F3 · Low · The ginnery's address and legal form are rendered differently than in the other examples
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` (languageID `en-XB`)
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company` (no languageID, no Lisavan rendering)
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Reef Street` (languageID `en-XB`; `en-XL` in 01, 04, 06 and 16)
- Why: In the examples the ginnery sends, its English address parts carry `languageID` `en-XL` and its legal form is given in Lisavan and English (`01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` with `en-XL`; `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`, `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`). Here the same English names are tagged `en-XB` (Bayvarran English), the Lisavan street and city names are kept, but the Lisavan legal form is dropped and the English one has no `languageID`. The names of a Lisavan street and town are Lisavan English whoever sends the document, so the same party is described in two ways in the flow (the same happens in 02, 07, 08, 09, 13, 15 and 18, all sent by Bayvarran parties).
- Condition: The ginnery's address and legal form carry the same renderings and the same `languageID`s in every example of the flow.
- Options: (a, preferred) the renderings and tags of 01-SelfBilledInvoice.xml everywhere, because `languageID` describes the text, not its reader; (b) if the tags are meant to follow the recipient's locale, apply that to every text of the party and record the rule.
- Needs decision: no

### cotton/18#F4 · Low · The remittance line repeats the header parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: The line-level parties are "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line" (and the customer counterpart). They matter when one remittance covers invoices of several suppliers or customers; here the single line pays one invoice between the same two parties as the header, so the line roles add nothing (no fillers, IND5).
- Condition: Line-level accounting parties are present only where they differ from the header parties.
- Options: (a, preferred) drop them from the line; (b) keep them only if the story has the mill pay on behalf of another party.
- Needs decision: no

### cotton/18#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/18#F6 · Low · Party master data the document does not use
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: Section 4.8 (presence): both parties' customs trader numbers are present. A remittance advice reports a payment and does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- Payer account `XB35BLUM38020504608076` is named `Lumeport Textile Mill Ltd`, the mill's registration name; payee account `XL31BSEL0020004922263` is the ginnery's account from 16.
- The parties are the supplier and customer of the invoice paid (16-Invoice.xml); the mill's full description is identical to 08 and 16 (compared block by block).
