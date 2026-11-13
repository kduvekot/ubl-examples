# LLM review: 03-DigitalAgreement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/03#F1 · Medium · The agreement's own terms referenced as a required certification document
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:ID` = `LD-EDI-TERMS-1.0`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentTypeCode` = `774`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentDescription` = `The terms of the digital trade agreement.`
- Why: RequiredCertificationDocumentReference is "a reference to a certification document required
  by this digital agreement", i.e. a certificate the participants must hold (an access point
  accreditation, a conformance certificate). The referenced document is typed 774 (general terms
  and conditions) and described as the terms of the agreement; its XPath points at the agreement's
  own `DigitalAgreementTerms`. Terms are not a certification, and the certifications that do exist
  in the agreement (`LTAC-CERT-26-017`, `ACCORD-CERT-PROC-ordering`, access point certificates) are
  referenced elsewhere.
- Condition: RequiredCertificationDocumentReference refers to a certification the participants are
  required to hold, or is absent; the terms document, if referenced, is referenced from
  DigitalAgreementTerms or as another kind of reference.
- Options: (a) preferred: make the required certification the Accord access-point or process
  certification (the ACCORD-CERT-PROC-… documents already named in the processes), and reference the
  terms document from the terms; (b) drop the element.
- Needs decision: no

### sea/03#F2 · Medium · A language code in LocaleCode (three places)
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used" (for the
  document reference: "the locale in which the language in the referenced document is used"). Each
  holds the ISO 639 language code already in the neighbouring Language ID or LanguageID, so none
  names a locale.
- Condition: every LocaleCode is absent or holds a locale.
- Options: (a) preferred: a Bayvarran English locale; (b) drop them.
- Needs decision: no

### sea/03#F3 · Low · One attachment carries two different files, and a character set for a PDF
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cbc:FileName` = `terms.txt`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:FileName` = `terms-1.0.pdf`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:CharacterSetCode` = `UTF-8`
- Why: Attachment is "the referenced document as an attachment"; here it embeds a plain-text file
  and at the same time points to an external PDF of a different name, so it is unclear which one is
  the referenced document. A PDF/A (`fmt/480`, MimeCode application/pdf, EncodingCode binary) has no
  character set; CharacterSetCode is "the character set of an external document" and applies to text.
- Condition: the attachment holds one rendering of the document (or two renderings explicitly of the
  same content), and CharacterSetCode is present only for a text resource.
- Options: (a) preferred: keep the external PDF with its hash and drop the embedded text and the
  character set; (b) keep only the embedded text.
- Needs decision: no

### sea/03#F4 · Low · External resource expires one day before the document's validity ends
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:ExpiryDate` = `2027-05-04`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`
- Why: ExpiryDate is "the date on which availability of the resource can no longer be relied upon";
  the document stays valid until 2027-05-05 (as does the agreement,
  `/DigitalAgreement/cac:DigitalAgreementTerms/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`), so
  on its last day of validity the terms can no longer be relied upon to be available.
- Condition: the external resource is available at least until the end of the validity period.
- Options: (a) preferred: expiry on or after 2027-05-05.
- Needs decision: no

### sea/03#F5 · Low · Signature verified before the agreement and its required terms were issued
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationTime` = `09:05:00`
- XPath: `/DigitalAgreement/cbc:IssueTime` = `12:59:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:IssueTime` = `12:00:00`
- Why: The Signature is "a signature applied to this document"; it was verified on 2026-05-05 at
  09:05, while the agreement was issued that day at 12:59 and the terms it requires at 12:00. The
  signature's OriginalDocumentReference (`LD-DOC-26-DA-1`, found in no example) could be an earlier
  draft, which is why this is only Low; but then the signature did not cover the terms it binds the
  parties to.
- Condition: the signature's validation time is after the issue of what it signs, or the signed
  original is identified as a document that existed at 09:05.
- Options: (a) preferred: validation after 12:59; (b) describe the signed original.
- Needs decision: no

### sea/03#F6 · Low · Only one participant signs the bilateral agreement
- XPath: `/DigitalAgreement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DigitalAgreement/cbc:AgreementTypeCode` = `BILATERAL`
- Why: A DigitalAgreement supports "business parties agreeing" on processes; a bilateral agreement
  binds both participants, but only the initiator signs. Nothing in the document records Velumi's
  acceptance.
- Condition: both participants' agreement is evidenced (two signatures), or the document states how
  Velumi accepts it.
- Options: (a) preferred: a second Signature by Velumi Trading; (b) a note that acceptance follows by
  a response.
- Needs decision: no

### sea/03#F7 · Low · Agreement country Bayvarra only, although one participant and half the exchanges are in Lisavu
- XPath: `/DigitalAgreement/cac:AgreementCountry/cbc:IdentificationCode` = `XB`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`
- Why: AgreementCountry is "the country to which this digital agreement applies". Velumi Trading is
  established in Lisavu and sends and receives through the agreement there; the agreement as encoded
  does not apply to Lisavu.
