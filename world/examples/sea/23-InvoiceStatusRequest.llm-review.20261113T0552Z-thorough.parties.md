# LLM review: 23-InvoiceStatusRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

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

### sea/23#F1 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of a party exchanging invoice status messages. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/23#F2 · Medium · A language code in LocaleCode
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/23#F3 · Low · Sales contacts for a question about invoice approval
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The request asks whether the invoice has been approved. The sender's contact is its sales customer service, not accounts receivable; the receiver's contact is named Purchasing but is a customer service officer in Sales, so name, title and department disagree, and none of them is accounts payable, which approves invoices. Both are the parties' master-data contacts.
- Condition: The receiver's contact agrees in name, title and department and is the function that approves invoices; the sender's contact is the one following up the receivable.
- Options: (a) accounts receivable at Lumeway and accounts payable at Velumi (preferred); (b) drop the contacts.
- Needs decision: no

### sea/23#F4 · Low · The receiver's Lisavu address and legal form are written differently than in its own documents
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings carry `languageID="en-XB"` and its legal form is in English only, without `languageID`. In its reply to this request Velumi describes itself with `en-XL` and the legal form in Lisavan and English (`24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The tag follows the issuer's locale, not the language of the rendering; over `world/examples/*/*.xml`, English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (counted with lxml over *.xml).
- Condition: Velumi's address and legal form are described the same way as in the other examples of the flow.
- Options: (a) `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (preferred); (b) keep the issuer's locale and state the convention once in the address rules.
- Needs decision: no

### sea/23#F5 · Low · Tax registration and share capital in a status request
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: An invoice status request identifies sender, receiver and invoice and asks one question. The sender's sales-tax registration and share capital, and both parties' customs trader numbers, play no part in it; they are copied from master data (section 4.8 of the review rules).
- Condition: Sender and receiver carry only the party data the request uses (identification, name, contact, electronic address).
- Options: (a) drop `PartyTaxScheme`, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Sender and signatory are Lumeway Distribution (`20410274`), the supplier of the referenced invoice `22-Invoice.xml`; the receiver is Velumi Trading (`IC41859`), its customer, and the one that answers in `24-InvoiceStatusResponse.xml`.
- Lumeway's description is identical to the other examples of the flow (compared with a script); its GLN passes its check digit.

## Considered and refuted
- `/InvoiceStatusRequest/cac:SenderParty/cac:PartyName/cbc:Name`: the supplier, not the factor, asking about an assigned invoice — refuted because approval by the buyer concerns the supplier's delivery, and the supplier remains the party the buyer deals with about the invoice's content; payment goes to the factor, which the reply confirms.
