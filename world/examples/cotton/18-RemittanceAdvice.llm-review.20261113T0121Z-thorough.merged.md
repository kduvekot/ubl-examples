# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/18#F1 · Medium · Language code in `LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F1), parties (F1)

### cotton/18#F2 · Low · The invoice referenced twice on the same line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SCG-INV-26-0210`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`
- Why: the line already refers to the paid invoice, with its issue date, through `BillingReference` ("A reference to a billing document associated with this remittance advice line"); the generic `DocumentReference` ("A reference to a document associated with this remittance advice line") repeats the same invoice with the same date and adds only the type "Invoice", which the billing reference's element already says. No second document is associated with the line (no fillers). Logistics checked it for a reference of the wrong kind and refuted that (both point to 16); the redundancy remains.
- Condition: each document associated with the line is referenced once, in the element meant for it.
- Options: (a, preferred) drop the line's `DocumentReference`.
- Needs decision: no
- From: broad (F2), money (F3), context (F1, reference part)

### cotton/18#F3 · Low · The remittance line repeats the header parties
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: the line-level parties are "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line" (and the customer counterpart). They matter when one remittance covers invoices of several suppliers or customers; here the single line pays one invoice between the same two parties as the header, so the line roles add nothing (no fillers).
- Condition: line-level accounting parties are present only where they differ from the header's.
- Options: (a, preferred) drop them from the line; (b) keep them only if the story has the mill pay on behalf of another party.
- Needs decision: no
- From: parties (F4), context (F1, party part)

### cotton/18#F4 · Low · Two different references for the same payment order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `LTM-PAY-26-0191`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `LTM-0191`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `LTM-PAY-26-0191`
- Why: `PaymentOrderReference` is "An internal reference to the order for payment from the payer to the payer's bank", `PayerReference` "An internal reference to the payer's order for payment" (checked in UBL-Entities-2.5.gc). Both name the mill's own payment order, which the payment means confirms as LTM-PAY-26-0191; LTM-0191 is a second, shorter number for the same order that nothing explains. A remittance advice exists so that the payee can match the payment; two numbers for one order invite a mismatch.
- Condition: the mill's payment order is identified by one reference, or the two references visibly identify two different things.
- Options: (a, preferred) drop `PayerReference`; (b) give it a different meaning (e.g. the mill's payment-run number) and a value that fits it.
- Needs decision: no
- From: money (F1)

### cotton/18#F5 · Low · The payer's contact: Purchasing, Customer service officer, Sales
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: here the mill is the payer reporting a payment; questions about it go to accounts payable. Name (buying) and job title and department (selling) also contradict each other. The combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: the payer's contact handles payments, with name, job title and department that agree.
- Options: (a, preferred) an accounts-payable contact; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F3), parties (F2)

### cotton/18#F6 · Low · Lisavan address parts of the ginnery and its bank tagged as Bayvarran English
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Reef Street`
- XPath: `16-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: these renderings carry `languageID` `en-XB` here and `en-XL` in the documents Lisavan parties issue (the ginnery's street in 01, 03-06, 10-12, 16; the Bank of Selanu's Reef Street in 01, 06 and 16), counted over *.xml with `grep -o 'languageID="[^"]*">Gin Yard Road'` / `'…">Reef Street'`. Parties: `languageID` describes the text, so Lisavan street and town names are Lisavan English whoever sends the document. Broad called it a plain inconsistency. The tags follow the issuer consistently (en-XB in all seven Bayvarran-issued examples), a convention earlier flows could not settle either.
- Condition: one rule for the tags of the same party's renderings, applied in every example and documented.
- Options: (a, preferred) the parties' own tags (en-XL) everywhere; (b) if tags follow the issuer, record the rule.
- Needs decision: yes
- From: broad (F4), parties (F3, address part)

### cotton/18#F7 · Low · The ginnery's legal form in one untagged rendering
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: elsewhere the ginnery's legal form is given in Lisavan and English with language tags; here the Lisavan rendering is dropped and the English one has no `languageID`, while the Lisavan street and city names are kept. The same party is described in two ways in the flow.
- Condition: the ginnery's legal form carries the same renderings and tags in every example.
- Options: (a, preferred) both renderings with their tags, as in 01.
- Needs decision: no
- From: parties (F3, legal-form part)

