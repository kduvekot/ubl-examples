# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
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

### sea/22#F1 · Low · Balance due from the shipment date, but no transport document or shipment date in the invoice
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: the balance terms run from "date of shipment as evidenced by the transport document(s)",
  but the invoice neither references that transport document (bill of lading TOL-BL-26-0139,
  shipped on board 2026-05-14, 14-BillOfLading.xml) or the despatch advice LD-DA-26-0145
  (20-DespatchAdvice.xml), nor gives the shipment date in its Delivery (which holds only the
  delivery party). The buyer, and the factor collecting the receivable, cannot see from the invoice
  when the term starts. Under CIF the goods are delivered when on board at Lumeport, which is the
  same date.
- Condition: the invoice states the shipment date (e.g. Delivery/ActualDeliveryDate or the
  shipment's despatch date) and refers to the transport document the term is based on.
- Options: (a, preferred) Delivery/ActualDeliveryDate 2026-05-14 with the Lumeport location, and
  an AdditionalDocumentReference to TOL-BL-26-0139 typed as a bill of lading; (b) a
  DespatchDocumentReference to LD-DA-26-0145 plus the date.
- Needs decision: no

## Checked and consistent
- Order VT-PO-26-0127 with lines 1 and 2 (05-Order.xml); quantities 96 benches and 12 side
  frames equal the despatch advice and the bill of lading; 96 × 520 = 49920.00 and
  12 × 64 = 768.00, sum 50688.00 = the bill of lading's FOB value.
- Delivery terms CIF Port of Selanu (XLSEL) as in 14-BillOfLading.xml; the freight charge
  2950.00 = ocean freight 2700.00 + bunker surcharge 250.00 and the insurance 140.00 equal the
  bill of lading; the terminal handling at Selanu (185.00, collect from the consignee) is
  correctly not invoiced. 53778.00 equals the bill of lading's declared customs (CIF) value.
- Delivery party Nalevi Warehousing is the bill of lading's notify party and the despatch
  advice's delivery customer. Issued 2026-05-14 12:32, after the bill of lading (10:54).
- GTINs, GLN, RF reference and account pass their check digits.
