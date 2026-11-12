# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/11-Invoice.xml`, Git blob `d14230a475262f9f8b47c7b7e1cbf9ab963fc61a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 83ce5da 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### wood/11#F1 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply. The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples already use locale-like tags (`en-XB`, `en-XU`) in `languageID`. The same element and value occur 362 times in 213 examples (merge recount, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47) and name that list in `listID`.
- Needs decision: no
- From: broad/F1, parties/F1, context/F1

### wood/11#F2 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in its role here. The accounting supplier's contact answers questions about the invoice (accounts receivable); the accounting customer's contact receives and pays it (accounts payable), not Brackenmere's trade sales desk, which sells furniture. `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml'`).
- Condition: Each accounting party's contact has a name, job title and department that fit its role in this invoice (receivables, payables) and agree with each other.
- Options: (a, preferred) role-specific contacts per party in the world, picked per document; (b) drop job title and department (or the contact) where only a functional mailbox is known.
- Needs decision: no
- From: broad/F3, parties/F2, context/F2

### wood/11#F3 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd and Brackenmere Furniture Ltd both carry 1996-01-01; the date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`) for about 25 companies of every kind in the registers of all three countries (parties part), while other dates are specific (Valdara: 1962-04-12). Counter-argument (context part of `10-Order.xml`): it may be the date the Bayvarran register began; nothing in the examples says so.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) its own date from the company's history; (b) record a 1996 (re-)registration in the story; (c) leave the date out.
- Needs decision: yes
- From: broad/F4, parties/F3

### wood/11#F4 · Low · Invoice for an ex-works sale with no delivery (collection) data
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-09`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `BF-PO-26-0637`
- XPath: `10-Order.xml:/Order/cbc:IssueDate` = `2026-03-08`
- XPath: `10-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `EXW`
- Why: The invoice bills 12 m³ of timber sold ex works, issued the morning after the order. It has no `Delivery` (no actual delivery date, no place), no `InvoicePeriod` and no despatch reference, and the flow has no despatch advice or other document recording that the buyer collected the goods. Nothing in the flow therefore says that or when the goods were delivered, so the reader cannot tell whether the invoice bills goods already collected or in advance, which also decides the tax point for the sales tax (own knowledge of the broad part).
- Condition: The invoice (or another document of the flow) states the delivery under EXW: the date the goods were made available or collected at the sawmill's yard.
- Options: (a, preferred) add `Delivery` with `ActualDeliveryDate` and the delivery location `Marrowdale Sawmill, timber yard`; (b) add a despatch advice to the flow and reference it, which changes the flow and needs a decision.
- Needs decision: no
- From: broad/F2, logistics/F1

### wood/11#F5 · Low · Resale/manufacture exemption without the buyer's exemption certificate
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `10-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- Why: The seller charges no state sales tax on a domestic sale within Upland State because the buyer, a furniture maker, uses the timber for manufacture. In state sales-tax practice (own knowledge of the money part, e.g. US resale and manufacturing exemptions) such an exemption is not the seller's to decide: it rests on an exemption or resale certificate of the buyer, which the seller keeps and usually quotes on the invoice. Neither the invoice nor the order names one, so nothing in the documents supports the exemption. Whether Bayvarra's state sales tax works this way is a question of the world.
- Condition: The exemption can be traced to the buyer's exemption certificate or registration (a referenced certificate or an identifier in the buyer's tax scheme data), or the story says why Bayvarra's state sales tax needs none.
- Options: (a, preferred) reference the buyer's resale/manufacture certificate (`AdditionalDocumentReference` with its number) in the invoice and the order; (b) record in the story that the exemption is granted without a certificate.
- Needs decision: yes
- From: money/F1

### wood/11#F6 · Low · Customs classification and origin in a domestic sale
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- Why: UBL defines `CommodityCode` as "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". This sale is between two companies in the same state of Bayvarra, collected ex works; no border is crossed, so the condition of the definition is not met, and the country of origin has no use either (no fillers).
- Condition: The domestic invoice carries only the classification its purpose uses (the CPC classification may stay), or the example states a domestic regulatory use of the HS code.
- Options: (a, preferred) drop the HS code and the origin country from the domestic documents; (b) keep them if a Bayvarran rule requires them, and say so in the world story.
- Needs decision: no
- From: context/F3

## Checked and consistent
- Arithmetic (recalculated): 12 MTQ × 540 XBL / 1 MTQ = 6 480.00 = LineExtensionAmount = TaxExclusiveAmount = TaxableAmount; tax 0.00; TaxInclusiveAmount = PayableAmount = 6 480.00 (broad, money).
- Price, quantity, item (`MS-TB`, HS `440799`), tax treatment and accounting cost (1100 "Timber and materials") agree with `10-Order.xml` (`BF-PO-26-0637`), which the order reference resolves to (broad, money, logistics, context).
- Tax category E / RESALE under STT fits seller and buyer both in Upland State and a furniture maker buying timber (broad, money).
- Terms: DueDate 2026-04-08 = 2026-03-09 + 30 days; 1.5 % × 6 480.00 = 97.20 PenaltyAmount; penalty period from 2026-04-09 (broad, money, context; recalculated).
- Payment means: RF02MSINV260638 (ISO 11649) and XB78BLUM38712004398618 pass `check_ids.py` (re-run by the merge); the payee account is the one of `08-Invoice.xml`, held in the supplier's registered name; MPNS on the domestic rail LUMEPAY fits a domestic payment, against RTNS on the Trade Accord rail in 08 (broad, money, parties, context).
- Dates: issued 2026-03-09 09:54, after the order of 2026-03-08 16:20 (logistics).
- Price plausibility: 540 XBL/m³ for kiln-dried sawn hardwood against about 1 108 XBL/m³ for the planed slats of `02-Quotation.xml` (money).

## Considered and refuted
- `/Invoice/cac:PaymentMeans` without ChargeBearerCode, unlike `08-Invoice.xml` — refuted because a domestic transfer has no shared foreign charges to allocate (from broad).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9523710900008` as a real GLN — refuted because GS1 prefix 952 is for demonstrations and the check digit is correct (from parties).

## Changed in the merge
- broad/F2 and logistics/F1 → F4: combined; the tax-point remark (broad) and the EXW context (logistics) kept.
- context/F1, parties/F1, broad/F1 → F1: preferred option is dropping `LocaleCode`.
