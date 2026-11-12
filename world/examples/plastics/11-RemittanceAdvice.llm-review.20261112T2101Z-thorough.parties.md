# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/11-RemittanceAdvice.xml`, Git blob `d0c26e7bbd846569482f83cb92b801d665bd1d34` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### plastics/11#F1 · Medium · Province of Ferrano in `Region` instead of `CountrySubentity`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is an administrative division of Urvania, so it belongs in `CountrySubentity` (with `CountrySubentityCode` if Urvania has a list), not in `Region`. The Bayvarran addresses of the same flow do it that way (`CountrySubentity` = `Coastal State`). The same `Region` value occurs in 104 of the 250 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address in this example carries the province in `Region`; where the province is given, it is in `CountrySubentity`.
- Options: (a) move the value to `CountrySubentity` (preferred: it is what the element is for, and it matches the Bayvarran addresses); (b) drop it where the postal code already identifies the place.
- Needs decision: no

### plastics/11#F2 · Medium · Language code in `LocaleCode`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; the language itself is `Language/ID`. The value `en` with `listID` `ISO 639` repeats the language code from `Language/ID` instead of naming a locale (a language plus a region, such as the Bayvarran variant the example itself writes as `en-XB`). The same value occurs in 213 of the 250 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<'`).
- Condition: Every `LocaleCode` holds a locale identifier from a locale list (e.g. a BCP 47 tag such as `en-XB`) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` (preferred unless the locale matters to the receiver: the language is already in `Language/ID`); (b) set it to the locale (`en-XB`) with a locale list as `listID`.
- Needs decision: no

### plastics/11#F3 · Low · Contacts do not fit the role the party has in this document
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's `Contact` fits its role. The parties carry one generic contact in every document of the flow: Rinova's "Customer service" in Sales, Rivermouth's "Order desk" with job title "Customer service officer" in Sales (a buyer's order desk is not a sales department), and Fiumella's "Chartering desk" in Operations. In this document `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party` is the payer that sends the remittance advice (accounts payable); `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party` is the payee that matches the payment (accounts receivable). The contacts shown are the ones for a different task.
- Condition: Each contact listed above is one that handles the task the party has in this document (or is absent where the document needs no contact for that party).
- Options: (a) give each party role-specific contacts and use the one for the role (preferred: it is what `Contact` is for); (b) drop the contact where the document does not need one.
- Needs decision: no

### plastics/11#F4 · Low · Rinova's waste-recovery permit carried in a document about a non-waste product
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: `Party/PartyAuthorization` is "An authorization issued to this party". The permit (Basel Annex IV R3, "Recovery of non-hazardous plastic waste") authorises Rinova to operate its recovery plant. The goods of the flow are recycled PE granulate classified as a product (HS `390110`, polyethylene in primary forms, not HS 3915 waste), so no step of this flow carries waste. Nothing in this document refers to the permit, so it looks copied from Rinova's master data. It could be argued that the permit supports the recycled-content claim, but that claim has its own `EnvironmentalCertificate` on the item where the document has an item.
- Condition: Rinova's party carries the permit only in documents whose purpose needs it, or the document states why it is there.
- Options: (a) drop it here (preferred if the granulate is a product, as the HS code says); (b) keep it and make its purpose explicit if the story wants the buyer or the authorities to see that the granulate comes from a licensed recovery plant.
- Needs decision: yes

### plastics/11#F5 · Low · Registration date 1996-01-01 looks like a default value
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Every company in this example (`20412740`, `XU-R-104548`) is registered on 1 January 1996, a public holiday on which registers do not normally register companies. The same date occurs in 181 of the 250 examples, for at least 24 unrelated companies (counted with `grep -rl --include='*.xml' 'RegistrationDate>1996-01-01'` and the `RegistrationName` before it), while some other parties have specific dates (e.g. `1962-04-12`, `1988-10-03`). Under the no-filler rule a value needs a reason in the world.
- Condition: Each company's `RegistrationDate` is a date that belongs to that company's history, or the element is absent.
- Options: (a) give each company its own registration date from its history (preferred); (b) drop `RegistrationDate` where no history is known.
- Needs decision: no

### plastics/11#F6 · Low · Italian text tagged as English
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: The checklist asks that each repeated rendering is in the language its `languageID` names. The second renderings of Urvanian street names are Italian ("Via del Riciclo" is "Recycling street", "Banchina del Fiume" "River quay", "Piazza della Banca" "Bank square", "Valico di Confine" "Border crossing"), and the English legal form is Italian with an English gloss, while they are tagged `en-XU` or `en-XB` (or, for `CompanyLegalForm` without a tag, sit in a document whose other texts are English). Bayvarran streets in the same flow are English (`Estuary Road`, `Exchange Street`). If the world gives Urvanian places Italianate names as their English exonyms (as `Ferrano` for `Ruldraz`), that convention is not visible in the documents; the same pattern occurs in 101 of the 250 examples (`grep -rlE --include='*.xml' 'languageID="en-X[UB]">(Via|Banchina|Piazza|Valico|Società)'`).
- Condition: Every rendering tagged `en-…` is English (or a proper name used as such in English), and Italian text, if the world has it, carries an Italian tag or none.
- Options: (a) translate the renderings into English ("Recycling Street", "River Quay") (preferred if English is meant); (b) if the Italianate forms are the world's official exonyms, record that in the world's story and keep them; (c) drop the second rendering where the local form suffices.
- Needs decision: yes

### plastics/11#F7 · Low · Rinova described differently from the other documents of the flow
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:CertificateType` = `Operating permit`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- Why: The checklist asks that the same party is described the same way in every example of the flow. In `02-OrderResponse.xml` to `08-DespatchAdvice.xml` and `10-Invoice.xml`, Rinova's legal form and permit type carry an Urvanian and an English rendering, each tagged (`qau`, `en-XU`). In this document (as in the other documents issued by Rivermouth, `01-Order.xml`, `09-ImportCustomsDeclaration.xml`, `11-RemittanceAdvice.xml`) they have one untagged rendering, while the address of the same party keeps both renderings and tags the same English text `en-XB` instead of `en-XU`. A tag of the issuer's locale on another party's master data, and dropping some renderings but not others, makes the same party look different depending on who writes.
- Condition: Rinova's legal form, permit type and address carry the same renderings and language tags in every document of the flow, or the difference follows one stated rule (e.g. the issuer's languages) applied to all its texts.
- Options: (a) describe Rinova identically everywhere, as in the documents it issues itself (preferred: party master data does not change with the reader); (b) apply the issuer's-language rule consistently to the address too.
- Needs decision: no