- Condition: AgreementCountry lists every country in which the agreement applies, or is absent.
- Options: (a) preferred: add XL; (b) drop AgreementCountry.
- Needs decision: no

### sea/03#F8 · Low · Same service certification for both participants' sending services
- XPath: `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID` = `LTAC-CERT-26-017`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID` = `LTAC-CERT-26-017`
- Why: CertificationDocumentReference is "a reference to a certification document associated with
  this digital service". The sending service of process 1 is Velumi's (`VT-Order-OUT`, participant
  `XL:IC41859`), that of process 2 is Lumeway's (`LD-Invoice-OUT`, participant `XB:20410274`); one
  certificate number for two parties' services, while their access-point certificates differ
  (`LTAC-AP-41859`, `LTAC-AP-20410274`), does not fit. The reference also says nothing about what
  it certifies.
- Condition: each sending service's certification is the one issued for that party's service, or the
  shared document is described as a certification that covers both.
- Options: (a) preferred: one certification number per party's service; (b) a description making
  clear it is a common accreditation.
- Needs decision: no

### sea/03#F9 · Low · Billing process does not cover the billing documents Velumi sends in the flow
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cbc:Description` = `Invoice, credit note, statement and remittance advice.`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:DigitalCollaboration/cac:SendingDigitalService/cbc:ID` = `LD-Invoice-OUT`
- Why: The flow exchanges under the billing profile also an invoice status request and response
  (`23-InvoiceStatusRequest.xml`, `24-InvoiceStatusResponse.xml`) and a debit note from Velumi to
  Lumeway (`28-DebitNote.xml:/DebitNote/cbc:ProfileID` = `urn:ubl-examples:world:profile:billing:1.0`).
  The billing process neither names them nor has a collaboration in which Velumi sends; the only
  billing collaboration runs Lumeway → Velumi. The debit note in turn refers to this agreement as
  its contract.
- Condition: the processes of the agreement cover every document the two participants exchange
  under its profiles, or the flow's other documents do not rely on this agreement.
- Options: (a) preferred: extend the description and add the Velumi → Lumeway collaboration;
  (b) leave as an example of an agreement covering only part of the exchanges, and say so.
- Needs decision: no

### sea/03#F10 · Low · A treaty council described as a company in the commercial register
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The GovernorParty is the Lumeport Trade Accord Council, a body of the Accord (ISIC 9411,
  membership organisation). A liquidation status ("the party's liquidation status") and a
  commercial register entry presuppose a company; for a treaty body they do not apply. The legal
  entity data also plays no role in an agreement the council only governs.
- Condition: the council's legal entity carries no company-only data (liquidation status,
  commercial register), or it is described as the kind of body it is.
- Options: (a) preferred: reduce GovernorParty to identification, name, contact and endpoint;
  (b) a register type for associations or public bodies, without liquidation status.
- Needs decision: yes (what kind of body the Council legally is)

### sea/03#F11 · Low · Velumi's contact: purchasing name with a seller's title and department
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a buyer named Purchasing carries the sales department and customer service
  title of Lumeway's contact.
- Condition: purchasing title and department, or none.
- Options: (a) preferred: purchasing title and department.
- Needs decision: no

### sea/03#F12 · Low · A gate in AdditionalStreetName
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is not a street and
  has no role in a digital agreement.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- Process 1 (ordering): Velumi sends (`XL:IC41859`, ap.velumi.example), Lumeway receives
  (`XB:20410274`, ap.lumeway.example); process 2 (billing) the other way round. Participant IDs agree
  with the parties' ElectronicAddressID; CustomizationID and ProfileID agree with 05-Order
  (`urn:ubl-examples:world:trns:order:1.0`, ordering profile) and 22-Invoice (billing).
- SLA: availability 07:00–19:00 Monday–Friday with maintenance 02:00–04:00 outside it; response,
  incident and recovery durations are plausible for a messaging service.
- AdoptionPeriod (2026-05-05 to 2026-05-19) lies within the validity period and before the first
  order of the flow (05-Order, 2026-05-07).
- InitiatingPartyIndicator true for Lumeway, who issues the agreement.

## Considered and refuted
- `/DigitalAgreement/cac:GovernorParty/cac:PartyName/cbc:Name`: a governor for a bilateral agreement,
  where the definition's example is a multilateral one — refuted: the agreement runs over the
  Accord's network and the council issues the access-point certificates, so a governing body is a
  legitimate reading.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:XPath`: an XPath into the
  agreement next to an internal address `section-2` of the referenced file — refuted as a separate
  finding: the definition allows a location "within the bounding document"; the problem is that the
  reference is not a certification (F1).
- `/DigitalAgreement/cac:ParticipantParty[1]/cac:LegalContact/cbc:Name`: four contacts with names
  only — refuted: functional names are what the Contact definition recommends.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cac:SignatoryParty/cac:PartyName/cbc:Name`:
  the Council as signatory of terms published by Lumeway — refuted: as governor the Council can sign
  (endorse) the terms used under its network; nothing in the flow contradicts it.
