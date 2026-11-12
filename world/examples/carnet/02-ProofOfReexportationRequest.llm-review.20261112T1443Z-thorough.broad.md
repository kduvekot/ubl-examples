# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/02-ProofOfReexportationRequest.xml`, Git blob `a90efbc0c48ac2900e792ec8e07f70218ed57e7c` (committed)
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

### carnet/02#F1 · High · "No re-export stamp" contradicts the carnet's stamped re-exportation counterfoil
- XPath: `/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: The request exists because the importation counterfoil IMP-1 was never discharged by a
  re-export stamp. The carnet (01) says its re-exportation counterfoil REEXP-1 at Selanu airport was
  stamped by customs, and the proof (04) attaches that counterfoil as "stamped by the Island
  Customs Service". If either were true, the island's customs would have had its own stamp and no
  reason to request proof.
- Condition: the flow tells one story about REEXP-1: either it was not stamped (and 01 and 04 say
  so, or say nothing about a stamp), or it was, and the request has another cause.
- Options: (a, preferred) keep this note and remove the "stamped" statements from 01 and 04 (see
  their reviews); (b) change the cause of the request.
- Needs decision: no

### carnet/02#F2 · Medium · Island Customs Service described as a company in a commercial register
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: A customs authority (ISIC 8411) is not registered as a business and has no liquidation
  status ("a register of businesses" is the world list's definition of COMMERCIAL). The same
  description of this party occurs in 9 examples (grep over *.xml for the party name and
  COMMERCIAL).
- Condition: the customs party carries no corporate registration scheme of a business register and
  no liquidation status.
- Options: (a, preferred) drop both for public bodies; (b) a world register type for public bodies.
- Needs decision: yes (how the world registers public bodies)

### carnet/02#F3 · Medium · A province in Region
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries"; a province
  belongs in CountrySubentity. 104 examples carry `<cbc:Region>Province…` (grep -rl over *.xml).
- Condition: the province is in CountrySubentity, not in Region.
- Options: (a, preferred) move it; (b) drop it.
- Needs decision: no

### carnet/02#F4 · Low · Request for proof sent before the re-exportation time limit has run out
- XPath: `/ProofOfReexportationRequest/cbc:IssueDate` = `2026-07-24`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- Why: The request treats the importation as undischarged ("found no re-export stamp"), but on
  2026-07-24 the goods may still lawfully be on the island until 2026-11-21. Under the ATA system
  (own knowledge) the importing customs raises a claim when the time limit for re-exportation has
  expired without discharge; before that, a missing re-export stamp proves nothing.
- Condition: the request is issued after the final re-exportation date, or the example says why the
  island's customs know earlier that the goods left without a stamp (for instance a departure
  record without carnet discharge).
- Options: (a) move the request after the time limit (with 03 and 04 following); (b) give the
  earlier trigger in the note; (c) shorten the time limit in 01.
- Needs decision: yes (timeline of the flow's story)

### carnet/02#F5 · Low · Address renderings tagged with the issuer's region
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The Urvanian chamber's address is tagged `en-XL` here and `en-XU` in 01 and 04; the Lisavan
  addresses are `en-XL` here and `en-XU` in 01 and 04. The tag follows the issuing country, so the
  same address differs between examples. "Piazza del Mercato" is also Italian, not English.
- Condition: the same address carries the same language tags in every example, and each rendering
  is in the language its tag names.
- Options: (a, preferred) tag by the address's own country; (b) record a world convention.
- Needs decision: yes (the world's language convention)

### carnet/02#F6 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Both chambers (ISIC 9411) are described as businesses with a liquidation status; the world
  list has an ASSOCIATION register, and chambers are associations or public-law bodies.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) the association register; (b) as for public bodies (F2).
- Needs decision: yes

### carnet/02#F7 · Low · Additional reference without a type
- XPath: `/ProofOfReexportationRequest/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: Presumably the island customs' claim or notice that started the request; the reference does
  not say so and no example has this ID.
- Condition: the reference states what document it is (DocumentType or DocumentTypeCode, issuer).
- Options: (a, preferred) add the type and the issuing party (Island Customs Service).
- Needs decision: no

## Checked and consistent
- GoodsItemPassportID FCC-DOC-26-0724 is the ID of `01-GoodsItemPassport.xml`; counterfoil IMP-1
  exists there (importation at Selanu airport) and is the one an undischarged importation leaves
  open.
- Parties in their roles: importing guarantor (Selanu Chamber of Commerce) issues and signs, the
  exporting guarantor (Ferrano Chamber of Commerce) is the issuing association of the carnet,
  Island Customs Service is the customs that asks; identifiers, contacts and addresses agree with 01.
- 03 refers to this request by its ID SCC-DOC-26-0726.

## Considered and refuted
- `/ProofOfReexportationRequest/cac:ImportingGuarantorParty`: UBL defines it here as the party "who
  on behalf of their Customs Authority issues the Proof of Reexportation" — refuted as an example
  problem: the definition is reused from the proof; the Selanu chamber acting for its customs fits.
- `/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID`: suspected that REEXP-1 should be
  cited — refuted: the open item is the importation counterfoil IMP-1.

## Outside this review
- Problems of the carnet itself (stamps at issue, final re-exportation date on the exportation
  counterfoil) are in the review of 01.
