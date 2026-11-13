# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit e7f2d60 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/29#F1 · Low · The cotton farm is registered as a commercial company with an expiring registration
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: Lisavu Cotton Farm is a sole proprietorship growing cotton (ISIC 0116). Its legal entity places it in the "Island companies register" of type "Commercial register", although the world's CorporateRegistrationTypeCode list has a code `FARM` for exactly this kind of registration (the list holds COMMERCIAL, CHARITY, ASSOCIATION, FARM; none but COMMERCIAL occurs in any example, 633 times over `world/examples/*/*.xml`, grep over *.xml). `RegistrationExpirationDate` is "the date upon which a registration expires (e.g., registration for an import/export license)"; an entry in a commercial companies register does not expire at the end of a year, while a farm registration renewed yearly would. The two values fit a farm register better than the companies register named. The description is identical in the cotton flow (`cotton/01-SelfBilledInvoice.xml`).
- Condition: The farm's registration scheme, its type code and the expiration date describe one register in which such a registration exists and expires.
- Options: (a) a farm register with type `FARM`, keeping the yearly expiry (preferred: uses the code the list provides and explains the expiry); (b) keep the companies register and drop the expiration date.
- Needs decision: yes (where the island registers its farms is a world decision)

### sea/29#F2 · Low · The contacts' names, job titles and departments disagree
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Farm office`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi sells here, but its contact is named Purchasing (and is a customer service officer in Sales). The farm buys, and its contact, the farm office, is a customer service officer in a Sales department, which a one-person farm buying two benches hardly has. Name, title and department contradict each other in both contacts.
- Condition: Each contact's name, job title and department agree and fit the party's role in the sale (seller's shop or sales; the farm's office).
- Options: (a) Velumi's shop or sales contact, and the farm office without a sales job title and department (preferred); (b) drop job title and department where the functional name suffices.
- Needs decision: no

### sea/29#F3 · Low · The farm's address lines repeat the structured address and mix two languages in one line
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[2]/cbc:Line` = `Farm track off Plantation Road at kilometre 4, past the cotton fields.`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: `AddressLine` is "a single address line expressed as unstructured text", and its `Line` "may be repeated only to provide the same content in multiple natural languages". The four lines repeat the structured street, description, district and town of the same address, and lines 1 and 4 put the Lisavan and the English name into one line, without `languageID`, instead of one rendering per language. The address is thus given twice, once structured with language tags and once unstructured in mixed languages.
- Condition: The address is given either structured or in address lines, and each address line is in one language (with `languageID` where the document's default does not apply).
- Options: (a) drop the address lines, since the structured address is complete (preferred); (b) keep them, one rendering per language and without repeating the structured parts.
- Needs decision: no

### sea/29#F4 · Low · The point of sale is named by the company and its street
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Velumi Trading, Reef Street, Selanu`
- Why: A location's name is the place; here it is the seller's company name and part of its postal address, which the document already gives in the supplier's address. The shop or counter itself (where cash register `T1` stands) is not named.
- Condition: The point of sale is named as a place (e.g. the shop or trade counter), and its address, if needed, is in its `Address`.
- Options: (a) a place name such as Velumi's trade counter, with the address in `Location/Address` if it differs from the party's (preferred); (b) drop the name and keep the location's identifier or address only.
- Needs decision: no

### sea/29#F5 · Low · The seller's customs trader number in a retail receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: The purchase receipt records a card sale of two benches on the island; Velumi's customs trader number plays no part in it and is copied from its master data (section 4.8 of the review rules).
- Condition: The seller carries only the identifiers the receipt uses.
- Options: (a) drop the customs trader identifier (preferred); (b) keep it with a reason.
- Needs decision: no

## Checked and consistent
- Seller Velumi Trading (`IC41859`) is described as in its other documents of the flow (address, legal form in Lisavan and English with `en-XL`); the merchant identifier `CORALCARD-M-0001859` carries Velumi's register number.
- The buyer, Lisavu Cotton Farm (`IC42544`, sole proprietorship, micro enterprise, ISIC 0116), is described identically to the cotton flow (compared element by element with a script); its sole proprietorship indicator agrees with its legal form code `SP`.
- The card holder name (`LISAVU COTTON FARM`) and the role `HOLDER` match the accounting customer; the card issuer `BSELXLSL` is the Bank of Selanu, an island bank, which fits an island farm.
- The farm's postal address and physical location carry the same coordinates, and the address description (directions along the farm track) is "text describing this address for clarification", which fits a farm without a building number.
- The item's GTIN passes its check digit (check_ids.py).

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Description`: driving directions in a postal address — refuted because the element is defined as clarifying text for the address, and a farm on a track without building number is found by such a description.
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode`: a liquidation status for a sole proprietorship — refuted because a registered business, sole or not, can be wound up; the status is meaningful.
