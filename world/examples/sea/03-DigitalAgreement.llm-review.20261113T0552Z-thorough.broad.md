# LLM review: 03-DigitalAgreement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

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

### sea/03#F1 · High · Signature verified before the agreement was issued and before the terms it requires existed
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationDate` = `2026-05-05`
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationTime` = `09:05:00`
- XPath: `/DigitalAgreement/cbc:IssueTime` = `12:59:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:IssueTime` = `12:00:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cbc:ValidationTime` = `12:05:00`
- Why: `Signature` is "A signature applied to this document" and `ValidationTime` "The time at which this signature was verified". The signature on the agreement was verified at 09:05 on 2026-05-05, almost four hours before the agreement was issued (12:59) and three hours before the terms document the agreement requires was issued (12:00) and verified (12:05). An agreement that includes those terms cannot have been signed and verified before they existed.
- Condition: on 2026-05-05, terms issue ≤ terms verification ≤ signature verification ≤ agreement issue (or the agreement's issue time is before the verification, if verification by the governor follows the issue).
- Options: (a) preferred: a signature validation time between 12:05 and 12:59; (b) earlier terms and verification times.
- Needs decision: no

### sea/03#F2 · Medium · General terms and conditions given as a required certification document
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentTypeCode` = `774`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentDescription` = `The terms of the digital trade agreement.`
- Why: `RequiredCertificationDocumentReference` is "A reference to a certification document required by this digital agreement" (e.g. a certificate of an access point or of conformance). The referenced document is typed "General terms and conditions" and described as the terms of the agreement, i.e. the content of `DigitalAgreementTerms`, not a certification. Its `XPath` element even points back into this document (`/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:XPath` holds the path "/DigitalAgreement/DigitalAgreementTerms", which moreover lacks the `cac:` prefix and so does not resolve in this document). The certifications the parties do need are referenced elsewhere (`/DigitalAgreement/cac:DigitalProcess[1]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-ordering`).
- Condition: `RequiredCertificationDocumentReference` refers to a certification document, and the terms are referenced from `DigitalAgreementTerms` or given there.
- Options: (a) preferred: move the terms reference into `DigitalAgreementTerms` (e.g. its description plus an attachment) and use `RequiredCertificationDocumentReference` for the accord's access-point or process certificate, if the agreement requires one; (b) drop it.
- Needs decision: no

### sea/03#F3 · Medium · Signature method and encoding disagree with the attached signature format
- XPath: `/DigitalAgreement/cac:Signature/cbc:CanonicalizationMethod` = `http://www.w3.org/2006/12/xml-c14n11`
- XPath: `/DigitalAgreement/cac:Signature/cbc:SignatureMethod` = `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- XPath: `/DigitalAgreement/cac:Signature/cac:DigitalSignatureAttachment/cbc:EmbeddedDocumentBinaryObject/@mimeCode` = `application/pkcs7-signature`
- Why: XML canonicalization and the `xmldsig-more` algorithm URI belong to an XML signature (XMLDSig/XAdES), which `DigitalSignatureAttachment` names as the example ("The actual encoded signature (e.g., in XMLDsig format)"). The attachment is declared as a PKCS#7/CMS signature, which is not canonicalized as XML and identifies its algorithms by OID, not by these URIs (own knowledge of XMLDSig and CMS).
- Condition: canonicalization method, signature method and the attachment's media type describe the same signature format.
- Options: (a) preferred: an XML signature (`application/xml` or the signature embedded) with these URIs; (b) a CMS signature without XML canonicalization.
- Needs decision: no

### sea/03#F4 · Medium · Language code in LocaleCode
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used" (in a document reference: "in which the language in the referenced document is used"). `en` with listID `ISO 639` repeats the language (`LanguageID` = `en` in the reference); it is not a locale. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/03#F5 · Medium · A gate in AdditionalStreetName
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples (`grep -c "Gate 3" world/examples/sea/*.xml`).
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/03#F6 · Low · Signature refers to another document than this agreement
- XPath: `/DigitalAgreement/cac:Signature/cac:OriginalDocumentReference/cbc:ID` = `LD-DOC-26-DA-1`
- XPath: `/DigitalAgreement/cbc:ID` = `LD-DAG-26-0125`
- Why: `OriginalDocumentReference` is "A reference to the document that the signature applies to". The signature is a signature of this document, yet the reference names an ID that is neither this agreement's ID nor any example's ID (`flow_index.py sea`: `-> ?`), and nothing says it is the document image the signatory saw.
- Condition: the reference is this agreement's ID, or it says what the referenced document (e.g. the image signed) is.
- Options: (a) preferred: `LD-DAG-26-0125`; (b) drop the reference, since the signature is embedded in the document it signs.
- Needs decision: no

### sea/03#F7 · Low · Bilateral agreement signed by one party only
- XPath: `/DigitalAgreement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DigitalAgreement/cbc:AgreementTypeCode` = `BILATERAL`
- Why: the document's purpose is "business parties agreeing on a set of digital processes, terms and conditions". Only Lumeway signs, with reason `APPROVAL`; nothing shows that Velumi agreed, although both are `ParticipantParty` and the agreement binds Velumi's access point and services.
- Condition: the agreement shows the consent of both participants (a second signature), or it says it is Lumeway's offer awaiting Velumi's acceptance.
- Options: (a) preferred: a signature of Velumi Trading; (b) keep one signature and make clear in the terms that acceptance happens otherwise.
- Needs decision: no

### sea/03#F8 · Low · Agreement country only Bayvarra, although one participant is in Lisavu
- XPath: `/DigitalAgreement/cac:AgreementCountry/cbc:IdentificationCode` = `XB`
- Why: `AgreementCountry` is "The country to which this digital agreement applies". Velumi Trading is in Lisavu and receives orders and invoices there (`/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cac:Country/cbc:IdentificationCode` = `XL`); the agreement applies to both countries.
- Condition: the agreement countries are the countries of the participants (or the element is absent).
- Options: (a) preferred: add `XL`; (b) drop the element.
- Needs decision: no

### sea/03#F9 · Low · Certification document references with only an ID
- XPath: `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID` = `LTAC-CERT-26-017`
- XPath: `/DigitalAgreement/cac:DigitalProcess[1]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-ordering`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-billing`
- Why: the references give no type, issuer or description; `LTAC-CERT-26-017` is attached to Velumi's sending order service and to Lumeway's sending invoice service (`/DigitalAgreement/cac:DigitalProcess[2]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID`), so one certificate is said to certify services of two different parties, which is not explained.
- Condition: each certification reference says what it certifies (type or description), and one certificate is not attached to two parties' services unless it says it covers both.
- Options: (a) preferred: add type/description and use separate certificate IDs per party's service; (b) drop the service-level references and keep the process-level ones.
- Needs decision: no

### sea/03#F10 · Low · Billing process lists a statement, but the flow's statement comes from a party outside the agreement
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cbc:Description` = `Invoice, credit note, statement and remittance advice.`
- Why: the billing process is agreed between Lumeway and Velumi, and its only collaboration is Lumeway's invoice to Velumi. The flow's statement is issued by Harbourline Factoring (`25-Statement.xml:/Statement/cbc:ID` = `HF-ST-26-0151`, a party not in this agreement), and the invoice names Harbourline as payee (`22-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). The agreement does not cover that party or those exchanges.
- Condition: the documents the billing process names are exchanged between the participants, or the agreement covers the factor's part.
- Options: (a) preferred: drop "statement" from the description (and add collaborations for credit note and remittance advice if they are in scope); (b) add the factor as a participant.
- Needs decision: yes (whether the factoring arrangement belongs in the agreement)

### sea/03#F11 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact is named `Purchasing` with e-mail `purchasing@velumi.example`; job title and department belong to a seller's customer service. Same values in every sea example with this contact.
- Condition: name, job title and department of Velumi's contact describe the same function.
- Options: (a) preferred: purchasing job title and department.
- Needs decision: no

### sea/03#F12 · Low · Trade accord council described as a company with public-service staff
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Contact/cbc:Department` = `Public services`
- Why: the council is classified as a business membership organisation (ISIC 9411) and registered in the commercial register with a liquidation status, i.e. as a private body; its secretariat is staffed by a "Public service officer" in "Public services", i.e. as a public body. Either description may be right, not both.
- Condition: legal entity and contact describe the same kind of body.
- Options: (a) if the council is a treaty body: no commercial registration or liquidation status; (b) if it is an association: a contact of its secretariat ("Secretariat officer").
- Needs decision: yes (what kind of body the council is)

### sea/03#F13 · Low · External terms file: character set for a PDF, and availability ends before the agreement
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:CharacterSetCode` = `UTF-8`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:ExpiryDate` = `2027-05-04`
- XPath: `/DigitalAgreement/cac:DigitalAgreementTerms/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`
- Why: `CharacterSetCode` is "A code signifying the character set of an external document"; a PDF/A file with binary encoding has no single text character set. `ExpiryDate` is the date "on which availability of the resource can no longer be relied upon"; the terms file stops being available a day before the agreement it governs ends.
- Condition: the external PDF carries no character set, and its availability covers the agreement's validity.
- Options: (a) preferred: drop `CharacterSetCode`; expiry on or after 2027-05-05.
- Needs decision: no

### sea/03#F14 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the English renderings of Velumi Trading's address in Lisavu are tagged `en-XB` (English as used in Bayvarra), while the same address of the same party is tagged `en-XL` in the documents Velumi sends itself (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`). Across the sea flow the tag follows the sender's country rather than the address: `en-XB` in 16 examples, `en-XL` in 8 (`grep -c 'languageID="en-XB">Reef Street'` and `'languageID="en-XL">Reef Street'` over `world/examples/sea/*.xml`). The same rendering of the same address should carry the same language tag; for a Lisavu address `en-XL` is the natural one.
- Condition: Velumi's address renderings carry the same `languageID` in every example of the flow.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere; (b) a world-wide rule that the tag is the sender's locale, stated where the world documents its conventions.
- Needs decision: no

## Checked and consistent
- The ordering process's customization and profile match the order and order response (`05-Order.xml:/Order/cbc:CustomizationID` = `urn:ubl-examples:world:trns:order:1.0`, profile `urn:ubl-examples:world:profile:ordering:1.0`); the billing process's customization matches the invoice (`22-Invoice.xml:/Invoice/cbc:CustomizationID` = `urn:ubl-examples:world:trns:billing:1.0`).
- Participant IDs in the delivery channels (`XL:IC41859`, `XB:20410274`) match the parties' electronic addresses; sending and receiving sides are the right parties for order (Velumi → Lumeway) and invoice (Lumeway → Velumi).
- Validity 2026-05-05 to 2027-05-05 and adoption until 2026-05-19 cover the order of 2026-05-07 and the invoice of 2026-05-14.
- SLA: maintenance window 02:00–04:00 lies outside the availability window 07:00–19:00; the durations are plausible. The document hash has the length of a SHA-256 value.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/DigitalAgreement/cac:GovernorParty`: a governor in a bilateral agreement — refuted because the definition only gives a multi-lateral agreement as an example, and the accord council runs the network the agreement uses.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`: the council signing Lumeway's terms file — refuted because the council can endorse terms used on its network; it is not a contradiction.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cbc:EmbeddedDocumentBinaryObject`: a plain-text embedded copy next to the external PDF — refuted because it decodes to a short summary of the terms, a legitimate companion of the full file.
