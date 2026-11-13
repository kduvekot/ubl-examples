# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/01-BusinessCard.xml`, Git blob `3b6f96c9fc61de8c4dad42aecf09e84a3a8c83dc` (committed)
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

### sea/01#F1 · Low · Additional document reference with only an ID
- XPath: `/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB`
- Why: `AdditionalDocumentReference` is "A reference to an additional document (e.g. presentations)". The reference carries only the ID: no `DocumentTypeCode`, `DocumentType`, `DocumentDescription` or attachment, and no example of the flow has this ID (`flow_index.py sea` resolves it to `?`). A receiver cannot tell what the document is (the ID suggests a registration extract for Bayvarra, but nothing in the card says so), unlike the brochure next to it, which has its own element and an attachment URI.
- Condition: the reference says what the document is (a type code or description), or it is removed if the card does nothing with it.
- Options: add `DocumentTypeCode`/`DocumentDescription` (and an attachment, if the receiver is to read it) (preferred: keeps the reference useful); or drop the reference.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: the GLN `9520610900008` has a valid check digit; prefix 952 is the GS1 prefix reserved for demonstrations and examples, so it cannot be mistaken for a real company (own knowledge of the GS1 prefix list).
- Party identifiers agree with the rest of the flow: Lumeway `20410274` (XB register), GLN and customs-trader ID `XB-TR-410274` as in `02-Catalogue.xml`, `05-Order.xml`, `07-TransportServiceDescriptionRequest.xml`; Velumi `IC41859` and `XL-TR-041859` as in `05-Order.xml`.
- The stock capability (2,000 benches in Marrowdale) fits the later story: the order of 96 benches is delivered "from the distributor's stock" and pre-carried by truck from Marrowdale to Lumeport (`09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:OriginalDespatchTransportationService/cbc:Name` = `Truck from Marrowdale to the port of Lumeport`); `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount` = `1040000.00` equals 2,000 × 520 XBL, the catalogue trade price.
- Dates: issued 2026-05-04 16:39, after the catalogue of the same day (09:17); the capability validity ends 2026-12-30, after every document of the flow.

## Considered and refuted
- `/BusinessCard/cac:BusinessCapability/cac:ValidityPeriod/cbc:EndDate` = `2026-12-30`: suspected an off-by-one against a year-end stock count (31 December) — refuted because the definition gives no rule for the end date and a validity ending before the next count is a legitimate choice.
- `/BusinessCard/cac:BrochureDocumentReference/cbc:ID` = `LD-BROCHURE-2026`: resolves to no example — refuted as a problem because the element names the kind of document and the attachment URI points to it.
