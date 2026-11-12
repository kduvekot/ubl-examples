# LLM review: 03-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/03-Order.xml`, Git blob `f14d6ba97f84855490d38ffc0a4d1386846aa813` (committed)
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

### wood/03#F1 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `Address/CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province belongs in `CountrySubentity`, as the Bayvarran address of the same example has it (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`; files with `grep -rl`).
- Condition: No Urvanian address in this example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` where the world has a list), and `cbc:Region`, if present, holds a region in the UBL sense.
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, as for Bayvarra; (b) if Ferrano is an economic region in the world, rename it without "Province" and record that in the story.
- Needs decision: no
- From: broad, context, parties

### wood/03#F2 · Medium · Language code `en` in `Language/LocaleCode`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with `listID="ISO 639"` is a language code only and repeats `Language/ID`; a locale is a language as used in a country (cf. the examples' `languageID` values `en-XU`, `en-XB`). The Urvanian buyer carries no `LocaleCode`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; files with `grep -rl`).
- Condition: Every `cbc:LocaleCode` in this example holds a locale with a `listID` naming a list of locales, or is absent.
- Options: (a, preferred) leave `LocaleCode` out where no locale matters, as here; (b) a real locale such as `en-XB` from a list of locales (e.g. BCP 47), named in `listID`.
- Needs decision: no
- From: broad, context, parties

### wood/03#F3 · Medium · The pallet charge has no tax category and is outside the taxable amount
- XPath: `/Order/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `34560.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `34800.00`
- Why: `TaxSubtotal/TaxableAmount` is "The net amount to which the tax percent (rate) is applied". The order adds a document-level charge of 240.00 XBL but gives it no `TaxCategory`, and the only subtotal covers the line amount alone, so the tax treatment of 240.00 of the anticipated 34 800.00 is undefined. The invoice of the same deal treats the charge as part of the exempt export supply: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `G` and `08-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `34800.00`. Counter-argument (broad part): the tax is 0.00 either way, so nothing is miscalculated. That is true of the amount, but the order's breakdown still leaves part of the anticipated total without a tax treatment and differs from the invoice's.
- Condition: Every amount in the anticipated total belongs to a tax subtotal (the charge has a `TaxCategory`), and the taxable amounts add up to line extension plus charges (34 800.00), as in the invoice.
- Options: (a, preferred) give the charge the category G/EXP under STT and set `TaxableAmount` to 34 800.00, matching the invoice; (b) drop `TaxTotal` from the order if the buyer anticipates no tax.
- Needs decision: no
- From: money (broad refuted it; see "Considered and refuted")

### wood/03#F4 · Low · Text tagged as English is Italian
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Both renderings are tagged `en-XU` but are Italian; the world's languages are English, Urvanian and Lisavan. 219 English-tagged street names in 104 examples start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml' 'StreetName languageID="en-X[A-Z]">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): street names are proper names, commonly left untranslated, and the world uses Italianate names consistently. That does not cover the legal form, a descriptive term. The merge could not settle whether the Italian forms are the world's English exonyms.
- Condition: Every text tagged with an English `languageID` is English, or the world's story states that these Italian forms are the English-language names used for Urvania.
- Options: (a, preferred if intended) record the convention in the story and give the legal form in English; (b) English renderings throughout.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/03#F5 · Low · Valdara's master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: An order needs the buyer's identity, contact and delivery details. Valdara's share capital, stock-exchange listing and logistics service provider are master data the order does nothing with (section 4.8): no security is traded, and Castrano has no role (the delivery party is Valdara itself, `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`). Castrano appears in 9 of the 11 wood examples (`grep -l Castrano world/examples/wood/*.xml | wc -l`), never in a role of its own.
- Condition: Valdara's description here carries share capital, listing and service provider only if the order uses them.
- Options: (a, preferred) leave them out of this document; (b) give Castrano a role the order uses (e.g. as the receiving warehouse), which changes the story.
- Needs decision: no
- From: broad, context, parties

