# LLM review: 03-DigitalAgreement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/03-DigitalAgreement.xml`, Git blob `2af11a686be2a4eb3d82b639256ce234b6e7bcf7` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit a9be40d 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/03#F1 · High · Signature verified before the agreement and the terms it binds were issued
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationDate` = `2026-05-05`
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationTime` = `09:05:00`
- XPath: `/DigitalAgreement/cbc:IssueTime` = `12:59:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:IssueTime` = `12:00:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cbc:ValidationTime` = `12:05:00`
- Why: `Signature` is "A signature applied to this document", `ValidationDate`/`ValidationTime` "The date upon which this signature was verified" and its time. The approval signature (`ReasonCode` `APPROVAL`) was verified on 2026-05-05 at 09:05, 3 h 55 min before the agreement was issued (12:59) and about three hours before the terms it requires were issued (12:00) and verified by the same validator `LTAC-VALIDATOR` (12:05). A signature on version 1.0 cannot be verified before version 1.0 and its terms exist. The context part rated it Low because the signed original (`LD-DOC-26-DA-1`, in no example) could be an earlier draft; the merge does not follow: the element says the signature is applied to this document, and a draft signature would not cover the terms that bind the parties (see also F8).
- Condition: on 2026-05-05, terms issue ≤ terms verification ≤ signature verification, consistent with the agreement's issue time (12:59), or the signed original is identified as a document that existed at 09:05.
- Options: (a) preferred: a validation time after 12:05 (just before or at 12:59), keeping the order terms → verification of terms → signature → issue; (b) earlier terms and verification times.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F5, Low)

### sea/03#F2 · Medium · Signature method and canonicalization are XML-signature URIs, the attachment is a PKCS#7 signature
- XPath: `/DigitalAgreement/cac:Signature/cbc:CanonicalizationMethod` = `http://www.w3.org/2006/12/xml-c14n11`
- XPath: `/DigitalAgreement/cac:Signature/cbc:SignatureMethod` = `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- XPath: `/DigitalAgreement/cac:Signature/cac:DigitalSignatureAttachment/cbc:EmbeddedDocumentBinaryObject/@mimeCode` = `application/pkcs7-signature`
- Why: XML canonicalization 1.1 and the `xmldsig-more` algorithm URI belong to an XML signature (XMLDSig/XAdES), the format `DigitalSignatureAttachment` names ("The actual encoded signature (e.g., in XMLDsig format)"). The attachment is declared as a PKCS#7/CMS signature, which is not canonicalized as XML and identifies its algorithms by OID (own knowledge of XMLDSig and RFC 5652). Method values and media type describe two different signature formats.
- Condition: canonicalization method, signature method and the attachment's media type describe the same signature format.
- Options: (a) preferred: an XML signature (`application/xml`, or the signature in the extension) with these URIs; (b) a CMS signature without an XML canonicalization method.
- Needs decision: no
- From: broad (F3)

### sea/03#F3 · Medium · A language code in LocaleCode (three places)
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used" (in a document reference: the locale "in which the language in the referenced document is used"). Each holds the ISO 639 language code already in the neighbouring `Language/ID` or `LanguageID`, so none names a locale. 362 such `Language/LocaleCode` elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, which also counts the document reference's).
- Condition: every `LocaleCode` is absent or holds a locale (language with region) from a locale list.
- Options: (a) preferred: drop them, as in all earlier flows; (b) a Bayvarran English locale (`en-XB`) from a list of language tags (broad's and context's preference).
- Needs decision: no
- From: broad (F4), parties (F1, the two party places), context (F2)

### sea/03#F4 · Medium · The Trade Accord Council described both as a company in the commercial register and as a public body
- XPath: `/DigitalAgreement/cac:GovernorParty/cbc:IndustryClassificationCode` = `9411`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/DigitalAgreement/cac:GovernorParty/cac:Contact/cbc:Department` = `Public services`
- Why: the governor is the council of the Lumeport Trade Accord: it governs the agreement, runs the network validator and issues the access-point certificates. Its legal entity places it in the federal business register as a commercial registration with a liquidation status ("Active, not in liquidation"), i.e. as a company; its contact is a "Public service officer" in "Public services", i.e. a public body; its ISIC 9411 (business and employers membership organisations) fits an association. A public body is not in a commercial register and has no liquidation status (checklist), and an association is not a company either. The descriptions contradict each other. Earlier flows set public bodies as companies to Medium/no; here it needs a decision, because the council's legal nature (treaty body or association) is not fixed by the document. The same description is used in 04-DigitalCapability.xml.
- Condition: legal entity, industry classification and contact describe the same kind of body; a public or treaty body carries no commercial-register scheme and no liquidation status.
- Options: (a) preferred: treaty body: keep `RegistrationName`, drop `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme` (or use a register of public bodies), as for the public bodies of earlier flows; (b) association: a register type for associations, no liquidation status, and a secretariat contact ("Secretariat officer"); (c) reduce `GovernorParty` to identification, name, contact and endpoint (context).
- Needs decision: yes (what kind of body the council is)
- From: parties (F3, Medium/yes), broad (F12, Low/yes), context (F10, Low/yes)

