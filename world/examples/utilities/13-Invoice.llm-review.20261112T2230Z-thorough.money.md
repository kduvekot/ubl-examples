# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/13-Invoice.xml`, Git blob `b2c86dfb706324ffa17a917a0b1b5d175a28be17` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/13#F1 · High · Due date is 21 days after the invoice date; the terms say 45 days net
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- Why: The invoice was issued 2026-04-02, and 45 days net gives 2026-05-17. All three due dates give 21 days. Interest on late payment (6 % a year) would accrue from 24 April on an amount that is not yet due under the note. The same pattern is in 02 and 06 ("30 days net").
- Condition: The note and the due dates give the same date.
- Options: (a) due date 2026-05-17; (b) note "21 days net". Prefer (a) if the 45 days are the island's business term.
- Needs decision: no

### utilities/13#F2 · Medium · Six lines for one month invoiced as six months
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:BaseQuantity` = `1`
- Why: unitCode MON makes the quantity six months of subscription at 21.18 per month. The invoice period is March 2026 only (`/Invoice/cac:InvoicePeriod/cbc:Description` = `March 2026`), and the purchase reference says "Six business lines". The quantity counts lines.
- Condition: The quantity's unit counts what is billed, consistent with the one-month period.
- Options: (a, preferred) a count unit (C62) for six lines, with the price per line per month; the same in statement 12.
- Needs decision: no

### utilities/13#F3 · Medium · A blockchain identifier on a current account in the national currency
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountTypeCode` = `CACC`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentRailID` = `CORAL-NET`
- Why: UBL defines `BlockchainID` as "An identifier of the Blockchain on which the crypto or stablecoin is being held." The account is an IBAN-like current account (CACC, format ISO13616) at Bank of Selanu, held in XLC, the island's currency. It is paid by credit transfer through an RTGS ("RealTimeGrossSettlementSystem"). Nothing in the invoice says that XLC is a crypto-asset or stablecoin held on CORAL-NET. If Coral is a central-bank digital currency in the world, the account would not be a CACC current account with a bank. The same identifier is repeated in remittance 14.
- Condition: BlockchainID is present only if the funds are held on that blockchain, and then the account, channel and rail describe that.
- Options: (a, preferred) remove BlockchainID, because the payment is an ordinary RTGS credit transfer; (b) if the world's Coral is a token on CORAL-NET, describe the account and channel accordingly.
- Needs decision: yes

### utilities/13#F4 · Low · Telephone lines booked to "Stock for municipal projects"
- XPath: `/Invoice/cbc:AccountingCostCode` = `500`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- Why: The buyer's code for stock purchases is applied to office telephone and data subscriptions. The value appears in 10 XML examples, mostly purchases of goods; here it looks copied from Velumi's master data.
- Condition: The accounting cost names a cost account that fits telecommunications.
- Options: (a, preferred) a telecom or office cost code, the same in 12.
- Needs decision: no

### utilities/13#F5 · Low · A 0 % rate on supplies outside the scope of tax, under a scheme named "No general sales tax"
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O has no rate, so a rate of 0 % describes zero-rating (Z). The TaxScheme has no ID, only the name "No general sales tax", which describes the absence of a scheme. That is defensible for an island without sales tax, but it should not be combined with a rate.
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no

## Checked and consistent
- 6 × 21.18 = 127.080 and 35 × 0.424 = 14.840 add up to 141.920, the LineExtensionAmount.
- The allowance is 5 % × 127.080 (BaseAmount) = 6.354. 141.920 − 6.354 = 135.566, which is TaxExclusive, TaxInclusive and Payable. AllowanceTotal and AllowanceTotalTaxInclusive are both 6.354 because no tax applies. The allowance reason code 95 means "Discount".
- RF26STINV260323 passes the ISO 11649 check. Payee account XL18BSEL0010004293889 passes the IBAN-like check. Both are used in remittance 14, which pays 135.566 on 2026-04-19.
- Penalty interest is 6 % a year (ANN), simple. Both lines have the purpose PHON (TelephoneBill).
