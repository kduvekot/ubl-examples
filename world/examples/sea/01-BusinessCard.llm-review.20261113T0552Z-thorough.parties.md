# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/01-BusinessCard.xml`, Git blob `3b6f96c9fc61de8c4dad42aecf09e84a3a8c83dc` (committed)
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

### sea/01#F1 · Medium · A language code in LocaleCode
- XPath: `/BusinessCard/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/01#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/01#F3 · Medium · The stock-count audit report is issued by Lumeway Distribution itself, though the auditor made it
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:EvidenceIssuingParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Description` = `Year-end count by the auditor.`
- Why: UBL defines `EvidenceIssuingParty` as "The Party who issues the evidentiary Document". The evidence is an audit report (`EvidenceTypeCode` = `AUDIT`) of the year-end stock count, and its description says the count was made "by the auditor". The party that issues an audit report is the auditor, not the audited company; with Lumeway Distribution as issuer the evidence is a self-declaration, which contradicts both the type code and the description and takes away what makes it evidence for the stock claim of `CAP-STOCK`.
- Condition: The `EvidenceIssuingParty` of the stock-count evidence is the party that issued that evidence document, and it agrees with `EvidenceTypeCode` and `Description`.
- Options: Preferred: name the audit firm of Lumeway Distribution as `EvidenceIssuingParty` (a party of the world, with its identifier), since the description already says the auditor counted. Alternative: if Lumeway issues the document itself, make it an internal stock report (another evidence type) and say in the description who counted.
- Needs decision: yes

### sea/01#F4 · Low · Velumi Trading described differently from the other examples of the flow (English renderings tagged en-XB, legal form only in English)
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by Lumeway Distribution) the English renderings of Velumi Trading’s street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself the same party has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example.
- Condition: Velumi Trading’s postal address, registration address and legal form carry the same renderings with the same `languageID` values in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/01#F5 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/01#F6 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (receiver). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

## Checked and consistent
- Sender, business party, signatory and evidence issuer all identify Lumeway Distribution with the same register number `20410274` (`/BusinessCard/cac:SenderParty/cac:PartyIdentification/cbc:ID`, `/BusinessCard/cac:BusinessParty/cac:PartyIdentification/cbc:ID`, `/BusinessCard/cac:Signature/cac:SignatoryParty/cac:PartyIdentification/cbc:ID`); the business card owner is the sender, as the definition of `SenderParty` allows.
- Lumeway Distribution’s full description (identifiers, GLN `9520610900008` with a valid check digit and the GS1 demonstration prefix 952, customs trader number, tax scheme of Upland State, legal entity, contact, endpoint) is identical in all 25 full renderings across the flow (compared leaf by leaf over `sea/*.xml`).
- Velumi Trading’s identifiers (`IC41859` in the island companies register, customs trader `XL-TR-041859`, endpoint `XL:IC41859`) are the same in every example of the flow, and the endpoint matches the participant ID used for Velumi in 03-DigitalAgreement.xml.
- Legal form, size (`MEDIUM`, share capital 2,500,000 lume, fully paid) and registration in the federal business register fit a private limited distributor; ISIC `4649` fits both wholesalers.

## Considered and refuted
- `/BusinessCard/cac:ReceiverParty`: no `PartyTaxScheme` for Velumi Trading — refuted: a business card sent to Velumi has no tax purpose for the receiver; nothing is implied by absence.
- `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset` = `-1` against Velumi’s `-1` in Lisavu — refuted: both countries are in the same time zone in all examples of the world; no contradiction.
