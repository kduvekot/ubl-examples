# LLM review: 08-DespatchAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/08-DespatchAdvice.xml`, Git blob `40cea0e7c3b5f742441038658c674f3f93c6cc68` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/08#F1 · Medium · Province of Urvanian addresses in Region
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as the Bayvarran addresses do. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/08#F2 · Medium · Language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/08#F3 · Low · Lot number differs from the waybill's trace identifier
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `RR-PE-0416`
- Why: The waybill traces the same goods as `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416`. The same lot (manufactured 2026-04-16) has two different identifiers in the two documents, so the consignee cannot match them.
- Condition: one lot identifier for the goods in the despatch advice and the waybill, or an explicit relation between the two.
- Options: (a) one lot number in both (preferred); (b) both identifiers in both documents.
- Needs decision: no

### plastics/08#F4 · Low · Best-before and expiry date for polymer granulate
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:BestBeforeDate` = `2027-04-16`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:ExpiryDate` = `2027-04-16`
- Why: PE granulate does not expire; producers sometimes give a recommended processing period (own knowledge). Giving both a best-before date and an expiry date, both exactly one year after manufacture, looks like a default pair rather than a property of this lot, and an expiry date says the lot must not be used afterwards, which is stronger than any reason visible here.
- Condition: at most one such date, with a business reason (e.g. a recommended processing period stated by the seller).
- Options: (a) keep a best-before date as recommended processing period and drop the expiry date (preferred); (b) drop both.
- Needs decision: no

### plastics/08#F5 · Low · Status codes "no status"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: Optional elements whose code says there is no status add nothing (IND5/IND6: no fillers).
- Condition: status codes are present only with a status that means something.
- Options: omit both (preferred).
- Needs decision: no

### plastics/08#F6 · Low · Packages and transport not stated in structured form
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One barge load of recycled granulate in jumbo bags.`
- Why: A despatch advice tells the recipient what is coming and how. The 120 jumbo bags, the barge and the consignment note are only implied by the note; the shipment has no goods item, packages, transport stage, expected delivery or reference to the waybill `FB-WB-26-0890`, although the document's own note asks the recipient to report damage "on the consignment note".
- Condition: the despatch advice states the number and type of packages and refers to the consignment note (and, preferably, the expected arrival).
- Options: (a) add package count/type, waybill reference and estimated delivery (preferred); (b) at least the waybill reference.
- Needs decision: no

### plastics/08#F7 · Low · Copied master data: delivery customer's bank account and the waste permit
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: Nothing is paid under a despatch advice, and the waste-recovery permit has no role in announcing a delivery; both are master data the document does nothing with.
- Condition: neither appears in the despatch advice.
- Options: remove both (preferred).
- Needs decision: no

### plastics/08#F8 · Low · Delivery customer's contact is a sales order desk
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The delivery recipient's contact receives and checks the goods (the note asks it to check them on arrival); a sales order desk is not goods receipt.
- Condition: the delivery customer's contact is a goods-receipt function.
- Options: a goods-receipt contact (preferred) or a neutral general contact.
- Needs decision: no

### plastics/08#F9 · Low · All three companies registered on 1 January 1996
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for three companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

### plastics/08#F10 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8) in the GTIN-12 (UPC) range; it could be taken for a real GTIN (see `01-Order.xml`).
- Condition: the number cannot be mistaken for a real GTIN, or it is verified as unassigned and documented.
- Options: (a) a non-GTIN format (preferred); (b) document the verification.
- Needs decision: yes

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `RP-PO-26-0882` and order line 1 resolve to `01-Order.xml`; 120 t despatched = 120 t ordered; item, HS code and certificate as in the order.
- Shipment `RR-SH-26-0889`, consignment `RR-CS-26-0885`, gross weight 120 480 kg and carrier Fiumella agree with `05` and `06`.
- Issued 2026-04-19 17:57, after the barge's departure; manufacture date 2026-04-16 before despatch.
- Melt flow index 0.9 g/10 min is plausible for a film-grade LDPE recyclate (own knowledge).
