# LLM review: 10-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/10-Invoice.xml`, Git blob `1e3f9e5ae5dac5d74b0e7b9130b9a13721e9ec83` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/10#F1 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the same invoice use CountrySubentity. The parts counted 219 occurrences in 104 example files.
- Condition: no Urvanian address carries the province in `cbc:Region`; it is in `cbc:CountrySubentity`.
- Options: (a) move it to CountrySubentity (preferred); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### plastics/10#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. The parts counted 362 LocaleCode elements in 213 example files, all `en`.
- Condition: every LocaleCode holds a locale from a list its listID names, or is absent.
- Options: (a) drop it where the locale has no use (preferred, as parties and the wood merges); (b) `en-XB` with a locale list (broad, context).
- Needs decision: no
- From: broad (F2), parties (F2), context (F2)

### plastics/10#F3 · Low · Customer's bank account in a credit-transfer invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". The invoice asks for a credit transfer (`/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`) to Rinova's account; the customer's own account would matter only for a direct debit (mandate, payer account). It is the account Rivermouth later pays from (`11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), but this invoice does nothing with it: copied master data (section 4.8). Money counted it in the Rivermouth party of 14 XML examples. (Context noted that the account being held in XBL gives the stated payment currency XUF a reason; that reason does not need the account in the invoice.)
- Condition: the customer party in the invoice carries no financial account unless the invoice uses it.
- Options: drop it (preferred).
- Needs decision: no
- From: broad (F3), money (F1), parties (F4), context (F3)

### plastics/10#F4 · Low · Rinova's waste-recovery permit in the goods invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The invoice bills a product (HS 390110); Rinova's permit to recover plastic waste (Basel Annex IV R3) is not needed for it, and the recycled-content claim already has its certificate on the item. Master data copied into every document of the flow (IND5).
- Condition: no permit in the invoice unless the invoice uses it.
- Options: (a) remove it (preferred); (b) link it to the item's environmental certificate if the claim is to rest on it.
- Needs decision: no (parties said yes; aligned with broad, context and 06)
- From: broad (F5), parties (F5), context (F4)

