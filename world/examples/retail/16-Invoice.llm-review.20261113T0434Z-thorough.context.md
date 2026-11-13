# LLM review: 16-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/16-Invoice.xml`, Git blob `e1ce518ac0f84644902623e83922648f889ca0d0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/16#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/16#F2 · Low · Outbound freight booked by the buyer as "Stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: AccountingCostCode/AccountingCost are "The buyer's accounting code, applied to the Invoice as a
  whole". The buyer here is Lumeway, and the invoice is for delivering goods it has sold to its
  customer (delivered duty paid to the store, 08-Order.xml). That is a distribution cost of the
  sale, not a purchase of stock; and nothing in the flow tells the carrier Lumeway's cost account (no
  order or request carries it).
- Condition: the accounting cost is a code the buyer gave the carrier for this kind of cost, or is
  absent.
- Options: (a) drop both (preferred, the carrier has no source for them); (b) an outbound-freight cost
  code given in 11-TransportExecutionPlanRequest.xml.
- Needs decision: no

### retail/16#F3 · Low · Master data the transport invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: the customer's customs trader number and share capital play no part in an invoice for a
  domestic carriage (IND5/IND6).
- Condition: the parties carry what the invoice uses.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- AccountingSupplierParty/SellerSupplierParty Bayforth and AccountingCustomerParty/BuyerCustomerParty
  Lumeway match the TransportServiceProviderParty and BillToParty of
  11-TransportExecutionPlanRequest.xml.
- AdditionalDocumentReference `BF-WB-26-0231` resolves to 13-Waybill.xml; the consignment
  `LD-CS-26-0228` and the carrier are those of 11 to 15.
- The service "price per kilometre driven loaded" fits the full truck load booked in 11.
- The invoice date (2026-04-30) is after the carriage (2026-04-29/30).

## Considered and refuted
- `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name`: the
  carrier repeats the seller — refuted because naming the carrier of the delivery invoiced is what the
  delivery aggregate says, and it lets the buyer match the invoice to the consignment.
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote`: repeats the RF reference — refuted because a
  payment instruction asking to quote the reference is ordinary practice.
