# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/21#F1 · Low · The receipt is not linked to the shipment, container or pallets received
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box crushed at the port; the frame inside is cracked.`
- Why: the advice has no Shipment (consignment LD-CS-26-0133, container TWLU4120872) and no
  handling units, although the goods arrived as 25 SSCC-labelled pallets (14-BillOfLading.xml);
  the bill of lading is referenced by number only, without saying it is one. The crushed box is on
  the one pallet of boxes,
  `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`,
  which the receipt does not name. The damage "at the port" is the basis of the credit requested
  here and of the later claim documents (26-CreditNote.xml, 28-DebitNote.xml), so the unit it
  happened to matters.
- Condition: the receipt identifies the consignment or container received and the pallet (SSCC)
  carrying the damaged box; the bill of lading reference states its type.
- Options: (a, preferred) a Shipment with the consignment and container, and the SSCC of pallet 25
  on line 2 (ReceiptLine/Shipment or a TransportHandlingUnit); (b) at least the container ID and
  the document type.
- Needs decision: no

### sea/21#F2 · Low · The rejected frame is not identified, although every frame has a serial number
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- Why: the despatch advice gives each of the twelve side frames its own serial and trace ID
  (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230`
  to VI-SF-01241). The receipt rejects one cracked frame without saying which, so the credit and
  any warranty or insurance claim cannot be tied to a unit.
- Condition: the receipt line identifies the rejected frame by its serial (ItemInstance).
- Options: add an ItemInstance with the serial of the cracked frame to line 2.
- Needs decision: no

## Checked and consistent
- References: order VT-PO-26-0127, despatch advice LD-DA-26-0145 (20-DespatchAdvice.xml) with
  despatch lines 1 and 2 and order lines 1 and 2, bill of lading TOL-BL-26-0139
  (14-BillOfLading.xml) all exist and agree in parties (DeliveryCustomer Nalevi Warehousing,
  DespatchSupplier Lumeway Distribution).
- Quantities: line 1 96 of 96 benches; line 2 11 received + 1 rejected = 12 despatched; the
  partial acceptance, header reject reason and credit request agree with line 2.
- Dates: received 2026-05-21, after discharge on 2026-05-18 (17-TransportationStatus.xml) and the
  import declaration of 2026-05-19 (19-ImportCustomsDeclaration.xml); issued the same day at 17:22.

## Outside this review
- 14-BillOfLading.xml plans the on-carriage receipt for 2026-05-19; the goods are received on
  2026-05-21 (timeline across documents).
