# LLM review: 08-Order.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/08-Order.xml`, Git blob `71ce9b04ed217222f38cfab91ff0f8de0f9cd595` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/08#F1 · Medium · Language code in `LocaleCode`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (`ISO 639`) is a language code and repeats `Language/ID`. 362 occurrences in 213 files. Same as 02#F3.
- Condition: every `Language/LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F2), parties (F1)

### cotton/08#F2 · Medium · Tax category "Services outside scope of tax" for an order of goods
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name[2]` = `Cotton lint, compressed bale`
- Why: as 01#F2: 5305 `O` is "Services outside scope of tax"; the order is for cotton lint, goods. (No `SupplyTypeCode` here, so this file is not among the 5 with `O` + `GOODS`; 17 files use `O`.)
- Condition: the subtotal carries a code whose meaning covers goods outside the scope of tax, or the deviation is recorded.
- Options: (a, preferred) one world-wide decision; (b) keep `O` as a recorded deviation.
- Needs decision: yes
- From: broad (F1)

### cotton/08#F3 · Low · Requested invoice currency equal to the document currency
- XPath: `/Order/cbc:RequestedInvoiceCurrencyCode` = `XLC`
- XPath: `/Order/cbc:DocumentCurrencyCode` = `XLC`
- Why: requesting invoices in coral adds nothing when the order is in coral and nothing suggests another currency (IND5). Context refuted it: it states a buyer's request to be invoiced in the seller's currency that a Bayvarran buyer would otherwise not be assumed to make. But the order already prices in coral, which says the same; the remark stays Low.
- Condition: the requested invoice currency is absent, or differs from the document currency, or the order says why it is stated.
- Options: (a, preferred) drop it; (b) keep it with a note if the mill, which pays from a Lume account (18), wants to confirm coral invoicing.
- Needs decision: no
- From: broad (F5); context (considered and refuted, argument carried)

### cotton/08#F4 · Low · Customs-trader numbers in the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: section 4.8. The order places the purchase; export and import are declared in 11 and 15, and the order does nothing with the numbers, which read as copied master data (IND5). (The mill's tax registration was refuted by money: it matters for the import and is quoted on the invoice.)
- Condition: every identifier of the parties is one the document has a use for.
- Options: (a, preferred) leave them out.
- Needs decision: no
- From: parties (F5)

### cotton/08#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`); reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) dates from the companies' histories; (b) drop them; (c) record a register-wide date.
- Needs decision: yes
- From: parties (F4)

### cotton/08#F6 · Low · The mill's contact: name, job title and department contradict each other
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: as 02#F6: "Purchasing" fits the mill as buyer; the sales department and customer-service title do not (52 files with this combination, parties).
- Condition: the buyer's contact has a name, job title and department that agree and fit a buyer.
- Options: (a, preferred) a purchasing department and a buyer's title; (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F6), parties (F2)

### cotton/08#F7 · Low · The ginnery's English address and the item texts tagged as Bayvarran English
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: as 02#F7: the ginnery's address and the seller's item text carry `en-XL` in the ginnery's own documents (01, 10, 11, 16) and `en-XB` here. Both parts said no; set to yes as in 02 and 07 (the tag following the issuer is a defensible reading, no convention recorded; earlier flows' merges and merger B).
- Condition: the same rendering carries the same `languageID` in every example, or the issuer rule is recorded.
- Options: (a, preferred) `en-XL` for the ginnery's texts everywhere; (b) record the issuer rule.
- Needs decision: yes
- From: broad (F7), parties (F3, address part)

### cotton/08#F8 · Low · The ginnery's legal form in one untagged English rendering
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: in the ginnery's own documents its legal form is given in Lisavan and English with `languageID`; here only the untagged English one. Split from F7, as 02#F8.
- Condition: the ginnery's legal form carries the same renderings and `languageID`s in every example.
- Options: (a, preferred) both renderings with their tags, as in 01.
- Needs decision: no
- From: parties (F3, legal-form part)

