# LLM review: 03-ProofOfReexportationReminder.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/03-ProofOfReexportationReminder.xml`, Git blob `a4b75fb8a0fa66ce587c269390e36886f30cf151` (committed)
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

### carnet/03#F1 · Medium · Duties and tax at risk are more than three times the value of the goods
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Note` = `Duties and import consumption tax of 1,300 coral fall due if no proof arrives within 30 days.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99800`
- XPath: `road/15-Invoice.xml:/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `packaging/09-PurchaseReceipt.xml:/PurchaseReceipt/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The carnet declares the two benches at 99800 XUF. With the rates used elsewhere in the
  world (1 XUF = 0.01 XBL, 1 XBL = 0.4 XLC), that is 99800 × 0.01 × 0.4 = 399.2 XLC. Import duties
  plus import consumption tax on goods worth about 400 XLC cannot reach 1300 XLC (326 % of the
  value) at any ordinary rate (own knowledge: duty on seats a few percent, consumption tax of the
  order of 10–25 %). The claim would be roughly 400 × (1 + duty) × tax rate + duty, i.e. well under
  200 XLC.
- Condition: the amount equals the island's duty and consumption tax on the carnet's customs value,
  converted at the world's exchange rate, with the rates the world gives Lisavu.
- Options: (a, preferred) recompute from 99800 XUF and the Lisavan rates; (b) if a penalty or
  surcharge is meant to be included, say so in the note and keep it plausible.
- Needs decision: yes (the island's duty and tax treatment)

### carnet/03#F2 · Medium · Island Customs Service described as a company in a commercial register
- XPath: `/ProofOfReexportationReminder/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationReminder/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: A customs authority is not in a register of businesses and has no liquidation status. The
  same description occurs in 9 examples.
- Condition: no business-register scheme and no liquidation status on the customs party.
- Options: (a, preferred) drop both; (b) a world register type for public bodies.
- Needs decision: yes

### carnet/03#F3 · Medium · A province in Region
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is a country subdivision (CountrySubentity), not a "region or group of countries".
  104 examples carry `<cbc:Region>Province…`.
- Condition: the province is in CountrySubentity.
- Options: (a, preferred) move it; (b) drop it.
- Needs decision: no

### carnet/03#F4 · Low · The issuer's "endorsement" of its own reminder has no endorsement meaning
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:DocumentID` = `SCC-DOC-26-0726`
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Open`
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode` = `GUARANTOR`
- Why: Endorsement DocumentID is "an identifier for this endorsement", but carries the ID of the
  request 02; ApprovalStatus is "the status of this endorsement", but "Open" is the status of the
  request (still unanswered), not of an approval. The endorser is the Selanu chamber, which also
  issues and signs the reminder, so the endorsement adds nothing an endorsement would add (a third
  party's approval). The request itself is already referenced in
  `/ProofOfReexportationReminder/cac:ProofOfReexportationRequestDocumentReference/cbc:ID` = `SCC-DOC-26-0726`.
- Condition: an IssuerEndorsement, if present, has its own identifier and an approval status, and
  states an endorsement the reminder needs.
- Options: (a, preferred) drop it, the signature covers the issuer; (b) give it a real endorsement
  (own ID, status "Endorsed") and a reason.
- Needs decision: no

### carnet/03#F5 · Low · Address renderings tagged with the issuer's region
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The Urvanian chamber's address is tagged `en-XL` here and `en-XU` in 01 and 04 (and the
  Lisavan addresses the other way round); "Piazza del Mercato" is Italian rather than English.
- Condition: the same address carries the same language tags in every example, each rendering in
  the language its tag names.
- Options: (a, preferred) tag by the address's own country; (b) record a world convention.
- Needs decision: yes

### carnet/03#F6 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportationReminder/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Chambers (ISIC 9411) are associations or public-law bodies; the world list has an
  ASSOCIATION register.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) association register.
- Needs decision: yes

### carnet/03#F7 · Low · Additional reference without a type
- XPath: `/ProofOfReexportationReminder/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: Does not say what it is (presumably the island customs' claim); no example has this ID.
- Condition: the reference states its document type and issuer.
- Options: (a, preferred) add DocumentType and the issuing party.
- Needs decision: no

## Checked and consistent
- ProofOfReexportationRequestDocumentReference SCC-DOC-26-0726 resolves to
  `02-ProofOfReexportationRequest.xml` (same parties, same carnet FCC-DOC-26-0724, same counterfoil
  IMP-1).
- Reminder 30 days after the request (2026-07-24 → 2026-08-23); due date 2026-09-22 = 2026-08-23 +
  30 days, as the note says.
- Amount in XLC with 3 decimals matches the currency's fractional digits (world currency list).
- The note's 1,300 coral equals the PaymentTerms amount.

## Considered and refuted
- `/ProofOfReexportationReminder/cbc:ProcedureCode`: suspected unrelated to a reminder — refuted:
  the reminder is sent under the temporary-admission procedure, and the code means "Temporary
  admission, no previous procedure".
- `/ProofOfReexportationReminder/cac:PaymentTerms`: suspected out of place in a reminder — refuted:
  UBL defines it for "generating a subsequent invoice in case no proof of re-exportation can be
  provided", exactly this use.

## Outside this review
- The timing of the claim against the final re-exportation date of the carnet is raised in the
  review of 02.
