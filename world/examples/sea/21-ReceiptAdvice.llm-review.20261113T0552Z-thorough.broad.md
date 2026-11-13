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

### sea/21#F1 · Medium · Gate number in AdditionalStreetName of the despatch party's postal address
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name, and is not part of a postal address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/21#F2 · Low · Received quantity 11 suggests a missing casting, though the twelfth arrived damaged
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `11`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- Why: Twelve castings were despatched (`20-DespatchAdvice.xml`), and the note says the twelfth arrived in a crushed box: it was received and then rejected. `ReceivedQuantity` is "The quantity received"; giving 11 reads as eleven arrived and one is missing, while `RejectedQuantity` 1 says one was refused. Read together, 11 + 1 = 12 works only if "received" means "accepted".
- Condition: The quantities state unambiguously that 12 arrived, 11 were accepted and 1 was rejected.
- Options: `ReceivedQuantity` 12 with `RejectedQuantity` 1 (preferred: received is what physically arrived); or keep 11 and record the reading as the world's rule.
- Needs decision: no

### sea/21#F3 · Low · Contacts whose name, title and department disagree
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The issuer's contact "Goods inwards", who counted and checked the goods, is a customer service officer in Sales; Velumi's "Purchasing" also sits in Sales. Name, job title and department contradict each other.
- Condition: The contacts' names, titles and departments agree and fit receiving goods / buying.
- Options: Goods inwards / Receiving clerk / Warehouse; Purchasing / Buyer / Purchasing.
- Needs decision: no

### sea/21#F4 · Low · Product master data copied into the receipt advice
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: A receipt advice reports what arrived; warranty text, search keywords, sales conditions, circularity and emission data (all present on line 1's item) are catalogue data the receipt does nothing with.
- Condition: The receipt line's item carries identification (and lot/serial where relevant) only, unless another element has a stated purpose.
- Options: reduce the item to its identifiers (preferred).
- Needs decision: no

### sea/21#F5 · Low · Bill of lading referenced without saying what it is
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
- `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`: credit requested from the seller for a casting crushed at Selanu although the bill of lading puts the risk on the buyer from loading at Lumeport (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRisk` = `Risk passes when the goods are on board the vessel in Lumeport.`) — refuted: the buyer may ask; `26-CreditNote.xml` grants the credit expressly as goodwill under CIF and claims from the insurer, so the flow is consistent.
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedDate` = `2026-05-21`: the B/L's on-carriage receipt event is 2026-05-19 — refuted: on the B/L (issued 05-14) that event is planned (`CompletionIndicator` false); the customs inspection at Selanu explains a later receipt.
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box crushed at the port; the frame inside is cracked.`: a sealed container's box crushed "at the port" — refuted: the container was opened for the customs inspection at Selanu (`28-DebitNote.xml`), where handling damage is plausible.