### cotton/08#F9 · Low · The order says nothing about when the lint is wanted
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: the order states what, how much, at what price and on which terms, but not when. Under FOB the seller must deliver on board at the port of shipment on the agreed date or within the agreed period, and the buyer names the vessel (Incoterms 2020, own knowledge); the `Delivery` carries only the delivery party, no requested period, and the order refers neither to the forecast (02, 07) nor to an agreement that would fix the date. The flow shows the shipment leaving on 2026-03-02 (13), but the order does not ask for it. Completeness remark, Low, as in the earlier flows' merges for orders without delivery dates.
- Condition: the order states the requested delivery (loading) date or period, or refers to the agreement or forecast that fixes it.
- Options: (a, preferred) a `RequestedDeliveryPeriod` for loading at the port of Selanu that fits 12/13; (b) refer to the season agreement or call-off rules as the source of the dates.
- Needs decision: no
- From: broad (F4), logistics (F2), context (F2)

### cotton/08#F10 · Low · FOB place given only as text, and FOB for containerised goods
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Port of Selanu`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- Why: the named place of the FOB term is only a description; the same port is identified elsewhere in the flow by its location code `XLSEL` (12). Broad refuted the missing identifier ("no example of the flow identifies the port of Selanu by code"); that is not so, 12 does. Parties left it to logistics. The goods travel in a 40-foot container (12, 17); for containerised goods handed over at the terminal Incoterms 2020 advises FCA rather than FOB (own knowledge, practice, not a UBL rule).
- Condition: the delivery location of the terms is identified as the same port is elsewhere in the flow; the Incoterms rule fits the hand-over, or the choice of FOB is deliberate.
- Options: (a, preferred) add `ID` `XLSEL` (UN/LOCODE) to the delivery location; (b) optionally FCA at the Selanu container terminal.
- Needs decision: yes (the choice of Incoterms rule is part of the sale)
- From: logistics (F3); broad and parties (considered and refuted, counter-arguments carried)

### cotton/08#F11 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: as 01#F8: a zero tax total for a scheme that is the absence of a tax, without ID, tells the seller nothing. Broad preferred dropping the tax total from the order (an anticipated total suffices); money refuted the tax total as a filler (the order states the anticipated tax treatment, which the invoice confirms). Same decision as for the other Lisavan examples.
- Condition: the order's tax total names a real scheme with ID, or the order carries no tax total, consistently with the world's rules for Lisavu.
- Options: (a, preferred) decide once for all Lisavan examples (scheme with ID, or no tax total).
- Needs decision: yes
- From: broad (F3, scheme part); money (considered and refuted the tax total, argument carried)

### cotton/08#F12 · Low · "No general sales tax" typed as a consumption tax, unlike the invoice for the same supply
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode` = `CONSUMPTION`
- XPath: `16-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxTypeCode` is "A code signifying the type of tax". Giving the absence of a sales tax the type "tax on consumption" describes a tax that does not exist. The invoice for the same order line (16) and the self-billed documents 01, 04 and 05 describe the same scheme without a type; money found this order the only one of the 9 files with a `TaxTypeCode` on it. Context refuted it: the absent tax is a consumption tax, so the code names the kind of tax that does not apply. Possible, but then the documents of the flow describe the same scheme differently; the consistency remark stays Low.
- Condition: the order and the invoice describe the tax scheme of the same supply the same way.
- Options: (a, preferred) drop the `TaxTypeCode`, as in the other eight; (b) if it is meant to say which kind of tax is absent, give it the same way in every document.
- Needs decision: no
- From: money (F1), broad (F3, type part); context (considered and refuted, argument carried)

### cotton/08#F13 · Low · A 0 % rate on tax category O
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage"; a supply outside the scope of tax has no rate, and 0 % reads as zero-rating. Added by the merge, as 01#F9.
- Condition: a category stating the supply is outside the scope of tax carries no `Percent`.
- Options: (a, preferred) drop `Percent`.
- Needs decision: no
- From: merge

