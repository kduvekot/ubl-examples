# LLM review: 23-InvoiceStatusRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/23-InvoiceStatusRequest.xml`, Git blob `d407b8e6ab91b5b8570b7d3b3be6645bd5336a72` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/23#F1 · Medium · Gate number in AdditionalStreetName of the sender's postal address
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name, and is not part of a postal address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/23#F2 · Low · Contacts do not fit an invoice status enquiry
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The request asks whether the invoice has been approved. The sender's contact is customer service in Sales, the receiver's "Purchasing" also in Sales; the people who ask and answer about invoice approval are accounts receivable and accounts payable. The receiver's name and department also contradict each other.
- Condition: Sender and receiver contacts are the ones who handle invoice status (receivables / payables), and each contact's name and department agree.
- Options: accounts receivable at Lumeway, accounts payable at Velumi (preferred).
- Needs decision: no

## Checked and consistent
- `LD-INV-26-0147` resolves to `22-Invoice.xml`; sender Lumeway is its supplier, receiver Velumi its customer.
- Request on 2026-05-29 10:00, 15 days after the invoice (05-14) and before the response of 05-30 (`24-InvoiceStatusResponse.xml`) and the due date.
- GLN `9520610900008` passes `check_ids.py`.

## Considered and refuted
- `/InvoiceStatusRequest/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: under the assignment to Harbourline Factoring the factor might ask — refuted: approval of the invoice by the buyer remains the seller's concern (and the factor's notice says only where to pay).
- `/InvoiceStatusRequest/cbc:RequestDate` = `2026-05-29`: no `IssueDate` — refuted: the document type has `RequestDate` as its mandatory date and no issue date of its own.
