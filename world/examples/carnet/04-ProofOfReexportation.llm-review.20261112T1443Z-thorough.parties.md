# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: parties

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### carnet/04#F1 · Medium · A province in Region
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "the recognized geographic or economic region or group of countries in which this address is located"; a province is a subdivision of the country, for which UBL has `CountrySubentity`, where the world puts the Bayvarran states. "Province of Ferrano" is in `Region` in 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no Urvanian province is in `Region`; if given, it is in `CountrySubentity`.
- Options: (a, preferred) move it to `CountrySubentity`; (b) drop it.
- Needs decision: no

### carnet/04#F2 · Medium · Urvania's customs administration described as a company in the commercial register
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania is a state authority (ISIC 8411). It is not a company in a commercial register and has no liquidation status. The same description of customs and maritime authorities occurs in 24 examples (lxml count of PartyLegalEntity by RegistrationName over `world/examples/*/*.xml`).
- Condition: the customs party is not described as registered in a commercial register and carries no liquidation status.
- Options: (a, preferred) drop `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` for public authorities; (b) a register of public bodies with its own type code, if the world has one.
- Needs decision: yes (affects every authority in the examples)

### carnet/04#F3 · Low · Customs VAT registration copied into the proof
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The customs administration appears here because it stamped the re-importation counterfoil that serves as evidence; its own VAT registration plays no part in a proof of re-exportation. It looks copied from master data.
- Condition: the customs party carries no `PartyTaxScheme`, or the document gives a reason for it.
- Options: (a, preferred) drop it.
- Needs decision: no

### carnet/04#F4 · Low · Italian text tagged as English
- XPath: `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: Both renderings carry `languageID="en-XU"` but are Italian. A `languageID` must name the language of the text. 104 examples carry Italian-style street names under an `en-X*` tag; this may be a convention of the world, hence the decision.
- Condition: each rendering is in the language its `languageID` names.
- Options: (a) English renderings ("Border Crossing", "Market Square"); (b) record the Italian-style names as the English exonyms of the world; (c) tag them with the language they are in.
- Needs decision: yes

### carnet/04#F5 · Low · The Selanu chamber's address tagged differently than in 02 and 03
- XPath: `/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: Here the Lisavan address of the Selanu Chamber of Commerce carries its English renderings (street, city, registration city) as `en-XU`; 02 and 03 tag the same renderings `en-XL`. The tag follows the issuer of the document, so the same party's address is described differently from example to example.
- Condition: each party's address renderings carry the same `languageID` in every example of the flow.
- Options: (a, preferred) tag by the address's own country (or plain `en`); (b) keep the issuer-based variant and record it as a convention.
- Needs decision: no

### carnet/04#F6 · Low · A second web domain for the Ferrano chamber
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cac:ExternalReference/cbc:URI` = `https://www.ferrano-chamber.example/ata/carnet-scan.pdf`
- XPath: `/ProofOfReexportation/cac:ExportingGuarantorParty/cac:Contact/cbc:ElectronicMail` = `certificates@camera-ferrano.example`
- Why: The chamber's e-mail domain is `camera-ferrano.example` here and in five other examples (01, 02, 03 and road/06 and road/07, counted with `grep -rl --include='*.xml' camera-ferrano world/examples`); the scan of the carnet is published under `ferrano-chamber.example`, which occurs nowhere else. The same party has two domains without a reason.
- Condition: the chamber's web resources and e-mail use one domain, or the second domain is explained.
- Options: (a, preferred) use `camera-ferrano.example` for the URI.
- Needs decision: no

## Checked and consistent
- Roles: the proof is issued by the Ferrano Chamber (ID prefix `FCC-DOC`, signature `XU-R-105370`), the issuing association that must obtain the proof from its holder and send it to the guaranteeing association abroad (ATA practice, own knowledge); ExportingGuarantorParty is that chamber, ImportingGuarantorParty the Selanu chamber that received the claim (02, 03), and ExportingCustomsParty Urvania's customs, whose stamp on `REIMP-1` is the evidence.
- The three parties' identifiers, names, tax IDs, address IDs, contacts and endpoints agree with 01, 02 and 03 (apart from F5).
- The ExportingCustomsParty contact ("Border office", the customs post at the land border) fits the office that stamped the re-importation counterfoil at "Customs post at the land border, Urvanian side" in 01.

## Considered and refuted
- `/ProofOfReexportation/cac:ImportingGuarantorParty`: in 02 and 03, UBL defines the ImportingGuarantorParty as "the Party who on behalf of their Customs Authority issues the Proof of Reexportation", which would make the Selanu chamber the issuer of this document — refuted because in 02/03 that definition belongs to the request and reminder documents, which the Selanu chamber does issue; in this document UBL defines the ImportingGuarantorParty only as the party "who provides the guarantee for the Goods while being temporarily imported", and the issuing association sending the proof is ATA practice.
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:Contact/cbc:Telefax`: a telefax number for a customs post as a filler — refuted because border customs posts commonly keep fax lines, and the same value is the party's contact in every example.