### wood/03#F6 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party", read in its role: the buyer placing the order should be reached in purchasing, not at a customer-service desk of its own Sales department. Valdara carries this contact in every role of the flow; `Customer service officer` occurs 395 times in 229 examples (`grep -rho --include='*.xml' 'Customer service officer' world/examples | wc -l`; files with `grep -rl`).
- Condition: The buyer's contact belongs to purchasing, with name, job title and department agreeing.
- Options: (a, preferred) role-specific contacts per party in the world, chosen by the role in each document; (b) drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no
- From: broad, context, parties

### wood/03#F7 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". The date occurs 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`; files with `grep -rl`), for about 25 companies of every kind in all three countries' registers (parties part), while other dates are specific (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`). It reads as a filler unless the world has an event that explains it.
- Condition: Each company's registration date is its own date in the world, or the world documents why these companies share 1996-01-01; otherwise it is absent.
- Options: (a, preferred) each company its own date; (b) record a 1996 re-registration in the story if intended; (c) leave the date out.
- Needs decision: yes
- From: broad, parties

### wood/03#F8 · Low · The order states no delivery period
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- Why: The order is the buyer's binding instruction, but its `Delivery` names only the receiving party, with no `RequestedDeliveryPeriod`. The request asked for 2026-03-02 to 2026-03-16 and the quotation promised it; the order refers to the quotation, so the period can be inferred, but it is ordered nowhere, and the transport arranged afterwards plans a different one (see the merged review of `04-TransportExecutionPlanRequest.xml`, F1).
- Condition: The order's `Delivery` states the delivery period the buyer orders, or the order makes explicit that the quotation's promised period applies.
- Options: (a, preferred) add `Delivery/RequestedDeliveryPeriod` 2026-03-02 to 2026-03-16 as agreed; (b) refer explicitly to the quotation's promised period.
- Needs decision: no
- From: broad, context, logistics

### wood/03#F9 · Low · The DAP place is free text, described differently in each example
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Valdara Industries, goods-in, Ferrano`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`
- XPath: `04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: The order fixes the named place of the Incoterm, but gives it only as a description, without name, address or identifier; the request for quotation gives the same text as the location's name, and the transport request names the place after the company and gives a full address. The same place is described three ways, and the binding document has the weakest description.
- Condition: The DAP delivery location of the order is identified in the same way as in the other examples of the flow (name and address, or an identifier).
- Options: (a, preferred) give `DeliveryTerms/DeliveryLocation` a name and address matching the transport request's destination (whose name itself is F12 of the merged review of 04); (b) keep the text and add an address.
- Needs decision: no
- From: logistics

### wood/03#F10 · Low · `OrderableUnitFactorRate` 50 while the order is placed in single slats
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `4800`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50`
- Why: `Price/OrderableUnitFactorRate` is "The factor by which the base price unit can be converted to the orderable unit". The order is placed in EA (4800 slats), which suggests the orderable unit is the slat; the bundle of 50 is already in `PackSizeNumeric`. Counter-argument (money part): the item is sold in packs of 50, so a factor of 50 from the slat to the pack is correct, and 4800 slats are 96 packs. The merge could not settle which reading is meant.
- Condition: The orderable unit implied by the factor is evident: the quantity is in that unit, or the order states that slats are ordered in whole packs of 50.
- Options: (a, preferred) drop the factor; (b) order 96 packs with factor 50, or state the pack as the orderable unit.
- Needs decision: yes
- From: broad (money refuted it; see "Considered and refuted")

### wood/03#F11 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length is given as a measurable dimension of the seller's item identification and again as `Item/Dimension[1]`; the identification carries no other dimension, so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the dimension under the identification distinguishes item variants and the example says so.
- Options: (a, preferred) keep it in `Item/Dimension` only; (b) keep it in the identification if the item number is length-specific and that is stated.
- Needs decision: no
- From: broad

### wood/03#F12 · Low · A 12-month validity on the property "Planed on four sides"
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what ends the property after 12 months. The moisture content, which does change, carries no period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear, or it is absent.
- Options: (a, preferred) remove it from the surface property; (b) move it to a property that changes and say what it means.
- Needs decision: no
- From: broad, context

