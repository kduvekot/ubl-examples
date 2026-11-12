# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/09#F1 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is a language code repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID; (b) leave it out.
- Needs decision: no

### energy/09#F2 · Medium · Province held in Region
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the payee's bank address in this document does (`/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/09#F3 · Low · Contacts of a remittance advice are trading and sales
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Energy trader`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- Why: The remittance advice tells the payee which invoice and surcharge a payment settles; it is sent by the payer's accounts payable or treasury to the payee's accounts receivable. Montebrio's energy trader and Kelpstone's gas sales manager are the commercial contacts of the deal, copied from the invoice `06-Invoice.xml`.
- Condition: the payer's contact handles payments and the payee's contact handles receivables.
- Options: (a) preferred: accounts contacts on both sides (as also for the reminder 08); (b) leave the contacts out.
- Needs decision: no

### energy/09#F4 · Low · Kelpstone's plant location copied into the remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: A remittance advice does nothing with the location of the payee's plant; the data looks copied from master data, and the `InformationURI` is the company's home page rather than a document about the location.
- Condition: the supplier carries no physical location the remittance advice does not use.
- Options: (a) preferred: leave `PhysicalLocation` out; (b) keep it only with a reason.
- Needs decision: no

## Checked and consistent
- The accounting customer (payer) Montebrio Power and accounting supplier (payee) Kelpstone Gas are the parties of the referenced invoice `06-Invoice.xml` and reminder `08-Reminder.xml`, with the same identifiers, legal entities and tax schemes.
- The payer account `XU720351041700000005021992` is held by `Montebrio Power SUA` and is the account Montebrio names as payee in `03-Invoice.xml`; the payee account is Kelpstone's account from 06 and 08.
- Montebrio's address here is tagged `en-XU`, as in 03 and 05 (the `en-XB` tags in 04, 06 and 08 are findings there).
