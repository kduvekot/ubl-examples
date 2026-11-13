# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
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

### cotton/15#F1 · Medium · The customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- Why: The Customs and Border Service of Bayvarra is a public authority (ISIC `8411`, general public administration). `cac:CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `cbc:CompanyLiquidationStatusCode` "the party's liquidation status": a government agency is not registered in a commercial companies register and cannot be in or out of liquidation. The checklist names exactly this case. All 7 example files that give this authority's `RegistrationName` also carry a `CompanyLiquidationStatusCode` (grep over *.xml).
- Condition: The authority's legal entity carries no commercial registration scheme and no liquidation status; if it has an identifier, it is one from a register of public bodies.
- Options: (a, preferred) keep only `RegistrationName` (and an identifier from a register of public bodies, if the world has one); (b) drop `cac:PartyLegalEntity` for the authority altogether.
- Needs decision: no

### cotton/15#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/15#F3 · Low · An inland border office processes a sea import at Lumeport
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName` = `Border Crossing Road`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CityName` = `Marrowdale`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- Why: The customs party is "The Authority who is legally responsible for processing the Declaration." The bales arrive by sea at Lumeport in the Coastal State (the bill of lading 13 and the pre-arrival report 14); the authority is described with the address and contact of a border office on Border Crossing Road in Marrowdale, Upland State. As a contact for this declaration the border office does not fit; the same address is used in every example that gives this authority an address (7 of the 8 example files that name it, all with `Border Crossing Road`, grep over *.xml), so it may be meant as the service's head office.
- Condition: The customs party's address and contact are those of the office that handles imports at the port of Lumeport, or explicitly the service's head office with a contact that handles this declaration.
- Options: (a, preferred) the customs office at the port of Lumeport (address in the harbour quarter, an import contact); (b) keep the head-office address, rename the contact to an import or clearance office, and say in the story where the service's head office is.
- Needs decision: yes

### cotton/15#F4 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the importer making the declaration; its import or customs contact would fit the role. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/15#F5 · Low · The ginnery's address and legal form are rendered differently than in the other examples
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` (languageID `en-XB`)
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company` (no languageID, no Lisavan rendering)
- Why: In the examples the ginnery sends, its English address parts carry `languageID` `en-XL` and its legal form is given in Lisavan and English (`01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` with `en-XL`; `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`, `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`). Here the same English names are tagged `en-XB` (Bayvarran English), the Lisavan street and city names are kept, but the Lisavan legal form is dropped and the English one has no `languageID`. The names of a Lisavan street and town are Lisavan English whoever sends the document, so the same party is described in two ways in the flow (the same happens in 02, 07, 08, 09, 13, 15 and 18, all sent by Bayvarran parties).
- Condition: The ginnery's address and legal form carry the same renderings and the same `languageID`s in every example of the flow.
- Options: (a, preferred) the renderings and tags of 01-SelfBilledInvoice.xml everywhere, because `languageID` describes the text, not its reader; (b) if the tags are meant to follow the recipient's locale, apply that to every text of the party and record the rule.
- Needs decision: no

### cotton/15#F6 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Importer, consignee, notifier and signatory are the mill (`20412603`), which declares its own import; the consignor is the ginnery, as in 09, 10 and 13; the customs trader numbers of both have a use here.
- The mill's full description is identical to 10 (compared block by block).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:NotifierParty`: suspected as a duplicate of the importer — refuted, the role ("responsible for contact on master level") may well be the importer itself, and it states who customs contacts.