### cotton/18#F8 · Low · Party master data the remittance advice does not use
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: the remittance advice reports a payment; it declares no tax, the paid invoice carries no tax, and nothing is declared to customs. The mill's Coastal State sales-tax registration and both parties' customs-trader numbers have no use here (section 4.8, master data copied in); the ginnery's own remittance advice 06 carries no party tax data.
- Condition: every identifier and registration in the parties is one the remittance advice has a use for.
- Options: (a, preferred) drop the customer's `PartyTaxScheme` and both customs-trader IDs.
- Needs decision: no
- From: money (F4), parties (F6)

### cotton/18#F9 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Mill and ginnery, in two registers, share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F5)

## Checked and consistent
- Total debit 6055.452 − total credit 0.000 = total payment 6055.452 XLC = `DebitLineAmount` = the payable amount of 16; balance 0.000, the invoice is paid in full.
- `InvoiceDocumentReference` SCG-INV-26-0210 with issue date 2026-03-02 resolves to 16; the creditor reference RF46SCGINV260210 that 16 asks to quote is given as `PaymentID` and as the invoicing party's reference (`check_ids.py`: valid).
- Paid on 2026-03-29, before the due date of 16 (2026-04-01 as stated, 2026-04-16 under "45 days net", cotton/16#F1), so no penalty interest arises either way.
- Payer account XB35BLUM38020504608076 (named Lumeport Textile Mill Ltd, Bank of Lumeport) and payee account XL31BSEL0020004922263 (the ginnery's account of 06 and 16) pass their check digits; purpose SUPP fits a supplier payment.
- Payment order reference and instruction ID are the same (LTM-PAY-26-0191), as expected for one transfer. The parties are the supplier and customer of 16; the mill's description is identical to 08 and 16.

## Considered and refuted
- `/RemittanceAdvice/cbc:TotalCreditAmount` = `0.000`: a zero credit total as a filler — refuted because it states explicitly that no credit is set off, which IND6 favours (from broad, context; money made it a finding, see "Refuted in the merge").
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`: a Lume account paying a coral amount without an exchange rate — refuted because the advice tells the payee what it receives (coral), as the invoice asked; the conversion is the payer's bank's matter (from broad, context).
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `LTM-PAY-26-0191`: the serial 0191 equals that of the ginnery's invoice SCG-SBI-26-0191 (01) — refuted because the two are in different issuers' series, and the mill numbers its payment orders as it likes (from logistics).
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`: a reference of the wrong kind — refuted for its lens by logistics (both references point to 16); the redundancy is F2.

## Refuted in the merge
### money/F2 · Low · Zero total of credits in an advice without credit lines
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `0.000`
- Why (money): "the totals of all credit amounts" is 0.000 because no line carries a credit amount; a zero total of something absent carries no information (rule "nothing implied by absence"). The other remittance advice of the flow (06), which does have a credit line, carries no totals of debits and credits at all.
- Condition (money): the advice carries a credit total only when it has credit amounts. Options: drop `TotalCreditAmount` (and keep `TotalDebitAmount`, or drop both as in 06).
- Refuted because: the rule cited works the other way: IND6 says nothing may be implied by absence, so an explicit total of 0.000 is how a remittance advice says that no credit is set off against the debit (broad and context refuted it on this ground); with the debit and payment totals present, a missing credit total would leave the reader to infer it. That 06 carries no totals is a question for 06's review, not a contradiction here.

## Changed in the merge
- broad/F2, money/F3, context/F1 (reference part) → F2; parties/F4 + context/F1 (party part) → F3: context's single finding split by problem.
- parties/F3 split into F6 (tags; with broad/F4; "Needs decision" set to yes, as cotton/13#F11 and cotton/15#F14) and F7 (untagged legal form, Low/no).
- money/F4 + parties/F6 → F8: grouped as copied party data.
- money/F2 moved to "Refuted in the merge".