## Checked and consistent
- Accounting customer Rivermouth (payer) and accounting supplier Rinova (payee) match `10-Invoice.xml`; payer account `XB96BLUM38020504712805` (Rivermouth, Bank of Lumeport) and payee account `XU700351041620000000418916` (Rinova) are the parties' own accounts and pass the check digit.
- Every party that appears in several documents of the flow was compared field by field (script over all `*.xml` of the flow): Rinova Recovery (`XU-R-104548`), Rivermouth Packaging (`20412740`), Fiumella Barges (`XU-R-104959`) and the Ferrano Chamber of Commerce (`XU-R-105370`) carry the same identifiers, names, tax registrations, legal entities, addresses, contacts and electronic addresses everywhere, apart from the language renderings noted in the findings.
- `check_ids.py`: every IBAN-like account and RF reference in the example passes its check digits (where present).
- Industry classifications fit the parties: Rinova `3830` (materials recovery), Rivermouth `2220` (manufacture of plastics products), Fiumella `5022` (inland freight water transport), customs `8411`.

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: an ISO 6523 identifier with ICD `0990` could clash with a real ICD — refuted because the ICDs assigned in the real ISO 6523 register are four-digit codes far below 0990 (own knowledge: the register runs to the 02xx range), so `0990` is free and stands for the world's identification agency.
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped bank identifier (`BLUMXBLX`) could be a real BIC — refuted because positions 5–6 carry the user-assigned ISO 3166 code of a fictional country (`XB`/`XU`), which no real BIC uses.
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID`: Rivermouth's account copied from master data, as in the other documents — refuted because here Rivermouth is the payer and the same account is the `PayerFinancialAccount` (`/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), so the remittance advice has a reason to carry it (it is redundant, not unused).
