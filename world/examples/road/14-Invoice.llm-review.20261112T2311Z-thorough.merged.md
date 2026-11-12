# LLM review: 14-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/14-Invoice.xml`, Git blob `1173f55bda6f9ffdefd8413a5ce62500697f236a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
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

### road/14#F1 · High · Freight invoice refers to a receipt advice issued the day after the invoice
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-25`
- XPath: `/Invoice/cbc:IssueTime` = `11:07:00`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `LD-RA-26-0164`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueDate` = `2026-03-26`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `10:48:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00`
- Why: the freight invoice, issued on 2026-03-25 at 11:07, points to line 1 of receipt advice LD-RA-26-0164, which Lumeway issues only on 2026-03-26 at 10:48 (the corrected advice, after the cancellation `12-FulfilmentCancellation.xml` of 10:46). At 11:07 on 2026-03-25 no receipt advice existed at all: even the first one (`11-ReceiptAdvice.xml`, LD-RA-26-0162) is issued at 15:40 that day. Refutation tried in the merge: the number could have been known in advance only if Lumeway had pre-allocated it, but the reference is to a document of the buyer that the carrier cannot hold before it is sent, and the correction that gave rise to this ID was not yet known at 11:07. A reference to a document that does not exist at the issue time is a broken reference (High). Logistics adds that the referenced line is the buyer's receipt line, not something the carrier holds.
- Condition: every document the invoice references exists at the invoice's issue date and time.
- Options: (a, preferred: logistics) base the carrier's proof of delivery on its own documents, the waybill already referenced and the actual delivery event of 09:40, and remove the `GoodsItem`/`ReceiptLineReference` (keeps the story and also resolves F11); (b, broad) issue the freight invoice after 2026-03-26 10:48 if it must cite the corrected receipt advice.
- Needs decision: no
- From: broad (F1), logistics (F1); money listed it under "Outside this review"

