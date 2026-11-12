# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/13-Invoice.xml`, Git blob `b2c86dfb706324ffa17a917a0b1b5d175a28be17` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1b44438 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/13#F1 · High · "45 days net" but due 21 days after the invoice date
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- Why: 2026-04-02 + 45 days = 2026-05-17; the three due dates are 2026-04-23, i.e. 21 days, the same as in the other invoices of the flow (02, 06, 09). The free text and the structured dates contradict each other.
- Condition: the payment terms' note and the due dates state the same term.
- Options: (a, preferred if Selanu Telecom's terms are 45 days) due dates 2026-05-17; (b) note "21 days net". The remittance 14 (paid 2026-04-19) fits either.
- Needs decision: no

### utilities/13#F2 · Low · Six line-months invoiced as "6 months"
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:Description` = `Six business lines`
- Why: unitCode MON is "month"; 6 MON reads as six months, while the invoice period is March 2026 and the quantity is six lines for one month. Same in the statement (see utilities/12#F5).
- Condition: quantity and unit say six line subscriptions for one month.
- Options: quantity 6 in EA/C62 at 21.18 per line and month (preferred), or six lines of 1 MON.
- Needs decision: no

### utilities/13#F3 · Low · Line references that the utility statement does not carry
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:ID` = `ST-L-BUS6`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:PurchaseReference/cbc:ID` = `ST-D-0042`
- Why: PurchaseReference is "A reference to an object, such as a subscription number, telephone number, meter …, to which this Invoice Line relates". The objects ST-L-BUS6 (the six business lines) and ST-D-0042 (the data pool) appear in no other example (counted over `world/examples/*/*.xml`: only this file). The supplementing statement 12-UtilityStatement.xml identifies the lines by phone number (+999 3 721 1850 … 1855) and the pool by the placeholder "data pool", so the invoice's objects cannot be matched to the statement's supply lines by identifier. In the other invoices of the flow the PurchaseReference is the meter number that the statement also carries.
- Condition: each object referenced on an invoice line is identified the same way in the statement (an ID or number that both carry).
- Options: (a, preferred) give the statement's data pool line the pool's identifier ST-D-0042 (e.g. as its number, see utilities/12#F2) and relate the business lines to ST-L-BUS6 (e.g. in their description); (b) use the phone numbers as purchase references.
- Needs decision: no

## Checked and consistent
- Lines: 6 × 21.18 = 127.08; 35 × 0.424 = 14.84; LineExtensionAmount 141.92; allowance 5 % of base 127.08 = 6.354; tax-exclusive 135.566 = taxable amount; no general sales tax; payable 135.566, as paid in 14-RemittanceAdvice.xml and as stated in 12-UtilityStatement.xml.
- Invoice period 2026-03-01 to 2026-03-31; the statement 12 (17:37) follows the invoice (11:19); line IDs 1 and 2 match the statement's ParentDocumentLineReferenceIDs.
- Check digits (check_ids.py): RF26STINV260323 and account XL18BSEL0010004293889 OK.

## Outside this review
- Outside the logistics lens (money): the payment means is an RTGS credit transfer to an IBAN-style account, but the payee account also carries a BlockchainID (CORAL-NET-L1); for the money part.
