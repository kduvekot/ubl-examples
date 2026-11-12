# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/04-ProofOfReexportation.xml`, Git blob `8c48bdf6e2b8e4826241a1f283bf58fe44ebe304` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### carnet/04#F1 · High · Attachment says the re-exportation counterfoil was stamped on the island
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- XPath: `/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- Why: The proof is needed because the island's customs found no re-export stamp (02), and its
  evidence is therefore the re-importation counterfoil stamped in Urvania. The attachment, however,
  describes a re-exportation counterfoil stamped by the Island Customs Service: that contradicts the
  request and makes the evidence of re-importation pointless.
- Condition: the attachment describes what the proof actually sends (the carnet with its
  re-importation counterfoil stamped by Urvania's customs), and no part of the proof says that
  the island stamped the re-exportation.
- Options: (a, preferred) let the attachment be the scan of the carnet's re-importation counterfoil
  REIMP-1; (b) drop the embedded text and keep only the external reference.
- Needs decision: no

### carnet/04#F2 · Medium · The proof does not identify the carnet or the claim in structured form
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724`
- Why: The document answers the request 02 / reminder 03 for carnet FCC-DOC-26-0724, counterfoil
  IMP-1. Its only structured link is a counterfoil ID "REIMP-1", which is not unique without the
  carnet number; the counterfoil's GoodsItemPassportID ("the identifier of the Goods Item Passport
  or ATA Carnet of this counterfoil") is not given, and the carnet number appears only in the free
  text of the attachment. Neither the request nor the reminder is referenced (the document type has
  no dedicated element, but AdditionalDocumentReference is available). The receiving chamber and
  customs need these to close the claim.
- Condition: the proof carries the carnet number in a structured element (the counterfoil's
  GoodsItemPassportID) and refers to the request SCC-DOC-26-0726 (or the reminder).
- Options: (a, preferred) add GoodsItemPassportID to the counterfoil and an AdditionalDocumentReference
  to SCC-DOC-26-0726; (b) at least the GoodsItemPassportID.
- Needs decision: no

### carnet/04#F3 · Medium · Exporting customs described as a company in a commercial register
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania is a state authority; it is not in a register of
  businesses and has no liquidation status. The same description occurs in 12 examples.
- Condition: no business-register scheme and no liquidation status on the customs party.
- Options: (a, preferred) drop both; (b) a world register type for public bodies.
- Needs decision: yes

### carnet/04#F4 · Medium · A province in Region
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province belongs in CountrySubentity, not in Region ("region or group of countries").
  104 examples carry `<cbc:Region>Province…`.
- Condition: the province is in CountrySubentity.
- Options: (a, preferred) move it; (b) drop it.
- Needs decision: no

### carnet/04#F5 · Low · The date of re-importation is referred to but not given
- XPath: `/ProofOfReexportation/cbc:Note[2]` = `The samples came home on the date stamped.`
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- Why: Whether the proof is accepted depends on the goods having left the island before the final
  re-exportation date (2026-11-21 in 01); the note points to "the date stamped" but no date is in
  the document. The re-importation document is given by ID only, without type, issuer or date,
  and outside the Evidence aggregate whose DocumentReference and Party ("the Party who issues the
  evidentiary Document") are meant for it.
- Condition: the proof states the re-importation date and identifies the re-importation document
  with its type, issuer (Customs Administration of Urvania) and date.
- Options: (a, preferred) put the re-importation declaration in ReexportationEvidence/DocumentReference
  with IssueDate and DocumentType, and the customs in Evidence/Party; (b) keep the
  AdditionalDocumentReference and add type and IssueDate.
- Needs decision: no

### carnet/04#F6 · Low · The counterfoil the proof discharges is not named
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:GoodsItemPassportCounterfoil/cbc:ID` = `IMP-1`
- Why: The request and the reminder ask about the importation counterfoil IMP-1. The proof lists
  only REIMP-1, which is already its evidence (ReexportationEvidence ID REIMP-1). The counterfoil
  "associated with this proof" that the island's customs must close is IMP-1.
- Condition: the proof names the counterfoil it discharges (IMP-1), with the re-importation
  counterfoil as evidence.
- Options: (a, preferred) list IMP-1 (and keep REIMP-1 in the evidence); (b) list both.
- Needs decision: no

### carnet/04#F7 · Low · Address renderings tagged with the issuer's region
- XPath: `/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: The Selanu chamber's address is tagged `en-XU` here and `en-XL` in 02 and 03. The
  Urvanian street names tagged as English ("Piazza del Mercato", "Valico di Confine") are Italian.
- Condition: the same address carries the same language tags in every example, each rendering in
  the language its tag names.
- Options: (a, preferred) tag by the address's own country; (b) record a world convention.
- Needs decision: yes

### carnet/04#F8 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Chambers (ISIC 9411) are associations or public-law bodies; the world list has an
  ASSOCIATION register.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) association register.
- Needs decision: yes

## Checked and consistent
- Issued 2026-08-28, within the 30 days the reminder set (due 2026-09-22).
- Issuer and signatory: Ferrano Chamber of Commerce, the carnet's issuing association (01), which
  answers the importing guarantor; parties agree with 01–03 apart from the language tags.
- A re-importation in the country of exportation as alternative proof of re-exportation is in line
  with the ATA system (own knowledge: Istanbul Convention, Annex A, alternative proofs).
- External reference MIME type application/pdf fits a scan.

## Considered and refuted
- `/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description`: "samples" for exhibits —
  refuted: everyday wording.
- `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument`: text in an embedded
  document — refuted as a type problem: UBL 2.5 defines it as "a clear text object containing an
  attached document"; the content is F1.
