# LLM review: 10-Invoice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/10-Invoice.xml`, Git blob `4f8e76fdb62682517ade76167e8a942e4bcac42e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/10#F1 · High · Freight billed per kg of chargeable weight on the gross weight, not the waybill's chargeable weight
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `81.6`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `554.88`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: The line says the price is "per kilogram chargeable weight" (6.8 XBL per 1 KGM), and the
  invoice refers to the waybill (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`),
  whose chargeable weight ("the weight upon which a charge is to be based") is 96 kg. The invoiced
  quantity is the gross weight 81.6 kg instead: 81.6 × 6.8 = 554.88, where 96 × 6.8 = 652.80. The
  description, the referenced waybill and the quantity contradict each other. (The waybill's 96 kg
  itself rests on a volume the forwarding instructions do not support; that is a finding of the
  waybill's review. Either way the invoiced quantity is not the chargeable weight: with one box it
  would be 82 kg after rounding up to the next half kilogram, own knowledge of IATA practice.)
- Condition: the invoiced quantity is the chargeable weight of the shipment as the waybill states
  it, and quantity × price = line amount = totals, tax base and penalty amount.
- Options: (a) preferred: invoice the waybill's chargeable weight (96 KGM → 652.80, with totals,
  TaxableAmount and PenaltyAmount 1.5 % = 9.79 following); (b) if the gross weight is meant, say
  "per kilogram gross weight" in the description, which the waybill then does not support as the
  charge basis.
- Needs decision: no

### air/10#F2 · High · Reference to a statement that does not exist (and could not yet exist on the issue date)
- XPath: `/Invoice/cac:StatementDocumentReference/cbc:ID` = `BF-SOA-26-05`
- Why: StatementDocumentReference is "a reference to a Statement associated with this document". No
  example has the ID BF-SOA-26-05 (`grep -rn --include='*.xml' BF-SOA world/examples`: this one hit
  only), and no statement of Bayforth Forwarding exists in any flow. The ID reads as the May
  statement of account, which cannot be issued before the end of May, while the invoice is issued
  on 2026-05-15; a forward reference to a statement not yet drawn up tells the customer nothing it
  can check.
- Condition: the referenced statement exists in the flow, is issued by Bayforth Forwarding to
  Lumeway Distribution, and is dated on or before the invoice; or the reference is absent.
- Options: (a) preferred: remove the reference (an invoice does not need to name a future
  statement; a statement lists its invoices, not the reverse); (b) add a statement of account to the
  flow that this invoice can refer to.
- Needs decision: yes

### air/10#F3 · Low · Buyer's accounting code "Stock purchases" on a freight-service invoice
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: AccountingCostCode is "the buyer's accounting code, applied to the Invoice as a whole". The
  buyer here is Lumeway Distribution buying air freight it owes as seller under CPT
  (`01-OrderChange.xml:/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`), i.e. an outbound
  distribution cost of a sale, not a purchase of stock. The same code and text are Lumeway's
  posting for goods it buys (`road/15-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410`,
  `rail/11-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410`; counted with
  `grep -rn --include='*.xml' '<cbc:AccountingCostCode>4410' world/examples`: 8 files: road/01,
  road/14, road/15, rail/01, rail/11, retail/16, sea/18 and this invoice). Lumeway posts every
  invoice it receives under it, goods and freight alike; for inbound freight (road/14, carriage of
  goods bought from Urvania) adding the cost to stock is defensible, for the outbound freight of a
  sale (here, and the CIF sea freight in sea/18) it is not, so it looks copied from Lumeway's
  purchasing data.
- Condition: the accounting code is one the buyer would use for outbound freight, or is absent.
- Options: (a) preferred: a code and text for outbound freight / distribution costs of Lumeway;
  (b) remove both elements.
- Needs decision: no

## Checked and consistent
- Line: 81.6 KGM × 6.8 XBL per 1 KGM = 554.88 (arithmetic holds for the quantity as stated; see F1).
- Totals: LineExtensionAmount = TaxExclusiveAmount = TaxInclusiveAmount = PayableAmount = 554.88;
  no allowances, charges or prepaid amount; TaxAmount 0.00.
- Tax: category E, 0 %, exemption reason SVCB2B "Service to a business", SupplyTypeCode SERVICES,
  scheme STT, in TaxSubtotal and ClassifiedTaxCategory alike; TaxableAmount 554.88 = line amount.
  The same exemption code is used for business services in other flows (cotton/17, furniture/14,
  retail/16, sea/18 invoices and debit note).
- Payment terms: DueDate 2026-06-14 = issue date 2026-05-15 + 30 days ("30 days net") =
  PaymentMeans/PaymentDueDate = PaymentTerms/PaymentDueDate; PenaltySurchargePercent 1.5 and
  PenaltyAmount 8.32 = 1.5 % × 554.88 (8.3232, rounded); PenaltyPeriod starts 2026-06-15, the day
  after the due date, for one month (= "per month").
- Payment means: credit transfer (30) to the payee account of Bayforth Forwarding (account name
  Bayforth Forwarding Ltd, holder country XB, currency XBL = document currency); ISO 11649 reference
  `RF66BFINV260331` (check digits OK per check_ids.py) repeated in the instruction note; the
  IBAN-like account number's check digits OK; PaymentMeansID `1` in the terms resolves to the
  payment means. BLUMXBLX has the fictional country code XB in positions 5–6, so it cannot be a
  real BIC.
- The payee is the seller of the service (AccountingSupplierParty = SellerSupplierParty = Bayforth),
  and the invoice goes to the party that owes the freight under CPT (Lumeway, the consignor in
  `04-Waybill.xml:/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`).

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description`: "airport-to-airport … road feeder included"
  against a waybill with an air main carriage only — refuted because a road feeder service is, in
  air cargo practice (own knowledge), trucking under the airline's flight number between airports,
  which stays airport-to-airport; not a money contradiction.
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `E`: international air freight is
  often zero-rated rather than exempt in real VAT systems — refuted because the world's state sales
  tax exempts services to businesses as a rule, applied consistently across flows, and the reason
  code describes the transaction as UBL expects.
- No valuation charge for the declared value of 512.00 XBL on the waybill — refuted as a finding
  here: whether a valuation charge applies depends on the declared value exceeding the carrier's
  limit, which cannot be judged in the fictional currency (see the waybill's review on
  AdValoremIndicator).

## Outside this review
- The cargo was offloaded and flew a day later (`07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`),
  while the status report of the same day says it arrived
  (`09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`):
  a timeline question across documents, not a money one.
