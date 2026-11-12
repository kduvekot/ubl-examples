# LLM review: 17-RemittanceAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/17-RemittanceAdvice.xml`, Git blob `9bee7dcb73c7b573cbe5ebbd0a5552954365dc02` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit adfced0 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/17#F1 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/17#F2 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/17#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/17#F4 · Low · Contacts that do not fit the role
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A remittance advice goes from accounts payable to accounts receivable. Lumeway's contact is its `Customer service` desk in `Sales`, Valdara's its `Order desk` in `Sales`.
- Condition: The accounting parties' contacts are payment/accounts contacts.
- Options: (a, preferred) give both parties accounts contacts; (b) omit JobTitle/Department.
- Needs decision: no

### road/17#F5 · Low · Paying account carries the alias "receivables"
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:AliasName` = `Lumeway receivables`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Lumeway Distribution Ltd`
- Why: `AliasName` is "An alias for the name of this financial account, to be used in place of the actual account name for security reasons". The account is the payer's, from which Lumeway pays its supplier; calling it "Lumeway receivables" describes an account for incoming payments, which does not fit, and no security reason for an alias appears.
- Condition: The payer account's alias (if any) fits its use for outgoing payments, or is absent.
- Options: (a, preferred) remove the alias; (b) use an alias such as "Lumeway payments".
- Needs decision: no

## Checked and consistent
- Amounts: total debit 4 862 160 XUF = line debit = invoice payable amount of `15-Invoice.xml`; credit 0; balance 0; full payment is right because the discount period ended on 2026-04-03 and payment is on 2026-04-22, before the due date 2026-04-23.
- Payment reference RF78VIINV260166 and payee account XU79… equal the invoice's; payer account XB19BLUM38712001466206 passes its check digits and agrees with branch 387120 of the Bank of Lumeport.
- Invoice references (billing reference and document reference) resolve to `15-Invoice.xml` with the right issue date 2026-03-24.
- Payment from an XBL account to an XUF account for an XUF amount is consistent; the conversion is done by the payer's bank.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:IssueDate` = `2026-03-24` duplicates the billing reference — refuted: the document reference adds the document type and is harmless.

## Outside this review
- The freight invoice `14-Invoice.xml` (Trasvia, due 2026-04-24) is not paid in the flow; whether the flow should show its payment is a question of the flow's scope.
