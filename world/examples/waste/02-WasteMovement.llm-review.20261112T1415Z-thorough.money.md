# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/02-WasteMovement.xml`, Git blob `32c42c37c829fb72899a0b9b0b8748b5caf542d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

### waste/02#F1 · Low · VAT registrations of every party in a movement document that does nothing with tax
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007337656`
- Why: a WasteMovement is "a document used to report the transport of waste"; it carries no amount, price or tax. `PartyTaxScheme` ("a tax scheme applying to this party") is given in full (VAT, `TaxLevelCode`, tax currency, jurisdiction) for four parties, including the receiving Customs Administration itself, and nothing in the document uses it; the parties are already identified by their register and customs trader IDs. This looks like party master data copied into the document (section 4.8). The invoice that bills this movement (`03-Invoice.xml`) carries the VAT registrations where they are needed. The same pattern occurs widely: of the 241 examples that carry `cac:PartyTaxScheme`, 154 are of non-financial document types (counted with `grep -rl --include='*.xml' '<cac:PartyTaxScheme>'` over `world/examples`, classified by root element).
- Condition: every `PartyTaxScheme` in the movement document has a stated reason in this document, or is absent.
- Options: (a) preferred: remove `PartyTaxScheme` from all parties, because the document identifies them sufficiently otherwise; (b) keep it only where the world's waste-movement rules ask for a tax ID, and remove it from the authority and the carrier.
- Needs decision: no

## Checked and consistent
- No amounts, prices, taxes, payment means or terms in the movement document.
- The movement is the billing basis of `03-Invoice.xml` (referenced there as `03-Invoice.xml:/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`): `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200` kg equals the invoiced `03-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2` t; the parties billed (Rinova Recovery as supplier, Valdara Industries as customer) are the recovery facility and the waste producer/notifier here, with the same VAT registrations.
- Tax scheme currency `XUF` matches the country of every party (XU).
- `check_ids.py`: ISIN `XU0001042501` of the notifier is correct.

## Considered and refuted
- `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`: the invoice bills per tonne collected on this gross weight, and gross includes the 12 big bags' tare — refuted as a money finding because a big bag weighs a few kilograms (own knowledge: about 2–3 kg each, about 30 kg for 12), which does not change the figure at the invoice's precision of 0.1 t (38.17 t rounds to 38.2 t); the weight statement `RR-WB-26-0412` the movement cites is the stated basis.
- `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: share capital in a non-financial document — not a transaction amount; left to the parties/context lenses.