### cotton/08#F14 · Low · `PackSizeNumeric` 227 for a bale "of about 227 kg"
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `6129`
- Why: as 02#F9: `PackSizeNumeric` is "The number of items in a pack of this item". Read as the bale weight in kg it is not a count (logistics, context: Medium); read per kilogram (the order is in KGM) it fits, but only nominally. The order quantity is exactly 27 bales of 227 kg (6 129 / 227 = 27, recomputed), yet the number of bales is nowhere stated as a count. Low with a decision, aligned with merger B.
- Condition: `PackSizeNumeric`, where present, is a count of items in the item's unit; a nominal weight, if meant as weight, is in an element with a weight unit; if the bale count matters, it is stated as one.
- Options: (a, preferred) drop the pack elements, give the nominal bale weight as an `AdditionalItemProperty` in KGM and, if wanted, the 27 bales in the description; (b) keep them with the per-kilogram reading documented.
- Needs decision: yes
- From: broad (F10, Low), logistics (F1, Medium), context (F1, Medium)

### cotton/08#F15 · Low · Origin area "North coast" in `Region`, in `District` in the farm's address
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: as 02#F10: the same area is a `District` in the farm's address and a `Region` here.
- Condition: the north coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in `OriginAddress`; (b) `Region` in both.
- Needs decision: no
- From: broad (F9), context (F3)

### cotton/08#F16 · Low · Classing results in the applicant's remarks
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as 02#F11: "Remarks by the applicant for this certificate", but the text is the classer's result.
- Condition: the result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark (grade and staple are item properties).
- Needs decision: no
- From: broad (F8)

## Checked and consistent
- Arithmetic (redone): 6 129 KGM × 0.988 per 1 KGM = 6 055.452 = line, anticipated line extension and payable amount, taxable amount; tax 0.000; 6 129 = 27 × 227.
- 16 invoices exactly this line (`16-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`), quantity, price, category O and the buyer's accounting cost 2200 "Raw cotton".
- FOB Port of Selanu with the buyer's forwarder Bayforth Forwarding (`20411644`) fits a buyer who arranges main carriage: 09 (instructions to that forwarder), 13 ("Freight collect") and 17 (forwarder's freight invoice to the mill) follow it; `DestinationCountry` XB and the mill as delivery party fit the import (15).
- The certificate (signature 2026-02-20) predates the order (2026-02-24) and states the grade the line asks for (Middling, 28.6 mm = 1-1/8 inch).
- 6 129 kg of lint is 34 % of the 18 000 kg of seed cotton in 03, a usual turnout (own knowledge).
- Buyer's and seller's item identifiers are both present and distinct; the mill's description is identical in 02, 07, 08, 16, 17, 18 (parties).

## Considered and refuted
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Port of Selanu`: place without an identifier — broad refuted (no example identifies the port by code), parties left it to logistics; the merge followed logistics (12 carries `XLSEL`): F10. (from broad, parties)
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate`: a lot certificate in an order — refuted: here the mill orders the classed lot itself (27 bales certified in 10), so the certificate identifies what is ordered. (from broad)
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`: the buyer's sales-tax registration as copied master data — refuted: the goods are imported into Bayvarra, where the registration matters (15), and the invoice quotes it (16). (from money)
- `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.000`: a tax total in an order as a filler — refuted by money (states the anticipated tax treatment); the scheme question remains F11. (from money)
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode` = `CONSUMPTION`: context refuted (names the kind of tax that does not apply); kept as F12. (from context)
- `/Order/cbc:RequestedInvoiceCurrencyCode` = `XLC`: context refuted (a buyer's request); kept as F3. (from context)
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`: a Middling certificate for the whole lot against the downgrade of part of the farm's delivery in 05 — refuted for this example: nothing in the order links the lot to the farm's delivery; recorded in 05#F2/F25. (from context)

## Changed in the merge
- broad/F2 + parties/F1 → F1.
- broad/F6 + parties/F2 → F6.
- broad/F7 + parties/F3 → F7 and F8: legal form split off (Low/no); F7 needs decision changed from no to yes (aligned with 02, 07, earlier flows and merger B).
- broad/F4 + logistics/F2 + context/F2 → F9.
- broad/F3 split: scheme name → F11 (Low/yes, with money's counter-argument), type code → F12 with money/F1 (Low/no, context's counter-argument).
- F13: added by the merge (O with 0 %).
- broad/F10 (Low), logistics/F1, context/F1 (Medium) → F14: Low/yes, aligned with merger B and 02#F9.
- broad/F9 + context/F3 → F15.
