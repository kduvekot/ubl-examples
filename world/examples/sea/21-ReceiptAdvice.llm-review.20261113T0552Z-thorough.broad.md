# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
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

### sea/21#F1 · Medium · Credit requested from the seller for damage after the risk had passed to the buyer
- XPath: `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectReason` = `One box crushed at the port; the frame inside is cracked.`
- XPath: `/ReceiptAdvice/cbc:RejectReason` = `Damaged in transit.`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRisk` = `Risk passes when the goods are on board the vessel in Lumeport.`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRiskResponsibilityCode` = `BUYER`
- Why: The goods were sold CIF Selanu, and the bill of lading states that the risk passed to the buyer when the goods were on board at Lumeport. The casting was crushed "at the port" of Selanu, i.e. after the risk had passed; the loss falls on the buyer and is recovered from the carrier/terminal or the cargo insurance (policy `WS-CP-26-4471`, arranged under CIF), not by a credit from the seller. Asking the despatch party for a credit contradicts the agreed risk transfer (and `26-CreditNote.xml` then grants it).
- Condition: The requested action and the later documents agree with the risk transfer: either a claim against carrier/insurer, or a stated reason why the seller credits anyway (goodwill, or damage traced to packing).
- Options: (a) keep the credit, but give it a reason the risk rules allow (e.g. insufficient packing, or goodwill agreed with the seller); (b) change the action to a claim against the insurer/carrier and drop the credit from the flow. Preferred (a) if the flow is to keep the credit note.
- Needs decision: yes

### sea/21#F2 · Medium · Gate number in AdditionalStreetName of the despatch party's postal address
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name, and is not part of a postal address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/21#F3 · Low · Received quantity 11 suggests a missing casting, though the twelfth arrived damaged
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `11`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- Why: Twelve castings were despatched (`20-DespatchAdvice.xml`), and the note says the twelfth arrived in a crushed box: it was received and then rejected. `ReceivedQuantity` is "The quantity received"; giving 11 reads as eleven arrived and one is missing, while `RejectedQuantity` 1 says one was refused. Read together, 11 + 1 = 12 works only if "received" means "accepted".
- Condition: The quantities state unambiguously that 12 arrived, 11 were accepted and 1 was rejected.
- Options: `ReceivedQuantity` 12 with `RejectedQuantity` 1 (preferred: received is what physically arrived); or keep 11 and record the reading as the world's rule.
- Needs decision: no

### sea/21#F4 · Low · Contacts whose name, title and department disagree
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The issuer's contact "Goods inwards", who counted and checked the goods, is a customer service officer in Sales; Velumi's "Purchasing" also sits in Sales. Name, job title and department contradict each other.
- Condition: The contacts' names, titles and departments agree and fit receiving goods / buying.
- Options: Goods inwards / Receiving clerk / Warehouse; Purchasing / Buyer / Purchasing.
- Needs decision: no

### sea/21#F5 · Low · Product master data copied into the receipt advice
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: A receipt advice reports what arrived; warranty text, search keywords, sales conditions, circularity and emission data (all present on line 1's item) are catalogue data the receipt does nothing with.
- Condition: The receipt line's item carries identification (and lot/serial where relevant) only, unless another element has a stated purpose.
- Options: reduce the item to its identifiers (preferred).
- Needs decision: no

### sea/21#F6 · Low · Bill of lading referenced without saying what it is
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: The additional reference gives only an ID, with no document type, so the receiver cannot tell it is the bill of lading under which the goods arrived.
- Condition: The reference states its document type.
- Options: add `DocumentTypeCode` / `DocumentType`.
- Needs decision: no

## Checked and consistent
- Order `VT-PO-26-0127` (lines 1, 2) and despatch advice `LD-DA-26-0145` (lines 1, 2) resolve; quantities 96 + 12 as despatched; 96 benches received, 11 + 1 castings.
- Header acceptance `PARTIAL`, reason `DAMAGED` and action `CREDIT` agree with line 2; line 1 "Received as despatched".
- Issue 2026-05-21 17:22 is on the received date and after discharge (05-18) and the import declaration (05-19).
- GTINs and GLN pass `check_ids.py`.
- Notes in Lisavan and English carry `qal` and `en-XL`.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedDate` = `2026-05-21`: the B/L's on-carriage receipt event is 2026-05-19 — refuted: on the B/L (issued 05-14) that event is planned (`CompletionIndicator` false); the customs inspection at Selanu explains a later receipt.
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box crushed at the port; the frame inside is cracked.`: a sealed container's box crushed "at the port" — refuted: the container was opened for the customs inspection at Selanu (`28-DebitNote.xml`), where handling damage is plausible.
