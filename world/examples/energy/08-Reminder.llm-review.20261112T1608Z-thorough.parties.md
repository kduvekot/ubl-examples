# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/08-Reminder.xml`, Git blob `e24bac5879420244e021d7b208594e7ca88f789d` (committed)
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

### energy/08#F1 · Medium · Language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is a language code repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID; (b) leave it out.
- Needs decision: no

### energy/08#F2 · Medium · Province held in Region
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the supplier's bank address in this reminder does (`/Reminder/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/08#F3 · Low · Contacts of a payment reminder are sales and trading
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Energy trader`
- Why: A reminder chases an overdue payment and adds a late surcharge; it comes from the supplier's credit control or accounts receivable and is addressed to the customer's accounts payable. The gas sales manager and the energy trader are the parties' commercial contacts, copied unchanged from the invoice `06-Invoice.xml`.
- Condition: the supplier's contact handles receivables and the customer's contact handles payables.
- Options: (a) preferred: give both parties accounts contacts in the reminder (and the remittance advice 09); (b) leave the contacts out.
- Needs decision: no

### energy/08#F4 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Montebrio Power's English address renderings carry `languageID="en-XB"`, while the same texts are `en-XU` in `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`, in 03 and in 05; the legal form, in `qau` and `en-XU` there, is one untagged text here. 107 Urvanian addresses in 39 `*.xml` files carry an `en-XB` rendering (lxml count).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag Urvanian names' English renderings `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no

### energy/08#F5 · Low · Kelpstone's plant location copied into the reminder
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: A payment reminder does nothing with the location of the producer's plant; the data looks copied from master data, and the `InformationURI` is the company's home page rather than a document about the location.
- Condition: the supplier carries no physical location the reminder does not use.
- Options: (a) preferred: leave `PhysicalLocation` out; (b) keep it only with a reason in the reminder.
- Needs decision: no

## Checked and consistent
- The reminder's accounting parties are the supplier and customer of the referenced invoice `06-Invoice.xml` (Kelpstone Gas `20412877`, Montebrio Power `XU-R-105918`), with the same identifiers, legal entities and tax schemes.
- The payee account `XB45BLUM38522004817534` is the one named in 06, held by `Kelpstone Gas Ltd`.
