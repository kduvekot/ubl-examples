# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### air/01#F1 · Medium · Language code `en` in LocaleCode
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." A locale is a language as used in a region (such as English as used in Bayvarra), not the language itself. The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries, so the element repeats the language instead of stating a locale. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples`).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode` where the party has no locale beyond its language; (b) carry a real locale (e.g. a BCP 47 tag such as `en-XB`, with a listID naming that list), if the world has a reason to state the locale.
- Needs decision: no

### air/01#F2 · Medium · A gate in AdditionalStreetName of a postal address
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but the entrance of the site where vehicles or visitors come in, i.e. information about access, not part of the postal address of Lumeway Distribution (whose street, building number, block and plot are already given). The skill's checklist for addresses: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles." The same value occurs 79 times in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate; where the gate matters (a pickup or delivery place), it is carried by an element meant for it (e.g. the description of the pickup or despatch `Location`), not as a street name.
- Options: (a) preferred: remove it from the postal address; (b) move it to the pickup/despatch location of the documents that need it (forwarding instructions, despatch advice).
- Needs decision: no

### air/01#F3 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Nalevi Warehousing)
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date `1996-01-01` (a New Year's Day) is given for 25 different companies in three countries and three registers (XB:FBR, XL:ICR, XU:CR), among them Bayforth Forwarding, Kelaro Air Cargo, Nalevi Warehousing, Velumi Trading, Selanu Airport Cargo and Lumeport Airport Cargo Terminal, while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`, Lisavu Cotton Farm `2009-08-17`). It occurs in 181 examples (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`; companies counted by RegistrationName over all `*.xml`). Unless the world has an event that registered all these companies on that day (e.g. a register re-founded under the Trade Accord, which would not explain the XU and XB registers that have earlier dates), it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) give each company a date that fits its history (company histories are open work for the encyclopaedia); (b) drop `RegistrationDate` where no date is known; (c) if 1996-01-01 is an event in the story (a new register), keep it and say so there.
- Needs decision: yes (company histories)

### air/01#F4 · Low · Contact job title and department contradict the contact name
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`; `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`; `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales` (Velumi Trading)
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`; `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`; `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales` (Nalevi Warehousing)
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The functional name says what the contact does, but its job title and department say something else: Nalevi Warehousing's `Goods inwards` contact (the contact of the party receiving the goods) is a customer service officer in Sales; Velumi Trading's `Purchasing` contact (the buyer's or consignee's contact) is a customer service officer in Sales. Name, job title and department of one contact do not agree with each other, and they do not show which function fits the party's role here. The same combinations recur for these parties in every example of the flow (and `Purchasing` with `Customer service officer`/`Sales` in 52 places over all `*.xml`, `grep -rh -A2 '<cbc:Name>Purchasing</cbc:Name>'`).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role in the document (a buyer's contact buys, a delivery party's contact receives goods, a carrier's contact handles the transport).
- Options: (a) preferred: give each party's contact a job title and department that match its functional name (e.g. Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse; Cargo sales: cargo sales agent / Sales, or rename the Kelaro contact to a cargo operations desk); (b) drop `JobTitle` and `Department` where they add nothing to the functional name.
- Needs decision: no

## Checked and consistent
- Lumeway Distribution is described identically wherever it appears in full: register `20410274`, GLN `9520610900008` (check digit correct, `check_ids.py`; GS1 prefix 952 is GS1's range for demonstrations, so not a real company), customs trader `XB-TR-410274`, tax number `UL-1230822` at state level with tax scheme `STT` and jurisdiction Upland State, which matches its `CountrySubentityCode` `XB-UL`; legal entity Ltd, MEDIUM, registered 1988-10-03 in the federal business register.
- Velumi Trading (`IC41859`, customs trader `XL-TR-041859`), Nalevi Warehousing (`IC41722`), Port of Selanu (`IC41037`) and Valdara Industries (`XU-R-104274`) carry the same identifiers as in the order this change refers to: `sea/05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `IC41859`, `sea/05-Order.xml:/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `IC41037`, `sea/05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PartyIdentification/cbc:ID` = `IC41722`, and with the same contacts.
- Kelaro Air Cargo `IC41311` in `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyIdentification/cbc:ID` is the carrier of the waybill: `04-Waybill.xml:/Waybill/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `IC41311`.
- Industry codes (ISIC Rev.4): Lumeway and Velumi `4649` (wholesale of household goods, including furniture), Nalevi `5210` (warehousing and storage); they fit what the parties do.
- Telephone numbers `+999 …`: E.164 country code 999 is not assigned to any country (reserved by the ITU), so the numbers cannot be mistaken for real ones (own knowledge); web and mail domains use `.example`.

## Considered and refuted
- `/OrderChange/cac:AccountingCustomerParty` and `/OrderChange/cac:AccountingSupplierParty`: suspected redundant copies of buyer and seller — refuted because their UBL definitions carry no "if different" condition and they only repeat the identifier, as the order does (`sea/05-Order.xml:/Order/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `IC41859`).
- `/OrderChange/cac:Delivery/cac:NotifyParty`: the delivery party Nalevi Warehousing is also the notify party; suspected redundant — refuted because the changed delivery ends at the airport (`/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal`), so the warehouse has to be notified to collect the goods there.
- `/OrderChange/cac:Delivery/cac:CarrierParty`: under CPT the seller contracts the carriage, so the buyer naming the carrier was suspected — refuted because the order change only names the expected airline, which the later waybill confirms; it does not contract it.
- `/OrderChange/cac:OriginatorCustomerParty` and `/OrderChange/cac:BeneficiaryParty` (Port of Selanu): suspected not to fit a company — refuted because the order is for the harbour parks of Selanu (`/OrderChange/cbc:CustomerReference` = `Harbour parks Selanu`), which the port company originates and benefits from, as in the order.
- English renderings of the island addresses carry `en-XL` here (e.g. `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`); the inconsistency with other examples is recorded in the reviews of the examples that use `en-XB`, since `en-XL` fits island names.
- `/OrderChange/cac:BuyerCustomerParty/cac:Party`: no `PartyTaxScheme` for Velumi Trading — refuted as a gap: the order change does nothing with the buyer's tax registration.
- `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: fits the definition (an area surrounded by streets with several buildings).
