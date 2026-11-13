# LLM review: 23-InvoiceStatusRequest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/23-InvoiceStatusRequest.xml`, Git blob `d407b8e6ab91b5b8570b7d3b3be6645bd5336a72` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in the postal address of a party exchanging invoice status messages. The value occurs 79 times in 76 files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>' world/examples`), always in Lumeway Distribution's address (broad counted 76 files).
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it (a delivery location); (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F1), parties (F1)

### sea/23#F2 · Medium · A language code in LocaleCode
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`, recounted).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode` where it only repeats the language; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F2)

### sea/23#F3 · Low · Sales contacts for a question about invoice approval
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The request asks whether the invoice has been approved. The sender's contact is its sales customer service, not accounts receivable; the receiver's contact is named Purchasing but is a customer service officer in Sales, so name, title and department disagree, and none of them is accounts payable, which approves invoices. Both are the parties' master-data contacts, used in every role of the flow.
- Condition: Each contact's name, job title and department agree; the receiver's contact is the function that approves invoices, the sender's the one following up the receivable.
- Options: (a) preferred: accounts receivable at Lumeway and accounts payable at Velumi; (b) drop the contacts.
- Needs decision: no
- From: broad (F2), parties (F3)

### sea/23#F4 · Low · Tax registration, share capital, legal-entity data and customs numbers in a status request
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyID` = `20410274`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41859`
- XPath: `/InvoiceStatusRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: An invoice status request is "A document used to request the status of a previously issued Invoice"; it identifies sender, receiver and invoice and asks one question, without amounts or taxes. The sender's state sales-tax registration and share capital, both parties' legal-entity descriptions (registration, legal form, size, liquidation status) and both customs trader numbers play no part in it; they are master data copied into a document that does not use them (section 4.8). The invoice the request refers to (`22-Invoice.xml`) carries them where they matter. The context part listed the legal entities, the money part the tax scheme and share capital, the parties part also the customs trader numbers; they are one problem and one fix.
- Condition: Sender and receiver carry only the party data the request uses (identification, name, contact, electronic address).
- Options: (a) preferred: drop `PartyTaxScheme`, `PartyLegalEntity` (or at least `CorporateStockAmount`/`FullyPaidSharesIndicator`) and the customs trader identifiers; (b) keep them with a stated reason.
- Needs decision: no
- From: context (F1), money (F1), parties (F5)

### sea/23#F5 · Low · Velumi's Lisavu address tagged en-XB and its legal form in English only
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/InvoiceStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings here carry `languageID="en-XB"` (English as used in Bayvarra), and its legal form is given once, in English, without `languageID`. In its reply to this request Velumi describes itself with `en-XL` and the legal form in Lisavan and English (`24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The tag follows the issuer, not the place; over `world/examples/*/*.xml` English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (parties part, lxml). Whether the tag follows the issuer's English or the place's is not stated anywhere; both are defensible, so the same party is described two ways in one flow.
- Condition: One documented rule decides the tag of English renderings of Lisavu names, and Velumi's address and legal form follow it in every example.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (the rendering belongs to the place); (b) keep the issuer's variety and state the convention once in the address rules.
- Needs decision: yes
- From: parties (F4)

## Checked and consistent
- `LD-INV-26-0147` resolves to `22-Invoice.xml` (issued 2026-05-14); sender and signatory Lumeway Distribution (`20410274`) is its supplier, receiver Velumi Trading (`IC41859`) its customer and the sender of the answer `24-InvoiceStatusResponse.xml` (2026-05-30).
- Request on 2026-05-29 10:00: after the invoice, before the response and before the due date 2026-06-28 (`22-Invoice.xml:/Invoice/cbc:DueDate` = `2026-06-28`).
- Lumeway's GLN `9520610900008` passes `check_ids.py` (re-run by the merge).
- Lumeway's description is identical to the other examples of the flow (parties part, compared with a script).

## Considered and refuted
- `/InvoiceStatusRequest/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: the supplier, not the factor Harbourline, asking about an assigned invoice — refuted because approval of the invoice by the buyer concerns the supplier's delivery and remains the supplier's concern (it bears the risk of disputes under the factoring agreement); the factor's notice concerns only where payment goes, and the reply confirms that (from broad, context, money, parties).
- `/InvoiceStatusRequest/cbc:RequestDate` = `2026-05-29`: no `IssueDate` — refuted because the document type has `RequestDate` as its mandatory date and no issue date of its own (from broad).

## Changed in the merge
- parties/F4 → F5: Needs decision no → yes, because whether the tag follows the issuer or the place is not settled anywhere and both readings are defensible; aligned with the earlier flows (air, wood, plastics, cotton) and the other sea merges.
- context/F1, money/F1, parties/F5 → F4: grouped into one finding (one problem, one fix: copied master data); wording combined.
