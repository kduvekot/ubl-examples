# LLM review: 06-DespatchAdvice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/06-DespatchAdvice.xml`, Git blob `87ee027fe7a7634e3733f7816740466502baaf2c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/06#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID, not a locale. The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent, for all three parties.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/06#F2 · Low · Despatch and delivery contacts are a purchasing mailbox and a buying office
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: Party/Contact is "The primary contact for this party". In DespatchSupplierParty ("The despatch party") it is whom the recipient calls about the despatched goods; Lumeport Textile Mill's purchasing mailbox, with a sales job title, is neither despatch nor shipping. In DeliveryCustomerParty ("The delivery recipient") the contact receives the goods, and the advice itself asks the recipient to check them on arrival (`/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`); Brightmarket's buying office in sales is not its goods receiving. Brightmarket has a goods-in contact in another flow (`retail/08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`). Both contacts are each party's single contact, used in every role (52 and 41 such contacts across the examples, lxml count over `*.xml`).
- Condition: the despatch party's contact handles despatch or shipping, and the delivery recipient's contact receives goods; name, job title and department agree in each.
- Options: (a) preferred: a despatch/shipping contact for the mill and a goods-in contact for Brightmarket (the latter could reuse the one from the retail flow); (b) omit the contacts if the advice needs none.
- Needs decision: no

### packaging/06#F3 · Low · The carrier is a forwarder whose contact is its export desk, for a delivery within Lumeport
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `5229`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- Why: Consignment/CarrierParty is "The Party who provides the transport of goods between named points". Bayforth Forwarding is classified as "Other transportation support activities" (ISIC 5229, i.e. forwarding, not haulage), and its contact is its export desk. The goods go from the mill at Mill Street 21 to Brightmarket's goods-in at Market Street 50, both in Lumeport, DDP (`05-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`); there is no export and nothing that needs a forwarder. A forwarder can act as contracting carrier, but then its contact for this consignment would be its domestic or road desk. The same contact appears in 25 examples (lxml count over `*.xml`).
- Condition: the carrier of this town delivery is a party that carries goods (or a forwarder acting as carrier, said so), with a contact that handles this kind of transport.
- Options: (a) preferred: a local haulier or the mill's own transport as carrier; (b) keep Bayforth as contracting carrier but with a domestic transport contact.
- Needs decision: yes

### packaging/06#F4 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". 25 companies in three countries' registers share exactly this date (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: each company's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: individual dates; (b) remove; (c) confirm as a story fact.
- Needs decision: yes

### packaging/06#F5 · Low · Marketing and customs data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: the delivery recipient's logo, web shop and social media profile, and the despatch party's customs trader ID, have no role in advising a domestic delivery of shirts. They look copied from master data (the logo reference is in 41 examples, Grep over `*.xml`).
- Condition: every party detail in the despatch advice has a role in it.
- Options: (a) preferred: leave them out here; (b) state in the example why they are needed.
- Needs decision: no

## Checked and consistent
- OrderReference `BS-PO-26-0525` resolves to `05-Order.xml`. The delivery customer there (delivery party `20410411`) and here is Brightmarket; buyer and seller are the same parties as in the order, with the same IDs.
- The delivery customer block is identical to the buyer block of `05-Order.xml`, and the despatch supplier block to the seller block there (compared line by line).
- Bayforth Forwarding: register ID, endpoint, Coastal State tax ID `CO-1234932`, legal entity and Lumeport address are internally consistent.
- check_ids.py: GLN `9522610900002` valid.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName` = `Dockside Way`: a dock in a street name — refuted because it is a street name ("Way"), not a dock or gate.
