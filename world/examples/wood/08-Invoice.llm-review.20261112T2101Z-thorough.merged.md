# LLM review: 08-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/08-Invoice.xml`, Git blob `cc18be7786d6372f4c7794e335c9b6d55250ba96` (committed)
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

### wood/08#F1 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply. The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples already use locale-like tags (`en-XB`, `en-XU`) in `languageID`; the Urvanian parties carry no `LocaleCode`. The same element and value occur 362 times in 213 examples (merge recount, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47) and name that list in `listID`.
- Needs decision: no
- From: broad/F2, parties/F2, context/F2

### wood/08#F2 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The same element and value occur 219 times in 104 examples (merge recount, `grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>'`).
- Condition: No Urvanian address carries an administrative division in `cbc:Region`; the province, where given, is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if the world has a list for it).
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, at the source of the Urvanian address format; (b) if the Urvanian "provinces" are economic regions in the world, rename them without "Province", record that in the story, and give any administrative division in `CountrySubentity`.
- Needs decision: no (the name itself says "province"; option (b) only would change the world)
- From: broad/F1, parties/F1, context/F1

### wood/08#F3 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in its role here. The accounting supplier's contact answers questions about the invoice (accounts receivable); the accounting customer's contact receives and pays it (accounts payable), not an "Order desk" in Sales. A customer-service officer in Sales answers a seller's customers. The parties carry the same contact in every example of the flow whatever their role; `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml'`).
- Condition: Each accounting party's contact has a name, job title and department that fit its role in this invoice (receivables, payables) and agree with each other.
- Options: (a, preferred) role-specific contacts per party in the world, picked per document; (b) drop job title and department (or the contact) where only a functional mailbox is known.
- Needs decision: no
- From: broad/F5, parties/F3, context/F3

### wood/08#F4 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd carries 1996-01-01; the date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`) for about 25 companies of every kind in the registers of all three countries (parties part), while other dates are specific (Valdara: 1962-04-12). Counter-argument (context part of `10-Order.xml`): it may be the date a register began; nothing in the examples says so.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) its own date from the company's history; (b) record a 1996 (re-)registration in the story; (c) leave the date out.
- Needs decision: yes
- From: broad/F11, parties/F6

### wood/08#F5 · Low · Valdara's master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Every optional element needs a reason in this document (section 4.8). Valdara's share capital, stock-exchange listing and logistics service provider Castrano Logistics are carried in full; nothing in the invoice uses them, and Castrano has no role (it appears in 9 of the 11 wood examples, never in a role of its own: `grep -l Castrano world/examples/wood/*.xml | wc -l`).
- Condition: Valdara's description in this invoice carries a service provider, share capital and security listing only if the invoice does something with them.
- Options: (a, preferred) leave them out of this document; fixing the party rendering per document type covers the flow; (b) give Castrano a role the document uses, which changes the story.
- Needs decision: no
- From: broad/F6, parties/F4, context/F4 (party part)

### wood/08#F6 · Low · Valdara's legal form in one untagged rendering, unlike its address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- Why: Valdara gives its address in two tagged renderings (Urvanian `qau` and English) but its legal form only once and without `languageID`. In the Urvanian-issued examples it gives both renderings of the legal form, each tagged (`01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). The same party is thus described differently between examples, and within this one address and legal form follow different language rules.
- Condition: Within this example the legal form follows the same language rule as the address: both renderings, each tagged, or one rendering with its `languageID`.
- Options: (a, preferred) render it like the address, as the Urvanian-issued examples do; (b) tag the single rendering and keep the Urvanian address rendering for delivery.
- Needs decision: no
- From: parties/F5

