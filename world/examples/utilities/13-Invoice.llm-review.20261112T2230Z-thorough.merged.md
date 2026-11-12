# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/13-Invoice.xml`, Git blob `b2c86dfb706324ffa17a917a0b1b5d175a28be17` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/13#F1 · High · Due dates 21 days after the invoice date; the terms say "45 days net"
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- Why: Recalculated in the merge: 2026-04-02 + 45 days = 2026-05-17 (28 days to 30 April, 17 more in May); all three due dates are 2026-04-23, i.e. 21 days, the same as in the flow's other invoices (02, 06, 09). The free text and the structured dates contradict each other, and the penalty interest (6 % a year) would accrue from 24 April on an amount that is not yet due under the note. The same terms ID XL-STD carries "45 days net." elsewhere in the world with a 45-day due date (`cotton/04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:DueDate` = `2026-03-24`, issued 2026-02-07), so the world's XL-STD terms are 45 days.
- Condition: The payment terms' note and the due dates state the same term.
- Options: (a, preferred) due dates 2026-05-17, because XL-STD means 45 days elsewhere in the world; the remittance 14 (paid 2026-04-19) fits either; (b) note "21 days net". This differs from merger A's preference for the Bayvarran invoices 02 and 06 (note "21 days net"), whose terms XB-STD are not defined elsewhere.
- Needs decision: no
- From: broad (F1), money (F1), context (F1), logistics (F1)

### utilities/13#F2 · Medium · A blockchain identifier on a bank current account in the national currency
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentRailID` = `CORAL-NET`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XL18BSEL0010004293889`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountTypeCode` = `CACC`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountFormatCode` = `ISO13616`
- Why: UBL defines BlockchainID as "An identifier of the Blockchain on which the crypto or stablecoin is being held." The account is an IBAN-structured (ISO 13616) current account (CACC) at Bank of Selanu, held in XLC, the island's currency, and paid by credit transfer through an RTGS channel; nothing says that XLC is a crypto-asset or stablecoin held on CORAL-NET, and the identifier is the rail's name with "-L1" appended. If Coral were a ledger currency in the world, the account would be a wallet, not a bank IBAN. The element occurs only here and in `14-RemittanceAdvice.xml` (`grep -rl --include='*.xml' 'BlockchainID'`).
- Condition: BlockchainID is present only on an account holding crypto or stablecoins on that chain, and the account, channel and rail then describe that.
- Options: (a, preferred) remove BlockchainID (an ordinary RTGS credit transfer), together with 14; (b) if the world's Coral is a token on CORAL-NET, say so in the story and describe the account and channel accordingly.
- Needs decision: yes
- From: broad (F2, Low/yes), money (F3, Medium/yes), context (F2, Medium/yes); logistics (under "Outside this review")

### utilities/13#F3 · Low · Telephone lines booked to "Stock for municipal projects"
- XPath: `/Invoice/cbc:AccountingCostCode` = `500`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". Telephone lines and data are office overheads; the text is Velumi's code for its goods purchases (recounted in the merge: 10 occurrences in 9 files over `world/examples/*/*.xml`), copied from master data. Statement 12 carries the same value (12#F10).
- Condition: Velumi's communication or office cost account (the same in 12 and 13), or absent.
- Options: (a, preferred) a communication cost account.
- Needs decision: no
- From: broad (F3), money (F4), context (F3)

### utilities/13#F4 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 companies of the world are registered on 1 January 1996 (parties' count), Selanu Telecom and Velumi Trading among them; recounted in the merge: 271 occurrences in 181 files. A shared default (no fillers). For Selanu Telecom, `SMALL` is also questionable for the island's operator of business lines, mobile data and roaming; on a small island it may still be intended.
- Condition: Both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits its story, the same in every example.
- Options: (a, preferred) a registration date of its own for each company, and review the operator's size; (b) drop the elements where the documents do not need them.
- Needs decision: yes
- From: parties (F1)

### utilities/13#F5 · Low · Customer's customs trader number in a telecom invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: A domestic telephone invoice does not use the customer's customs trader number (island lines, data and roaming, no goods); it is Velumi's party data repeated in every example that carries it.
- Condition: The customer carries only identifiers the invoice uses.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (F4), parties (F2), context (F4, part)

### utilities/13#F6 · Low · Customer's contact: "Purchasing" with a sales job title and department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name, job title and department contradict each other, and neither purchasing (which buys goods for trade) nor the sales side is the natural contact for the telecom bills Velumi receives. The contact is the same in every example with Velumi's full data.
- Condition: Name, job title and department agree, and the function fits receiving the bill (accounts payable or office management).
- Options: (a, preferred) an accounts-payable or office contact; (b) drop the job title and department.
- Needs decision: no
- From: parties (F3), context (F4, part)

