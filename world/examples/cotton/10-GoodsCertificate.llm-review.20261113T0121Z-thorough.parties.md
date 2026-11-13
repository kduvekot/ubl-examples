# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/10-GoodsCertificate.xml`, Git blob `a573492644f6156f64f31e963d3578b9c5d69634` (committed)
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

### cotton/10#F1 · Medium · A phytosanitary certificate issued by a chamber of commerce and sanctioned by customs
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:IssuerParty/cbc:IndustryClassificationCode` = `9411`
- XPath: `/GoodsCertificate/cac:Attestation/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:LegalAuthorityParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: The certificate is a phytosanitary certificate (`PHYTO`): it attests freedom from the pests named by Bayvarra's plant health rules. Under the International Plant Protection Convention (Art. V; ISPM 12, my own knowledge) phytosanitary certificates are issued only by the exporting country's national plant protection organisation, a public authority. The issuer, the attestation issuer and the signatory here are the Selanu Chamber of Commerce, classified as a business membership organisation (ISIC `9411`), whose contact is its carnet office; and `cac:LegalAuthorityParty`, "The legal Authority, when different from the issuer, who sanctions this Goods Certificate", is the customs service, which has no plant health competence. Neither party is the right one for the role; a chamber of commerce issues certificates of origin, and its classing of cotton (the classing certificate `XL-CLS-2026-0042`) is a commercial quality service, not plant protection.
- Condition: The issuer of a phytosanitary certificate, and the legal authority if one is named, is Lisavu's plant protection authority; or the certificate is of a type the chamber of commerce can issue.
- Options: (a, preferred) a Lisavan plant protection authority (e.g. a plant health service of the island administration) as issuer and signatory, without a separate legal authority; (b) keep the chamber and change the certificate to a type chambers issue (certificate of origin), which changes what the document attests.
- Needs decision: yes

### cotton/10#F2 · Medium · Language code in `LocaleCode`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/10#F3 · Low · The issuer's contact is its carnet office
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:Contact/cbc:Name` = `Carnet office`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `carnet@chamber-selanu.example`
- Why: The contact of the party issuing a plant health certificate is its carnet office, the desk for ATA carnets (temporary admission); it has nothing to do with this certificate or with the inspection at the ginnery's warehouse.
- Condition: The issuer's contact is the office responsible for the certificate the document is (plant health inspection or certification).
- Options: (a, preferred) the issuing authority's inspection or certification office; (b) drop the contact.
- Needs decision: no

### cotton/10#F4 · Low · The chamber of commerce described as a company in the commercial register
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The checklist: a public body is not a company in a commercial register and has no liquidation status. A chamber of commerce is a membership body, in many countries one under public law; here it has no legal form or size but is registered in the island companies register with a liquidation status. Whether the Selanu chamber is a public-law body or a registered association is a question of the world's story.
- Condition: The chamber's legal entity describes the kind of body it is in the world (public-law body or registered association), with a registration scheme of that kind and a liquidation status only if it can be liquidated as a company.
- Options: (a, preferred) decide the chamber's legal status in the story and describe it accordingly (e.g. no commercial registration and no liquidation status for a public-law chamber); (b) keep it if the world's chambers are companies, and give a legal form.
- Needs decision: yes

### cotton/10#F5 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the importer named on a plant health certificate; its import or goods-receiving contact would fit the role. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/10#F6 · Low · A freight forwarder named on a phytosanitary certificate
- XPath: `/GoodsCertificate/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: Section 4.8 (presence): the certificate attests the plant health of the bales for the importing country; it does nothing with the forwarder that books the carriage, and a phytosanitary certificate does not name one.
- Condition: The certificate names only parties it has a use for.
- Options: (a, preferred) drop the forwarder; (b) keep it only if the story gives it a role in the certificate (e.g. as applicant).
- Needs decision: no

### cotton/10#F7 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/GoodsCertificate/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Exporter, consignor, applicant, warehouse and processing party are all the ginnery (`IC42681`), which fits: it ginned and stores the bales and applies for the certificate; importer and consignee are the mill, as in 15.
- The ginnery's and the mill's full descriptions are identical to those in 11 (exporter) and 15 (importer) (compared block by block).
- The certificate's issuer, attestation issuer and signatory are the same party (`IC42133`).

## Considered and refuted
- `/GoodsCertificate/cac:WarehouseParty`: suspected as a duplicate of the exporter — refuted, the note says the bales were inspected at the ginnery's warehouse, so the ginnery is the party storing them.

## Outside this review
- The classing certificate `XL-CLS-2026-0042` is signed with `cbc:ValidationDate` `2026-02-20` but cited in 02-Forecast.xml, issued on 2026-02-02 (a date question across documents).
