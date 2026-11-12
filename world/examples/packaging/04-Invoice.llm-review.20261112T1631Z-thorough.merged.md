# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/04-Invoice.xml`, Git blob `b7615e989edc233d99c6d2b1a77b5e429b9d95e3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1d81251 2026-11-12 Reviews of the packaging flow, run 20261112T1631Z-thorough: parts written so far
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

### packaging/04#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language of Language/ID and names no locale (a language in a
  region). The same value occurs 362 times in 213 example files, always `en` (grep over `*.xml`,
  re-counted in the merge).
- Condition: LocaleCode is absent, or holds a locale (language and region) from a list named in its
  listID, for both parties.
- Options: (a) preferred: remove it, because Language/ID already says English and nothing in the
  invoice uses a locale; (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, context

### packaging/04#F2 · Low · Garment bags booked to the buyer's cost centre "Raw cotton"
- XPath: `/Invoice/cbc:AccountingCostCode` = `2200`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Garment bag`
- Why: Invoice/AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole,
  expressed as text". The invoice bills polyethylene garment bags, not cotton; it repeats the cost
  centre of `03-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`, which is Lumeport Textile Mill's
  account for its cotton purchases (`cotton/08-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`)
  and is on every purchase of the mill (5 files, grep -rl over `*.xml` for `>Raw cotton<`, re-done in
  the merge).
- Condition: the invoice's cost centre is one for packaging material and equals the one in the
  (corrected) order, or it is absent from both.
- Options: (a) preferred: the same packaging or consumables cost centre as the order; (b) drop the
  accounting cost from order and invoice.
- Needs decision: no
- From: broad, money, context

### packaging/04#F3 · Low · The invoice says nothing about the delivery it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `20000`
- Why: The invoice bills 20 000 garment bags delivered DAP to the mill
  (`03-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`) but carries no Delivery (no actual
  delivery date or place) and no despatch reference; the flow has no despatch advice for this order
  and the order gives no date. So nowhere in the flow is it recorded when the bags arrived, which
  under DAP is when the seller's obligation was fulfilled and what the invoice bills (IND6).
  Completeness remark.
- Condition: the invoice states when (and where) the bags were delivered, or refers to a document
  that records it.
- Options: (a) preferred: Delivery/ActualDeliveryDate, with the place if useful; (b) a
  DespatchDocumentReference, if the flow gets a despatch document; (c) record that the order
  reference suffices.
- Needs decision: no
- From: broad, logistics

### packaging/04#F4 · Low · Customs trader identifiers in a domestic invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-412740`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: The customs trader identifiers (schemeID `urn:ubl-examples:world:XB:customs-trader`) identify
  the parties to customs. Supplier and customer are both in Lumeport, the supply is taxed domestically
  (exempt for resale or manufacture under the Coastal State sales tax), and no customs formality is
  involved. They look copied from master data (section 4.8). In the cross-border `02-Invoice.xml` the
  same kind of ID was accepted for that reason.
- Condition: the invoice carries customs identifiers only where the supply involves customs.
- Options: (a) preferred: leave them out here; (b) keep them only with a reason stated in the
  example.
- Needs decision: no
- From: parties

### packaging/04#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". 25 different companies in the
  registers of all three countries share exactly this date (271 occurrences in 181 files; counted over
  `*.xml`, re-done in the merge); it reads as a default (IND5).
- Condition: each company's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: individual dates from the company histories; (b) omit; (c) confirm as a
  story fact.
- Needs decision: yes (company histories)
- From: broad, parties

### packaging/04#F6 · Low · The contacts of the accounting parties do not fit invoicing; the customer's contradicts itself
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party"; for the accounting customer of an
  invoice it is whom the supplier contacts about the invoice and its payment (accounts payable), for
  the accounting supplier whom the customer asks (accounts receivable). Lumeport Textile Mill's
  contact is named purchasing but has a sales job title and department (the same contradiction as in
  `03-Order.xml`), and neither is accounts payable; Rivermouth's accounting contact is its order desk.
  World-wide 52 contacts carry (`Purchasing`, `Customer service officer`, `Sales`) and 89 files have
  a `Purchasing` or `Buying office` contact in Sales (lxml count over `*.xml`, re-done in the merge).
- Condition: the contacts of the accounting parties belong to invoicing or payment, and their name,
  job title and department agree.
- Options: (a) preferred: accounts payable / receivable contacts for both accounting parties; (b) at
  least consistent purchasing values for the mill; (c) omit the Contact where not needed.
- Needs decision: no
- From: broad, parties, context

### packaging/04#F7 · Low · A one-month penalty period against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-06-03`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: PenaltyPeriod is "The period during which penalties may apply"; a one-month period from
  2026-06-03 limits penalties to about a month, while the note makes the surcharge recur for every
  month late. `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `24.00` is one month's surcharge
  (1.5 % × 1600.00, re-computed). Same pattern as `02-Invoice.xml` and `07-Invoice.xml`: all 18 files
  with a PenaltyPeriod have a one-month duration (grep over `*.xml`, re-counted in the merge).
- Condition: the penalty period does not end before the terms say penalties stop.
- Options: (a) preferred: start date only, no duration, and the note states that 24.00 is the
  surcharge per month; (b) a stated cap in the terms, with the duration kept.
- Needs decision: no
- From: money

### packaging/04#F8 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a
  standard system", here the world's own scheme `urn:ubl-examples:world:item`. The value is a
  well-formed GTIN-12 (valid mod-10 check digit) whose GTIN-13 prefix 077 lies in the range GS1 US
  allocates to real companies (060–139, own knowledge); whether it is assigned could not be checked.
  All 8 distinct values of the scheme share this (82 occurrences in 64 files, grep over `*.xml`; check
  digits recomputed in the merge). The rule "fictional values must not be mistaken for real ones"
  applies.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates
  to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN (letters, another length, or a failing
  mod-10 digit); (b) GTINs with GS1's example prefix 952; (c) keep them and record why they are not
  mistaken for real UPCs.
- Needs decision: yes (whether the numbers are assigned could not be settled; the change touches the
  world's item scheme)
- From: broad, logistics

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523` resolves to `03-Order.xml` (an order with the
  same buyer and seller); the invoice (2026-05-03) is issued after the order (2026-04-29). Parties,
  quantity 20 000 EA (40 boxes of 500), price 0.08 XBL, item IDs (`RP-GB-60`), HS 392321, CPC 36410
  and the tax treatment (E, RESALE, STT) agree.
- Arithmetic (re-done): 20 000 × 0.08 = 1600.00 = line = TaxExclusive = TaxInclusive = Payable; tax
  0.00. Due date 2026-05-03 + 30 days = 2026-06-02 in DueDate, PaymentMeans and PaymentTerms;
  penalty 1.5 % × 1600.00 = 24.00; penalty period from 2026-06-03.
- Payment means: domestic credit transfer over LUMEPAY (`MPNS`) between two Lumeport companies to
  Rivermouth's own account (equal to the supplier party's account and to `02-Invoice.xml`); no charge
  bearer for a domestic transfer is fine; RF reference `RF72RPINV260524` and the account pass
  check_ids.py.
