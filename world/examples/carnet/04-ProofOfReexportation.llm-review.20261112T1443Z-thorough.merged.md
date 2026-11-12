# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/04-ProofOfReexportation.xml`, Git blob `8c48bdf6e2b8e4826241a1f283bf58fe44ebe304` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8533627 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### carnet/04#F1 · Medium · No date of re-exportation or re-importation, though the note relies on it
- XPath: `/ProofOfReexportation/cbc:Note[2]` = `The samples came home on the date stamped.`
- XPath: `/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- Why: A proof of re-exportation has to show that the goods left the country of temporary admission
  within the time limit (01 sets 2026-11-21). The note refers to "the date stamped", but no date of
  re-exportation or re-importation appears anywhere in the document (not on the counterfoil, the
  evidence or the attachment), nor elsewhere in the flow. The importing guarantor cannot see from the
  data that the re-exportation was in time, which is what it needs to release the guarantee.
- Condition: the proof states the date of re-exportation (or of re-importation, as evidence for it)
  in a structured element or at least in the evidence description, and the note refers to a date
  that is in the document.
- Options: (a, preferred) an evidence DocumentReference for the re-importation with its IssueDate
  (see F12); (b) the date in the evidence description or in the note itself.
- Needs decision: no
- From: context (F2), broad (part of F5), logistics (part of F3)

### carnet/04#F2 · Medium · A province in Region
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province is a subdivision of the country (CountrySubentity), where the world
  puts the Bayvarran states. "Province of …" is in Region in 104 examples
  (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no province is in Region; if given, it is in CountrySubentity.
- Options: (a, preferred) move it to CountrySubentity; (b) drop it.
- Needs decision: no
- From: broad (F4), parties (F1)

### carnet/04#F3 · Medium · Urvania's customs administration described as a company in the commercial register
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania (ISIC 8411) is a state authority; it is not in "a
  register of businesses" and has no liquidation status. The same description occurs in 10 examples
  for Urvania's customs, 6 for the Island Customs Service and 7 for Bayvarra's (lxml count over
  `world/examples/*/*.xml`).
- Condition: no business-register scheme and no liquidation status on the customs party.
- Options: (a, preferred) drop both for public bodies; (b) a world register type for public bodies.
- Needs decision: yes (how the world registers public bodies)
- From: broad (F3), parties (F2)

### carnet/04#F4 · Medium · The proof does not identify the carnet or the claim it answers in structured form
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:ID` = `SCC-DOC-26-0726`
- XPath: `03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cbc:ID` = `SCC-DOC-26-0727`
- Why: The document answers the request (02) and reminder (03) about carnet FCC-DOC-26-0724,
  counterfoil IMP-1. A counterfoil ID such as REIMP-1 is unique only within one carnet, and the
  counterfoil's GoodsItemPassportID ("The identifier of the Goods Item Passport or ATA Carnet of this
  counterfoil") is not given; the carnet number appears only in the free text of the attachment.
  Neither the request nor the reminder is referenced: the document type has no dedicated element for
  it, but AdditionalDocumentReference can carry it, and its only reference is a customs record no
  example has. The Selanu chamber and the island's customs, who must close the claim, cannot link the
  proof to the carnet and the claim from the data, and the proof's purpose depends on that link.
- Condition: `GoodsItemPassportCounterfoil/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724` (or the
  carnet is otherwise identified in a structured element), and the document references the request
  SCC-DOC-26-0726 (and optionally the reminder) with its document type.
- Options: (a, preferred) add the carnet ID on the counterfoil and AdditionalDocumentReferences to 02
  (and 03) with a DocumentType; (b) at least the carnet ID.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F1)

### carnet/04#F5 · Low · Italian text tagged as English
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: Both renderings carry `languageID="en-XU"` but are Italian. 104 examples carry Italian-style
  street names under an `en-X*` tag (grep as in carnet/01#F9); it may be a convention of the world.
- Condition: each rendering is in the language its languageID names, or the world records the
  convention.
- Options: (a) English renderings ("Border Crossing", "Market Square"); (b) record the Italian-style
  names as the world's English exonyms; (c) tag them with the language they are in.
- Needs decision: yes (the world's language convention)
- From: parties (F4), broad (part of F7)

### carnet/04#F6 · Low · Customs VAT registration copied into the proof
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The customs administration is here because it stamped the re-importation counterfoil that
  serves as evidence; its own VAT registration plays no part in a proof of re-exportation (no tax is
  charged or reported, as the money part also noted). It looks copied from master data.
- Condition: the customs party carries no PartyTaxScheme, or the document gives a reason for it.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: parties (F3)

### carnet/04#F7 · Low · The Selanu chamber's address tagged differently than in 02 and 03
- XPath: `/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: Here the Lisavan address of the Selanu Chamber of Commerce carries its English renderings
  (street, city, registration city) as `en-XU`; 02 and 03 tag the same renderings `en-XL`. The tag
  follows the issuer of the document, so the same party's address is described differently from
  example to example.
- Condition: each party's address renderings carry the same languageID in every example of the flow.
- Options: (a, preferred) tag by the address's own country (or plain `en`); (b) keep the issuer-based
  variant and record it as a convention.
- Needs decision: no
- From: parties (F5), broad (part of F7)

### carnet/04#F8 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Chambers (ISIC 9411) are associations or public-law bodies; the world's list has a "Register
  of associations". Against it (parties part of 01): chambers can be private associations or
  companies, and the world gives both a register number. The merge could not settle it.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) the association register; (b) as for public bodies (F3).
- Needs decision: yes
- From: broad (F8)

### carnet/04#F9 · Low · Counterfoils listed, evidence and attachment name different counterfoils, and not the one claimed
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:ReexportationEvidence/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID` = `IMP-1`
- XPath: `03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:GoodsItemPassportCounterfoil/cbc:ID` = `IMP-1`
- Why: GoodsItemPassportCounterfoil is "One or more goods item passport or ATA Carnet counterfoils
  associated with this proof of re-exportation". The request and the reminder concern the
  importation counterfoil IMP-1; the proof lists only the re-importation counterfoil REIMP-1, while
  its attachment is the re-exportation counterfoil REEXP-1, which is not listed and is not stated as
  evidence. The evidence ID re-uses the counterfoil ID, so evidence and counterfoil cannot be told
  apart. Both counterfoils are valid ATA evidence (own knowledge: the stamped re-export counterfoil and
  re-importation into the home country are both accepted), so the document should state them
  consistently and link them to the claimed IMP-1.
- Condition: the counterfoils listed include the claimed counterfoil (IMP-1) and every counterfoil
  the proof brings as evidence or attaches, and each evidence has an identifier of its own.
- Options: (a, preferred) list IMP-1, REEXP-1 and REIMP-1, with one ReexportationEvidence each for
  REEXP-1 and REIMP-1 under their own evidence IDs; (b) keep one evidence counterfoil and attach that
  one, so text and structure agree.
- Needs decision: no
- From: broad (F6), context (F4), logistics (F2)

### carnet/04#F10 · Low · Attachment text describes the attachment instead of containing it
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cac:ExternalReference/cbc:URI` = `https://www.ferrano-chamber.example/ata/carnet-scan.pdf`
- Why: EmbeddedDocument is "A clear text object containing an attached document". The value is a
  sentence about the scanned counterfoil, which is itself referenced as a PDF; it does not contain the
  document. A description of an attachment belongs in a description element.
- Condition: EmbeddedDocument, if present, contains the attached document; a description of the
  attachment is in a description element or the Note.
- Options: (a, preferred) remove EmbeddedDocument and describe the scan in the ExternalReference's
  Description; (b) keep only the external reference.
- Needs decision: no
- From: context (F3)

### carnet/04#F11 · Low · A second web domain for the Ferrano chamber
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cac:ExternalReference/cbc:URI` = `https://www.ferrano-chamber.example/ata/carnet-scan.pdf`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:Contact/cbc:ElectronicMail` = `certificates@camera-ferrano.example`
- Why: The chamber's e-mail domain is `camera-ferrano.example` here and in 01, 02, 03, road/06 and
  road/07 (`grep -rl --include='*.xml' camera-ferrano world/examples`, 6 files); the scan is published
  under `ferrano-chamber.example`, which occurs in no other example. The same party has two domains
  without a reason.
- Condition: the chamber's web resources and e-mail use one domain, or the second is explained.
- Options: (a, preferred) use `camera-ferrano.example` for the URI.
- Needs decision: no
- From: parties (F6)

### carnet/04#F12 · Low · Re-importation document identified differently from the carnet, by ID only
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cac:ReimportationDocumentReference/cbc:ID` = `REIMP-1-STAMP`
- Why: The reference carries only an ID; from the ID it is the Urvanian customs' re-importation
  record, but nothing says so, and the carnet references the re-importation as REIMP-1-STAMP, so the
  two cannot be recognised as the same document or told apart. It also sits outside the evidence,
  although Evidence has a DocumentReference and a Party ("the Party who issues the evidentiary
  Document") meant for it.
- Condition: the reference says what it is (type, issuer Customs Administration of Urvania, date),
  and the same customs document has the same ID in 01 and 04.
- Options: (a, preferred) put the re-importation document in ReexportationEvidence/DocumentReference
  with DocumentType and IssueDate (which also meets F1), the customs as Evidence/Party, and the same ID
  in 01; (b) keep the AdditionalDocumentReference and add type and IssueDate.
- Needs decision: no
- From: broad (part of F5), context (F5), logistics (part of F3)

## Checked and consistent
- Dates: issued 2026-08-28 13:19, five days after the reminder (2026-08-23) and before its due date
  2026-09-22, so the claim's duties do not fall due and the flow rightly has no invoice after it
  (money, broad, logistics, context).
- REIMP-1 exists in the carnet
  (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:ID` = `REIMP-1`),
  stamped at the Urvanian land border, which fits "stamped by Urvania's customs" in the evidence; a
  re-importation in the country of exportation is accepted alternative proof (own knowledge: Istanbul
  Convention, Annex A).
- Roles: issued and signed by the Ferrano chamber (`FCC-DOC`, signature XU-R-105370), the issuing
  association that obtains the proof from its holder and sends it to the guaranteeing association
  abroad; ImportingGuarantorParty is the Selanu chamber, ExportingCustomsParty the Urvanian customs,
  whose contact ("Border office") fits the post that stamped REIMP-1. Identifiers, names, tax IDs,
  address IDs, contacts and endpoints agree with 01–03 (language tags aside, F7).
- External reference `application/pdf` with an `.example` URI fits a scan.

## Considered and refuted
- `/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description`: "samples" for exhibits —
  refuted, everyday wording (from broad).
- `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument`: text in an embedded
  document — refuted as a type problem, UBL defines it as "a clear text object" (from broad); that the
  text describes rather than contains the document is F10 (context).
- `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument`: contradiction with
  02's "found no re-export stamp" — refuted as a finding of this example, the holder's stamped
  counterfoil is the evidence that answers a missing customs record; the wording lies in 02 (from
  logistics; see also "Refuted in the merge" and carnet/02#F4).
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyName/cbc:Name`: a party the proof does
  nothing with — refuted, this customs stamped the re-importation counterfoil that is the evidence
  (from context).
- `/ProofOfReexportation`: the proof should say that the claim of 1,300 coral
  (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`)
  is withdrawn — refuted, the claim is conditional on no proof arriving in time, and the document has
  no element for a withdrawn amount (from money).
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID`: a tax
  registration the proof does nothing with — not a money question, left to parties (from money); it
  is F6.
- `/ProofOfReexportation/cac:ImportingGuarantorParty`: in 02 and 03 the ImportingGuarantorParty is
  defined as the party "who on behalf of their Customs Authority issues the Proof of Reexportation" —
  refuted, in this document UBL defines it only as the party "who provides the guarantee for the Goods
  while being temporarily imported" (from parties).
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:Contact/cbc:Telefax`: a fax number as filler —
  refuted, border posts commonly keep fax lines, and it is the party's contact in every example (from
  parties).

## Refuted in the merge
### broad/F1 · High · Attachment says the re-exportation counterfoil was stamped on the island
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- XPath: `/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- Why (broad): the proof is needed because the island's customs found no re-export stamp, so its
  evidence is the re-importation counterfoil; an attachment describing a re-exportation counterfoil
  stamped by the Island Customs Service contradicts the request and makes the re-importation
  evidence pointless.
- Condition (broad): the attachment describes what the proof actually sends (the re-importation
  counterfoil), and no part of the proof says the island stamped the re-exportation. Needs decision:
  no.
- Refuted because: the carnet (01) also shows REEXP-1 stamped at Selanu airport, with its voucher, so
  01 and 04 agree. In the ATA procedure (own knowledge) the stamped counterfoil stays in the carnet
  while customs detach the voucher; when the voucher is missing from the importation office's
  records, that office claims, and the holder proves re-exportation with the stamped counterfoil and,
  as alternative evidence, re-importation at home. Bringing both is not pointless. What remains is the
  wording of 02's note, which is carnet/02#F4, and the inconsistent listing of counterfoils and
  evidence here, which is F9.

## Changed in the merge
- context/F2 (Medium), broad/F5 (Low, date and reference together), logistics/F3 (Low, date and
  reference together) → split: the missing date → F1 at Medium (the proof's purpose depends on it,
  section 6); the untyped re-importation reference and its different ID in 01 → F12 at Low with
  context/F5.
- broad/F2, context/F1, logistics/F1 → F4: combined; condition made checkable (GoodsItemPassportID
  value).
- broad/F6, context/F4 (Needs decision yes), logistics/F2 → F9 at Low, Needs decision no: the fix
  changes the encoding of the counterfoils and evidence, not the story (which already has both
  counterfoils stamped); options of context and logistics merged.
- broad/F7 (Needs decision yes) split: Italian under `en` → F5 with parties/F4 (Needs decision yes);
  the issuer-based region subtag → F7 with parties/F5 (Needs decision no).
- broad/F3, parties/F2 → F3 (counts redone); broad/F4, parties/F1 → F2: combined without change of
  severity.
- broad/F8 → F8 kept; counter-argument from the parties part of 01 added.

## Outside this review
- Whether the re-importation date fits the transport legs of the samples (timeline across
  documents; from logistics).