### plastics/10#F5 · Low · Contacts are sales functions, not accounts
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers questions on the invoice (accounts receivable), the accounting customer's contact receives and pays it (accounts payable); "Customer service" and an "Order desk" in Sales are contacts for orders.
- Condition: the accounting parties' contacts handle billing and payables, or are absent.
- Options: (a) role-specific contacts (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad (F4), parties (F3), context (F5)

### plastics/10#F6 · Low · Both companies registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Two companies in two registers on New Year's Day 1996; the parts counted 271 occurrences in 181 example files. A default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (parties said no; aligned with broad, context and the wood merges)
- From: broad (F6), parties (F6), context (F6)

### plastics/10#F7 · Low · Recycled-content certificate issued by a chamber of commerce
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: EnvironmentalCertificate/IssuerParty is "The authorised Organisation who issues this Certificate". The chamber issues certificates of origin and carnets in the world (`road/06-CertificateOfOrigin.xml`, `carnet/01-GoodsItemPassport.xml`, per parties); recycled content is normally certified by an accredited certification body or the environment authority (own knowledge, EN 15343 / ISO 14021). Same as plastics/08#F8.
- Condition: the issuer is an organisation the world authorises to certify recycled content, or the world records why the chamber does.
- Options: (a) a certification body or the environment authority (preferred); (b) record the chamber's role in the story.
- Needs decision: yes
- From: parties (F8), context (F7)

### plastics/10#F8 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8, recalculated in the merge); as GTIN-13 `0771030000048` its prefix 077 lies in a range GS1 US issues to real companies (own knowledge). It could be taken for a real GTIN; the real register was not checked. Same as plastics/08#F9.
- Condition: the number cannot be mistaken for a real GTIN, or its absence from the register is verified and recorded.
- Options: (a) a non-GTIN format (preferred); (b) record the verification.
- Needs decision: yes
- From: broad (F7)

### plastics/10#F9 · Low · Italian text tagged as English
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: Renderings tagged `en-XU` are Italian street names, and the English legal form is Italian with a gloss; a world convention of Italianate exonyms is not visible, and a legal form is not a proper name. Parties counted the pattern in 101 of 250 examples.
- Condition: every rendering tagged `en-…` is English or a proper name used as such, and the convention is recorded.
- Options: (a) record the convention and render the legal form in English (preferred, aligned with the wood flow); (b) translate; (c) drop the second rendering.
- Needs decision: yes
- From: parties (F7)

## Checked and consistent
- Arithmetic (recalculated in the merge): 120 t × 83 200 XUF (base 1 t) = 9 984 000 = line extension = tax-exclusive = tax-inclusive = payable; tax 0; 2 % × 9 984 000 = 199 680; settlement period 2026-04-20 to 2026-04-30 (10 days); due 2026-05-20 = issue + 30 days in all three due-date elements (broad, money, context).
- Tax: category `G`, 0 %, exemption `EXP`, supply type `GOODS`, evidenced by the export declaration 05 (exporter = seller) and the exportation event on 2026-04-20 in 06; tax point 2026-04-20 = exportation day (broad, money, context).
- References: order `RP-PO-26-0882` line 1 (01) and despatch advice `RR-DA-26-0892` (08, issued the day before) exist; quantity, price and item agree; the invoice is referenced by 11 (broad, logistics, context; flow index re-run in the merge).
- CPT note agrees with the order's delivery terms (`01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`) and the unloading place in 04/06; the freight is billed to Rinova in 07 (broad, money, logistics, context).
- What follows: 11 pays 9 984 000 on 2026-05-19, after the discount period and before the due date, with the same RF reference `RF89RRINV260894` and payee account; neither discount nor penalty applies (broad, money).
- RF reference and accounts pass `check_ids.py`; payee account in Rinova's name; parties identical across the flow apart from language renderings (broad, money, parties).

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:ID`: `XU-STD` also used by another supplier in 07 — refuted for this invoice: they are Rinova's own standard terms; the conflict with the agreed transport terms is plastics/07#F1 (from broad).
- `/Invoice/cac:PaymentMeans/cbc:PaymentRailID`: a Trade Accord rail for a cross-border payment in XUF — refuted: fits a payment from Bayvarra to Urvania (from broad).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:CurrencyCode` = `XBL` against payment currency XUF — refuted: paying a foreign-currency amount from a home-currency account is ordinary (from money).
- Charge bearer `SHAR` while the remittance reports the full amount — refuted: with shared charges the payer sends the full amount and bears its own bank's fees (from money).
- `/Invoice/cbc:IssueDate` = `2026-04-20` before the planned discharge — refuted: under CPT the seller has delivered when the goods are handed to the carrier (2026-04-19) (from logistics).
- `/Invoice/cac:DespatchDocumentReference/cbc:ID` = `RR-DA-26-0892` instead of the waybill — refuted: the despatch advice is the document this element is meant for (from logistics).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` could be real — refuted: real ICDs stay far below 0990 (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `BLUMXBLX` — refuted: fictional country code in positions 5–6 (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: the buyer's customs-trader ID as copied data — refuted: plausible commercial data in a cross-border trade (from parties).
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF` equal to the document currency — refuted: the buyer's account is held in XBL, so stating the payment currency has a reason (from context).

## Changed in the merge
- broad/F5, parties/F5, context/F4 → F4: Needs decision changed from yes (parties) to no.
- broad/F6, parties/F6, context/F6 → F6: Needs decision yes (parties said no).
- broad/F2, parties/F2, context/F2 → F2: preferred option set to dropping LocaleCode.
- parties/F7 → F9: preferred option aligned with the wood flow.
- broad/F7 → F8: check digit recalculated and the GS1 prefix range added.
- Combined without change of severity: broad/F1, parties/F1, context/F1 → F1; broad/F3, money/F1, parties/F4, context/F3 → F3; broad/F4, parties/F3, context/F5 → F5; parties/F8, context/F7 → F7.
