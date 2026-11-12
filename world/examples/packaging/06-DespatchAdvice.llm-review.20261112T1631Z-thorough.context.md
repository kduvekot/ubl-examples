# LLM review: 06-DespatchAdvice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/06#F1 · Medium · Despatch advice without a despatch or delivery date
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-05-12`
- Why: A Despatch Advice is "A document used to describe the despatch or delivery of goods and services". The shipment carries no `Delivery` (no despatch, estimated or requested delivery date or period), and no line carries one either, so the document does not say when the 600 shirts leave the mill or when the store can expect them; only the issue date suggests it, which is implying by absence (UBL IND6, rule of the repository). The goods-in staff the despatch advice is meant for need that date to plan receipt.
- Condition: the despatch advice states when the goods were (or will be) despatched and when delivery is expected, in the dedicated elements of `Shipment/Delivery` (e.g. `Despatch/ActualDespatchDate`, `EstimatedDeliveryPeriod` or `PromisedDeliveryPeriod`).
- Options: (a) preferred: a `Shipment/Delivery` with the actual despatch date and time and the estimated delivery period, because both are what the receiver acts on; (b) at least the despatch date.
- Needs decision: no

### packaging/06#F2 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/06#F3 · Low · Carrier's "Export desk" for a delivery within Lumeport
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- Why: The consignment goes from the mill to the store, both in Lumeport (`/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` = `Lumeport`, `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` = `Lumeport`). The carrier's contact for it is its export desk, which deals with export forwarding (its role in the sea, air and cotton flows), not with a local delivery. 25 examples carry `Export desk` (`grep -rc --include='*.xml'`).
- Condition: the carrier's contact in this despatch advice is the one that handles local (domestic) deliveries.
- Options: (a) preferred: a domestic transport or dispatch desk of Bayforth; (b) leave the carrier's contact out.
- Needs decision: no

### packaging/06#F4 · Low · Despatch and delivery contacts are the parties' buying contacts
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The despatch party's contact should be the one who despatches (dispatch, warehouse); the delivery customer's the one who receives goods (goods-in, which the order names as delivery location, `05-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`). Here both are purchasing contacts, and both sit in Sales as customer service officers, so name and department also contradict each other. 89 examples have a `Purchasing` or `Buying office` contact in Sales (XPath count).
- Condition: the despatch party's contact has a despatch function and the delivery customer's a goods-receiving function, each with agreeing name, title and department.
- Options: (a) preferred: dispatch contact for the mill, goods-in contact for the store.
- Needs decision: no

### packaging/06#F5 · Low · Delivery customer's marketing data in a despatch advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The store's logo reference, online shop and photo-sharing profile have no use in announcing a delivery of goods; they are master data of Brightmarket copied into the document (section 4.8).
- Condition: the despatch advice carries none of these, or a reason to.
- Options: (a) preferred: leave them out.
- Needs decision: no

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml`; order line 1, 600 EA, item identifiers and parties agree.
- Physics: 168 kg gross for 600 shirts is 0.28 kg per shirt including garment bag and outer packaging; a men's woven cotton shirt weighs about 0.2–0.25 kg (own knowledge), so the figure is plausible.
- Issue 2026-05-12 11:35 is after the order (2026-05-07) and before the invoice `07-Invoice.xml` (same day, 14:49).

## Considered and refuted
- `/DespatchAdvice/cbc:Note`: asks to report damage "on the consignment note", which no example of the flow contains — refuted because a carrier's consignment note travels with the goods and need not be a document of this flow; the note is a normal receiving instruction.
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode`: a forwarder (ISIC 5229) as `CarrierParty` — refuted because a forwarder that contracts the carriage in its own name is the carrier towards the shipper.
- `/DespatchAdvice/cac:DespatchLine/cbc:Note`: "The store's spring order of shirts." in May — refuted; the order was placed in spring.
- `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`: refuted because it states that this is the original advice, which fits.