### wood/08#F7 · Low · The same Urvanian address is tagged `en-XB` here and `en-XU` elsewhere
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `09-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same English rendering of Valdara's address is tagged `en-XB` in this Bayvarran-issued invoice and `en-XU` in the Urvanian-issued examples (01, 03, 07, 09). Broad part: `languageID` names the language of the text, which does not change with the sender. Parties part (refuted): the tag names the variant of the issuer's English, and the text is the same. Both readings are defensible; the merge cannot settle which rule the world wants. 55 Italianate Urvanian street names are tagged `en-XB` over the examples (merge recount).
- Condition: The same rendering of the same address follows one documented tagging rule in every example of the flow.
- Options: (a, preferred) tag the rendering by the variant of the text itself (en-XU) everywhere; (b) keep the issuer's variant and record that rule.
- Needs decision: yes
- From: broad/F9; parties considered and refuted it (CityName), carried here with its argument

### wood/08#F8 · Low · English-tagged renderings of Urvanian names are Italian
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The English-tagged street name is Italian, and the legal form is Italian with an English gloss. The world's languages are English, Urvanian and Lisavan. 219 English-tagged street names in 104 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (merge recount, `grep -rhoE --include='*.xml' '<cbc:StreetName languageID="en[^"]*">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) '`; the broad part counted 217 in 102). Parties part (refuted): proper names are commonly kept untranslated and the world uses Italianate names consistently. The merge accepts that for street names but not for the legal form, a descriptive term; it cannot settle whether Italian is an intended exonym layer.
- Condition: Every text tagged with an English `languageID` is English, or the world states that these Italian forms are the official English-language names and legal forms in Urvania.
- Options: (a, preferred if intended) record the convention in the world's story; (b) English renderings.
- Needs decision: yes
- From: broad/F10; parties considered and refuted it, carried here with its argument

### wood/08#F9 · Low · Export zero-rating without delivery data, despatch reference or export evidence
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `/Invoice/cbc:IssueTime` = `08:56:00`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `08:31:00`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:ID` = `MS-EX-26-0630`
- Why: The invoice refers only to the order. It has no `Delivery` (no place or country of delivery, no actual delivery date), no delivery terms (DAP Ferrano, in the order), no `DespatchDocumentReference` to the despatch advice MS-DA-26-0633 issued 25 minutes earlier, and no reference to the export declaration MS-EX-26-0630. The sales-tax exemption for export rests on the goods leaving Bayvarra, which an invoice usually shows by the place of delivery or a reference to the export evidence (own knowledge of the parts); the buyer's Urvanian address alone does not establish where the goods go. A reader also cannot tell which despatch the invoice bills or when the goods were delivered.
- Condition: The invoice identifies the despatch it bills and states the delivery (date and place, country XU) or references the export evidence, so the exemption can be checked from the invoice and its references.
- Options: (a, preferred) add `Delivery` with the delivery location in Ferrano and the (actual or expected) delivery date, a `DespatchDocumentReference` to MS-DA-26-0633, and an `AdditionalDocumentReference` to MS-EX-26-0630; (b) at least the delivery date and the despatch reference.
- Needs decision: no
- From: broad/F4, money/F1, logistics/F1

