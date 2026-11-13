# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
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

### sea/05#F1 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/05#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/05#F3 · Low · Velumi Trading and Nalevi Warehousing described differently from the documents that answer this order (en-XL renderings and Lisavan legal form here, en-XB and English only there)
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: Here the English renderings of both Lisavan parties carry `languageID="en-XL"` and the legal form is given in Lisavan and English. The order response to this order describes the buyer with `languageID="en-XB"` and the legal form once, in English, without `languageID`: `06-OrderResponse.xml:/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`; the bill of lading does the same for Nalevi Warehousing: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the en-XB form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the en-XL form. A party’s address names and legal form do not change with the issuer, and the checklist asks that the same party be described the same way in every example. This example has the fuller description; the finding is that the flow is not consistent.
- Condition: Velumi Trading and Nalevi Warehousing carry the same address renderings, `languageID` values and legal-form renderings in every example of the flow.
- Options: Preferred: use this example’s description (Lisavan and en-XL renderings, legal form in both languages) in every example, because those are the names used in Lisavu. Alternative: record a world rule that the English rendering is tagged with the issuer’s variety of English, and still give the Lisavan legal form everywhere.
- Needs decision: yes

### sea/05#F4 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/05#F5 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (buyer) and Nalevi Warehousing (delivery party). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

### sea/05#F6 · Low · Delivery location named as a warehouse that cannot be linked to the delivery party
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Lanoro warehouse, Selanu`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[1]` = `Vilafa Natii`
- Why: The delivery location is given only as a description, `Lanoro warehouse, Selanu`, with no identifier or address, while the delivery party Nalevi Warehousing has its postal address in Vilafa Natii (Lagoon Road) 9. Nothing says that the Lanoro warehouse is Nalevi’s, and the name occurs in no other example of the world (`grep -rl --include='*.xml' Lanoro` finds only this file); the packing list says only "Deliver to the buyer’s 3PL, Nalevi Warehousing, Selanu" (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:DeliveryInstructions` = `Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.`). The checklist asks that a location carry the identifier or address by which the same place is identified elsewhere.
- Condition: The delivery location of the order can be linked to the delivery party and to the place of delivery in the transport documents (the same address or identifier).
- Options: Preferred: give the location Nalevi’s warehouse address (or an identifier used for it in the transport documents) and keep the name. Alternative: drop the location and let the delivery party’s address stand for it, if the goods go to that address.
- Needs decision: no

### sea/05#F7 · Low · The delivery party’s contact: goods inwards described as a sales customer-service officer
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of the warehouse that receives the goods is called `Goods inwards`, which fits the delivery party, but its job title and department are the sales customer-service pair the world uses for sellers (the same as Lumeway Distribution’s). Goods receipt is a warehouse operations function; name, title and department do not agree.
- Condition: Name, job title and department of Nalevi Warehousing’s contact agree with each other and with goods receipt.
- Options: Preferred: a warehouse or goods-receipt title and department (e.g. operations). Alternative: keep only the functional name.
- Needs decision: no

## Checked and consistent
- Buyer and accounting customer are both Velumi Trading (`IC41859`); seller is Lumeway Distribution, as in the catalogue 02-Catalogue.xml the order lines refer to.
- Originator and beneficiary are the Port of Selanu (`IC41037`) at document and line level, consistent with the customer reference `Harbour parks Selanu` and with 06-OrderResponse.xml, which carries the port’s request `PS-REQ-26-0031` as originator document.
- The manufacturer of both items is Valdara Industries and the property identifier issuer Codana Identification Agency, with the same identifiers as in 02-Catalogue.xml.

## Considered and refuted
- `/Order/cac:AccountingCustomerParty`: the accounting customer equals the buyer — refuted: UBL sets no "if different" condition on this element in an order, and the buyer is indeed the party invoiced (22-Invoice.xml).
- `/Order/cbc:AccountingCost` = `Stock for municipal projects` while the beneficiary is a port company — refuted for the parties lens: it is Velumi’s own cost allocation, not a statement about the beneficiary.
