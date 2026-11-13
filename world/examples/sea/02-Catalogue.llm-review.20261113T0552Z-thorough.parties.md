# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/02-Catalogue.xml`, Git blob `9ab014c2e27df7270bfea2ec3db014a3637bf54d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/02#F1 · Medium · A language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/02#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/02#F3 · Medium · A province in Region (Codana Identification Agency)
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". `Province of Ferrano` is an administrative division of Urvania, so it belongs in `CountrySubentity` (with `CountrySubentityCode` if Urvania has a list), not in `Region`. The checklist names this case. The value occurs 219 times in 104 examples of the world (counted with `grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano<'`), so it is the standard rendering of Urvanian addresses.
- Condition: No address in this example carries a province (or other administrative division) in `Region`; Codana Identification Agency’s province is in `CountrySubentity`.
- Options: Preferred: move the province to `CountrySubentity` (and add `CountrySubentityCode` where Urvania has a subdivision list), for every Urvanian address. Alternative: none that keeps `Region`; `Region` is for regions above or across administrative divisions.
- Needs decision: no

### sea/02#F4 · Low · Velumi Trading described differently from the other examples of the flow (English renderings tagged en-XB, legal form only in English)
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by Lumeway Distribution) the English renderings of Velumi Trading’s street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself the same party has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example.
- Condition: Velumi Trading’s postal address, registration address and legal form carry the same renderings with the same `languageID` values in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/02#F5 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/02#F6 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (receiver) and Codana Identification Agency (GTIN issuer). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

### sea/02#F7 · Low · The GTIN issuer’s full master data copied into one catalogue line
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Codana Identification Agency SRU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `member@codana.example`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`
- Why: `StandardItemIdentification/IssuerParty` only needs to say who issued the GTIN (UBL: "The Party who issues this Item Identification"). In line 1 Codana Identification Agency comes with its VAT number, legal entity, contact, postal address and endpoint; in line 2 the same issuer of the same kind of identifier is given with identifier and name only, and so is Codana as issuer of the property identifier `UR-SF-0450`. The catalogue does nothing with Codana’s tax registration or contact; this is master data copied into a document that does not use it (section 4.8), and the two lines describe the same party differently.
- Condition: Codana Identification Agency is described the same way in both catalogue lines, with no tax, legal-entity or contact data the catalogue does not use.
- Options: Preferred: give the issuer by identifier and name only, as in line 2. Alternative: if the catalogue receiver needs to reach the issuing agency, keep only that (e.g. the website or electronic address), the same in both lines.
- Needs decision: no

### sea/02#F8 · Low · Codana’s contact: a private agency’s member services described as public services
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: Codana Identification Agency is a private limited company (SRU). Its contact is called `Member services`, but the job title and department are those the world gives to public authorities (the same `Public service officer` / `Public services` pair is used for the Trade Accord Council and the customs services in this flow). Name, title and department do not agree, and the department does not fit a private company.
- Condition: Name, job title and department of Codana’s contact agree with each other and with a private numbering agency, or the contact is absent (see the finding on the copied master data).
- Options: Preferred: drop the contact from the catalogue (it has no use there). Alternative: a member-services title and department.
- Needs decision: no

## Checked and consistent
- Provider and seller are both Lumeway Distribution (`20410274`), receiver is Velumi Trading (`IC41859`), as in 01-BusinessCard.xml and 05-Order.xml.
- Manufacturer and information content provider of both items are Valdara Industries (`XU-R-104274`), the same identifier in every example of the flow that names it (22 short renderings compared).
- Codana Identification Agency is described identically in retail/02-Catalogue.xml (same address, legal form and contact), so the description is consistent across the world; the findings above apply there too.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty`: a GTIN is allocated by the brand owner from a GS1 company prefix, so the issuer could be Valdara Industries — refuted: the repository’s convention for item identification is "GS1 / ISO via Codana", Codana acting as the numbering organisation; naming the organisation that issues the number is a legitimate reading of "The Party who issues this Item Identification".
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`, an Italian-looking name tagged `en-XB` — refuted as a separate finding: Urvanian English names are Italianate throughout the world (e.g. `Via delle Officine`), and the `en-XB` tag follows the same issuer convention as F4 (Velumi Trading’s renderings); it is the same question and is decided with it.
