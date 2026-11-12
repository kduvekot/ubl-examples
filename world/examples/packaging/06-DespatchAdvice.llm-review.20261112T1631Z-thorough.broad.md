# LLM review: 06-DespatchAdvice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

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

### packaging/06#F1 · Medium · Despatch advice says neither when the goods leave nor when they arrive
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and
  services"; the receiver uses it to plan goods-in. The shipment has no Delivery, no Despatch, and no
  despatch or (estimated) delivery date or time anywhere in the document; the order
  (`05-Order.xml`) has no requested date either. Only the issue date 2026-05-12 is known, and by IND6
  it cannot be read as the despatch date.
- Condition: the despatch advice states when the goods were (or will be) despatched and when they
  are expected at Brightmarket, in the dedicated elements.
- Options: (a) Shipment/Delivery with Despatch/ActualDespatchDate (and time) and an
  EstimatedDeliveryPeriod (preferred: both dedicated elements exist); (b) at least the despatch date.
- Needs decision: no

### packaging/06#F2 · Medium · Language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/06#F3 · Low · Contacts do not fit despatch and receiving
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- Why: The despatch party's contact should be its despatch or warehouse function, not its purchasing
  desk (which also has job title "Customer service officer" in "Sales"); the delivery customer's
  contact should receive goods (the order says "goods-in"), not the buying office; the carrier's
  contact is its export desk although this is a delivery within Lumeport (both addresses in
  Coastal State, Bayvarra).
- Condition: each contact is the function that handles this despatch, receipt or transport, with
  fitting name, job title and department.
- Options: (a) despatch / goods-in / domestic transport contacts (preferred); (b) at least goods-in
  for the delivery customer, whom the note asks to check the goods on arrival.
- Needs decision: no

### packaging/06#F4 · Low · Consignment note named in the note but not identified
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The note directs the receiver to a consignment note, but the document references none (no
  AdditionalDocumentReference, no consignment-note ID in Consignment); the consignment
  `LTM-CS-26-0528` is not referred to by any other example (grep over `*.xml`).
- Condition: the consignment note the note mentions is identified in the document, or the note
  refers to something the document identifies.
- Options: (a) an AdditionalDocumentReference to the carrier's consignment note (preferred);
  (b) reword the note (e.g. report damage on this despatch advice or to the carrier).
- Needs decision: no

### packaging/06#F5 · Low · Retail marketing data in a despatch advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The delivery recipient's logo, online shop and social media play no part in a delivery
  (IND5); also its share capital (`/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`).
- Condition: the despatch advice carries none of them, or states a use.
- Options: (a) remove them (preferred).
- Needs decision: no

### packaging/06#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: A valid GTIN-12 (GS1 US prefix 077, own knowledge); all world item numbers share this (82
  occurrences in 64 files, grep over `*.xml`).
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/06#F7 · Low · Default-looking registration date
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: 25 companies in all three countries carry 1 January 1996 (271 occurrences in 181 files,
  counted over `*.xml`); it reads as a default (IND5).
- Condition: each date is the company's own, or absent.
- Options: (a) dates from the company histories (preferred); (b) omit.
- Needs decision: yes

## Checked and consistent
- Order reference `BS-PO-26-0525` resolves to `05-Order.xml`; order line 1, 600 EA, item IDs,
  description and parties agree.
- Physics: Shipment gross weight 168 kg for 600 shirts = 0.28 kg per shirt including garment bag and
  cartons; a men's woven cotton shirt weighs about 0.2–0.25 kg, a 60 cm polyethylene bag some 10–20 g
  (own knowledge), leaving roughly 10–20 kg for cartons: plausible. No equipment is named, so the
  "plus transport equipment" part of the definition adds nothing.
- Seller arranges carriage (Bayforth as carrier), consistent with DDP in the order.
- Issued 2026-05-12 11:35, before the invoice `07-Invoice.xml` (14:49 the same day).

## Considered and refuted
- `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus` and `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
  as fillers — refuted: they state that document and line are in their original state, which the
  definition covers.
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `5229`
  (a forwarder, not a haulier, as CarrierParty) — refuted: a forwarder can contract as carrier; the
  definition ("provides the transport") is met by the contracting carrier.
- `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `The store's spring order of shirts.` — refuted: an
  order of 7 May for spring/summer stock fits.