- Parties: the supplier block is identical to the one in `02-Invoice.xml`; buyer and seller of
  `03-Order.xml` are the accounting parties here with the same IDs, tax IDs, legal entities,
  addresses and endpoints; BuyerCustomerParty and SellerSupplierParty repeat them by ID and name.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`:
  repeated next to the payee account — refuted because the supplier is paid to it under this invoice;
  the two agree (from broad, money, parties).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
  without a resale-certificate reference — refuted because the exemption reason is stated; a
  certificate reference is optional in UBL and not required by the story (from broad).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `MPNS` against `RTNS` in `02-Invoice.xml` from
  the same supplier — refuted because 02 is paid from Urvania over the Trade Accord rail, 04
  domestically over LUMEPAY; different rails explain different channels (from money, context).

## Changed in the merge
- broad/F3, parties/F2, context/F3 → F6: combined; the XPath lines are reordered (supplier first, by
  position) and the job title of the customer's contact, cited by broad only, is kept; severity
  unchanged.
- broad/F1, parties/F1, context/F1 → F1; broad/F2, money/F1, context/F2 → F2; broad/F4, logistics/F1
  → F3; parties/F4 → F4; broad/F6, parties/F3 → F5; money/F2 → F7 (StartDate line added);
  broad/F5, logistics/F2 → F8: combined, evidence and options merged; severities unchanged. For
  LocaleCode the merge prefers removal (broad, context) over `en-XB` (parties), which stays option (b).
