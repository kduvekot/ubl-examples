# LLM review: 12-FulfilmentCancellation.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/12-FulfilmentCancellation.xml`, Git blob `e80b06a59cdefc8b05210e1023501fad527985dd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### road/12#F1 · Low · Despatch advice referenced in a document that cancels only the receipt advice
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`
- XPath: `/FulfilmentCancellation/cac:ReceiptDocumentReference/cbc:ID` = `LD-RA-26-0162`
- Why: A Fulfilment Cancellation is "a document used to cancel an entire fulfilment document (Despatch Advice or Receipt Advice)"; the document itself carries no other element saying which one it cancels, so its Despatch and Receipt Document References (each defined only as "associated with this document") are what a receiver reads as the documents cancelled. Here the cancellation note and the note "A corrected receipt advice follows" concern only the receipt advice LD-RA-26-0162 (`11-ReceiptAdvice.xml`); the despatch advice CL-DA-26-0153 (`04-DespatchAdvice.xml`) remains valid — the corrected receipt advice still refers to it (`13-ReceiptAdvice.xml:/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`). Listing it as well makes the document readable as cancelling the despatch advice too. Low, because the definitions allow an associated document that is not cancelled.
- Condition: the cancellation names only the document it cancels (the receipt advice); any other document it mentions is referenced in a way that does not mark it as cancelled.
- Options: (a) preferred: remove DespatchDocumentReference (the OrderReference already links the order); (b) move it to an AdditionalDocumentReference, if the despatch party needs the link.
- Needs decision: no

## Checked and consistent
- ReceiptDocumentReference LD-RA-26-0162 resolves to `11-ReceiptAdvice.xml`; the cancellation (2026-03-26 10:46) comes after it (2026-03-25 15:40) and before the corrected advice `13-ReceiptAdvice.xml` (10:48).
- The cancellation reason (the reported short bench did not exist) agrees with the corrected receipt of 96 benches in `13-ReceiptAdvice.xml`.
- The despatch party Castrano Logistics is the party that has to correct its records, so its presence fits.
