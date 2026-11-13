# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
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

### sea/24#F1 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of a party exchanging invoice status messages. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/24#F2 · Medium · A language code in LocaleCode
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/24#F3 · Low · Sales contacts for the approval of an invoice
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi approves the invoice and announces the payment. Its contact is named Purchasing but is a customer service officer in Sales: name, title and department disagree, and none of them is accounts payable, which approves and pays invoices. The receiver's contact is Lumeway's sales customer service rather than accounts receivable. Both are the parties' master-data contacts.
- Condition: The sender's contact agrees in name, title and department and is the function that approved the invoice; the receiver's contact is the one following up the receivable.
- Options: (a) accounts payable at Velumi and accounts receivable at Lumeway (preferred); (b) drop the contacts.
- Needs decision: no

### sea/24#F4 · Low · Tax registration, share capital and customs numbers in a status response
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: The response says that the invoice is approved and how it will be paid; the receiver's sales-tax registration and share capital and both parties' customs trader numbers play no part in it. They are copied from master data (section 4.8 of the review rules).
- Condition: Sender and receiver carry only the party data the response uses.
- Options: (a) drop `PartyTaxScheme`, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Sender and signatory are Velumi Trading (`IC41859`), the customer of the referenced invoice `22-Invoice.xml`; the receiver is Lumeway Distribution (`20410274`), the sender of the request `23-InvoiceStatusRequest.xml`.
- Velumi's address and legal form carry `en-XL` and Lisavan renderings, as in the other examples issued on the island.
- The note that the balance goes to the factor agrees with the invoice's payee (Harbourline Factoring) and with the remittance advice `27-RemittanceAdvice.xml` it references, whose payee is the same factor.

## Considered and refuted
- `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyName/cbc:Name`: the response going to the supplier rather than the factor — refuted because it answers the supplier's request; the factor is informed through the remittance advice.
