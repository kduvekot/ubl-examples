# LLM review: 04-DigitalCapability.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/04-DigitalCapability.xml`, Git blob `6b0fee9db96b3c9a3d5831840cb45c0145a4dc62` (committed)
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

### sea/04#F1 · Medium · Digital capabilities without any technical capability
- XPath: `/DigitalCapability/cac:DigitalProcess[1]/cbc:Description` = `Receives orders and order changes, sends order responses.`
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- Why: the document is "used to provide information about a business party and its digital trade capabilities". Its two processes have only an ID and a sentence: no profile, no digital collaboration, no document formats or versions, no delivery channel or endpoint. A receiver cannot tell from it in which format, over which network or at which access point Lumeway exchanges these documents; that information is what the agreement of the same day then fixes (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[1]/cbc:ProfileID` = `urn:ubl-examples:world:profile:ordering:1.0`).
- Condition: each digital process states at least its profile and the documents it sends and receives (format and version), and the channel where they are received.
- Options: (a) preferred: give `ProfileID` and `DigitalCollaboration` with the sending and receiving services and the delivery channel, matching the agreement; (b) at least `ProfileID`.
- Needs decision: no

### sea/04#F2 · Medium · Language code in LocaleCode
- XPath: `/DigitalCapability/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalCapability/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/04#F3 · Medium · A gate in AdditionalStreetName
- XPath: `/DigitalCapability/cac:BusinessParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples (`grep -c "Gate 3" world/examples/sea/*.xml`).
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/04#F4 · Low · Billing capability names statements, but the flow's statement is not Lumeway's
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- Why: the capabilities are Lumeway's (`BusinessParty`). The statement of the flow is issued by Harbourline Factoring (`25-Statement.xml:/Statement/cbc:ID` = `HF-ST-26-0151`), to whom the invoice assigns payment (`22-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). Nothing in the flow shows Lumeway sending a statement.
- Condition: the capabilities name what the business party itself sends and receives, consistent with the flow.
- Options: (a) preferred: drop "statements" (or say statements come from the factor); (b) keep it if Lumeway sends statements outside factoring, and say so.
- Needs decision: no

### sea/04#F5 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact is named `Purchasing`; job title and department belong to a seller's customer service. Same values in every sea example with this contact.
- Condition: name, job title and department of Velumi's contact describe the same function.
- Options: (a) preferred: purchasing job title and department.
- Needs decision: no

### sea/04#F6 · Low · Trade accord council contact as public service, but registered as a company
- XPath: `/DigitalCapability/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/DigitalCapability/cac:SenderParty/cac:Contact/cbc:Department` = `Public services`
- Why: the council is a business membership organisation (ISIC 9411) registered in the commercial register (as in `03-DigitalAgreement.xml:/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`); its secretariat is described as public service. Legal entity and contact describe different kinds of body.
- Condition: legal entity and contact describe the same kind of body.
- Options: (a) treaty body: no commercial registration; (b) association: a secretariat job title.
- Needs decision: yes (what kind of body the council is)

### sea/04#F7 · Low · Signature ID in Lumeway's numbering, signed by the council
- XPath: `/DigitalCapability/cac:Signature/cbc:ID` = `LD-SIG-26-DC`
- XPath: `/DigitalCapability/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- Why: the world's identifiers carry their assigner's prefix (`LD-` for Lumeway, `LTAC-` for the council, as in this document's own `ID` `LTAC-DCP-26-0126`). The signature is the council's but numbered like Lumeway's signatures (`01-BusinessCard.xml:/BusinessCard/cac:Signature/cbc:ID` = `LD-SIG-26-BC`). Either the council signs and the ID is wrong, or Lumeway, the owner of the capabilities, was meant to sign.
- Condition: signature ID and signatory belong to the same party.
- Options: (a) preferred: decide who signs (Lumeway as owner, or the council as sender) and align ID and signatory.
- Needs decision: no

### sea/04#F8 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the English renderings of Velumi Trading's address in Lisavu are tagged `en-XB` (English as used in Bayvarra), while the same address of the same party is tagged `en-XL` in the documents Velumi sends itself (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`). Across the sea flow the tag follows the sender's country rather than the address: `en-XB` in 16 examples, `en-XL` in 8 (`grep -c 'languageID="en-XB">Reef Street'` and `'languageID="en-XL">Reef Street'` over `world/examples/sea/*.xml`). The same rendering of the same address should carry the same language tag; for a Lisavu address `en-XL` is the natural one.
- Condition: Velumi's address renderings carry the same `languageID` in every example of the flow.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere; (b) a world-wide rule that the tag is the sender's locale, stated where the world documents its conventions.
- Needs decision: no

## Checked and consistent
- Sender (the council) sends on behalf of the owner Lumeway, as the definition of `SenderParty` allows; business party data match `01-BusinessCard.xml`.
- The processes agree with the agreement of the same day: Lumeway receives orders and sends invoices (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:ReceivingDigitalService/cbc:ID` = `LD-Order-IN`).
- Issued 09:44, before the agreement (12:59) that builds on it.
- GLN check digit correct (`check_ids.py`).
