# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: parties

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.


## Findings

### carnet/02#F1 · Medium · A province in Region
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "the recognized geographic or economic region or group of countries in which this address is located"; a province is a subdivision of the country, for which UBL has `CountrySubentity` ("the political or administrative division of a country in which this address is located"), and the Bayvarran states in the world are given there. "Province of Ferrano" is in `Region` in 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: the Ferrano chamber's province is not in `Region`; if given, it is in `CountrySubentity`.
- Options: (a, preferred) move it to `CountrySubentity`; (b) drop it.
- Needs decision: no

### carnet/02#F2 · Medium · The island's customs service described as a company in the companies register
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ProofOfReexportationRequest/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Island Customs Service is a state authority (ISIC 8411). A state authority is not entered in a companies register and has no liquidation status ("the party's liquidation status"). The same description of customs and maritime authorities occurs in 24 examples (lxml count of PartyLegalEntity by RegistrationName over `world/examples/*/*.xml`).
- Condition: the customs party is not described as registered in a companies register and carries no liquidation status.
- Options: (a, preferred) drop `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` for public authorities; (b) describe a register of public bodies with its own type code, if the world has one.
- Needs decision: yes (affects every authority in the examples)

### carnet/02#F3 · Low · Italian street name tagged as Lisavan English
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The rendering carries `languageID="en-XL"` (English as used in Lisavu) but is Italian. A `languageID` must name the language of the text. 104 examples carry Italian-style street names under an `en-X*` tag; this may be a convention of the world, hence the decision.
- Condition: the rendering is in the language its `languageID` names.
- Options: (a) an English rendering ("Market Square"); (b) record the Italian-style names as the English exonyms of the world; (c) tag the text with the language it is in.
- Needs decision: yes

### carnet/02#F4 · Low · The same addresses tagged with a different English variant than in 01 and 04
- XPath: `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: All English renderings in this example are tagged `en-XL`, including those of the Ferrano chamber's Urvanian address, while 01 and 04 tag the same renderings `en-XU`, including those of the Selanu chamber. The tag follows the issuer of the document, so the same party's address is described differently from example to example.
- Condition: each party's address renderings carry the same `languageID` in every example of the flow.
- Options: (a, preferred) tag by the address's own country (or plain `en`); (b) keep the issuer-based variant and record it as a convention.
- Needs decision: no

## Checked and consistent
- Roles against their UBL definitions: ImportingGuarantorParty (Selanu Chamber of Commerce) is the party who "on behalf of their Customs Authority issues" this document; the ID prefix `SCC-DOC` and the signature agree. ExportingGuarantorParty (Ferrano Chamber) is "fiscally responsible for the Goods Item Passport counterfoils" (the issuing association of carnet `FCC-DOC-26-0724` in 01). ImportingCustomsParty (Island Customs Service) "originally requests the Proof of Reexportation"; the note says the island's customs found no stamp.
- All three parties have the same identifiers, names, tax IDs, address IDs, contacts and endpoints as in 01 (apart from the language tags of F4).

## Considered and refuted
- `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyTaxScheme/cbc:CompanyID`: the chamber's VAT number as master data copied into the request — refuted because the exporting guarantor is the party liable for the duties claimed from the guarantee, so its fiscal identification is relevant to the claim.
- `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:Contact/cbc:Name`: the Ferrano chamber's contact is its "Certificates office" rather than a carnet office — refuted as a separate finding here; it is the chamber's single contact in every example (01, 02, 03, 04, and the certificates of origin in road), so it is a choice of the world, and the naming question is raised in 01#F11.

## Outside this review
- Outside the parties lens: the note "The island's customs found no re-export stamp." against the re-exportation counterfoil `REEXP-1` marked "Stamped by customs." in 01 (for the logistics and context parts).
