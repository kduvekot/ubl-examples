# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/01-WasteNotification.xml`, Git blob `59bbf75435c6cd8c4e16f9d3d8ff87cea9ce93be` (committed)
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

### waste/01#F1 · Low · VAT registrations of every party in a notification that does nothing with tax
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007337656`
- Why: a WasteNotification is "a document used to notify the competent authorities of planned movements of waste"; it carries no amount, price or tax. `PartyTaxScheme` is "a tax scheme applying to this party", and each of the four parties here carries a full VAT registration (VAT scheme, `TaxLevelCode`, tax currency XUF, jurisdiction). Nothing in the notification uses them: the parties are already identified by their commercial register IDs (`PartyIdentification`, `PartyLegalEntity/CompanyID`) and the customs trader IDs. The VAT registration of the receiving authority itself (`ReceiverParty`, the Customs Administration) is the least explicable of the four. This looks like party master data copied into the document (section 4.8). Counterargument considered: a competent authority might want a tax ID to identify the notifier; but the notifier is already identified three ways, and the authority's own VAT number serves no purpose. The same pattern is common: of the 241 examples that carry `cac:PartyTaxScheme`, 154 are of document types other than invoices, credit and debit notes, orders, order responses, quotations, catalogues, statements, utility statements, reminders and remittance advices (counted with `grep -rl --include='*.xml' '<cac:PartyTaxScheme>'` over `world/examples`, classified by root element).
- Condition: every `PartyTaxScheme` in the notification has a stated reason in this document (e.g. the competent authority's form asks for the notifier's tax registration), or is absent.
- Options: (a) preferred: remove `PartyTaxScheme` from all parties of the notification, because the document identifies them sufficiently otherwise; (b) keep it only for the notifier/sender if the world's notification rules require a tax ID, and remove it from the authority and the carrier.
- Needs decision: no

## Checked and consistent
- No amounts, prices, taxes on transactions, payment means, accounts or payment terms in the notification; nothing in the money lens to calculate.
- The tax registrations of Valdara Industries (`XU007299291`), Rinova Recovery (`XU007318479`), the Customs Administration (`XU007385602`) and Trasvia Haulage (`XU007337656`) are the same as in `02-WasteMovement.xml` and, for Valdara and Rinova, in `03-Invoice.xml` (`03-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`, `03-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`).
- Tax scheme currency `XUF` (Ferra, 0 decimals, world currency list) matches the country of every party (XU).
- `check_ids.py`: the ISIN `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501` has a correct check digit.

## Considered and refuted
- `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: an amount (share capital) in a document without financial content was suspected as master-data copying — refuted for the money lens because it describes the party's legal entity, not a transaction; whether it belongs in the notification is a question of the parties/context lenses.