### sea/03#F5 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name and has no use in a postal address, least of all in a digital agreement. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F5), parties (F2), context (F12, Low)

### sea/03#F6 · Medium · The agreement's own terms referenced as a required certification document
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:ID` = `LD-EDI-TERMS-1.0`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentTypeCode` = `774`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:DocumentDescription` = `The terms of the digital trade agreement.`
- Why: `RequiredCertificationDocumentReference` is "A reference to a certification document required by this digital agreement", i.e. a certificate the participants must hold. The referenced document is typed 774 (general terms and conditions), described as the terms of the agreement, and its `XPath` points at the agreement's own `DigitalAgreementTerms`. Terms are not a certification; the certifications the agreement does use (`ACCORD-CERT-PROC-ordering`, `LTAC-CERT-26-017`, the access-point certificates) are referenced elsewhere (`/DigitalAgreement/cac:DigitalProcess[1]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-ordering`).
- Condition: `RequiredCertificationDocumentReference` refers to a certification the participants must hold, or is absent; the terms document, if referenced, is referenced from `DigitalAgreementTerms` or as another kind of reference.
- Options: (a) preferred: make the required certification the Accord's access-point or process certification and reference the terms from `DigitalAgreementTerms`; (b) drop the element.
- Needs decision: no
- From: broad (F2), context (F1)

### sea/03#F7 · Low · Only one participant signs the bilateral agreement
- XPath: `/DigitalAgreement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DigitalAgreement/cbc:AgreementTypeCode` = `BILATERAL`
- Why: the document serves "business parties agreeing on a set of digital processes, terms and conditions"; a bilateral agreement binds both participants and Velumi's access point and services, but only the initiator signs, and nothing records Velumi's acceptance. The parties part refuted it: the document is issued by the initiating participant, the counterparty's acceptance is a separate act, and nothing claims both signed. Both readings hold; whether Velumi's acceptance belongs in the document is a story question.
- Condition: both participants' consent is evidenced (a second signature), or the document says how Velumi accepts it.
- Options: (a) a second `Signature` by Velumi Trading (broad, context); (b) a note in the terms that acceptance follows separately (parties' reading).
- Needs decision: yes
- From: broad (F7), context (F6); parties (Considered and refuted, carried as counter-argument)

### sea/03#F8 · Low · The signed document reference does not identify the agreement
- XPath: `/DigitalAgreement/cac:Signature/cac:OriginalDocumentReference/cbc:ID` = `LD-DOC-26-DA-1`
- XPath: `/DigitalAgreement/cbc:ID` = `LD-DAG-26-0125`
- Why: `OriginalDocumentReference` is "A reference to the document that the signature applies to". The ID is neither this agreement's nor any example's (`flow_index.py sea`: `-> ?`), and the reference has no type, version or description, so it is unclear what was signed (an image of the agreement, draft 0.9, the terms?).
- Condition: the reference identifies the signed document (this agreement and its version, or a described image of it).
- Options: (a) preferred: the agreement's ID with version 1.0; (b) a described separate ID (`DocumentDescription`, attachment); (c) drop the reference, since the signature sits in the document it signs.
- Needs decision: no
- From: broad (F6), logistics (F2)

### sea/03#F9 · Low · Velumi Trading described differently from the documents it issues (en-XB tags, legal form only in English)
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: as in 01 and 02: the English renderings of Velumi's Lisavu address are tagged `en-XB` and its legal form is given once, in English, while in the order Velumi issues they are `en-XL` and in both languages (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`, `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); the flow splits along the issuer (16 vs 8 sea examples, `grep -c`).
- Condition: Velumi's postal address, registration address and legal form carry the same renderings and `languageID` values in every example, following one documented rule.
- Options: (a) preferred: `en-XL` and the legal form in both languages everywhere; (b) a documented issuer-variety rule, still with the Lisavan legal form.
- Needs decision: yes
- From: broad (F14, Low/no), parties (F4)

### sea/03#F10 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID"; Velumi shares the New Year's Day date with companies in all three registers (271 times in 181 examples, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway has its own (`/DigitalAgreement/cac:ParticipantParty[1]/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1988-10-03`). A default value, not a fact of the world.
- Condition: every `RegistrationDate` is the party's date in the world, or absent.
- Options: (a) preferred: an own date per company; (b) drop it.
- Needs decision: yes
- From: parties (F6)

### sea/03#F11 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact named Purchasing (e-mail `purchasing@velumi.example`) carries the title and department of Lumeway's customer service contact. Its `CommercialContact` "Purchasing" fits (parties).
- Condition: name, job title and department of Velumi's contact describe its purchasing function.
- Options: (a) preferred: a purchasing title and department; (b) drop title and department.
- Needs decision: no
- From: broad (F11), parties (F5), context (F11)

### sea/03#F12 · Low · Agreement country Bayvarra only, although one participant is in Lisavu
- XPath: `/DigitalAgreement/cac:AgreementCountry/cbc:IdentificationCode` = `XB`
- XPath: `/DigitalAgreement/cac:ParticipantParty[2]/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`
- Why: `AgreementCountry` is "The country to which this digital agreement applies". Velumi Trading is established in Lisavu and sends orders and receives invoices there; as encoded the agreement does not apply to Lisavu.
- Condition: `AgreementCountry` lists every country in which the agreement applies, or is absent.
- Options: (a) preferred: add `XL`; (b) drop `AgreementCountry`.
- Needs decision: no
- From: broad (F8), context (F7)

### sea/03#F13 · Low · The XPath of the terms reference selects nothing
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:ReferencedDocumentInternalAddress` = `section-2`
- Why: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:XPath` holds the path "/DigitalAgreement/DigitalAgreementTerms" (quoted here without backticks, since the value is itself a path). `XPath` is "An unambiguous location within the bounding document or the document referenced by the parent DocumentReference, expressed as an XPath". In the referenced PDF/text an XPath has no meaning; in the bounding document the element is `cac:DigitalAgreementTerms` in the UBL namespaces, so a path without prefixes selects nothing. The reference also has the internal address `section-2`, a second, different pointer. The context part refuted this as a separate finding (the definition allows a location in the bounding document; the problem is F6); the merge keeps it, because the path does not resolve as written, whatever F6's outcome.
- Condition: the `XPath`, if kept, selects the intended element in the document it applies to, and does not compete with the internal address.
- Options: (a) preferred: drop the `XPath` and keep `section-2` (the terms are not XML); (b) a namespace-qualified path into this agreement.
- Needs decision: no
- From: logistics (F3); broad (inside F2); context (Considered and refuted, counter-argument above)

### sea/03#F14 · Low · Character set for a PDF, and one attachment with two files
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:CharacterSetCode` = `UTF-8`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:MimeCode` = `application/pdf`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cbc:FileName` = `terms.txt`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:FileName` = `terms-1.0.pdf`
- Why: `CharacterSetCode` is "A code signifying the character set of an external document"; a binary PDF/A has no text character set. The same `Attachment` ("the referenced document as an attachment") embeds a plain-text file and points to an external PDF of another name, so it is unclear which is the referenced document. Broad and logistics refuted the two-file part (the embedded text decodes to a short summary naming version 1.0, a legitimate companion of the full file); the character set remains wrong either way.
- Condition: `CharacterSetCode` is present only for a text resource; the attachment holds one rendering of the document, or two renderings explicitly of the same content.
- Options: (a) preferred: drop `CharacterSetCode`; keep the external PDF with its hash and drop the embedded text (context); (b) keep both renderings and describe the text as a summary (broad's reading).
- Needs decision: no
- From: context (F3), broad (F13, character set); broad and logistics (Considered and refuted, embedded text)

### sea/03#F15 · Low · The terms file stops being available a day before the terms end
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:ExpiryDate` = `2027-05-04`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`
- XPath: `/DigitalAgreement/cac:DigitalAgreementTerms/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`
- Why: `ExpiryDate` is "The date on which availability of the resource can no longer be relied upon"; the terms and the agreement stay valid until 2027-05-05, so during the last day(s) of validity the full terms can no longer be relied upon to be reachable.
- Condition: the external resource is available at least until the end of the terms' validity.
- Options: (a) preferred: expiry on or after 2027-05-05; (b) end the validity periods earlier.
- Needs decision: no
- From: broad (F13), logistics (F4), context (F4)

### sea/03#F16 · Low · Lumeway's own EDI terms shown as signed by the Trade Accord Council
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:URI` = `https://www.lumeway.example/edi/terms-1.0.pdf`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- Why: `ResultOfVerification` is "The result of an attempt to verify a signature associated with the referenced document", its `SignatoryParty` "The signing party". The referenced document is Lumeway's terms (Lumeway numbering `LD-EDI-TERMS-1.0`, published on Lumeway's site), but the verified signature is the council's, which also acts as validator (`LTAC-VALIDATOR`). Broad and context refuted it: as governor of the network, the council can endorse terms used on it, and nothing contradicts that. Both readings hold.
- Condition: the `SignatoryParty` of the verification result is the party that signed the referenced document, and the document's ID and location agree with it.
- Options: (a) Lumeway as signatory of its own terms, the council remaining validator (parties' preference); (b) keep the council and say that it endorses the terms (a certificate of its own, or a description).
- Needs decision: yes
- From: parties (F7); broad and context (Considered and refuted, carried as counter-argument)

### sea/03#F17 · Low · Certification references with only an ID, one certificate for two parties' services
- XPath: `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID` = `LTAC-CERT-26-017`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:CertificationDocumentReference/cbc:ID` = `LTAC-CERT-26-017`
- XPath: `/DigitalAgreement/cac:DigitalProcess[1]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-ordering`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:CertificationDocumentReference/cbc:ID` = `ACCORD-CERT-PROC-billing`
- Why: `CertificationDocumentReference` is "A reference to a certification document associated with this digital service" (or process). The references carry no type, issuer or description. The sending service of process 1 is Velumi's (participant `XL:IC41859`), that of process 2 Lumeway's (`XB:20410274`); one certificate number for two parties' services, while their access-point certificates differ, is not explained.
- Condition: each certification reference says what it certifies; one certificate is attached to two parties' services only if it says it covers both.
- Options: (a) preferred: type/description, and one certification per party's service; (b) drop the service-level references and keep the process-level ones.
- Needs decision: no
- From: broad (F9), context (F8)

### sea/03#F18 · Low · Billing process does not match the billing exchanges of the flow
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cbc:Description` = `Invoice, credit note, statement and remittance advice.`
- XPath: `/DigitalAgreement/cac:DigitalProcess[2]/cac:DigitalCollaboration/cac:SendingDigitalService/cbc:ID` = `LD-Invoice-OUT`
- Why: the billing process's only collaboration is Lumeway's invoice to Velumi. The flow's statement is issued by Harbourline Factoring, a party outside the agreement (`25-Statement.xml:/Statement/cbc:ID` = `HF-ST-26-0151`; the invoice names it payee, `22-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`), and Velumi sends an invoice status request and a debit note under the billing profile (`28-DebitNote.xml:/DebitNote/cbc:ProfileID` = `urn:ubl-examples:world:profile:billing:1.0`), for which no Velumi → Lumeway collaboration exists. The two parts found different sides of the same mismatch; grouped.
- Condition: the processes cover every document the participants exchange under their profiles, and name only exchanges between the participants, or the agreement covers the factor's part.
- Options: (a) preferred: a description matching the exchanges between the two participants (drop "statement"), and a Velumi → Lumeway billing collaboration; (b) add the factor as a participant.
- Needs decision: yes (whether the factoring arrangement belongs in the agreement)
- From: broad (F10, yes), context (F9, no)

## Checked and consistent
- Ordering process: customization and profile match `05-Order.xml:/Order/cbc:CustomizationID` = `urn:ubl-examples:world:trns:order:1.0`; billing matches `22-Invoice.xml:/Invoice/cbc:CustomizationID` = `urn:ubl-examples:world:trns:billing:1.0`.
- Participant IDs of the delivery channels agree with the parties' electronic addresses: `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:SendingDigitalService/cac:DigitalDeliveryChannel/cbc:ParticipantID` = `XL:IC41859` (Velumi sends orders), `/DigitalAgreement/cac:DigitalProcess[1]/cac:DigitalCollaboration/cac:ReceivingDigitalService/cac:DigitalDeliveryChannel/cbc:ParticipantID` = `XB:20410274`; billing runs the other way.
- The agreement is the contract of `06-OrderResponse.xml:/OrderResponse/cac:Contract/cbc:ID` = `LD-DAG-26-0125`; validity 2026-05-05 to 2027-05-05 and adoption until 2026-05-19 cover the order (2026-05-07), the order response (2026-05-08) and the invoice (2026-05-14).
- Terms issued 12:00 and verified 12:05, before the agreement's issue at 12:59; version 1.0 after 0.9.
- SLA: maintenance 02:00–04:00 outside the availability window 07:00–19:00; durations plausible. `PrivatePartyIndicator` true / `PublicPartyIndicator` false fit both companies; `InitiatingPartyIndicator` true for Lumeway, the issuer. The document hash has the length of a SHA-256 value. GLN check digit correct (`check_ids.py`).
- The access-point certificates are issued by the council in all four channels, consistent with it running the network.

## Considered and refuted
- `/DigitalAgreement/cac:GovernorParty`: a governor in a bilateral agreement, where the definition's example is multilateral — refuted: the definition only gives an example, and the council runs the network the agreement uses (from broad, parties, context).
- `/DigitalAgreement/cac:ParticipantParty[2]/cac:CommercialContact/cbc:Name` = `Purchasing` — refuted: for the buyer, purchasing is the right commercial contact (from parties).
- `/DigitalAgreement/cac:ParticipantParty[1]/cac:LegalContact/cbc:Name`: four contacts with names only — refuted: functional names are what the `Contact` definition recommends (from context).
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cbc:EmbeddedDocumentBinaryObject`: an embedded text next to the external PDF — refuted by broad and logistics (summary of the same terms); carried into F14 as counter-argument.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ResultOfVerification/cac:SignatoryParty/cac:PartyName/cbc:Name`: refuted by broad and context — not followed, see F16.
- `/DigitalAgreement/cac:Signature`: one signatory, refuted by parties — not followed, see F7.
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:XPath`: refuted by context as a separate finding — not followed, see F13.

## Changed in the merge
- context/F5 → F1: Low raised to High with broad and logistics (the signature is applied to this document; verified before it existed).
- broad/F4, parties/F1, context/F2 → F3: preferred option set to dropping `LocaleCode`, aligned with earlier flows.
- parties/F3 (Medium/yes), broad/F12 (Low/yes), context/F10 (Low/yes) → F4: grouped (legal entity and contact of the same party); Medium kept from parties (company-only values for a body that is not a company), yes kept (the council's nature).
- context/F12 → F5: Low raised to Medium, aligned.
- broad/F7, context/F6 → F7: needs decision set to yes, because parties' refutation cannot be dismissed.
- broad/F14 (no) + parties/F4 (yes) → F9: grouped, yes.
- broad/F13 split: its character-set part grouped with context/F3 into F14, its expiry part with logistics/F4 and context/F4 into F15.
- broad/F10 (yes) + context/F9 (no) → F18: grouped, yes.
- logistics/F3 → F13 kept although context refuted it as separate.
