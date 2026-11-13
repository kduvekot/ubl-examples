# LLM review: 21-PurchaseReceipt.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/21-PurchaseReceipt.xml`, Git blob `7f75d1791cf92b3eb6f0f963657d0181e309ff88` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 44b84c0 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/21#F1 · High · Home delivery "booked for Saturday", requested for Sunday
- XPath: `/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.`
- XPath: `/PurchaseReceipt/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-05-17`
- XPath: `/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`
- Why: the purchase was made on Friday 2026-05-15; the next Saturday is 2026-05-16. The
  RequestedDeliveryPeriod, "The period requested for delivery", starts on 2026-05-17, a Sunday,
  09:00–12:00. The note and the structured delivery period name different days.
- Condition: the note and the requested delivery period name the same day.
- Options: start date 2026-05-16 (preferred, matches "Saturday"), or change the note.
- Needs decision: no

### retail/21#F2 · High · Emission factor times base does not give the emission
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor.
- Options: drop factor and base (preferred; the footprint itself may interest a consumer), or correct
  the factor.
- Needs decision: no

### retail/21#F3 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples). LocaleCode is "A
  code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is a language
  code (213 examples; both counted with `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/21#F4 · Low · The customer's bank account on a receipt paid by debit card
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `55`
- Why: the purchase was paid by debit card; the card account (masked PAN) is in PaymentMeans. The
  person's FinancialAccount, "The financial account associated with this person", with full IBAN-like
  number and bank address, is used for nothing on the receipt: no refund, no direct debit. A shop
  receipt that prints a consumer's full account number is also implausible.
- Condition: the receipt carries no consumer bank account unless it is used (e.g. for a refund).
- Options: drop the FinancialAccount (preferred).
- Needs decision: no

### retail/21#F5 · Low · The warranty period as the purchase line's period
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:StartDate` = `2026-05-15`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:EndDate` = `2031-05-15`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- Why: PurchaseLinePeriod is "A period to which this purchase line applies", e.g. the period a
  subscription or ticket covers. The purchase of a bench applies to no period; the five years are the
  maker's warranty, which the item's warranty information already states. Nothing on the receipt says
  the period is the warranty.
- Condition: the purchase line period is absent, or expresses a period the purchase itself covers.
- Options: drop it (preferred); the warranty document reference `VI-WARRANTY-B180` and the warranty
  text already cover it.
- Needs decision: no

### retail/21#F6 · Low · Delivery and payment identifiers dated the 18th for a purchase on the 15th
- XPath: `/PurchaseReceipt/cac:SalesDocumentReference/cbc:ID` = `BM-DEL-26-0518-07`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:ID` = `BM-G2-26-0518-0047`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:TransactionID` = `TX-26-0518-773104`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:PaidDate` = `2026-05-15`
- Why: SalesDocumentReference is "A reference to the sales document to which this purchase receipt is
  related"; `BM-DEL-…` reads as a delivery note rather than a sales document. The delivery note, the
  payment and the card transaction all carry `26-0518`, which in this flow's numbering is a date
  (compare `BM-SIG-26-0424` on the order of 2026-04-24), i.e. Monday 18 May, while the payment was made
  on Friday 15 May and the delivery is for the 16th or 17th (F1).
- Condition: identifiers that encode a date carry the date of their event, and the sales document
  reference is a sales document (or is typed as the delivery note it is).
- Options: identifiers with `0515`; a typed reference to the delivery order, or none.
- Needs decision: no

### retail/21#F7 · Low · Point of sale named after the company, signature without content
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- XPath: `/PurchaseReceipt/cac:Signature/cbc:ID` = `BM-SIG-POS-G2`
- Why: PointOfSaleLocation is "The location of the point of sale"; the name is the company and town,
  without the store's address or GLN. The signature (presumably the till's fiscal signature) has only
  an ID and a signatory, no value or method, so it signs nothing.
- Condition: the location identifies the store; the signature carries what makes it one, or is absent.
- Options: add the store's address or GLN; complete or drop the signature.
- Needs decision: no

## Checked and consistent
- AccountingSupplierParty Brightmarket (the seller at the till) and AccountingCustomerParty the
  consumer Robin Ashdale; the cashier, register G2, payment terminal PT-G2 and point-of-sale location
  fit together.
- Price: 749.00 − 10 % (74.90) = 674.10, the promotion of 06-RetailEvent.xml, which runs from
  2026-05-11 to 2026-05-24 and so includes the purchase date. Home delivery 25.00; 674.10 + 25.00 =
  699.10; 6.5 % = 45.44; 699.10 + 45.44 = 744.54 = PaidAmount.
- The item `BM-551210` is the buyer's item number of 08-Order.xml, now the seller's at the till; the
  grey variant is the one delivered in 12-DespatchAdvice.xml.
- Delivery by the store itself (CarrierParty Brightmarket) to a residential address in Lumeport.

## Considered and refuted
- `/PurchaseReceipt/cac:CashierContact/cbc:Name`: a personal first name although UBL recommends
  functional names — refuted because a cashier is a person and receipts commonly show the first name.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseReference/cbc:ID`: the frame serial number as
  a purchase reference — refuted because the definition names objects to which the purchase relates,
  and a product serial number for a warranty is such an object.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric`:
  the full product data on a consumer receipt — refuted as a finding here because repairability and
  footprint can legitimately be handed to the consumer with the purchase (only the factor of F2 is
  wrong).
