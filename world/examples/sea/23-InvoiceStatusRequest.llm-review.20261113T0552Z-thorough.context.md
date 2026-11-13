# LLM review: 23-InvoiceStatusRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/23-InvoiceStatusRequest.xml`, Git blob `d407b8e6ab91b5b8570b7d3b3be6645bd5336a72` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0919fae 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/23#F1 · Low · Tax registration and legal-entity data of the sender in a status request
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyID` = `20410274`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41859`
- Why: An invoice status request asks the buyer whether an invoice has been processed ("A document used to request the status of a previously issued Invoice"). Sender and receiver need to be identified and reachable; the sender's tax scheme (state sales tax registration, tax currency) and both parties' legal-entity descriptions (registration name, register, legal form …) play no part in this exchange. They are master data copied into a document that does not use them; the invoice that the request refers to (`22-Invoice.xml`) already carries them where they matter.
- Condition: Sender and receiver carry identification, name and the contact or address the exchange needs, and no tax or legal-entity data without a reason in this document.
- Options: (a) preferred: reduce both parties to identifier, name, electronic address and contact.
- Needs decision: no

## Checked and consistent
- The request (2026-05-29 10:00) comes after the invoice (`22-Invoice.xml`, 2026-05-14) and before its due date (2026-06-28); the response `24-InvoiceStatusResponse.xml` follows on 2026-05-30 and answers the question in the note ("Approved").
- The referenced invoice `LD-INV-26-0147` exists; sender and receiver are its supplier and customer.

## Considered and refuted
- `/InvoiceStatusRequest/cac:SenderParty/cac:PartyName/cbc:Name`: the seller asking about approval although the receivable is assigned to Harbourline suspected as the wrong sender — refuted because the factoring in this flow is disclosed but Lumeway remains the invoice's issuer and the natural party to follow up approval; the clause on the invoice concerns only where payment goes.
