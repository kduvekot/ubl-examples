# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/02-ProofOfReexportationRequest.xml`, Git blob `a90efbc0c48ac2900e792ec8e07f70218ed57e7c` (committed)
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

### carnet/02#F1 · Medium · Proof of re-exportation requested before the re-exportation time limit
- XPath: `/ProofOfReexportationRequest/cbc:IssueDate` = `2026-07-24`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:ValidityPeriod/cbc:EndDate` = `2027-05-25`
- Why: The request starts a claim: the importing guarantor asks for proof because the island's
  customs have no re-export record. Under the ATA Convention (own knowledge) such a claim arises only
  once the time limit for re-exportation has expired without discharge; before that, a missing
  re-export record proves nothing. The carnet the request names (`GoodsItemPassportID`
  FCC-DOC-26-0724) still allows re-exportation until 2026-11-21, almost four months after this
  request, so the goods may lawfully still be on the island. The reminder (03) and its due date
  carry the same problem (see its review).
- Condition: the request is issued after the final re-exportation date the carnet records for the
  importation, or the example says why the island's customs know earlier that the goods left without
  discharge (e.g. a departure record without carnet discharge).
- Options: (a, preferred) give the carnet a final re-exportation date, on the importation counterfoil,
  that has passed by 2026-07-24 (a short fair admission), because the claim story then holds as it
  is; (b) move request, reminder and proof after 2026-11-21; (c) give the earlier trigger in the note.
- Needs decision: yes (timeline of the flow's story)
- From: logistics (F1), broad (F4)

### carnet/02#F2 · Medium · A province in Region
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province is a subdivision of the country, for which UBL has
  CountrySubentity, where the world puts the Bayvarran states. "Province of …" is in Region in 104
  examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: the province is not in Region; if given, it is in CountrySubentity.
- Options: (a, preferred) move it to CountrySubentity; (b) drop it.
- Needs decision: no
- From: broad (F3), parties (F1)

### carnet/02#F3 · Medium · The Island Customs Service described as a company in the companies register
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: A customs authority (ISIC 8411) is not in "a register of businesses" (the world list's
  definition of COMMERCIAL) and has no liquidation status. The same description of the Island Customs
  Service occurs in 6 examples, of Urvania's customs in 10 and of Bayvarra's in 7 (lxml count of
  PartyLegalEntity by RegistrationName with COMMERCIAL over `world/examples/*/*.xml`).
- Condition: the customs party carries no business-register scheme and no liquidation status.
- Options: (a, preferred) drop both for public bodies; (b) a world register type for public bodies.
- Needs decision: yes (how the world registers public bodies)
- From: broad (F2), parties (F2)

### carnet/02#F4 · Low · "No re-export stamp" against a carnet and a proof that show the re-exportation counterfoil stamped
- XPath: `/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cac:VoucherDocumentReference/cbc:ID` = `V-REEXP-1`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: The request's reason is that the island's customs "found no re-export stamp", while the
  carnet shows the re-exportation counterfoil REEXP-1 at Selanu airport stamped, with its voucher
  V-REEXP-1, i.e. by the same Island Customs Service, and the proof later attaches exactly that
  counterfoil stamped. Under the ATA procedure (own knowledge) the documents can be reconciled:
  customs stamp the counterfoil, which stays in the carnet, and detach the voucher; when the voucher
  does not reach the importation office's records, that office claims, and the holder proves with the
  stamped counterfoil. The note, however, says a stamp was not found, not that a voucher or discharge
  is missing, and read literally contradicts 01 and 04. Broad rated this High (a contradiction);
  context and logistics Low (loose wording). The merge could not settle whether it is a contradiction
  or wording.
- Condition: the request's stated reason agrees with what the carnet and the proof say about the
  re-exportation counterfoil and voucher (e.g. "no discharged re-exportation voucher on file").
- Options: (a, preferred) reword the note to the missing voucher or discharge record, which keeps the
  story; (b) if the stamp was really missing, 01 and 04 must not show REEXP-1 stamped (see
  carnet/01#F1).
- Needs decision: yes (whether the story is a missing voucher or a missing stamp)
- From: broad (F1), context (F1), logistics (F2)

### carnet/02#F5 · Low · The same addresses tagged with a different English variant than in 01 and 04
- XPath: `/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: All English renderings here are tagged `en-XL`, including those of the Ferrano chamber's
  Urvanian address, while 01 and 04 tag the same renderings `en-XU`, including those of the Selanu
  chamber. The tag follows the issuer of the document, so the same party's address is described
  differently from example to example.
- Condition: each party's address renderings carry the same languageID in every example of the flow.
- Options: (a, preferred) tag by the address's own country (or plain `en`); (b) keep the issuer-based
  variant and record it as a convention.
- Needs decision: no
- From: parties (F4), broad (part of F5)

### carnet/02#F6 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Both chambers (ISIC 9411) are described as businesses with a liquidation status; the world's
  list has a "Register of associations" (ASSOCIATION). Against it (parties part of 01): chambers can
  be private associations or companies and the world gives both a register number. Whether this is a
  problem depends on what chambers are in the world; the merge could not settle it.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) the association register; (b) as for the public bodies (F3).
- Needs decision: yes
- From: broad (F6)

### carnet/02#F7 · Low · Italian street name tagged as Lisavan English
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The rendering carries `languageID="en-XL"` but is Italian. A languageID names the language of
  the text. 104 examples carry Italian-style street names under an `en-X*` tag
  (`grep -rlE --include='*.xml' 'languageID="en-X[UBL]">(Via|Piazza|Valico|Corso|Strada|Viale|Largo)' world/examples | wc -l`);
  it may be a convention of the world.
- Condition: the rendering is in the language its languageID names, or the world records the
  convention.
- Options: (a) an English rendering ("Market Square"); (b) record the Italian-style names as the
  world's English exonyms; (c) tag the text with the language it is in.
- Needs decision: yes (the world's language convention)
- From: parties (F3), broad (part of F5)

### carnet/02#F8 · Low · Customs reference with only an ID
- XPath: `/ProofOfReexportationRequest/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: The reference is the one document the request rests on (presumably the island customs' claim
  or non-discharge notice), but it has no DocumentType or issuer, and no example has this ID. It is
  also not the importation reference the carnet gives for the same counterfoil
  (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:ImportationDocumentReference/cbc:ID` = `IMP-1-STAMP`),
  which is fine if it is a different document but cannot be told from the data.
- Condition: the reference says what kind of document it is (DocumentType or DocumentTypeCode) and
  who issued it; where it is the importation document, it matches the carnet's reference.
- Options: (a, preferred) add the type and the issuing party (Island Customs Service); (b) drop it.
- Needs decision: no
- From: broad (F7), context (F2), logistics (F3)

## Checked and consistent
- `/ProofOfReexportationRequest/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724` is the ID of
  `01-GoodsItemPassport.xml`; the counterfoil `IMP-1` exists there
  (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:ID` = `IMP-1`)
  and is the one an undischarged importation leaves open (all parts).
- Parties in their roles: the Selanu chamber as ImportingGuarantorParty issues and signs ("on behalf
  of their Customs Authority"), the Ferrano chamber is the ExportingGuarantorParty "fiscally
  responsible" for the counterfoils, the Island Customs Service the ImportingCustomsParty; identifiers,
  names, tax IDs, address IDs, contacts and endpoints agree with 01 (language tags aside, F5).
- The exporting guarantor's tax registration XU007376017 is the one 01 gives the same chamber
  (money).
- Dates: issued 2026-07-24 08:50, after the carnet (2026-05-25), within its validity, before the
  reminder (2026-08-23), which refers to this request by its ID; same ProfileExecutionID.
- Merge: definitions re-read with `annotate.py`; counts redone over `*.xml` only.

## Considered and refuted
- `/ProofOfReexportationRequest/cac:ImportingGuarantorParty`: defined here as the party "who on
  behalf of their Customs Authority issues the Proof of Reexportation" — refuted as an example
  problem, the definition is reused from the proof; the Selanu chamber acting for its customs fits
  (from broad).
- `/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID`: REEXP-1 should be cited —
  refuted, the open item is the importation counterfoil IMP-1 (from broad, logistics).
- `/ProofOfReexportationRequest/cbc:VersionID`: filler — refuted, "the current version of this
  request for proof" fits this document exactly (from context).
- `/ProofOfReexportationRequest/cac:Signature/cbc:ID`: a signature without reason — refuted, a
  guarantor's claim is a formal, signed act in the ATA chain (from context).
- `/ProofOfReexportationRequest`: the request should state the duties at stake — refuted, it only
  asks for proof; the amount follows in the reminder
  (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`),
  and the document type has no amount element (from money).
- `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyTaxScheme/cbc:CompanyID`:
  master data copied into the request — refuted, the exporting guarantor is "fiscally responsible"
  for the counterfoils and liable for the duties claimed from the guarantee (from money, parties).
- `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:Contact/cbc:Name`: "Certificates
  office" rather than a carnet office — refuted as a finding here, it is the chamber's single contact
  in every example; the naming question is carnet/01#F12 (from parties).

## Changed in the merge
- logistics/F1 (Medium), broad/F4 (Low) → F1 at Medium: the request contradicts the time limit in
  the carnet it names, on the basis of the ATA rule (own knowledge); options of both parts merged,
  logistics' preferred option kept.
- broad/F1 (High), context/F1 (Low, needs decision yes), logistics/F2 (Low) → F4 at Low, Needs
  decision yes: the stamped counterfoil in 01 and the attachment in 04 are reconcilable with a
  missing voucher (ATA practice), so it is not a certain contradiction; the merge could not settle it
  and keeps both arguments (section 3, merge). The corresponding broad finding in 01 is under
  "Refuted in the merge" there, since the wording lies in this example.
- broad/F5 (Needs decision yes) split: the issuer-based region subtag → F5 with parties/F4 (Needs
  decision no); Italian under `en` → F7 with parties/F3 (Needs decision yes).
- broad/F2, parties/F2 → F3 (counts redone); broad/F3, parties/F1 → F2; broad/F7, context/F2,
  logistics/F3 → F8: combined without change of severity.
- broad/F6 → F6 kept; counter-argument from the parties part of 01 added.

## Outside this review
- Problems of the carnet itself (stamps at issue, final re-exportation date on the exportation
  counterfoil) are in the review of 01 (from broad).
