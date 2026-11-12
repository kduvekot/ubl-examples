# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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

### utilities/13#F1 · High · "45 days net" contradicts the due date 21 days after issue
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- Why: 45 days from 2026-04-02 is 2026-05-17; every structured due date is 2026-04-23 (21 days). The note contradicts the structured terms.
- Condition: Note and due dates give the same date.
- Options: (a) "21 days net"; (b) due dates 2026-05-17. Preferred: the one matching Selanu's standard terms XL-STD as the world defines them.
- Needs decision: no

### utilities/13#F2 · Medium · A blockchain identifier on a bank current account
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XL18BSEL0010004293889`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountFormatCode` = `ISO13616`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`
- Why: BlockchainID is "An identifier of the Blockchain on which the crypto or stablecoin is being held." The account is an IBAN-structured current account (ISO 13616) at a bank, in the fiat currency Coral, paid by credit transfer through an RTGS channel. Nothing is held on a blockchain; the identifier is the rail's name with "-L1" appended (PaymentRailID CORAL-NET). It is the only BlockchainID in the world apart from `14-RemittanceAdvice.xml` (grep over `*.xml`).
- Condition: BlockchainID appears only on a wallet or account that holds crypto or stablecoins on that chain.
- Options: (a, preferred) remove it; (b) if the world's Coral is a digital currency settled on a ledger, say so in the story and describe the account as such (wallet ID, no IBAN).
- Needs decision: yes

### utilities/13#F3 · Low · Buyer's cost centre "Stock for municipal projects" for telephone bills
- XPath: `/Invoice/cbc:AccountingCostCode` = `500`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- Why: Telephone lines and mobile data are office overheads of Velumi Trading, not stock for municipal projects (Velumi's purchasing default, 10 examples, grep over `*.xml`).
- Condition: The cost centre fits telecommunication costs, or is absent.
- Options: (a, preferred) an office/telecommunication cost centre.
- Needs decision: no

### utilities/13#F4 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- Why: A customs trader number has no role in a telephone invoice, and the purchasing department (which buys goods for trade) is not the natural contact for telecom bills.
- Condition: The customer carries what the invoice uses.
- Options: (a, preferred) remove the customs ID; an accounts payable or office contact.
- Needs decision: no

## Checked and consistent
- Lines: 6 × 21.18 = 127.08; 35 × 0.424 = 14.84; LineExtension 141.92; allowance 5 % × 127.08 = 6.354; TaxExclusive 135.566 = Payable; tax 0.000 (outside the scope, "No general sales tax").
- Document-level allowance with BaseAmount = line 1, consistent with "Business bundle discount" on the subscriptions only.
- PaymentID RF26STINV260323 check digits OK; paid in full by `14-RemittanceAdvice.xml` on 2026-04-19.
- `12-UtilityStatement.xml` totals equal this invoice's.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[2]/cac:PurchaseReference/cbc:ID`: data pool ST-D-0042 as purchase reference — refuted because PurchaseReference names subscription numbers and telephone numbers as its objects, and the pool is such an object.
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: SERVICES — refuted because telecommunication is a service.
