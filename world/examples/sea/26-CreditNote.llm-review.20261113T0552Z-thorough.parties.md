# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/26-CreditNote.xml`, Git blob `27ef7cc12dad5d613bda5ae257e7fc61371126be` (committed)
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

### sea/26#F1 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of the supplier of a credit note. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/26#F2 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/26#F3 · Low · The credit for an assigned receivable leaves out the factor, and is settled differently than the payment shows
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `LD-INV-26-0147`
- XPath: `/CreditNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- Why: The credited invoice was assigned to Harbourline Factoring, its payee, with the clause "Payment to any other account does not discharge the buyer" (`22-Invoice.xml:/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:Clause/cbc:Content` = `Payment to any other account does not discharge the buyer.`), and the factor's statement shows the balance owed to the factor. The credit note names only Lumeway and Velumi, and its terms settle the credit "against the next payment to the seller". Velumi's remittance advice then deducts the credit from its payment to the factor (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `64.00`, payee `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). Netting the seller's credit against the factor's receivable is a matter between three parties; the credit note neither names the factor nor says that it agreed, and its own wording points to a different settlement than the one that happens.
- Condition: The credit note says with whom the credit is settled, consistently with the remittance advice, and where it is netted against the assigned receivable the factor appears (as payee or in a note) and has agreed.
- Options: (a) name the factor as `PayeeParty` and say the credit is deducted from the payment of the assigned invoice to the factor (preferred: matches what the remittance advice does); (b) keep the settlement with the seller and have the remittance advice pay the factor the full amount.
- Needs decision: yes (who carries the credit under the factoring agreement is part of the story)

### sea/26#F4 · Low · The customer's contact does not match its name, nor the claims routing
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CreditNote/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `VT-CLAIMS`
- Why: The buyer routes the credit note to its claims unit, but the customer's contact is named Purchasing while being a customer service officer in Sales: name, title and department disagree, and none of them is the claims or accounts payable function that handles a credit for transport damage.
- Condition: The customer's contact agrees in name, title and department and is the function the credit note is routed to.
- Options: (a) a claims or accounts payable contact matching `VT-CLAIMS` (preferred); (b) drop the contact.
- Needs decision: no

### sea/26#F5 · Low · Velumi's Lisavu address and legal form are written differently than in its own documents
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings carry `languageID="en-XB"` (English as used in Bayvarra) and its legal form is in English only, without `languageID`. In the documents Velumi issues itself it is described with `en-XL` and the legal form in Lisavan and English (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The tag follows the issuer's locale, not the language of the rendering; over `world/examples/*/*.xml`, English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (counted with lxml over *.xml).
- Condition: Velumi's address and legal form are described the same way as in the other examples of the flow.
- Options: (a) `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (preferred: the rendering belongs to the place); (b) keep the issuer's locale and state the convention once in the address rules.
- Needs decision: no

## Checked and consistent
- Supplier and signatory are Lumeway Distribution (`20410274`), the supplier of the credited invoice `22-Invoice.xml`; customer is Velumi Trading (`IC41859`), its customer; the receipt advice `21-ReceiptAdvice.xml` it refers to was issued for the same parties.
- The insurer and policy in the annotation (Wavesure, `WS-CP-26-4471`) are the cargo insurance policy of the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`).
- The manufacturer of the credited side frame (Valdara Industries, `XU-R-104274`) is the same as in the invoice; GLN and GTIN pass their check digits.
- Lumeway's tax registration and share capital on its own credit note are those of the issuer, as on its invoice.

## Considered and refuted
- `/CreditNote/cbc:Note`: the distributor, not the buyer who bore the risk under CIF, claiming from the insurer — refuted because the seller under CIF takes out the policy, and a policyholder may claim with the buyer's consent; the credit note states the goodwill arrangement in which it does so.
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: the customer's customs trader number on a credit note — refuted because a credit on an imported item can bear on the customs value declared for it.
