# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/18-Invoice.xml`, Git blob `8959fff2666b14c481d466f04457f91ebe10f1e4` (committed)
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

### sea/18#F1 · Medium · A gate in the customer's AdditionalStreetName
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A gate of the business park is not a street; it is an access point that matters for vehicles delivering goods, not for the postal address to which the forwarder sends an invoice. The same value occurs 79 times in 76 files over `world/examples/*/*.xml` (25 times in the sea flow; grep over *.xml), always in Lumeway Distribution's postal address.
- Condition: The postal address holds no gate; where the gate matters (delivery), it is in a delivery location or delivery instructions.
- Options: (a) drop the gate from the postal address and give it in `Delivery/DeliveryLocation` or as a delivery note where vehicles must find it (preferred); (b) if the business park's internal road has a name, use that name.
- Needs decision: no

### sea/18#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used". The values repeat the ISO 639 language code of `Language/cbc:ID`, with `listID="ISO 639"`, and name no locale (the parties are Bayvarran, so English in Bayvarra). The same `LocaleCode` = `en` occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country), not a bare language code.
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) give a locale such as `en-XB` with a list identifier that defines locales.
- Needs decision: no

### sea/18#F3 · Low · The contacts on the invoice are operations and sales, not billing
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier is the party that claims payment and the accounting customer the party that pays; their contacts are where questions about the invoice go. Bayforth's contact is its export desk (an operations planner) and Lumeway's is the customer service of its sales department, which serves Lumeway's own customers. Neither handles invoices (accounts receivable at Bayforth, accounts payable at Lumeway). The same contacts are used for all roles of these parties in the flow, so they are master data rather than the contact for this role.
- Condition: The accounting supplier's and accounting customer's contacts are the functions that handle this invoice, and name, job title and department agree.
- Options: (a) billing contacts for the accounting roles (preferred); (b) leave the contacts out of the invoice.
- Needs decision: no

### sea/18#F4 · Low · Master data the invoice does nothing with
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The carrier is not a party to this invoice (Bayforth bills its own service of booking the freight); naming it identifies the booking, but its sales-tax registration, share capital and bookings contact play no part in Bayforth's invoice. The customer's share capital is likewise not needed (where a law asks for share capital on invoices, it asks for the issuer's, not the customer's). Section 4.8 of the review rules: data copied from master data.
- Condition: The carrier is identified (identifier, name) without its tax, capital and contact data; the customer carries no share capital.
- Options: (a) reduce the carrier to `PartyIdentification` and `PartyName` and drop the customer's `CorporateStockAmount`/`FullyPaidSharesIndicator` (preferred); (b) keep them with a reason the invoice needs them.
- Needs decision: no

## Checked and consistent
- Accounting supplier and seller are both Bayforth Forwarding (`20411644`), accounting customer and buyer both Lumeway Distribution (`20410274`); the two pairs carry the same identifiers as in the forwarding instructions `12-ForwardingInstructions.xml` and the export declaration `11-ExportCustomsDeclaration.xml`, where Bayforth is the forwarder and Lumeway the exporter, which fits who bills whom.
- Bayforth's and Lumeway's full descriptions (address, tax scheme, legal entity, contact, electronic address) are identical in every example of the flow that describes them in full (compared element by element with a script).
- The payee account name (`Bayforth Forwarding Ltd`) and its country (`XB`) match the supplier's registered name and country; the GLN `9520610900008` of the customer passes its check digit (check_ids.py).
- The carrier named in the delivery (Tidewell, `20411918`) is the carrier of the referenced bill of lading `14-BillOfLading.xml`.
- Industry classifications fit: 5229 freight forwarding, 4649 wholesale, 5012 sea carrier.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer equal to the accounting customer — refuted because UBL does not condition `BuyerCustomerParty` on being different, and repeating it is harmless.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:BlockName`: a business park as block name — refuted because `BlockName` is an area containing several buildings, which a business park is.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: the customer's customs trader number in an invoice — refuted because the invoice bills an export declaration lodged for that trader, so the number links the service to the declarant.
