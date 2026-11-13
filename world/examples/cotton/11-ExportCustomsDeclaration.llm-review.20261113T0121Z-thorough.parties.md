# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
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

### cotton/11#F1 · Medium · The customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- Why: The Island Customs Service is a public authority (ISIC `8411`, general public administration). `cac:CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `cbc:CompanyLiquidationStatusCode` "the party's liquidation status": a government agency is not registered in a commercial companies register and cannot be in or out of liquidation. The checklist names exactly this case. All 6 example files that give this authority's `RegistrationName` also carry a `CompanyLiquidationStatusCode` (grep over *.xml).
- Condition: The authority's legal entity carries no commercial registration scheme and no liquidation status; if it has an identifier, it is one from a register of public bodies.
- Options: (a, preferred) keep only `RegistrationName` (and an identifier from a register of public bodies, if the world has one); (b) drop `cac:PartyLegalEntity` for the authority altogether.
- Needs decision: no

### cotton/11#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/11#F3 · Low · The customs service's contact for an export declaration is its import office
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Import office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:ElectronicMail` = `import@customs-xl.example`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- Why: The customs party is "The Authority who processes this Customs Declaration", an export declaration whose exit office is the customs office at the port of Selanu; the contact given is the service's import office.
- Condition: The customs party's contact is the office that handles exports (or the exit office at the port of Selanu), or is absent.
- Options: (a, preferred) an export or port office contact; (b) drop the contact.
- Needs decision: no

### cotton/11#F4 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the consignee on an export declaration; a consignee's contact is the one who receives the goods, not purchasing. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/11#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Exporter and consignor are the ginnery (`IC42681`, customs trader `XL-TR-042681`), consignee the mill (customs trader `XB-TR-412603`); both trader numbers have a use in a customs declaration.
- The customs party's address (`Wharf Road 53`, Selanu) lies on the same street as the port (`12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`), fitting a port customs office.
- The signatory is the ginnery, which declares the export; the full descriptions of ginnery and mill are identical to those in 10 (compared block by block).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`: suspected because the port has a UN/LOCODE in 12 — not kept: a customs office is identified by a customs office code rather than a LOCODE, and identifying it is a logistics question.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Cotton sales`: the exporter's sales desk for an export sale — acceptable, not a finding.
