# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
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

### cotton/16#F1 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/16#F2 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the accounting customer of the invoice; a purchasing or accounts payable contact fits the role, the job title and department do not. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/16#F3 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Supplier and seller (the ginnery), customer and buyer (the mill) agree with the order 08 and the remittance 18; the payee account `XL31BSEL0020004922263` is the ginnery's account, the same one it pays from in 06 and that 18 pays into.
- The ginnery's full description, with `en-XL` tags and both renderings of its legal form, is identical to 01; the mill's is identical to 08 and 18 (compared block by block).

## Considered and refuted
- Customs trader numbers of both parties (`/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`): suspected as master data the invoice does not use — refuted, the commercial invoice of an export sale accompanies the export and import declarations, where the trader numbers are used.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`: the seller's sales desk on its sales invoice — fits the role.
