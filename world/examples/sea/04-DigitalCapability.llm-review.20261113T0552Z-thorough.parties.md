# LLM review: 04-DigitalCapability.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/04-DigitalCapability.xml`, Git blob `6b0fee9db96b3c9a3d5831840cb45c0145a4dc62` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0919fae 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/04#F1 · Medium · A language code in LocaleCode
- XPath: `/DigitalCapability/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalCapability/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/04#F2 · Medium · The Lumeport Trade Accord Council described as a company in a commercial register, with a liquidation status
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- Why: The Lumeport Trade Accord Council is the governing body of the Lumeport Trade Accord: it publishes this capability record of a participant of the Accord’s network, governs the digital agreement 03-DigitalAgreement.xml and issues the access-point certificates there, and its own contact is a `Public service officer` in `Public services`. Its legal entity places it in a register of companies with `CorporateRegistrationTypeCode` = commercial register and gives it `CompanyLiquidationStatusCode` (UBL: "A code signifying the party’s legal status", here "Active, not in liquidation"). A public body is not entered in the commercial register and cannot go into liquidation; the checklist names exactly this case. Its ISIC code `9411` (business and employers membership organisations) would fit an association rather than a treaty body; an association is not a company in a commercial register either. The same description is used in 03-DigitalAgreement.xml.
- Condition: The legal entity of The Lumeport Trade Accord Council describes it as the public body it is: no commercial-register scheme, no liquidation status (an official register of public bodies, or only the registration name, if anything).
- Options: Preferred: keep `RegistrationName` and drop `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme`; if the world has a register of public bodies, use it with a registration type that says so. Alternative: drop `PartyLegalEntity` altogether for public bodies.
- Needs decision: yes

### sea/04#F3 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/DigitalCapability/cac:BusinessParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/04#F4 · Low · Signature ID in Lumeway’s numbering, signatory the Trade Accord Council
- XPath: `/DigitalCapability/cac:Signature/cbc:ID` = `LD-SIG-26-DC`
- XPath: `/DigitalCapability/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- XPath: `/DigitalCapability/cbc:ID` = `LTAC-DCP-26-0126`
- Why: The document is issued and signed by the Trade Accord Council (document ID `LTAC-…`, signatory the Council), but the signature carries an ID in Lumeway Distribution’s series (`LD-SIG-…`, as `LD-SIG-26-BC` in 01-BusinessCard.xml). A signature identifier is assigned by whoever applies the signature; an `LD-` ID suggests Lumeway signed, which contradicts `SignatoryParty`.
- Condition: The signature’s ID and its `SignatoryParty` name the same party (the Council’s numbering for a Council signature, or Lumeway as signatory if Lumeway signs its own capability record).
- Options: Preferred: a Council signature ID (`LTAC-SIG-…`), since the Council sends the record. Alternative: Lumeway Distribution as signatory, if the world means the owner to sign its capabilities and the Council only to send them.
- Needs decision: no

### sea/04#F5 · Low · Velumi Trading described differently from the other examples of the flow (English renderings tagged en-XB, legal form only in English)
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by the Lumeport Trade Accord Council) the English renderings of Velumi Trading’s street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself the same party has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example.
- Condition: Velumi Trading’s postal address, registration address and legal form carry the same renderings with the same `languageID` values in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/04#F6 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/04#F7 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (receiver). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

## Checked and consistent
- Sender (the Council, a third party sending on behalf of the owner, as the definition of `SenderParty` allows), receiver (Velumi Trading, the trading partner) and business party (Lumeway Distribution, the owner of the capabilities) fit their roles; the processes described (receives orders, sends invoices) agree with the directions in 03-DigitalAgreement.xml.
- Lumeway Distribution and the Council are described identically to 03-DigitalAgreement.xml.
