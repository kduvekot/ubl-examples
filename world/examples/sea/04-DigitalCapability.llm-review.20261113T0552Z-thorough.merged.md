# LLM review: 04-DigitalCapability.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/04-DigitalCapability.xml`, Git blob `6b0fee9db96b3c9a3d5831840cb45c0145a4dc62` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b75057e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/04#F1 · Medium · A language code in LocaleCode (two places)
- XPath: `/DigitalCapability/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalCapability/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; both hold the ISO 639 language code already in the neighbouring `Language/ID`, so neither names a locale. 362 such elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: each `LocaleCode` is absent or a locale (language with region) from a locale list.
- Options: (a) preferred: drop them, as in all earlier flows; (b) `en-XB` from a list of language tags (broad's and context's preference).
- Needs decision: no
- From: broad (F2), parties (F1), context (F1)

### sea/04#F2 · Medium · The Trade Accord Council described both as a company in the commercial register and as a public body
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/DigitalCapability/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/DigitalCapability/cac:SenderParty/cac:Contact/cbc:Department` = `Public services`
- Why: same description as in 03-DigitalAgreement.xml (03#F4): the council of the Accord, which publishes this capability record and governs the network, is registered as a commercial company with a liquidation status ("Active, not in liquidation"), staffed with a public-service officer, and classified ISIC 9411 (membership organisation). A public body is not in a commercial register and has no liquidation status (checklist); an association is not a company either. The descriptions contradict each other, and the council's legal entity plays no role in a statement of Lumeway's capabilities (context).
- Condition: legal entity, classification and contact describe the same kind of body; a public or treaty body carries no commercial-register scheme and no liquidation status.
- Options: (a) preferred: as 03#F4 (a): drop liquidation status and the commercial scheme, keep `RegistrationName`; (b) association with a secretariat contact; (c) reduce `SenderParty` to identification, name, contact and endpoint (context).
- Needs decision: yes (what kind of body the council is)
- From: parties (F2, Medium/yes), broad (F6, Low/yes), context (F5, Low/yes)

### sea/04#F3 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/DigitalCapability/cac:BusinessParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name and has no use in a postal address. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F3), parties (F3), context (F8, Low)

### sea/04#F4 · Medium · Digital capabilities without profile, documents or channel
- XPath: `/DigitalCapability/cac:DigitalProcess[1]/cbc:Description` = `Receives orders and order changes, sends order responses.`
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- Why: the document is "used to provide information about a business party and its digital trade capabilities". Both processes have only an ID and a sentence: no `ProfileID`, no `DigitalCollaboration`, no document formats or versions, no delivery channel or endpoint. A partner cannot tell from it in which format, over which network or at which access point Lumeway exchanges these documents, which is what the document is for; the agreement of the same day shows they were known (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[1]/cbc:ProfileID` = `urn:ubl-examples:world:profile:ordering:1.0`). Medium (information the purpose depends on), not Low as context had it: a capability statement that names no capability detail does not serve its purpose; context's option (b), a minimal capability completed by the agreement, is kept.
- Condition: each digital process states at least its profile and the documents it sends and receives (format and version), and the channel where they are received.
- Options: (a) preferred: `ProfileID` and `DigitalCollaboration` with sending and receiving services and the delivery channel, matching 03-DigitalAgreement.xml; (b) at least `ProfileID`; (c) keep a minimal capability and accept that the agreement adds the rest (context).
- Needs decision: no
- From: broad (F1), context (F2, Low)

### sea/04#F5 · Low · Signature in Lumeway's numbering, signed by the council, with nothing signed
- XPath: `/DigitalCapability/cac:Signature/cbc:ID` = `LD-SIG-26-DC`
- XPath: `/DigitalCapability/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- XPath: `/DigitalCapability/cbc:ID` = `LTAC-DCP-26-0126`
- Why: throughout the flow the prefix of an identifier names the party that assigned it (`LD-` Lumeway, `LTAC-` the council, `PL-` the Port of Lumeport, e.g. `PL-SIG-TS-13` signed by the port in 13-TransportationStatus.xml). The document is issued by the council and signed by it, but the signature ID is in Lumeway's series (as `01-BusinessCard.xml:/BusinessCard/cac:Signature/cbc:ID` = `LD-SIG-26-BC`), which reads as Lumeway's signature. In addition the signature holds only an ID and a signatory, as 137 of 147 `Signature` aggregates of the world do (lxml count; the world-wide question is 01#F6, Low/yes in earlier merges).
- Condition: signature ID and signatory belong to the same party.
- Options: (a) preferred: an `LTAC-` signature ID, since the council issues and signs; (b) Lumeway as signatory, if the owner is meant to sign its capabilities and the council only to send them.
- Needs decision: no
- From: broad (F7), parties (F4), logistics (F1), context (F4)

### sea/04#F6 · Low · Velumi Trading described differently from the documents it issues (en-XB tags, legal form only in English)
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: as in 01–03: `en-XB` on the English renderings of Velumi's Lisavu address and the legal form once in English, while in the order Velumi issues they are `en-XL` and in both languages (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`, `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). Here the issuer is the council in Lumeport, so the tag again follows the issuer.
- Condition: Velumi's addresses and legal form carry the same renderings and `languageID` values in every example, following one documented rule.
- Options: (a) preferred: `en-XL` and both languages everywhere; (b) a documented issuer-variety rule, with the Lisavan legal form still given.
- Needs decision: yes
- From: broad (F8, Low/no), parties (F5)

### sea/04#F7 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID"; Velumi shares the New Year's Day date with companies in all three registers (271 times in 181 examples, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway has its own (`/DigitalCapability/cac:BusinessParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1988-10-03`).
- Condition: every `RegistrationDate` is the party's date in the world, or absent.
- Options: (a) preferred: an own date per company; (b) drop it.
- Needs decision: yes
- From: parties (F7); context (inside F6)

### sea/04#F8 · Low · Receiver's legal entity and address in a capability statement about another party
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `LTD`
- Why: the document tells Velumi about Lumeway's capabilities; Velumi's legal form, size, registration and address are not used. Master data copied into a document that does not use it (section 4.8).
- Condition: `ReceiverParty` carries identification, name, contact and endpoint only.
- Options: (a) preferred: reduce `ReceiverParty`.
- Needs decision: no
- From: context (F6)

### sea/04#F9 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: title and department are those of Lumeway's contact, not of the purchasing function the name and e-mail state.
- Condition: name, job title and department of Velumi's contact describe its purchasing function.
- Options: (a) preferred: a purchasing title and department; (b) drop them.
- Needs decision: no
- From: broad (F5), parties (F6), context (F7)

### sea/04#F10 · Low · Billing capability does not match the agreement and the flow
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- XPath: `03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[2]/cbc:Description` = `Invoice, credit note, statement and remittance advice.`
- Why: the capabilities are Lumeway's (`BusinessParty`). The flow's statement is issued by Harbourline Factoring (`25-Statement.xml:/Statement/cbc:ID` = `HF-ST-26-0151`), the payee of the invoice (`22-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`); nothing shows Lumeway sending a statement. Conversely the capability omits the credit note Lumeway sends (`26-CreditNote.xml`) and that the agreement names, the invoice status request it sends (`23-InvoiceStatusRequest.xml`) and the debit note it receives (`28-DebitNote.xml`). Two sides of the same mismatch, grouped.
- Condition: the billing capability names what Lumeway itself sends and receives in the flow, and agrees with the agreement's billing process.
- Options: (a) preferred: a description matching Lumeway's own exchanges (credit notes, status requests, debit notes; statements only if Lumeway sends them), with F4's collaborations.
- Needs decision: no
- From: broad (F4), context (F3)

## Checked and consistent
- `SenderParty` (the council, sending on behalf of the owner, which the definition allows: "a third-Party who acts on behalf of the owner"), `ReceiverParty` (Velumi) and `BusinessParty` (Lumeway, the owner, with the full description, unlike 01-BusinessCard) fit their roles.
- Business party identifiers (`20410274`, GLN `9520610900008`, `XB-TR-410274`) and receiver identifiers (`IC41859`, `XL-TR-041859`) agree with `01-BusinessCard.xml` and `05-Order.xml`; Lumeway and the council are described as in 03-DigitalAgreement.xml. GLN check digit correct (`check_ids.py`).
- The process IDs `ordering` and `billing` and their directions (Lumeway receives orders, sends invoices) match `03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:ReceivingDigitalService/cbc:ID` = `LD-Order-IN`; this document (09:44) precedes the agreement (12:59) the same day.

## Considered and refuted
- `/DigitalCapability/cbc:PreviousVersionID` = `0.9`: version 0.9 not in the flow — refuted: earlier versions can exist outside the flow (from context).

## Changed in the merge
- broad/F2, parties/F1, context/F1 → F1: preferred option set to drop, aligned with earlier flows.
- parties/F2 (Medium/yes), broad/F6 (Low/yes), context/F5 (Low/yes) → F2: grouped (legal entity and contact of the same party), as 03#F4.
- context/F8 → F3: Low raised to Medium, aligned.
- context/F2 (Low) + broad/F1 (Medium) → F4: Medium kept (purpose depends on it); context's option kept.
- broad/F7, parties/F4, logistics/F1, context/F4 → F5: grouped; the signature's ID-and-signatory-only form noted in Why, referring to 01#F6 for the world-wide question.
- broad/F8 (no) + parties/F5 (yes) → F6: grouped, yes.
- broad/F4 + context/F3 → F10: grouped.
