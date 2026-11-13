# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/28#F1 · High · Reference to a statement issued three weeks after this debit note
- XPath: `/DebitNote/cbc:IssueDate` = `2026-05-22`
- XPath: `/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- Why: the referenced statement is
  `25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`, 22 days after this debit note was
  issued, so the debit note refers to a document that does not exist when it is issued. The
  statement does not list this debit note either (its two lines are the invoice and the deposit).
- Condition: the debit note refers only to documents issued before it.
- Options: (a, preferred) remove the statement reference; (b) if the debit note is meant to answer
  a statement, issue it after that statement, which changes the order of the flow.
- Needs decision: no

### sea/28#F2 · Medium · The bill of lading is referenced as a delivery note
- XPath: `/DebitNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: DeliveryNoteDocumentReference is "a reference to a Delivery Note associated with this
  document". TOL-BL-26-0139 is the ocean carrier's bill of lading (14-BillOfLading.xml), a
  different document type (UBL has both a BillOfLading and a DeliveryNote). No delivery note
  exists in the flow; the final delivery to Nalevi is documented by the despatch advice and the
  receipt advice, which the debit note already references.
- Condition: the bill of lading, if referenced, is referenced in an element meant for any document
  (e.g. AdditionalDocumentReference) with its type; DeliveryNoteDocumentReference refers only to a
  delivery note.
- Options: (a, preferred) move it to AdditionalDocumentReference with DocumentTypeCode
  `BillOfLading`; (b) remove it, since despatch and receipt are already referenced.
- Needs decision: no

## Checked and consistent
- The pallet named in `/DebitNote/cac:DiscrepancyResponse/cbc:Description` = `Heat-treatment mark illegible on pallet 095206101230000070.`
  is pallet 7 of 25 in the container, a pallet of four benches
  (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[7]/cbc:ID` = `095206101230000070`);
  so the debit line correctly points to order line 1, despatch line 1 and receipt line 1 (benches).
- The hold of the container for the heat-treatment mark agrees with the detention and quarantine
  events of 2026-05-18 in 17-TransportationStatus.xml; one day of storage
  (`/DebitNote/cac:CollectionDebitNoteLine/cbc:DebitedQuantity` = `1`) fits a hold from midday on the
  18th to the import declaration on the 19th (19-ImportCustomsDeclaration.xml, 09:07).
- References that resolve: order VT-PO-26-0127, despatch advice LD-DA-26-0145, receipt advice
  NW-RA-26-0146, statement HF-ST-26-0151, invoice LD-INV-26-0147, agreement LD-DAG-26-0125; all
  except the statement (F1) were issued before the debit note (2026-05-22).
- Container TWLU4120872 passes the ISO 6346 check digit.

## Considered and refuted
- `/DebitNote/cac:PurchaseReference/cbc:ID` = `TWLU4120872`: a container number as a purchase reference
  looked like an identifier of the wrong kind — refuted because PurchaseReference is "a reference to
  an object, such as a subscription number, telephone number, meter, vehicle, person, etc., to which
  this Debit Note relates", and the debit is for the inspection and storage of that container.
- `/DebitNote/cac:InvoicePeriod/cbc:EndDate` = `2026-05-19`: the hold in 17-TransportationStatus.xml ends
  with the quarantine on 2026-05-18 at 15:00 — refuted because the container stayed under customs
  control until the import declaration on 2026-05-19, so a period of 18 to 19 May for one day of
  storage is consistent.
- `/DebitNote/cac:WorkReportDocumentReference/cbc:ID` = `XL-CUS-INSP-26-0517`: "0517" looked like 17 May,
  a day before the inspection — refuted because the ID is an opaque number of the customs service.
