# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/01#F1 · Medium · The card's subject is described under SenderParty, not under BusinessParty
- XPath: `/BusinessCard/cac:BusinessParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Lumeway Distribution Ltd`
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:StreetName` = `Distribution Drive`
- XPath: `/BusinessCard/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- Why: A BusinessCard is "a document used to provide information about a business party and its
  business capabilities"; BusinessParty is "the Party who owns this Business Card", SenderParty
  "the Party who sends this Business Card. This Party may be the owner … or a third-Party who acts
  on behalf of the owner". The information the card exists to give (address, legal entity, tax
  registration, contact, industry classification, website) is carried by the sending party, while
  the business party the card is about holds only an identifier and a name. A receiver reading the
  card per its definition finds the business data on the transport role, not on the subject.
- Condition: the address, legal entity, tax scheme, contact, website and industry classification
  of Lumeway Distribution are carried in `cac:BusinessParty`; `cac:SenderParty` carries no more
  than what identifies the sender.
- Options: (a) preferred: move the full party description to BusinessParty and reduce SenderParty
  to identification, name and electronic address, because the card's content then sits on its
  subject; (b) drop SenderParty altogether, since the sender is the owner.
- Needs decision: no

### sea/01#F2 · Medium · A language code in LocaleCode
- XPath: `/BusinessCard/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used". The value is
  the ISO 639 language code already given in `/BusinessCard/cac:SenderParty/cac:Language/cbc:ID`
  = `en` (listID ISO 639), so it names no locale. The same element and value occur 362 times over
  `world/examples/*/*.xml` (`grep -rho --include='*.xml'` for `<cbc:LocaleCode listID="ISO 639">en`),
  and nowhere with another value.
- Condition: LocaleCode is absent, or holds a locale (language and region, e.g. a Bayvarran English
  locale) from a list of locales.
- Options: (a) preferred: a locale such as the `en-XB` tag the examples already use in `languageID`,
  with a matching list, since Lumeway works in Bayvarran English; (b) drop LocaleCode.
- Needs decision: no

### sea/01#F3 · Medium · CandidateStatement and evidence Language used outside a tendering context
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:CandidateStatement` = `The stock is counted every year.`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:Language/cbc:ID` = `en`
- Why: Under Evidence, CandidateStatement is "information about a candidate statement that the
  contracting authority accepts as a sufficient response", and Language is "information about a
  required translation to be part of the response, i.e. the language". Both presuppose a
  procurement procedure with a contracting authority and a response. A business card sent by a
  distributor to a trading customer has neither; the value is a description of how the evidence
  is produced, and the language is the language of the stock count, not a required translation.
- Condition: no CandidateStatement and no Evidence/Language remain in the card, or the card is set
  in a situation where a contracting authority defines accepted statements and translations.
- Options: (a) preferred: drop both and, if needed, put "counted every year" into
  `cac:SuppliedEvidence/cbc:Description`, which already describes the count; (b) keep them only in
  a tendering flow, where these definitions apply.
- Needs decision: no

### sea/01#F4 · Medium · Audit evidence issued by the audited company itself
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Description` = `Year-end count by the auditor.`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:EvidenceIssuingParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: EvidenceIssuingParty is "the Party who issues the evidentiary Document". The evidence is
  typed as an audit report and described as a count by the auditor, yet its issuer is Lumeway
  Distribution, the party whose stock is audited. An audit report is issued by the auditor; issued
  by the company it is a self-declaration and does not support the claim the way the type code and
  text say. It partly survives refutation only because Lumeway could be issuing its own record of
  the count, but then the type is not an audit report.
- Condition: the issuer of the evidence and its type and description agree: either the auditor is
  the EvidenceIssuingParty of an audit report, or Lumeway issues evidence typed and described as
  its own stock record.
- Options: (a) preferred: name the auditing firm as EvidenceIssuingParty, since the text and code
  both say audit; (b) change type and description to a self-declared stock count.
- Needs decision: yes (introduces or names an auditor in the world)

### sea/01#F5 · Low · Receiver's contact: name, job title and department do not agree
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi Trading receives the card as a prospective buyer; its contact is named Purchasing,
  but the job title and department are those of a seller's customer service (they repeat the
  sender's `/BusinessCard/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
  and `/BusinessCard/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`). The same combination
  is on Velumi's contact in 02-Catalogue, 03-DigitalAgreement, 04-DigitalCapability and 05-Order
  (grep over sea `*.xml` for the lines after `<cbc:Name>Purchasing`).
- Condition: Velumi's contact has a job title and department of its purchasing function (or none).
- Options: (a) preferred: a purchasing title and department, since the name and role are purchasing;
  (b) drop JobTitle and Department.
- Needs decision: no

### sea/01#F6 · Low · Full legal and tax data of the receiver in a card about the sender
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Velumi Trading Ltd`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/BusinessCard/cac:ReceiverParty/cbc:IndustryClassificationCode` = `4649`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: The card informs Velumi about Lumeway; it does nothing with Velumi's legal form, size,
  registration date, registration scheme, industry classification or postal address. To address
  the card, identification and an electronic address suffice. The block looks copied from Velumi's
  master data.
- Condition: ReceiverParty carries only what identifies and reaches the receiver, or the card has a
  stated reason for the rest.
- Options: (a) preferred: reduce ReceiverParty to PartyIdentification, PartyName and
  ElectronicAddress; (b) keep, with a reason in the card.
- Needs decision: no

### sea/01#F7 · Low · A gate in AdditionalStreetName of a postal address
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "an additional street name used to further clarify the address".
  "Gate 3" is a vehicle entrance, not a street, and matters for deliveries, not for a postal
  address; the BlockName, BuildingNumber and PlotIdentification already locate the premises. The
  same value occurs on 79 lines over `world/examples/*/*.xml` (grep for
  `<cbc:AdditionalStreetName>Gate 3`).
- Condition: the postal address carries no gate; where a gate matters (delivery, pickup) it is
  given in a delivery location.
- Options: (a) preferred: drop it from the postal address; (b) move it to the delivery or despatch
  location of transport documents.
- Needs decision: no

### sea/01#F8 · Low · Reference with only an ID that does not say what it is
- XPath: `/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB`
- Why: AdditionalDocumentReference is "a reference to an additional document (e.g. presentations)".
  It has no type, description or attachment, so the receiver cannot tell what LD-REG-XB is
  (a register extract?) or why the card refers to it; no example of any flow carries this ID.
- Condition: the reference says what kind of document it is (type code or description) and where
  it can be obtained, or it is removed.
- Options: (a) preferred: add a DocumentTypeCode/DocumentDescription and an attachment or URI, if
  a register extract is meant; (b) drop it.
- Needs decision: no

### sea/01#F9 · Low · Capability validity ends on 30 December without a start
- XPath: `/BusinessCard/cac:BusinessCapability/cac:ValidityPeriod/cbc:EndDate` = `2026-12-30`
- Why: The capability is a stock level supported by the year-end count 2025. A stock level is valid
  until the next year-end count, which would be 31 December; 30 December has no reason in the card,
  and the period has no start (the count date).
- Condition: the validity period matches what supports the claim (e.g. from the 2025 count to the
  next count), or is removed.
- Options: (a) preferred: start at the count date and end at the next count; (b) drop the period.
- Needs decision: no

## Checked and consistent
- GLN `9520610900008` check digit passes (`check_ids.py`).
- SenderParty and BusinessParty are the same party (same register ID 20410274), consistent with the
  definition that the sender may be the owner.
- Capability ValueAmount 1,040,000 XBL for 2,000 benches is 520 XBL per bench; stock capability is
  typed WAREHOUSING, which fits a stock held in Marrowdale.
- WebSiteAccess with login and password fits its definition ("access information … e.g. guest
  credentials") for an extranet offered to one receiver.

## Considered and refuted
- `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: the definition says
  "the number of shares" while the value is an amount in XBL — refuted because the element is an
  Amount type; the definition text is UBL's own inconsistency, and a share capital amount is the
  only value the type can carry.
- `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: an address on Lisavu with
  its English rendering tagged `en-XB` (Bayvarran English), while 05-Order and other Lisavan-issued
  documents tag the same names `en-XL` — refuted for this lens because the tag describes the variety
  of English the document's author writes; the issuer here is Bayvarran. The cross-example
  difference is a matter for the parties lens.
- `/BusinessCard/cac:Signature/cbc:ID`: a signature with only an ID and a signatory — refuted:
  the card is version 2 of a published card, and a signature identifying the signer is a legitimate
  minimal use.
- `/BusinessCard/cbc:PreviousVersionID`: version 1 is not in the flow — refuted: an earlier card can
  exist outside the flow; nothing refers to it.
