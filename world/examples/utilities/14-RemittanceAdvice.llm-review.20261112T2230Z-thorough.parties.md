# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/14#F1 · Medium · Velumi's remittance advice numbered in Valdara's series, and its payer references carry Ferrano's invoice number
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- Why: the document `ID` is "An identifier for this document, assigned by the sender". The sender is Velumi Trading (accounting customer and signatory, whose own references start `VT-`), but the ID has the `VI-` prefix of Valdara Industries and is exactly the ID of Valdara's remittance advice `04-RemittanceAdvice.xml` (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`) and of Brightmarket's `07-RemittanceAdvice.xml`. Three documents of one collaboration (`UTILITIES-2026-01`) from three senders share one ID. The payment order and payer references end in `0313`, the number of Ferrano Energy's invoice that 04 pays (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PayerReference` = `VI-0313`), while this advice pays ST-INV-26-0323. The identifiers look copied from 04 with the prefix partly changed.
- Condition: the remittance advice's ID belongs to Velumi's own numbering and differs from the IDs of 04 and 07; the payer references are Velumi's own and do not echo another party's invoice number.
- Options: (a) a `VT-RM-…` document ID and payment references numbered for this payment (preferred); (b) any other numbering of Velumi's, as long as it is not Valdara's series.
- Needs decision: no

### utilities/14#F2 · Low · Payer's customs trader number in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: Velumi's customs trader number has no use in a domestic telecom document (island lines, data and roaming, no goods). It is part of Velumi's party data repeated in every example that carries it.
- Condition: the customs trader number appears here only with a use in this document.
- Options: (a) drop it here (preferred); (b) keep it only with a stated reason.
- Needs decision: no

### utilities/14#F3 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), Selanu Telecom and Velumi Trading among them, while every other registration date is used by one company only; the shared New Year's Day looks like a default value, not the companies' story (no-fillers rule). For Selanu Telecom, `SMALL` ("Small enterprise") is also questionable: it runs the island's business lines, a mobile data service and roaming agreements, which suggests a national operator rather than a small firm; on a small island this may still be intended.
- Condition: both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits what the story makes of it, the same in every example.
- Options: (a) give each company a registration date of its own and review the operator's size (preferred); (b) drop the elements where the documents do not need them.
- Needs decision: yes

### utilities/14#F4 · Low · Payer's contact: purchasing with a sales job title and department
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: name and job title/department contradict each other, and on a remittance advice the payer's contact is the one who answers for the payment (accounts payable), not the sales side. The contact is the same in every example with Velumi's full data.
- Condition: name, job title and department agree, and the function deals with payments.
- Options: (a) an accounts payable contact for Velumi in the payment documents (preferred); (b) drop the job title and department.
- Needs decision: no

## Checked and consistent
- Payer Velumi Trading and payee Selanu Telecom are the accounting customer and supplier of the invoice paid, `13-Invoice.xml`, with the same register numbers and descriptions; `SignatoryParty` is Velumi, the issuer.
- Payer account `XL40BSEL0010003665515` is named "Velumi Trading Ltd" (its registration name) and is Velumi's account in the sea flow as well; payee account `XL18BSEL0010004293889` is the one invoice 13 gives. Both are at the Bank of Selanu, branch `001`.
