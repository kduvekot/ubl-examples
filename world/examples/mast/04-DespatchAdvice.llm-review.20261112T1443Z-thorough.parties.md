# LLM review: 04-DespatchAdvice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/04-DespatchAdvice.xml`, Git blob `96e68e1c850420976f9df7c6ba1c6da30707cd43` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### mast/04#F1 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language code again. 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale with a matching listID.
- Options: (a, preferred) `en-XB` from a locale list (BCP 47); (b) drop it.
- Needs decision: no

### mast/04#F2 · Low · Contacts that do not fit despatch and receipt
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- Why: The despatch party's contact answers for the despatch, and the delivery recipient's contact receives the goods; the note asks the recipient to "check the goods on arrival and report any damage". Here they are Saltmere's procurement "Bids office" and Selanu Telecom's sales desk for business customers. The carrier's contact is called "Cargo sales" while its job title and department are operations.
- Condition: the despatch party's contact handles despatch, the delivery customer's contact receives goods, and the carrier contact's name agrees with its job and department.
- Options: (a, preferred) a despatch contact for Saltmere, a goods-receiving contact for Selanu Telecom, "Cargo operations" for Kelaro.
- Needs decision: no

### mast/04#F3 · Low · Selanu Telecom and Kelaro described differently than in the order and the waybill
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `03-Waybill.xml:/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: In 01 and 03 the legal forms of Selanu Telecom and Kelaro Air Cargo are given in Lisavan and English with `languageID`s, and their English address renderings are tagged `en-XL`; here each legal form has one rendering without `languageID`, and the English address renderings are tagged `en-XB` (the issuer's country). The same party should be described the same way in every example.
- Condition: each party's legal form and address renderings are the same, with the same `languageID`s, in every example of the flow.
- Options: (a, preferred) both legal-form renderings with their tags, and English address renderings tagged by the address's country, everywhere.
- Needs decision: no

### mast/04#F4 · Low · Registration date 1 January 1996
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is the registration date of 25 different companies in 181 examples (lxml count and `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`); it reads as a default, not as each company's history.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes (company histories)

## Checked and consistent
- Roles: Saltmere Engineering is DespatchSupplierParty and SellerSupplierParty, Selanu Telecom DeliveryCustomerParty and BuyerCustomerParty, matching the order `ST-PO-26-0713` (01), where Selanu Telecom is buyer and DeliveryParty; Kelaro Air Cargo `IC41311` is the carrier, as in 03.
- The parties' identifiers, names, address IDs, tax ID, contacts and endpoints agree with 01–03 (apart from F3).

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:WebsiteURI`: the carrier's full master data (website, legal entity) copied into a despatch advice — refuted because a despatch advice tells the recipient who carries the goods, and an identifiable carrier with its contact is useful for the recipient; only the size of the description is debatable.
