# LLM review: 01-Order.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/01-Order.xml`, Git blob `1c959f7204add325b43b103744bcf375fb8ba1db` (committed)
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

### plastics/01#F1 · Medium · Province of the seller's address in Region
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located", while a province is "The political or administrative division of a country … such as the name of its county, province, or state", i.e. `CountrySubentity` (with `CountrySubentityCode`). The Bayvarran addresses of the same document use `CountrySubentity` for their state (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). The value also has no `languageID`, while the other parts of this Urvanian address are given in `qau` and `en-XB`. The same element and value occur 219 times in the world (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no Urvanian province is carried in `cbc:Region`; the province is in `cbc:CountrySubentity` (rendered in the languages of the other address parts) and, where a code list exists, `cbc:CountrySubentityCode`.
- Options: (a) move the province to `CountrySubentity` (+ code) for all Urvanian addresses (preferred: it is what the element means and matches the Bayvarran addresses); (b) keep `Region` only if Ferrano is in fact an economic region that is not an administrative division, and then say so in the world data.
- Needs decision: no

### plastics/01#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; a locale is language plus region (e.g. `en-XB`), not the bare ISO 639 language code, which is already in `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`. The `listID` `ISO 639` confirms that a language list is used for a locale. The buyer is in Bayvarra, and the documents of the flow tag Bayvarran English as `en-XB`. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples`).
- Condition: `LocaleCode` either carries a locale (language and country/region, e.g. `en-XB`, from a locale list named in `listID`) or is absent.
- Options: (a) use `en-XB` with a locale list (BCP 47 / CLDR) as `listID` (preferred: the flow already uses `en-XB` as `languageID`); (b) drop `LocaleCode`, since `ID` already says English.
- Needs decision: no

### plastics/01#F3 · Low · Buyer's contact is a sales/customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: In an Order the buyer's contact is the person or desk that buys (purchasing). Rivermouth Packaging buys raw material here (`/Order/cbc:AccountingCost` = `Raw materials`), but its contact is a customer-service officer in Sales, which is the seller-side function. The seller's contact is the same function (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`).
- Condition: the buyer's contact in the Order is a purchasing function (name, job title and department agreeing with each other).
- Options: (a) give Rivermouth a purchasing contact for documents in which it acts as buyer (preferred); (b) keep one contact per party but make it a neutral one (e.g. a general office) that fits all its roles.
- Needs decision: no

### plastics/01#F4 · Low · Buyer's bank account in an Order that pays nothing
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". The Order has no payment means or payment terms; nothing in it is paid from or to this account, so it reads as master data copied into a document that does not use it (section 4.8).
- Condition: the Order carries the buyer's account only if the Order says something about payment that uses it.
- Options: (a) remove the account from the Order (preferred); (b) keep it only together with payment information the Order actually agrees.
- Needs decision: no

### plastics/01#F5 · Low · Both parties registered on 1 January 1996
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". A Bayvarran and an Urvanian company, in different registers, share the same date, which is also the most frequent registration date in the world (271 occurrences, `grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*' world/examples | sort | uniq -c`). This looks like a default rather than each company's own registration date (IND5/IND6: no fillers). It may have a story reason (e.g. registers created on that date), which this review cannot see.
- Condition: each party's registration date is its own, or the shared date is explained by the world's history.
- Options: (a) give each company its own registration date (preferred); (b) if 1 January 1996 is a re-registration date of all companies (e.g. a new register), record that in the world's story and keep it.
- Needs decision: yes

### plastics/01#F6 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: The identifier is in the fictional scheme `urn:ubl-examples:world:item`, but it has 12 digits with a correct GS1 mod-10 check digit (computed: 8), and 12-digit numbers starting with 7 are GTIN-12 (UPC) numbers from the GS1 US range. A reader can take it for a real UPC (rule: fictional values must not be mistaken for real ones). Whether this exact number is assigned could not be checked here. The same kind of numbers occur 82 times (`grep -rhoE --include='*.xml' 'schemeID="urn:ubl-examples:world:item">[0-9]+' world/examples | wc -l`).
- Condition: the item number cannot be mistaken for a real GTIN, or the world's item scheme is documented as deliberately GTIN-shaped with numbers verified as unassigned.
- Options: (a) change the format of the world's item numbers so they are not valid GTINs (preferred); (b) keep them and record the verification against the GS1 register in the sources.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 120 t × 83 200 XUF/t = 9 984 000 XUF = line extension = anticipated total = payable; tax 0 % of 9 984 000 = 0.
- Tax: category `G` with exemption `EXP` (export of goods outside Urvania) fits an Urvanian seller delivering CPT to Bayvarra; seller's tax scheme is Urvanian VAT.
- HS 390110 (PE, specific gravity < 0.94, primary forms) fits the density property 0.92 g/cm³ and the description; CPC 34710 fits.
- Physics: 1 t of PE granulate at a bulk density of about 0.55–0.6 t/m³ (own knowledge) needs about 1.7–1.8 m³, within the usual volume of a 1 t jumbo bag (FIBC).
- The delivery place of CPT (`River quay, Lumeport`) matches the unloading place of the transport documents (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`).
- Buyer and seller identities (register numbers, tax IDs, names) are the same as in the other examples of the flow.

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode`: the seller's waste-recovery authorisation looked like master data copied into the Order — refuted because the buyer orders recycled granulate with a recycled-content claim (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`), and the permit of the recovery operation backs that claim.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: an Italian-looking street name tagged `en-XB` — refuted: the world's exonyms of Urvanian places in English are given as such; a fictional convention, not a clash with a real standard.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` — refuted as a real-register clash: to my knowledge the ICD list does not assign 0990 (own knowledge).
- The Order has no requested delivery date — refuted as a finding: an Order does not need one for its purpose, and the delivery place is given through the delivery terms.
