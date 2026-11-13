# LLM review: 04-DigitalCapability.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/04-DigitalCapability.xml`, Git blob `6b0fee9db96b3c9a3d5831840cb45c0145a4dc62` (committed)
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

### sea/04#F1 · Low · Signature ID in Lumeway's number series for a signature of the Trade Accord Council
- XPath: `/DigitalCapability/cac:Signature/cbc:ID` = `LD-SIG-26-DC`
- XPath: `/DigitalCapability/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- Why: throughout the flow the prefix of an identifier names the party that assigned it (`LD-` Lumeway Distribution, `TOL-`/`TWL-` Tidewell, `BF-` Bayforth, `PL-` Port of Lumeport, e.g. `PL-SIG-TS-13` signed by the Port of Lumeport in `13-TransportationStatus.xml`). This document is issued by the Council (`LTAC-DCP-26-0126`) and the signatory is the Council, but the signature ID is in Lumeway's series, which reads as Lumeway's signature.
- Condition: the signature ID belongs to the signatory's (or the issuer's) number series.
- Options: an `LTAC-` signature ID (preferred: matches signatory and issuer); or, if Lumeway signs its own capability statement, make Lumeway the signatory.
- Needs decision: no

## Checked and consistent
- Business party identifiers (`20410274`, GLN `9520610900008`, `XB-TR-410274`) and receiver identifiers (`IC41859`, `XL-TR-041859`) agree with `01-BusinessCard.xml` and `05-Order.xml`.
- The two digital processes (`ordering`, `billing`) have the same IDs as the processes of `03-DigitalAgreement.xml`, issued the same day at 12:59, after this document (09:44).
