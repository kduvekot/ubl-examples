# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: money

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Checked and consistent
- The request names the carnet (`/ProofOfReexportationRequest/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724`, which is `01-GoodsItemPassport.xml:/GoodsItemPassport/cbc:ID` = `FCC-DOC-26-0724`) and the counterfoil (`IMP-1`), and the tax registration it gives the exporting guarantor, `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007376017`, is the one the carnet gives the same chamber as issuer, `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007376017` (the carnet's `ExportingGuarantorParty` carries only identifier and name).

## Considered and refuted
- `/ProofOfReexportationRequest`: suspected that the request should state the duties at stake, since the exporting guarantor is the party "fiscally responsible" for the counterfoils — refuted because the request only asks for proof; the amount follows in the reminder (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`), and the UBL document has no amount element of its own.
- `/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PartyTaxScheme`: suspected copied master data in a document without a tax transaction — refuted as far as money goes: the definition of the role ("fiscally responsible for the Goods Item Passport counterfoils") gives the guarantor's fiscal identity a reason to be here. Whether it is the right registration for the role is for the parties lens.