## Checked and consistent
- Reference: `/Order/cac:QuotationDocumentReference/cbc:ID` = `MS-DOC-26-0626` resolves to `02-Quotation.xml`; the order (`/Order/cbc:IssueDate` = `2026-02-22`) is within the quotation's validity (to 2026-03-21) (broad, context, logistics).
- Arithmetic, recalculated in the merge: 4800 × 7.20 = 34 560.00; + 240.00 charge = 34 800.00 `AnticipatedMonetaryTotal/PayableAmount`; `ChargeTotalAmount` 240.00 (broad, money, context).
- Price, charge, currency and DAP agree with the quotation; the order is for the main quoted item (38 mm), not the substitute or the alternative (money, context, logistics).
- Tax category G ("Free export item, tax not charged") with exemption reason EXP "Export outside Bayvarra" under STT fits a sale from Upland State to Ferrano (broad, money).
- The order is referenced as `VI-PO-26-0627` by `05-ExportCustomsDeclaration.xml`, `06-DespatchAdvice.xml` and `08-Invoice.xml`; all resolve (broad, logistics). DAP puts the carriage on the seller, who books and pays the haulage in `04-TransportExecutionPlanRequest.xml` (logistics).
- Item (seller's ID MS-SL-1800, 1800 × 95 × 38 mm, HS 440799) agrees with the quotation, the despatch advice and the customs declarations (logistics).
- Parties identical to their other full descriptions in the flow apart from language renderings; identifiers and tax schemes consistent; `check_ids.py` passes (parties).

## Considered and refuted
- `/Order/cbc:AccountingCostCode` = `3100`, equal to Valdara's ISIC code 3100 — refuted: `/Order/cbc:AccountingCost` = `Raw materials and parts` identifies it as a cost account of the buyer; the coincidence with the industry code is not a contradiction, and the invoice repeats it (from broad, money, context).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` does not choose between the ash and oak offered — refuted: the item is ordered as "hardwood", leaving the species to the seller as the quotation allowed (from broad).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `VI-R-SL1800`, a number not in the request — refuted: the buyer assigns its item number when it orders (from context).
- Item specification (moisture with test method and range, thickness tolerance, forestry certificate): copied — refuted: in an ordering document these are the requirements delivery is measured against (from context).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `NameCode` — refuted: the ID identifies the occurrence, `NameCode` classifies it (from context).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50` — refuted: together they state the pack structure (from context).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`: delivery party equal to the buyer, redundant — refuted: `DeliveryParty` is "the Party who receives the goods", stated explicitly and consistent with DAP and the delivery location (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: a default contact — refuted: a sales office is the right contact for the seller of an order (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427` (real ICD?), `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER` (real MIC?), `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501` (check digit) — refuted: not in the repository's ICD and MIC lists; `check_ids.py` passes (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: definition says "number of shares" — refuted: the element is an Amount; whether it belongs here is F5 (from parties).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `34560.00` excludes the 240.00 charge — refuted by the broad part (no tax category on the charge; tax 0.00 either way). Not followed: kept as F3 (money).
- `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50` — refuted by the money part (the pack of 50 is the orderable unit). Not followed: kept as F10, Needs decision: yes.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text tagged English — refuted by the parties part as a world convention. Not followed: kept as F4, Needs decision: yes.

## Changed in the merge
- broad/F1, context/F1, parties/F1 → F1: combined; context's "Needs decision: yes" set to no (encoding, not story), aligned with the merge of wood 06–11.
- broad/F2, context/F2, parties/F2 → F2: combined; preferred option set to "leave out" (context's), as in the other merged reviews.
- money/F1 → F3: kept Medium; broad's refutation added as counter-argument; `PayableAmount` added as evidence.
- broad/F9 → F4: count corrected (219 in 104 files instead of 217 in 102); parties' counter-argument added.
- broad/F6, context/F5, parties/F4 → F5; broad/F5, context/F4, parties/F3 → F6; broad/F10, parties/F5 → F7: combined, wording only.
- broad/F3, context/F3 and the period part of logistics/F1 → F8: combined.
- the place part of logistics/F1 → F9: split off as a finding of its own, because it is a different problem (the description of the DAP place) from the missing period.
- broad/F4 → F10: Needs decision changed from no to yes, with money's refutation as counter-argument (cannot settle).
- broad/F8 → F11; broad/F7, context/F6 → F12: wording only.
