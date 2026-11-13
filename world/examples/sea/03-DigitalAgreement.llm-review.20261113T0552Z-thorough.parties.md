# LLM review: 03-DigitalAgreement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/03-DigitalAgreement.xml`, Git blob `2af11a686be2a4eb3d82b639256ce234b6e7bcf7` (committed)
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

### sea/03#F1 · Medium · A language code in LocaleCode
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/03#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/03#F3 · Medium · The Lumeport Trade Accord Council described as a company in a commercial register, with a liquidation status
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- Why: The Lumeport Trade Accord Council is the governing body of the Lumeport Trade Accord under which Urvania, Bayvarra and Lisavu trade: it governs this agreement, runs the Accord’s network validator and issues the access-point certificates, and its own contact is a `Public service officer` in `Public services`. Its legal entity places it in a register of companies with `CorporateRegistrationTypeCode` = commercial register and gives it `CompanyLiquidationStatusCode` (UBL: "A code signifying the party’s legal status", here "Active, not in liquidation"). A public body is not entered in the commercial register and cannot go into liquidation; the checklist names exactly this case. Its ISIC code `9411` (business and employers membership organisations) would fit an association rather than a treaty body; an association is not a company in a commercial register either. The same description is used in 04-DigitalCapability.xml.
- Condition: The legal entity of The Lumeport Trade Accord Council describes it as the public body it is: no commercial-register scheme, no liquidation status (an official register of public bodies, or only the registration name, if anything).
- Options: Preferred: keep `RegistrationName` and drop `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme`; if the world has a register of public bodies, use it with a registration type that says so. Alternative: drop `PartyLegalEntity` altogether for public bodies.
- Needs decision: yes

### sea/03#F4 · Low · Velumi Trading described differently from the other examples of the flow (English renderings tagged en-XB, legal form only in English)
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by Lumeway Distribution) the English renderings of Velumi Trading’s street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself the same party has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example.
- Condition: Velumi Trading’s postal address, registration address and legal form carry the same renderings with the same `languageID` values in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/03#F5 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/03#F6 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (second participant). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

### sea/03#F7 · Low · Lumeway’s own EDI terms shown as signed by the Trade Accord Council
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:ID` = `LD-EDI-TERMS-1.0`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:URI` = `https://www.lumeway.example/edi/terms-1.0.pdf`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- Why: `ResultOfVerification` is "The result of an attempt to verify a signature associated with the referenced document", and its `SignatoryParty` is "The signing party". The referenced document is Lumeway Distribution’s EDI terms: its ID is in Lumeway’s numbering and it is published on Lumeway’s website. The verified signature is nevertheless the Trade Accord Council’s. Either the Council signs (certifies) Lumeway’s terms, which nothing in the example says, or the signatory should be Lumeway Distribution, which also signs this agreement (`/DigitalAgreement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`). The Council appears in the result as the validator (`LTAC-VALIDATOR`), which is a different role.
- Condition: The `SignatoryParty` of the verification result is the party that signed the referenced terms document, and the document’s ID and location agree with that party.
- Options: Preferred: Lumeway Distribution as signatory of its own terms, the Council remaining the validator. Alternative: if the Council certifies the terms, make the referenced document the Council’s certificate (its own ID) and say so in the description.
- Needs decision: yes

## Checked and consistent
- Both participants are the trading partners of the flow: Lumeway Distribution (initiating, private) and Velumi Trading (private), each with legal, technical, support and commercial contacts; the indicators `PrivatePartyIndicator` = true and `PublicPartyIndicator` = false fit both companies.
- The participant IDs of the delivery channels match the parties’ electronic addresses: `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:DigitalDeliveryChannel/cbc:ParticipantID` = `XL:IC41859` (Velumi sends orders) and `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:ReceivingDigitalService/cac:DigitalDeliveryChannel/cbc:ParticipantID` = `XB:20410274` (Lumeway receives them); the billing process runs the other way round, which fits seller and buyer.
- The access-point certificates are issued by the Trade Accord Council in all four channels, consistent with the Council running the network named in `DigitalAgreementTerms/Description`.
- The Trade Accord Council is described identically in 04-DigitalCapability.xml.

## Considered and refuted
- `/DigitalAgreement/cbc:AgreementTypeCode` = `BILATERAL` together with a `GovernorParty`, whose definition gives a multilateral agreement as its example — refuted: the definition only gives an example; a bilateral agreement over the Accord’s network can be governed by the network’s operator.
- `/DigitalAgreement/cac:Signature`: only Lumeway Distribution signs the bilateral agreement — refuted: the document is issued by the initiating participant; the counterparty’s acceptance is a separate act and nothing in the example claims it is signed by both.
- `/DigitalAgreement/cac:ParticipantParty[2]/cac:CommercialContact/cbc:Name` = `Purchasing` — refuted: for the buyer, purchasing is the right commercial contact (unlike the contact in its party description, finding F5).