### road/14#F2 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address in the same invoice uses `CountrySubentity` (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Recounted: 219 occurrences in 104 files (`grep -rho --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with `CountrySubentityCode` where a list exists).
- Options: (a, preferred) move it to `CountrySubentity`, as Bayvarra does; (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no
- From: broad (F2), parties (F1), context (F1)

### road/14#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (e.g. `en-XB`, used in the examples as `languageID`); `en` with `listID` `ISO 639` repeats `Language/ID` and names no locale (section 6: Medium). Recounted: 364 occurrences in 213 files (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<'`); the parts said 362.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales named in its listID.
- Options: (a, preferred: broad, parties) drop `LocaleCode`; (b, context's preference) `en-XB` with a locale list as listID.
- Needs decision: no (parties said yes; encoding only, as in all earlier flows)
- From: broad (F3), parties (F2), context (F2)

### road/14#F4 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance for vehicles, not a street name, and an invoice address has no use for it. Recounted: 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop the gate from the party address; (b) keep it only in delivery addresses, in a location description.
- Needs decision: no
- From: broad (F4), parties (F3)

### road/14#F5 · Low · The buyer's stock-purchase cost code on the carrier's invoice
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- XPath: `01-Order.xml:/Order/cbc:AccountingCostCode` = `4410`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Invoice as a whole". The carrier's invoice carries the same code and text as Lumeway's purchase order for the benches; the transport request, the only document Lumeway sent Trasvia, gives no cost code (verified: `AccountingCost` occurs in this flow only in 01, 14 and 15), so the code looks copied from the goods order. Broad and money refuted it: inbound freight is part of the cost of inventory (IAS 2), so booking it to stock purchases is a legitimate choice of the buyer. That answers whether the account fits, not how the carrier knows it; it could come from the framework contract (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-TH-FW-2026`), which no example shows. The merge cannot settle it.
- Condition: the freight invoice carries a buyer's accounting code only if the buyer gave it for the transport, visibly in the flow or by a stated arrangement.
- Options: (a, preferred: context) drop both elements; (b) add the cost code to the transport request (or the framework contract) and repeat it here.
- Needs decision: yes
- From: context (F3); refuted by broad and money (their "Considered and refuted")

### road/14#F6 · Low · Waybill referenced with only an ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TH-WB-26-0159`
- Why: an invoice's `AdditionalDocumentReference` can be any supporting document; this one carries only an ID, no `DocumentTypeCode`, type text or issue date, so nothing in the invoice says it is the CMR waybill (`08-Waybill.xml`), the carrier's proof of the transport invoiced. Context refuted it: the carrier refers to its own consignment note, and no other kind of document has this number. Partly survives: the recipient's system does not know Trasvia's numbering, and the remittance advice of the same flow types its reference; the checklist asks for a type where it is not obvious. Low, as in the earlier flows.
- Condition: the reference states the kind of document it refers to (type code or text).
- Options: (a, preferred) add `DocumentTypeCode` for the waybill from the world's document type list (as `17-RemittanceAdvice.xml` does for the invoice); (b) add `DocumentType` or `DocumentDescription`.
- Needs decision: no
- From: broad (F5), logistics (F3); refuted by context

### road/14#F7 · Low · Italian names and legal form tagged as English
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: the renderings carry `languageID` `en-XU` but are Italian text (the legal form with an English gloss). The parties part refuted it for the street name: English text keeps foreign street names unchanged. Against that: `languageID` names the language of the content, and the legal form is not a proper name. The merge cannot settle which convention the world wants; aligned with the utilities and rail merges (Low, decision). Counted: 217 street renderings beginning with an Italian street word tagged en-XU or en-XB, in 102 files.
- Condition: the world has one stated rule for the language tag of Urvanian names and legal forms rendered in English, and every rendering follows it.
- Options: (a, preferred) document that English renderings keep Urvanian proper names, tagged with the party's own variety; give the legal form an English rendering or tag the Italian part as such; (b) document the present practice as the convention.
- Needs decision: yes
- From: merge (from the parties' "Considered and refuted")

### road/14#F8 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Trasvia Haulage SRU carries 1 January 1996, a public holiday; recounted, `1996-01-01` occurs 271 times in 181 files for many companies, while Lumeway (1988-10-03) has its own date. It reads as a filler (IND5).
- Condition: Trasvia's `RegistrationDate` is its own plausible date, or the element is absent.
- Options: (a, preferred) give Trasvia its own date from its history; (b) leave the element out.
- Needs decision: yes (parties said no; aligned with the earlier flows and road merges a and b)
- From: parties (F4)

### road/14#F9 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Planning desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the supplier's contact answers billing questions (accounts receivable) and the customer's contact receives and checks invoices (accounts payable). Trasvia gives its planning desk in Operations, Lumeway its customer service desk in Sales; each party carries one fixed contact in every role of the flow.
- Condition: the accounting parties' contacts are their billing / accounts functions.
- Options: (a, preferred) accounts receivable and accounts payable contacts; (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F6), parties (F5), context (F5, contact part)

### road/14#F10 · Low · The carrier's operating permit in the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: section 4.8: Trasvia's `PartyAuthorization` ("An authorization issued to this party", its international haulage licence) qualifies it as a carrier in the transport documents; in the freight invoice, where Trasvia is the accounting supplier, it has no function.
- Condition: every optional party aggregate present has a reason in the invoice's purpose.
- Options: (a, preferred) leave the authorization out of the invoice; (b) state a reason if the world's billing rules require the licence on freight invoices.
- Needs decision: no
- From: parties (F6), context (F5, permit part)

### road/14#F11 · Low · Freight for the whole load linked to the bench receipt line only
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:GoodsItem/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Full truck load, price per kilometre driven loaded, tolls included.`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- Why: the invoice bills a full truck load per kilometre for consignment LD-CS-26-0152, which carried the benches and the side frames (`13-ReceiptAdvice.xml` lines 1 and 2). Its only goods item points to receipt line 1, the benches, so the reference suggests the freight is for the benches only.
- Condition: the delivery the invoice describes covers the whole consignment (or carries no goods item, since the consignment ID identifies it).
- Options: (a, preferred) remove the goods item together with F1's reference and keep the consignment; (b) refer to the receipt advice as a whole, or add a goods item for line 2.
- Needs decision: no
- From: broad (F7), logistics (F2), context (F4)

### road/14#F12 · Low · Rate 0 % on a category "outside the scope of tax"
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage". Category `O` (UN/EDIFACT 5305 "Services outside scope of tax") means no tax applies, so there is no rate; a rate of 0 % reads as a zero-rated supply, a different category (Z/G). No part raised it; added by the merge for consistency with the utilities merges, which made the same value a Low finding.
- Condition: a tax category `O` carries no `Percent`.
- Options: (a, preferred) drop `Percent` on both categories; (b) if the world treats the haulage as zero-rated, change the category instead (a tax judgment, which would need a decision).
- Needs decision: no
- From: merge

## Checked and consistent
- Arithmetic (redone): 186 KMT × 240.5 XUF per 1 KMT = 44 733 = line amount = `LineExtensionAmount` = `TaxExclusiveAmount` = `TaxInclusiveAmount` = `PayableAmount`; taxable amount 44 733, tax 0.
- Payment terms (redone): 2 % of 44 733 = 894.66, rounded to `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `895`; settlement period 2026-03-25 to 2026-04-04 = 10 days; due date 2026-03-25 + 30 = `/Invoice/cbc:DueDate` = `2026-04-24`, the same in `PaymentMeans` and `PaymentTerms`, matching "30 days net; 2 % discount when paid within 10 days."
- Payment means: `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF49THINV260165` (ISO 11649) and the payee account `XU320351041600000000628374` (IBAN-style, held in XUF, named after Trasvia's registered name) pass `check_ids.py`.
- Parties and terms: billed party = bill-to party of the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyIdentification/cbc:ID` = `20410274`); the waybill says the consignee pays the freight (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `The freight is paid by the consignee under its contract with the carrier.`), consistent with FCA.
- `/Invoice/cbc:TaxPointDate` = `2026-03-25` is the day of the actual delivery (`/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:ActualDeliveryTransportEvent/cbc:OccurrenceTime` = `09:40:00` on 2026-03-25), before the issue time.
- Physics: 61 l of diesel for 186 km loaded (`08-Waybill.xml`) = 32.8 l/100 km, plausible for a loaded articulated truck (own knowledge).

## Considered and refuted
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD` with category `O`: suspected that a transport starting in Urvania is taxable there — refuted because it is a business-to-business transport for a customer established and registered for tax in Bayvarra (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`); under the usual general B2B rule the place of supply is the customer's country, so the service is outside the scope of Urvanian VAT (own knowledge of VAT practice); zero-rating instead would be a choice of the world's tax rules (from broad, money). The rate on `O` is F12.
- `/Invoice/cbc:AccountingCost` = `Stock purchases` for freight: refuted by broad and money (landed cost, IAS 2); not followed in full, kept as F5 with both arguments.
- `/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`, the same as in `15-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD` from another seller: suspected copied terms — refuted because the world uses country standard terms (13 files carry `XU-STD`), and each seller links its own terms page (from money).
- No reference to the framework contract `LD-TH-FW-2026` on which the kilometre price rests: considered as missing — refuted because the invoice's purpose does not depend on it; the waybill identifies the transport (from money).
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TH-WB-26-0159` with ID only — refuted by context (the carrier's own note); not followed, kept as F6.
- `/Invoice/cbc:DefaultLanguageCode` = `en` from an Urvanian carrier — refuted because the invoice goes to an English-speaking Bayvarran customer and carries the Urvanian renderings with their own `languageID` (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian street name tagged as English — refuted by parties; not followed, made F7.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be real — refuted because prefix 952 is reserved by GS1 for examples and the check digit is correct (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because +999 is reserved in ITU-T E.164 (from parties).

## Changed in the merge
- broad/F1, logistics/F1 → F1: combined; preferred option set to logistics' (drop the receipt reference), broad's later issue kept as (b). Money's "Outside this review" entry absorbed: the contradiction is with a referenced example, hence a finding of this review.
- broad/F3, parties/F2, context/F2 → F3: parties' "Needs decision: yes" set to no; count corrected to 364.
- context/F3 → F5: kept against the refutation of broad and money; Needs decision no → yes because the merge cannot settle it.
- broad/F5, logistics/F3 → F6: kept against context's refutation, with the counter-argument.
- context/F5 split: contacts → F9 (with broad/F6, parties/F5), permit → F10 (with parties/F6), as in the utilities merges.
- parties/F4 → F8: needs decision no → yes, aligned with the earlier flows and road merges a and b.
- broad/F7, logistics/F2, context/F4 → F11: combined; preferred option tied to F1(a).
- F7 and F12 added by the merge.

## Outside this review
- Whether 186 km loaded fits the route from Ferrano to Marrowdale on the map, with a transit from 2026-03-23 to 2026-03-25, is a question for the cross-flow consistency review (from context).
- The freight invoice is not paid in the flow (no remittance for TH-INV-26-0165, due 2026-04-24); a question of the flow's scope (from the broad review of `17-RemittanceAdvice.xml`).