### utilities/13#F7 · Low · A 0 % rate on supplies outside the scope of tax
- XPath: `/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O (outside the scope of tax) has no rate, so a rate of 0 % describes zero-rating (Z). Same in statement 12 (12#F17).
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no
- From: money (F5)

### utilities/13#F8 · Low · A tax total for a tax scheme that, by its name, does not exist
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: TaxScheme is "a tax scheme"; here it has no ID, and its name says there is no such tax. A tax total of 0 under a non-existent scheme, with category O, states the absence of tax as if it were a tax, close to "nothing implied by absence" (IND5/IND6) read the other way. If the world requires a tax statement on every invoice (as EN 16931 does for O), it would be the scheme the island's law defines, with an identifier. Money called the name "defensible for an island without sales tax"; that is why this stays Low and a decision.
- Condition: Either the tax scheme is a real scheme of Lisavu with an identifier, or the invoice carries no tax total, consistently with the world's rules for Lisavu.
- Options: (a) drop TaxTotal and the tax categories if the world's Lisavan invoice rules allow it; (b) name the scheme by an identifier from the world's tax list. Preference: decide once for all Lisavan examples.
- Needs decision: yes
- From: broad (F5)

### utilities/13#F9 · Low · Six lines for one month invoiced as "6 months"
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:BaseQuantity` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:Description` = `Six business lines`
- XPath: `/Invoice/cac:InvoicePeriod/cbc:Description` = `March 2026`
- Why: unitCode MON makes the quantity six months of subscription at 21.18 per month, while the invoice period is March 2026 only and the purchase reference says "Six business lines": the quantity counts lines. Read as six line-months the arithmetic holds (6 × 21.18 = 127.08), so the unit is ambiguous rather than wrong (Low, as in 12#F19).
- Condition: The quantity's unit counts what is billed, consistent with the one-month period, the same in statement 12.
- Options: (a, preferred) quantity 6 in C62 (or EA) at 21.18 per line and month; (b) six lines of 1 MON.
- Needs decision: no
- From: money (F2, Medium), logistics (F2, Low)

### utilities/13#F10 · Low · Line references that the utility statement does not carry
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:ID` = `ST-L-BUS6`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:PurchaseReference/cbc:ID` = `ST-D-0042`
- Why: PurchaseReference is "A reference to an object, such as a subscription number, telephone number, meter …, to which this Invoice Line relates". ST-L-BUS6 (the six business lines) and ST-D-0042 (the data pool) appear in no other example (counted over `world/examples/*/*.xml`: only this file). The supplementing statement `12-UtilityStatement.xml` identifies the lines by phone number (+999 3 721 1850 … 1855) and the pool by the placeholder "data pool" (12#F7), so the invoice's objects cannot be matched to the statement's supply lines by identifier; in the other invoices of the flow the PurchaseReference is the meter number the statement also carries. Context refuted the data-pool reference as a legitimate object; that is right for the element, but does not answer the missing link to the statement.
- Condition: Each object referenced on an invoice line is identified the same way in the statement (an ID or number both carry).
- Options: (a, preferred) give the statement's data pool line the pool's identifier ST-D-0042 (see 12#F7) and relate the business lines to ST-L-BUS6 (e.g. in their description); (b) use the phone numbers as purchase references.
- Needs decision: no
- From: logistics (F3); context's refutation answered above

## Checked and consistent
- Lines (redone in the merge): 6 × 21.18 = 127.08; 35 × 0.424 = 14.84; LineExtensionAmount 141.92; allowance 5 % × 127.080 (BaseAmount) = 6.354, reason code 95 (Discount), on the subscriptions only; 141.920 − 6.354 = 135.566 = TaxExclusive = TaxInclusive = Payable = taxable amount; AllowanceTotal and AllowanceTotalTaxInclusive 6.354 (no tax); LineCountNumeric 2.
- Agreement with `12-UtilityStatement.xml` (quantities, prices, discount, payable; the statement at 17:37 follows the invoice at 11:19; line IDs 1 and 2 match its ParentDocumentLineReferenceIDs) and with `14-RemittanceAdvice.xml` (pays 135.566 on 2026-04-19).
- Penalty interest 6 % per annum (ANN), simple; both lines have purpose PHON (TelephoneBill).
- Parties: supplier/seller Selanu Telecom and customer/buyer Velumi Trading as in 12 and 14; BuyerCustomerParty and SellerSupplierParty carry no condition; payee account `XL18BSEL0010004293889` named "Selanu Telecom Ltd" at Bank of Selanu, branch 001; neither party carries a tax scheme, matching "No general sales tax".
- check_ids.py: RF26STINV260323 and XL18BSEL0010004293889 correct; BIC-like BSELXLSL uses the user-assigned code XL.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: RTGS for a 135 XLC bill — refuted, the world's Coral rail CORAL-NET may be the only interbank system on the island (from broad).
- `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount`: three decimals in Coral — refuted, consistent across all Lisavan amounts (a three-decimal minor unit) (from broad).
- `/Invoice/cac:InvoiceLine[2]/cac:PurchaseReference/cbc:ID`: data pool ST-D-0042 as purchase reference — refuted, PurchaseReference names subscription and telephone numbers as its objects, and the pool is such an object (from context; the missing link to the statement is F10).
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: SERVICES — refuted, telecommunication is a service (from context).

## Changed in the merge
- broad/F1, money/F1, context/F1, logistics/F1 → F1: preference set to the 45-day due date, after finding XL-STD = 45 days in `cotton/04-SelfBilledInvoice.xml`; explained against merger A's preference for 02/06.
- broad/F2 (Low) → F2: Medium, with money and context: the value does not meet the definition's condition (crypto or stablecoin held on the chain).
- money/F2 (Medium), logistics/F2 (Low) → F9: Low, as 12#F19.
- broad/F4, parties/F2, context/F4 → F5 (customs ID) and F6 (contact): context's combined finding split by element.
- Counts re-made ("Stock for municipal projects" 10 in 9 files; RegistrationDate 271 in 181 files).
