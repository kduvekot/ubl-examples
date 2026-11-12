# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/13-Invoice.xml`, Git blob `b2c86dfb706324ffa17a917a0b1b5d175a28be17` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit f9f7596 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/13#F1 · High · Due date contradicts "45 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- Why: Issued on 2026-04-02 (`/Invoice/cbc:IssueDate` = `2026-04-02`), 45 days net gives 2026-05-17; the due dates are 21 days after issue. The same 21-day due date with a different stated term occurs in 02-Invoice.xml and 06-Invoice.xml.
- Condition: The due dates and the payment terms note state the same term.
- Options: (a) due date 2026-05-17; (b) note "21 days net". Preference: whatever the terms "XL-STD" say; if 45 days, (a).
- Needs decision: no

### utilities/13#F2 · Low · Blockchain ID on a bank current account
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountTypeCode` = `CACC`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`
- Why: BlockchainID identifies the blockchain on which a wallet account is held. The payee account is an IBAN-structured current account at Bank of Selanu, paid by credit transfer through an RTGS channel; a blockchain plays no part in that. If the world's Coral is held on a ledger, the account would be a wallet (wallet ID, wallet account type), not a bank IBAN. The element is used in 2 examples (`grep -rl --include='*.xml' 'BlockchainID'`).
- Condition: BlockchainID appears only on an account held on that blockchain, consistent with the account's identifier, type and the payment channel.
- Options: (a, preferred) drop BlockchainID here; (b) if Coral is a ledger currency in the world, describe the account as a wallet and the channel accordingly.
- Needs decision: yes

### utilities/13#F3 · Low · Telecom costs booked as "Stock for municipal projects"
- XPath: `/Invoice/cbc:AccountingCostCode` = `500`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". Telephone lines and data are communication costs; the text is the one Velumi uses for its goods purchases (10 occurrences in `*.xml`, `grep -rh --include='*.xml' -o 'Stock for municipal projects'`).
- Condition: Velumi's communication cost account, or absent.
- Options: (a, preferred) a communication cost account.
- Needs decision: no

### utilities/13#F4 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: A domestic telephone invoice does not use the customer's customs trader number; it looks copied from master data.
- Condition: The customer carries only identifiers the invoice uses.
- Options: (a, preferred) drop it.
- Needs decision: no

### utilities/13#F5 · Low · A tax total for a tax that does not exist
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: TaxScheme is "a tax scheme"; here it has no ID and its name says that there is no such tax. A tax total of 0 under a non-existent scheme, with category O, states the absence of tax as if it were a tax, close to "implied by absence" (IND5/IND6). If the world requires a tax statement on every invoice (as EN 16931 does for category O), it would be the scheme the island's law defines, with an identifier.
- Condition: Either the tax scheme is a real scheme of Lisavu with an identifier, or the invoice carries no tax total, consistently with the world's rules for Lisavu.
- Options: (a) drop TaxTotal and the tax categories (if the world's Lisavan invoice rules allow it); (b) name the scheme by an identifier from the world's tax list. Preference: decide once for all Lisavan examples.
- Needs decision: yes

## Checked and consistent
- Lines: 6 × 21.18 = 127.08; 35 × 0.424 = 14.84; sum 141.92; discount 5 % of 127.08 = 6.354 (base amount 127.080); tax exclusive 135.566 = taxable amount = payable; AllowanceTotal 6.354; LineCountNumeric 2.
- Agreement with 12-UtilityStatement.xml (quantities, prices, discount, payable) and with 14-RemittanceAdvice.xml (refers to ST-INV-26-0323).
- Penalty interest 6 % per annum, simple; time basis ANN from UNECE Rec. 20.
- check_ids.py: RF26STINV260323 and XL18BSEL0010004293889 correct; BIC-like BSELXLSL uses the user-assigned code XL.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a 135 XLC bill — refuted, the world's Coral rail CORAL-NET may be the only interbank system on the island.
- `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount`: three decimals in Coral — refuted, consistent across all Lisavan amounts (a three-decimal minor unit).
