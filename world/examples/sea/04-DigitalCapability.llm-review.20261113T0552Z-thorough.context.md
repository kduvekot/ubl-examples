# LLM review: 04-DigitalCapability.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/04#F1 · Medium · A language code in LocaleCode (two places)
- XPath: `/DigitalCapability/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalCapability/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; both hold the ISO
  639 language code that is already in the Language ID next to them, so neither names a locale.
- Condition: LocaleCode absent or holding a locale.
- Options: (a) preferred: a Bayvarran English locale; (b) drop it.
- Needs decision: no

### sea/04#F2 · Low · Capabilities do not say which profiles or formats are supported
- XPath: `/DigitalCapability/cac:DigitalProcess[1]/cbc:Description` = `Receives orders and order changes, sends order responses.`
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- Why: A DigitalCapability provides "information about a business party and its digital trade
  capabilities"; a partner uses it to know which processes, profiles, document formats and channels
  it can use. Both processes carry only an ID and a description: no ProfileID, no collaboration with
  document metadata or delivery channel. The agreement built on it
  (`03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[1]/cbc:ProfileID` =
  `urn:ubl-examples:world:profile:ordering:1.0`) states them, so they were known.
- Condition: each capability process names at least its profile (and, where the agreement relies on
  them, the documents and channel).
- Options: (a) preferred: add ProfileID and the DigitalCollaboration with document metadata, as in
  03-DigitalAgreement; (b) leave as a minimal capability, accepting that the agreement adds what the
  capability left out.
- Needs decision: no

### sea/04#F3 · Low · Billing capability differs from the agreement and the flow
- XPath: `/DigitalCapability/cac:DigitalProcess[2]/cbc:Description` = `Sends invoices and statements, receives remittance advices.`
- XPath: `03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalProcess[2]/cbc:Description` = `Invoice, credit note, statement and remittance advice.`
- Why: Lumeway's billing capability omits the credit notes the agreement includes and that Lumeway
  sends in the flow (`26-CreditNote.xml`), and the invoice status request it sends
  (`23-InvoiceStatusRequest.xml`) and the debit note it receives (`28-DebitNote.xml`). A capability
  that does not cover what the party then exchanges does not describe the party.
- Condition: the billing capability names every billing document Lumeway sends or receives in the
  flow, and agrees with the agreement's billing process.
- Options: (a) preferred: extend the description (and, with F2, the collaborations).
- Needs decision: no

### sea/04#F4 · Low · Signature numbered by Lumeway, signed by the Council
- XPath: `/DigitalCapability/cac:Signature/cbc:ID` = `LD-SIG-26-DC`
- XPath: `/DigitalCapability/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- Why: The document is issued by the Council (`/DigitalCapability/cbc:ID` = `LTAC-DCP-26-0126`) and
  signed by it, but the signature carries Lumeway's numbering prefix (LD-, as in Lumeway's signatures
  `01-BusinessCard.xml:/BusinessCard/cac:Signature/cbc:ID` = `LD-SIG-26-BC`). Either Lumeway signed
  its own capabilities (then the SignatoryParty is wrong) or the Council did (then the ID is not
  Lumeway's).
- Condition: signature ID and signatory belong to the same party.
- Options: (a) preferred: decide who vouches for the capabilities; if the Council publishes them on
  Lumeway's behalf, a Council signature ID; if Lumeway, Lumeway as signatory.
- Needs decision: no

### sea/04#F5 · Low · The Council described as a company in the commercial register
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalCapability/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The sender is the Accord's council (ISIC 9411); a liquidation status and a commercial register
  presuppose a company, and the sender's legal entity plays no role in a capability statement about
  Lumeway.
- Condition: no company-only data for the council, or none of its legal entity at all.
- Options: (a) preferred: reduce SenderParty to identification, name, contact and endpoint.
- Needs decision: yes (what kind of body the Council legally is)

### sea/04#F6 · Low · Receiver's legal entity and address in a capability statement about another party
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The document tells Velumi about Lumeway's capabilities; Velumi's legal form, size, registration
  and address are not used. Looks copied from master data.
- Condition: ReceiverParty carries identification, name, contact and endpoint only.
- Options: (a) preferred: reduce ReceiverParty.
- Needs decision: no

### sea/04#F7 · Low · Velumi's contact: purchasing name with a seller's title and department
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalCapability/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Title and department are those of Lumeway's contact, not of a purchasing function.
- Condition: purchasing title and department, or none.
- Options: (a) preferred: purchasing title and department.
- Needs decision: no

### sea/04#F8 · Low · A gate in AdditionalStreetName
- XPath: `/DigitalCapability/cac:BusinessParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name": a gate is not a street and plays no role in digital capabilities.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- BusinessParty (owner) is Lumeway, SenderParty is the Council acting on its behalf, which the
  SenderParty definition allows ("a third-Party who acts on behalf of the owner"); unlike
  01-BusinessCard, the owner carries the full description here.
- The capabilities (2026-05-05 09:44) precede the agreement that builds on them (03, 12:59 the same
  day); process IDs `ordering` and `billing` match the agreement's.

## Considered and refuted
- `/DigitalCapability/cbc:PreviousVersionID`: version 0.9 not in the flow — refuted: earlier versions
  can exist outside the flow.
