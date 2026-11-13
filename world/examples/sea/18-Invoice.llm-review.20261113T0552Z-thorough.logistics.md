# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/18-Invoice.xml`, Git blob `8959fff2666b14c481d466f04457f91ebe10f1e4` (committed)
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

### sea/18#F1 · Low · The bill of lading is referenced without saying what it is
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: AdditionalDocumentReference is "a reference to an additional document associated with this
  document"; with only an ID the receiver has to guess from the number that it is the carrier's
  bill of lading (14-BillOfLading.xml). Nothing in the reference says so (no DocumentTypeCode or
  DocumentType).
- Condition: the reference states that the document is a bill of lading.
- Options: add DocumentTypeCode (e.g. `BillOfLading` from the world's UBLDocumentTypeCode list,
  which 14-BillOfLading.xml uses in its DocumentDistribution) or DocumentType.
- Needs decision: no

### sea/18#F2 · Low · The customs clearance line does not identify the declaration it bills
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description` = `Preparing and lodging one export declaration as customs agent.`
- Why: the forwarder bills "one export declaration"; the declaration exists in the flow
  (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:ID` = `BF-EX-26-0135`, lodged by
  Bayforth), but neither the line nor the invoice refers to it, so the service billed cannot be
  linked to the declaration the customer can check it against.
- Condition: the invoice (or line 2) refers to BF-EX-26-0135.
- Options: (a, preferred) a DocumentReference on line 2 to BF-EX-26-0135; (b) an
  AdditionalDocumentReference on the invoice.
- Needs decision: no

## Checked and consistent
- Delivery consignment `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
  and carrier Tidewell Ocean Lines agree with 14-BillOfLading.xml.
- Line 1 "one 40-foot container": the bill of lading has one 42G1 container TWLU4120872; the
  amount 2950.00 equals the bill of lading's ocean freight 2700.00 + bunker surcharge 250.00.
- Line 3 cargo insurance 140.00 equals the premium of the policy in the bill of lading, arranged by
  Bayforth as broker.
- Issue date 2026-05-19 lies after the arrival in Selanu (2026-05-18, 17-TransportationStatus.xml),
  so the port-to-port service billed has been performed.
- Check digits: GLN 9520610900008, RF98BFINV260143 and the account XB40BLUM38020502618225 pass.

## Considered and refuted
- `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0133`: Shipment without its
  ID LD-SH-26-0132 looked incomplete — refuted because the consignment ID alone identifies the goods
  carried in every document of the flow.
