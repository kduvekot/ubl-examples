# LLM review: 07-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/07-Invoice.xml`, Git blob `a1e9b7e2c326a01d31d3b741f419d375d10a04e9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/07#F1 · Medium · Province of Ferrano in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is an administrative division of Urvania, so it belongs in `CountrySubentity` (with `CountrySubentityCode` if Urvania has a list), not in `Region`. The Bayvarran addresses of the same flow do it that way (`CountrySubentity` = `Coastal State`). The same `Region` value occurs in 104 of the 250 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address in this example carries the province in `Region`; where the province is given, it is in `CountrySubentity`.
- Options: (a) move the value to `CountrySubentity` (preferred: it is what the element is for, and it matches the Bayvarran addresses); (b) drop it where the postal code already identifies the place.
- Needs decision: no

### plastics/07#F2 · Low · Contacts do not fit the role the party has in this document
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Chartering desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's `Contact` fits its role. The parties carry one generic contact in every document of the flow: Rinova's "Customer service" in Sales, Rivermouth's "Order desk" with job title "Customer service officer" in Sales (a buyer's order desk is not a sales department), and Fiumella's "Chartering desk" in Operations. In this document `/Invoice/cac:AccountingSupplierParty/cac:Party` is the supplier that issues the invoice (billing or accounts receivable); `/Invoice/cac:AccountingCustomerParty/cac:Party` is the customer that pays the invoice (accounts payable). The contacts shown are the ones for a different task.
- Condition: Each contact listed above is one that handles the task the party has in this document (or is absent where the document needs no contact for that party).
- Options: (a) give each party role-specific contacts and use the one for the role (preferred: it is what `Contact` is for); (b) drop the contact where the document does not need one.
- Needs decision: no

### plastics/07#F3 · Low · Rinova's waste-recovery permit carried in a document about a non-waste product
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: `Party/PartyAuthorization` is "An authorization issued to this party". The permit (Basel Annex IV R3, "Recovery of non-hazardous plastic waste") authorises Rinova to operate its recovery plant. The goods of the flow are recycled PE granulate classified as a product (HS `390110`, polyethylene in primary forms, not HS 3915 waste), so no step of this flow carries waste. Nothing in this document refers to the permit, so it looks copied from Rinova's master data. It could be argued that the permit supports the recycled-content claim, but that claim has its own `EnvironmentalCertificate` on the item where the document has an item.
- Condition: Rinova's party carries the permit only in documents whose purpose needs it, or the document states why it is there.
- Options: (a) drop it here (preferred if the granulate is a product, as the HS code says); (b) keep it and make its purpose explicit if the story wants the buyer or the authorities to see that the granulate comes from a licensed recovery plant.
- Needs decision: yes

### plastics/07#F4 · Low · Registration date 1996-01-01 looks like a default value
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Every company in this example (`XU-R-104548`, `XU-R-104959`) is registered on 1 January 1996, a public holiday on which registers do not normally register companies. The same date occurs in 181 of the 250 examples, for at least 24 unrelated companies (counted with `grep -rl --include='*.xml' 'RegistrationDate>1996-01-01'` and the `RegistrationName` before it), while some other parties have specific dates (e.g. `1962-04-12`, `1988-10-03`). Under the no-filler rule a value needs a reason in the world.
- Condition: Each company's `RegistrationDate` is a date that belongs to that company's history, or the element is absent.
- Options: (a) give each company its own registration date from its history (preferred); (b) drop `RegistrationDate` where no history is known.
- Needs decision: no

### plastics/07#F5 · Low · Italian text tagged as English
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: The checklist asks that each repeated rendering is in the language its `languageID` names. The second renderings of Urvanian street names are Italian ("Via del Riciclo" is "Recycling street", "Banchina del Fiume" "River quay", "Piazza della Banca" "Bank square", "Valico di Confine" "Border crossing"), and the English legal form is Italian with an English gloss, while they are tagged `en-XU` or `en-XB` (or, for `CompanyLegalForm` without a tag, sit in a document whose other texts are English). Bayvarran streets in the same flow are English (`Estuary Road`, `Exchange Street`). If the world gives Urvanian places Italianate names as their English exonyms (as `Ferrano` for `Ruldraz`), that convention is not visible in the documents; the same pattern occurs in 101 of the 250 examples (`grep -rlE --include='*.xml' 'languageID="en-X[UB]">(Via|Banchina|Piazza|Valico|Società)'`).
- Condition: Every rendering tagged `en-…` is English (or a proper name used as such in English), and Italian text, if the world has it, carries an Italian tag or none.
- Options: (a) translate the renderings into English ("Recycling Street", "River Quay") (preferred if English is meant); (b) if the Italianate forms are the world's official exonyms, record that in the world's story and keep them; (c) drop the second rendering where the local form suffices.
- Needs decision: yes

## Checked and consistent
- Accounting supplier and seller Fiumella, accounting customer and buyer Rinova fit a freight invoice under CPT (the seller pays the carriage); the payee account `XU590351041620000000733103` is in Fiumella's name and passes the check digit.
- Every party that appears in several documents of the flow was compared field by field (script over all `*.xml` of the flow): Rinova Recovery (`XU-R-104548`), Rivermouth Packaging (`20412740`), Fiumella Barges (`XU-R-104959`) and the Ferrano Chamber of Commerce (`XU-R-105370`) carry the same identifiers, names, tax registrations, legal entities, addresses, contacts and electronic addresses everywhere, apart from the language renderings noted in the findings.
- `check_ids.py`: every IBAN-like account and RF reference in the example passes its check digits (where present).
- Industry classifications fit the parties: Rinova `3830` (materials recovery), Rivermouth `2220` (manufacture of plastics products), Fiumella `5022` (inland freight water transport), customs `8411`.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped bank identifier (`CREVXUFR`) could be a real BIC — refuted because positions 5–6 carry the user-assigned ISO 3166 code of a fictional country (`XB`/`XU`), which no real BIC uses.
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the seller of the goods (Rinova) as buyer — refuted because in this invoice Rinova buys the freight service from Fiumella.
