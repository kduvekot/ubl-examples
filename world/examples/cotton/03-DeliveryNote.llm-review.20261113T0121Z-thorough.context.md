# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### cotton/03#F1 · Medium · The textile mill as originator and beneficiary of a seed cotton delivery from farm to gin
- XPath: `/DeliveryNote/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- Why: OriginatorCustomerParty is "A customer party as originator" (in the invoice of the same
  delivery, 04: "The Party who originated the Order to which this Invoice is related");
  BeneficiaryParty is "A Party for whom the associated transaction is ultimately intended or who
  derives benefit from it". The transaction of this delivery note is the farm delivering 18,000 kg
  of seed cotton to the ginnery under the ginnery's own call-off SCG-SEASON-2026/03 of its season
  agreement with the farm. The mill did not originate that order (it orders lint from the ginnery
  later, in 08) and is not the party for whom seed cotton is intended: the ginnery buys it, gins it
  and sells lint, with the seeds and waste staying at the gin. Nothing in the note ties this seed
  cotton to a mill order. The same two roles are in the self-billed invoice 04.
- Condition: the delivery note names in originator and beneficiary roles only parties that, by the
  documents of the flow, originated the order referenced or benefit from this delivery; or the
  example states the link (e.g. a mill order the seed cotton is earmarked for).
- Options: (a, preferred) leave both roles out: the farm–ginnery delivery stands on its own;
  (b) if the story wants the mill as the end customer of this lot, make it explicit with a reference
  to the mill's order or contract and keep the roles.
- Needs decision: yes (it changes who the parties of the delivery are)

### cotton/03#F2 · Low · Project reference to a chamber of commerce quality project in a delivery note
- XPath: `/DeliveryNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: ProjectReference is "A reference to a project with which this Delivery Note is associated".
  The ID prefix SCC is the Selanu Chamber of Commerce's (its certificates and signatures in the flow
  carry it), which is not a party to this delivery. A delivery of seed cotton from a farm to its gin
  under a season call-off is not a project, and nothing in the note says what the project is or does
  with this delivery. The same reference is in 04 and 05.
- Condition: the delivery note carries a project reference only if the story has a project this
  delivery belongs to, and then says what it is.
- Options: (a, preferred) leave it out; (b) give the project a role in the story (e.g. a quality
  programme the delivery is sampled for) and describe it.
- Needs decision: yes (whether such a project exists in the world)

### cotton/03#F3 · Low · Additional document reference with only an ID
- XPath: `/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: An AdditionalDocumentReference says nothing about the kind of document. The note ("weighed at
  the gin") and the ID prefix suggest the ginnery's weighbridge ticket, but neither DocumentTypeCode
  nor DocumentDescription says so; the self-billed invoice 04 cites the same ID as a
  ReceiptDocumentReference (a Receipt Advice), so readers of the flow get two different kinds for
  one document.
- Condition: the reference states what kind of document SCG-WB-26-0311 is.
- Options: (a, preferred) add a DocumentTypeCode or DocumentDescription naming the weighbridge ticket.
- Needs decision: no

### cotton/03#F4 · Low · The buyer's cost centre "Seed cotton purchases" in the farm's delivery note
- XPath: `/DeliveryNote/cbc:AccountingCostCode` = `200`
- XPath: `/DeliveryNote/cbc:AccountingCost` = `Seed cotton purchases`
- Why: AccountingCost is "The accounting cost centre, applied to the Delivery Note as a whole". The
  delivery note is issued by the farm (ID prefix LCF, signed by the farm); "Seed cotton purchases"
  with code 200 is the ginnery's cost centre (the same values head the ginnery's self-billed
  invoices 01 and 04). The farm purchases no seed cotton. Without a statement that it is the buyer's
  cost centre quoted for routing, the value reads as the issuer's own.
- Condition: the cost centre in the delivery note is one that fits the issuer, or the document makes
  clear it is the buyer's routing code.
- Options: (a, preferred) leave the cost centre out of the farm's delivery note; (b) keep it if the
  season agreement asks the farm to quote the gin's cost centre, and say so in a note.
- Needs decision: no

### cotton/03#F5 · Low · DocumentStatusCode "NoStatus" states nothing
- XPath: `/DeliveryNote/cbc:DocumentStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Delivery Note with respect to its
  original state, e.g., original, revised, or cancelled". "No status on document" gives no status;
  the element is present without carrying information (UBL IND5, no fillers).
- Condition: the delivery note carries no DocumentStatusCode, or one that states a status the story
  has.
- Options: (a, preferred) leave it out.
- Needs decision: no

## Checked and consistent
- Despatch supplier (farm) and delivery customer (ginnery) fit a delivery of seed cotton to the gin;
  seller and buyer are the same as in 01 and 04.
- The farm's PhysicalLocation (the cotton fields) fits the despatch party of this delivery.
- 18,000 kg delivered on 2026-02-05, invoiced as 18,000 kg in
  `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `18000`;
  ActualDeliveryDate is the issue date, which is plausible for
  a note issued at 14:29 after three loads.
- Item description, HS and CPC codes are the same as in 01 and 04.

## Considered and refuted
- `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`: a contract-based ID used as an
  order reference — refuted because a call-off under a season agreement is an order, and the ID
  reads as call-off 03 of SCG-SEASON-2026.
- `/DeliveryNote/cac:Shipment/cbc:GrossWeightMeasure` = `20400`: gross weight above the delivered
  quantity — refuted because the shipment's gross weight includes transport equipment (the
  definition says so), i.e. the trailers of the three loads.
