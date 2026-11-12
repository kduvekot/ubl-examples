# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/01#F1 · Medium · Language code in LocaleCode of the buyer
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode/@listID` = `ISO 639`
- Why: UBL defines Language. Locale Code as "A code signifying the locale in which this language is used." A locale is a language in a region (e.g. English as used in Bayvarra, the form the examples use themselves in `languageID="en-XB"`). `en` from ISO 639 is a language code and only repeats `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`. The seller's Language in the same document carries no LocaleCode. The same value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the buyer's Language either has no LocaleCode, or a LocaleCode that names a locale (language plus region) from a list of locales, not a bare ISO 639 language code.
- Options: (a) drop LocaleCode (preferred: Language/ID already says English and nothing in the order depends on the locale); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47) as listID.
- Needs decision: no

### rail/01#F2 · Medium · Gate in AdditionalStreetName of the buyer's postal address
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is not a street name but an entrance of the site, which only matters to vehicles delivering there (section 5: a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles). The address is the party's business address (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AddressTypeCode` = `BUSINESS`), used for every purpose of the party. AdditionalStreetName starting with "Gate" occurs in 76 example files (`grep -l 'AdditionalStreetName>Gate'` over `*.xml`).
- Condition: Lumeway's postal address has no gate in AdditionalStreetName (or anywhere else in the postal address).
- Options: (a) remove the gate from the postal address and, where a delivery needs it, state it at the delivery location (e.g. in `cac:DeliveryTerms/cac:DeliveryLocation`) (preferred); (b) if "Gate 3" is in fact part of the official address in Bayvarra, say so in the world's address rules and use the element the format defines for it.
- Needs decision: no

### rail/01#F3 · Medium · Province in Region of the seller's address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The buyer's Bayvarran address in the same document uses CountrySubentity for its state (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where the province is given, it is in cbc:CountrySubentity (optionally with CountrySubentityCode).
- Options: (a) move the province to CountrySubentity (preferred: the element's definition names provinces, and it matches the Bayvarran addresses); (b) drop it where the postal zone and city already locate the address.
- Needs decision: no

### rail/01#F4 · Low · Seller's address and legal form described differently from the other examples
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Valdara Industries appears with a full description in eight examples of the flow. In all others the English renderings of its address are tagged `en-XU` (e.g. `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XU`) and the legal form is given in Urvanian and English (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). Here the same text is tagged `en-XB` and the legal form has a single rendering without languageID. The order is written by a Bayvarran buyer, which may explain the tag, but the same party is then described in two ways within one flow.
- Condition: Valdara's address renderings and legal form carry the same text and the same languageIDs in every example of the flow, or the difference follows a stated rule (e.g. the issuer's locale) applied to every party of the document.
- Options: (a) describe Valdara as in the other examples (`en-XU`, both legal-form renderings) (preferred: the party's own master data); (b) keep the issuer's locale, but then apply it consistently and record the rule.
- Needs decision: no

### rail/01#F5 · Low · "English" renderings of the seller's address and legal form are Italian
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Section 5 asks for each repeated rendering to be in the language its languageID names. The street name tagged as English (`en-XB`) is Italian ("street of the workshops"), and the legal form is Italian with an English gloss (own knowledge of Italian). The Urvanian rendering (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`) is a different name, so the Italian text is neither the local name nor English. The pattern is world-wide: 63 example files have an `en-XU` street name starting with Via, Viale, Piazza, Valico, Corso, Largo or Strada (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that Urvanian places and legal forms have Italianate names in English usage and the rendering is that established English-usage name.
- Options: (a) record in the world's story that English usage keeps Italianate exonyms for Urvania, and keep the values (preferred if that is the intent: it is a world decision, not an encoding error); (b) translate into English (e.g. "Workshops Street"); (c) tag the text with the language it is in, if Italian exists in the world.
- Needs decision: yes

### rail/01#F6 · Low · Buyer's contact is its sales customer service
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party. Contact is "The primary contact for this party". In an order the buyer's contact is the one the seller asks about the order: purchasing. Lumeway's sales customer service serves Lumeway's own customers. The same contact is used for Lumeway in every role in the flow (consignee, accounting customer).
- Condition: the buyer's contact in the order is a purchasing (or order-handling) function of Lumeway, with matching name, job title and department.
- Options: (a) a purchasing contact (e.g. "Purchasing", buyer, department Purchasing) (preferred); (b) give Lumeway role-specific contacts in its master data so each document picks the fitting one.
- Needs decision: no

### rail/01#F7 · Low · Seller master data the order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: data copied from a party's master data into a document that does not use it is a finding. The order is written by the buyer; nothing in it depends on the seller's stock-exchange listing, on the seller's warehousing provider Castrano Logistics (the order names no despatch party or despatch place), or on either party's share capital.
- Condition: every element of the parties' legal entity and service providers present in the order has a purpose in the order.
- Options: (a) drop SecurityListing, ServiceProviderParty and CorporateStockAmount from the order (preferred); (b) keep the service provider only if the order gets a role for it (e.g. a despatch party or place).
- Needs decision: no

### rail/01#F8 · Low · Delivery location identified elsewhere by GLN, here by text only
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rail siding of Lumeway Distribution, Marrowdale`
- Why: The waybill identifies the same place with a GLN (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9520610900015`, check digit correct, prefix 952 is GS1's range for examples). Section 5: a location carries its identifier where the same place is identified elsewhere. The order, which sets the delivery place under DAP, does not.
- Condition: the order's delivery location carries the siding's GLN (and the name) used in the waybill.
- Options: (a) add the GLN and a Name to the DeliveryLocation (preferred: the buyer owns the GLN); (b) leave it, if the GLN is assigned only later — then the world should say so.
- Needs decision: no

## Checked and consistent
- Lumeway Distribution is described identically (54 values) in the Order, the transport request and plan, the transit declaration, the waybill and the goods invoice (`11-Invoice.xml`); Valdara Industries identically in all examples except the differences in F4.
- GLN `9520610900008` (Lumeway) and ISIN `XU0001042501` (Valdara): check digits correct (`check_ids.py`). GS1 prefix 952 is reserved by GS1 for demonstrations; country code XU in the ISIN is a user-assigned ISO 3166 code, so neither is a real assigned value.
- ISO 6523 ICD `0990` in `0990:10427` is not an assigned ICD (own knowledge: assigned ICDs end well below 0990).
- Roles: buyer Lumeway, seller Valdara, delivery party Lumeway with the same register ID; the invoice `11-Invoice.xml` has the same buyer and seller.
- Buyer's tax scheme (state sales tax, Upland State, in XBL) and seller's (national VAT in XUF) fit their countries; registration and tax names agree within each party.
- Codana Identification Agency as issuer of the property identifier: same ID and name as in `06-TransitCustomsDeclaration.xml` and `11-Invoice.xml`.

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: a sales order desk as the seller's contact in an order — refuted because that is exactly the role (the seller's order handling).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: delivery party equal to the buyer — refuted because UBL's Delivery Party is "The Party who receives the goods" and under DAP to Lumeway's own siding the buyer does receive them.
