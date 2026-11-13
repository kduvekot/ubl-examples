# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
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

### sea/22#F1 · Medium · A gate in the supplier's AdditionalStreetName
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street; the supplier's postal address on an invoice has no use for it. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/22#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and name no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/22#F3 · Low · The contacts on the factored invoice do not fit their roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The accounting customer's contact is named Purchasing but is a customer service officer in Sales; name, title and department disagree, and none is accounts payable, which receives an invoice. The warehouse's contact is named Goods inwards but is likewise a customer service officer in Sales. The supplier's contact is its sales customer service; with the receivable assigned, questions about payment go to the factor. The factor's contact is its client relationship manager for "client accounts", but the factor's client is Lumeway, not Velumi, which this contact would serve as debtor; a factor's debtor collections function fits the payee role on the invoice the debtor receives.
- Condition: Each contact's name, job title and department agree, and the accounting customer's and payee's contacts are the functions that deal with this invoice and its payment.
- Options: (a) role-specific contacts: accounts payable at Velumi, debtor collections at Harbourline (preferred); (b) drop the contacts that do not serve the invoice.
- Needs decision: no

### sea/22#F4 · Low · The Lisavu parties' addresses and legal forms are written differently than in the other examples
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's and Nalevi's English address renderings carry `languageID="en-XB"` and their legal forms are in English only, without `languageID`. Velumi describes itself, in its own remittance advice for this invoice, with `en-XL` and the legal form in Lisavan and English (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`), and Nalevi does the same in `21-ReceiptAdvice.xml`. The tag follows the issuer's locale, not the language of the rendering. Over `world/examples/*/*.xml`, English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (counted with lxml over *.xml).
- Condition: Velumi's and Nalevi's addresses and legal forms are described the same way as in the other examples of the flow.
- Options: (a) `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (preferred); (b) keep the issuer's locale and state the convention once in the address rules.
- Needs decision: no

### sea/22#F5 · Low · The factor's tax registration and the warehouse's legal entity in the invoice
- XPath: `/Invoice/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41722`
- Why: The factor receives the payment; its sales-tax registration has no bearing on the tax of a supply between Lumeway and Velumi (taxed as an export, category G). The delivery party is named to say where the goods went; its full legal entity description adds nothing to the invoice. Both come from master data (section 4.8 of the review rules).
- Condition: The payee carries no tax scheme and the delivery party no legal entity, unless the invoice has a reason for them.
- Options: (a) drop them (preferred); (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- Supplier and seller are Lumeway Distribution (`20410274`); customer and buyer Velumi Trading (`IC41859`); originator and beneficiary (document and lines) the Port of Selanu (`IC41037`), as in the order `05-Order.xml`; the delivery party Nalevi Warehousing (`IC41722`) is the order's delivery party and the receiver in `21-ReceiptAdvice.xml`.
- Payee, financing party and remittance recipient are the same factor (Harbourline Factoring, `20411233`), and the payee account is in its name (`Harbourline Factoring Ltd`) and its country; this fits invoice type 393 (factored invoice) and the assignment note. The same factor is payee in the statement `25-Statement.xml` and the remittance advice `27-RemittanceAdvice.xml`.
- Harbourline's ISIC 6499 covers factoring; Lumeway's and Velumi's 4649 wholesale; Nalevi's 5210 warehousing.
- Lumeway's tax registration on its own invoice is needed for the supply's tax treatment.
- GLN, GTINs, IBAN-like accounts and RF references pass their checks (check_ids.py).

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: share capital on an invoice — refuted for the supplier, because company law in many countries requires the issuer's share capital on business documents.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: the customer's customs trader number in an invoice — refuted because the commercial invoice supports the import declaration of that trader.
- `/Invoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the port as originator although Velumi placed the order — refuted because `OriginatorCustomerParty` here is "the Party who originated the Order", and the order `05-Order.xml` names the port in that role, from its own requisition.