### wood/08#F10 · Low · The charged pallets appear in no document that describes the goods
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`
- XPath: `/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`
- Why: The invoice charges 240.00 XBL for heat-treated export pallets, but none of the documents that describe the shipment (`04-TransportExecutionPlanRequest.xml`, `05-ExportCustomsDeclaration.xml`, `06-DespatchAdvice.xml`, `07-ImportCustomsDeclaration.xml`) has a pallet, package or transport handling unit (money part searched `wood/*.xml` for pallet, Package, HandlingUnit: only the charge in 02, 03 and 08). The object of the charge cannot be linked to the goods shipped, nor the amount to a number of pallets.
- Condition: The pallets the charge is for are visible in the despatch advice (or another shipment document of the flow), with a count that makes 240.00 XBL plausible.
- Options: (a, preferred) describe the pallets as transport handling units in the despatch advice and the transport request (see `06-DespatchAdvice.xml`, F12 of this merge); (b) drop the charge if the slats are not shipped on charged pallets.
- Needs decision: no
- From: money/F2

### wood/08#F11 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both under the seller's item identification and as `Item/Dimension[1]`; the identification carries no other dimension, so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the identification's `MeasurementDimension` is needed to distinguish variants and the example says so.
- Options: (a, preferred) keep it in `Item/Dimension` only; (b) keep it in the identification if the item number is length-specific and that is stated.
- Needs decision: no
- From: broad/F8

### wood/08#F12 · Low · The full commercial specification of the slats repeated in the invoice
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty[1]/cbc:TestMethod` = `Oven-dry method on samples from each kiln charge`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty[2]/cbc:Name` = `Thickness tolerance`
- Why: An invoice needs the parties' identities, tax and payment details and enough of the item to identify it; the full specification (tolerance, test method, standard property identification) was fixed by the order and does nothing for the invoice (no fillers).
- Condition: The invoice line carries the item data the invoice uses, or the example states why the specification is repeated.
- Options: (a, preferred) identify the item by name, seller's ID and classification and leave the specification to the order; (b) keep it if the world gives the invoice a quality-confirmation role.
- Needs decision: no
- From: context/F4 (item part)

### wood/08#F13 · Low · A 12-month validity period on the property "Planed on four sides"
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what would end the property after 12 months. The moisture content, which does change, has no period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear, or it is absent.
- Options: (a, preferred) drop it; (b) move it to a property that changes and say in the value qualifier what it means.
- Needs decision: no
- From: broad/F7, context/F5

### wood/08#F14 · Low · `OrderableUnitFactorRate` 50 while ordered and invoiced in single slats
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:OrderableUnitFactorRate` = `50`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `4800`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1`
- XPath: `03-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`
- Why: `OrderableUnitFactorRate` is "The factor by which the base price unit can be converted to the orderable unit". Broad part: the goods are ordered and invoiced in EA, so the orderable unit is the slat and the factor 50 contradicts it (the bundle of 50 is `Item/PackSizeNumeric`). The broad part's option "as in the order" is wrong: the order and the quotation carry the same factor 50 (merge check). Counter-argument (as weighed in the merge of `02-Quotation.xml` and `03-Order.xml`, this run): the bundle of 50 is the orderable unit, the price is per slat, and 4800 EA is a whole number of bundles (96), so the factor is consistent. The merge cannot settle which reading the example intends; in an invoice the factor in any case only repeats the ordering conditions.
- Condition: The orderable unit implied by the factor is the unit in which the goods are ordered (bundles or slats) and this is the same in quotation, order and invoice, or the factor is absent.
- Options: (a, preferred) if slats are ordered by the bundle, keep the factor and make the bundle the orderable unit explicit (e.g. order quantity in bundles); (b) drop the factor throughout if single slats are orderable.
- Needs decision: yes
- From: broad/F3

## Checked and consistent
- Arithmetic (recalculated): 4800 × 7.2 / 1 = 34 560.00 LineExtensionAmount; + 240.00 ChargeTotalAmount = 34 800.00 TaxExclusiveAmount; tax 0.00; TaxInclusiveAmount = PayableAmount = 34 800.00; TaxableAmount 34 800.00 = line (category G) + charge (category G) (broad, money).
- Tax: G / 0 % / EXP under the state sales tax fits a sale from Upland State to Urvania; tax currency = document currency (money).
- Price, quantity, charge, currency and accounting cost code `3100` agree with `03-Order.xml` and the quotation (broad, money, context, logistics).
- Terms: DueDate 2026-03-28 = 2026-02-26 + 30 days; PenaltySurchargePercent 1.5 × 34 800.00 = 522.00 for a one-month penalty period starting 2026-03-29; PaymentTerms/PaymentMeansID 1 resolves (broad, money; recalculated).
- Payment means: RF83MSINV260635 (ISO 11649) and XB78BLUM38712004398618 pass `check_ids.py` (re-run by the merge); bank code BLUM and branch 387120 agree with the branch ID and BLUMXBLX; account name = the seller's registration name; SHAR and RTNS on TRADE-ACCORD-PAY fit a cross-border transfer, against MPNS/LUMEPAY in the domestic `11-Invoice.xml` (broad, money, parties).
- Paid in full by `09-RemittanceAdvice.xml` (34 800.00 XBL on 2026-03-26, before the due date, balance 0.00), which references this invoice by ID and issue date (broad, money, logistics).
- Item data (seller's ID `MS-SL-1800`, HS `440799`, origin `XB`, certificate `XB-FOR-2025-0118`) agree with the despatch advice and the customs declarations (logistics).

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode` = `3100` — refuted because it is the buyer's code from the order, as the definition ("The buyer's accounting code") expects (from broad, context).
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR` — refuted because shared charges fit a cross-border transfer, and each party bearing its own bank's charges does not change the amount the remittance reports as paid (from broad, money).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` — refuted because a note for the payee's own statement naming the invoice is what the definition describes (from broad).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian under an English tag — refuted as a world convention (from parties). The merge keeps it as F8 with both arguments.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`: `en-XB` here, `en-XU` elsewhere — refuted because the tag follows the issuer's English (from parties). The merge keeps it as F7 with both arguments.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ICD — refuted because `0990` is not in `world/codelists/sources/peppol/ICD.xml` (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: a real MIC — refuted because it is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv` (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted by `check_ids.py` (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: "number of shares" against an amount — refuted because the element is of type Amount; whether it belongs here is F5 (from parties).
- The forestry certificate on the invoiced item as copied data — refuted because buyers subject to timber due-diligence rules keep the proof of origin with the invoice (from context).

## Changed in the merge
- broad/F4, money/F1 and logistics/F1 → F9: combined (same missing link to delivery, despatch and export evidence); all XPaths kept.
- context/F4 → F5 and F12: split into party master data and the item's commercial specification.
- context/F1 "Needs decision: yes" → F2 "no", as in the other examples of this merge.
- context/F2, parties/F2, broad/F2 → F1: preferred option is dropping `LocaleCode`.
- broad/F3 → F14: "Needs decision: yes" added and the counter-argument (bundle as orderable unit) stated; the broad option "drop the factor, as in the order" corrected, because `03-Order.xml` carries the same factor; aligned with the other merger's grading for 02 and 03.
- broad/F10: count corrected to 219 in 104 files (merge recount); joined with the parties' refuted candidate as F8.
- broad/F9 joined with the parties' refuted CityName candidate as F7, "Needs decision: yes".

## Outside this review
- `06-DespatchAdvice.xml` and `04-TransportExecutionPlanRequest.xml` describe no packaging or handling units; whether they should, for the shipment's own sake, belongs to their reviews (from money; it is F12 of the merged review of 06).
