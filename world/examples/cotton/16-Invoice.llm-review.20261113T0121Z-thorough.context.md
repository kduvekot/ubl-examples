# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
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

### cotton/16#F1 · High · Due date 30 days after issue, terms "45 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-02`
- Why: The invoice is issued on 2026-03-02 under payment terms XL-STD, "45 days net"; 45 days after
  issue is 2026-04-16. All three due dates are 2026-04-01, 30 days after issue. The same terms ID and
  note in the self-billed invoice 04 give a due date exactly 45 days after issue (2026-02-07 →
  2026-03-24). The terms text and the due dates contradict each other.
- Condition: the due dates and the payment terms text agree (45 days after the issue date, or a
  terms text that gives 30 days).
- Options: (a, preferred) set the due dates to 2026-04-16; (b) change the note (and terms ID) to 30
  days if the export sale has its own terms; the remittance advice 18 (issued 2026-03-29) fits
  either.
- Needs decision: no

### cotton/16#F2 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item"; 227 is the bale weight
  in kilograms ("compressed bales of about 227 kg"). As in 02, 07, 08, 10, 11 and 15.
- Condition: no element meant for a count holds the bale weight.
- Options: (a, preferred) leave PackSizeNumeric out; give the bale weight, if needed, as an item
  property with a KGM quantity.
- Needs decision: no

### cotton/16#F3 · Low · An export invoice without its delivery terms or delivery
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: The invoice bills lint shipped from Lisavu to Bayvarra. The order agreed FOB Port of Selanu,
  which defines what the price includes (no freight: the forwarder invoices freight separately in
  17) and is the basis of the customs values in 11 and 15. The invoice carries no DeliveryTerms, no
  Delivery (date shipped, place) and no reference to the bill of lading, so the invoice alone does
  not show what its price covers or which shipment it bills.
- Condition: the invoice states the delivery terms and the delivery (or a reference to the B/L or
  shipment) of the goods it bills.
- Options: (a, preferred) add DeliveryTerms FOB Port of Selanu and a Delivery with the shipped date
  of the B/L 13 (or a DespatchDocumentReference/AdditionalDocumentReference to TOL-BL-26-0206).
- Needs decision: no

### cotton/16#F4 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: The same area is a District in the farm's address and a Region here.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress.
- Needs decision: no

## Checked and consistent
- 6,129 kg × 0.988 XLC = 6,055.452 XLC, equal to the order 08 and to every total; tax category O
  (no general sales tax in Lisavu) with tax 0.
- OrderReference and order line reference resolve to line 1 of 08.
- AccountingCost "Raw cotton" (2200) is the buyer's cost centre of the order, which is what
  Invoice/AccountingCost is ("The buyer's accounting code").
- RF46SCGINV260210 and the payee account XL31BSEL0020004922263 pass `check_ids.py`; the account is
  the ginnery's, the one the remittance advice 18 pays.
- RTNS over the Trade Accord payment rail with shared charges fits a cross-border payment from
  Bayvarra to Lisavu.

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XLC`: the document currency repeated, suspected as a filler —
  refuted because for a buyer in Bayvarra, whose currency is the Lume, it states that payment is
  expected in coral.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`: a certificate in
  an invoice line — refuted because the grade it certifies determines the price invoiced.
