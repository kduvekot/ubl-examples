# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/14-RemittanceAdvice.xml`, Git blob `13ca288b96ca5f33f56aefe8db004930ea15062a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### utilities/14#F1 · High · Document ID of another payer's remittance advice
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: ID is "An identifier for this document, assigned by the sender." The sender is Velumi Trading, whose other references use the prefix VT (VT-PAY-…, VT-BANK-…, VT-SIG-RA). VI-RM-26-0316 is Valdara Industries' advice `04-RemittanceAdvice.xml`, and is used a third time in `07-RemittanceAdvice.xml`; the flow has three advices with one ID.
- Condition: The advice has an ID of Velumi's own numbering, unique in the flow.
- Options: (a, preferred) a VT-RM-… number.
- Needs decision: no

### utilities/14#F2 · Low · Payment order and payer references numbered after Valdara's invoice
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0313`
- Why: The suffix 0313 follows Ferrano's invoice FE-INV-26-0313 paid in `04-RemittanceAdvice.xml`; Velumi pays ST-INV-26-0323.
- Condition: The payer's references follow Velumi's numbering or the paid invoice.
- Options: (a, preferred) VT-PAY-26-0323 / VT-0323 or a Velumi sequence.
- Needs decision: no

### utilities/14#F3 · Medium · A blockchain identifier on a bank current account
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountFormatCode` = `ISO13616`
- Why: BlockchainID is "An identifier of the Blockchain on which the crypto or stablecoin is being held"; the payee account is an ISO 13616 bank account in Coral, copied from `13-Invoice.xml`. The payer's account in this same advice has no blockchain, so the transfer is bank to bank.
- Condition: BlockchainID only for an account holding crypto or stablecoins on that chain.
- Options: (a, preferred) remove; (b) as in `13-Invoice.xml`, if Coral is a ledger currency in the world.
- Needs decision: yes

### utilities/14#F4 · Low · Payment purpose "supplier payment" where the invoice names a telephone bill
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `PHON`
- Why: The invoice gives the ISO 20022 purpose PHON (TelephoneBill); the advice reports the generic SUPP.
- Condition: The purpose agrees with the invoice's, or is absent.
- Options: (a, preferred) PHON.
- Needs decision: no

### utilities/14#F5 · Low · Additional document reference with only an ID; invoice referenced twice
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VT-BANK-26-04`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `ST-INV-26-0323`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `ST-INV-26-0323`
- Why: VT-BANK-26-04 says nothing about what it is, and no example carries it; the line's DocumentReference repeats its billing reference.
- Condition: The additional reference says what it is; each document is referenced once per line.
- Options: (a, preferred) add type and description; keep BillingReference only.
- Needs decision: no

### utilities/14#F6 · Low · Payer master data the remittance does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- Why: A customs trader number and the purchasing department play no part in a payment advice.
- Condition: The payer carries what the advice uses, with an accounts payable contact.
- Options: (a, preferred) remove the customs ID; accounts payable contact.
- Needs decision: no

## Checked and consistent
- References ST-INV-26-0323 resolve to `13-Invoice.xml` (issued 2026-04-02); 135.566 paid in full on 2026-04-19, before the due date; balance 0.000.
- PaymentID / InvoicingPartyReference RF26STINV260323 and the payee account equal the invoice's.

## Considered and refuted
- `/RemittanceAdvice/cbc:TotalCreditAmount`: 0.000 stated — refuted because a zero credit total is an actual statement of a debit-only advice.
