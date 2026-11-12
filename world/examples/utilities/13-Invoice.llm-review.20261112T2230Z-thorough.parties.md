# LLM review: 13-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/13#F1 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), Selanu Telecom and Velumi Trading among them, while every other registration date is used by one company only; the shared New Year's Day looks like a default value, not the companies' story (no-fillers rule). For Selanu Telecom, `SMALL` ("Small enterprise") is also questionable: it runs the island's business lines, a mobile data service and roaming agreements, which suggests a national operator rather than a small firm; on a small island this may still be intended.
- Condition: both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits what the story makes of it, the same in every example.
- Options: (a) give each company a registration date of its own and review the operator's size (preferred); (b) drop the elements where the documents do not need them.
- Needs decision: yes

### utilities/13#F2 · Low · Customer's customs trader number in a telecom invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: Velumi's customs trader number has no use in a domestic telecom document (island lines, data and roaming, no goods). It is part of Velumi's party data repeated in every example that carries it.
- Condition: the customs trader number appears here only with a use in this document.
- Options: (a) drop it here (preferred); (b) keep it only with a stated reason.
- Needs decision: no

### utilities/13#F3 · Low · Customer's contact: purchasing with a sales job title and department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name says purchasing, its job title and department say customer service in Sales; they contradict each other. For telecom bills Velumi receives, purchasing (or accounts payable) fits, the sales side does not. The contact is the same in every example with Velumi's full data.
- Condition: name, job title and department of Velumi's contact agree, and the function fits the role of receiving the telecom statement and bill.
- Options: (a) a purchasing job title and department, or an accounts payable contact (preferred); (b) drop the job title and department.
- Needs decision: no

## Checked and consistent
- Supplier/seller Selanu Telecom and customer/buyer Velumi Trading match statement `12-UtilityStatement.xml` and remittance advice `14-RemittanceAdvice.xml`, with the same register numbers and descriptions.
- `BuyerCustomerParty` and `SellerSupplierParty` repeat the accounting parties; their definitions carry no condition.
- Payee account `XL18BSEL0010004293889` is named "Selanu Telecom Ltd", the supplier's registration name, at the Bank of Selanu, branch `001`, matching the account digits; it is the payee account of 14.
- Neither party carries a tax scheme, matching the "No general sales tax" tax categories of the lines.
