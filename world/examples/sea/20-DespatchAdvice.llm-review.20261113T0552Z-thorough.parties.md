# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/20-DespatchAdvice.xml`, Git blob `48649a02a6dba4b51ed92b3c8c00d3a15724cd7a` (committed)
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

### sea/20#F1 · Medium · A gate in the despatch party's AdditionalStreetName
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street; where the gate matters for the despatch it belongs to the despatch (pickup) location, not to the party's postal address. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address; give it in `Shipment/Delivery/DespatchLocation` or a pickup note where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/20#F2 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and name no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/20#F3 · Low · Contact name, job title and department disagree for the recipient and the buyer
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The delivery recipient's contact is its goods-inwards function, which fits the role, but the job title and department make it a customer service officer in Sales, which is not where a warehouse receives goods. The buyer's contact is Purchasing, but again a customer service officer in Sales. Name, title and department of each contact contradict each other; both are the parties' master-data contacts and recur in every example that describes them in full.
- Condition: Each contact's name, job title and department describe the same function: goods receipt at the warehouse, purchasing at the buyer.
- Options: (a) job titles and departments that match the function (e.g. warehouse supervisor in Warehouse operations; buyer in Purchasing) (preferred); (b) drop job title and department and keep the functional name.
- Needs decision: no

### sea/20#F4 · Low · The Lisavu parties' addresses and legal forms are written differently than in the receipt advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: The English renderings of Nalevi's and Velumi's Lisavu addresses carry `languageID="en-XB"` (English as used in Bayvarra), and their legal forms are given in English only, without `languageID`. The receipt advice for this despatch describes the same two parties with `en-XL` and the legal form in Lisavan and English (`21-ReceiptAdvice.xml:/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The tag follows the locale of the issuer rather than the language of the rendering. Over `world/examples/*/*.xml`, English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (counted with lxml over *.xml).
- Condition: Nalevi's and Velumi's addresses and legal forms are described the same way as in the other examples of the flow: the same `languageID` on the same rendering and the legal form in the same languages.
- Options: (a) `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (preferred: the rendering belongs to the place); (b) keep the issuer's locale and state the convention once in the address rules.
- Needs decision: no

### sea/20#F5 · Low · Tax registrations and share capital in a despatch advice
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- Why: A despatch advice describes what is sent and how; it states no prices or taxes. The despatch party's and the carrier's sales-tax registrations and capital stock play no part in it and are copied from master data (section 4.8 of the review rules). The buyer and the delivery recipient, by contrast, carry no tax scheme here.
- Condition: The despatch party and the carrier carry only the party data a despatch advice uses.
- Options: (a) drop their `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator` (preferred); (b) keep them with a reason the despatch advice needs them.
- Needs decision: no

## Checked and consistent
- Despatch party, seller and signatory are Lumeway Distribution (`20410274`); buyer is Velumi Trading (`IC41859`); originator and beneficiary are the Port of Selanu (`IC41037`), as in the order `05-Order.xml` the despatch advice refers to.
- The delivery recipient, Nalevi Warehousing (`IC41722`, ISIC 5210 warehousing), is the delivery party of the order (`05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`) and the party that confirms receipt in `21-ReceiptAdvice.xml`.
- The carrier (Tidewell, `20411918`) is the carrier of the bill of lading `14-BillOfLading.xml`; the manufacturer (Valdara Industries, `XU-R-104274`) is the same in both lines and across the flow.
- Lumeway's GLN `9520610900008` and the items' GTINs pass their check digits (check_ids.py).
- The full descriptions of Lumeway and Tidewell are identical to the other examples of the flow (compared element by element with a script).

## Considered and refuted
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name`: the seller's customer service as despatch contact — refuted because customer service is where a recipient reports delivery problems, which is what the note asks for.
- `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: the buyer's customs trader number in a despatch advice — refuted because the goods cross a customs border and the despatch advice accompanies them to the importer's warehouse.
- `/DespatchAdvice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the Port of Selanu as originator and beneficiary in a despatch advice — refuted because the order names it in both roles, and the despatch advice repeats the order's parties.
