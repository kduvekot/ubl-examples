# LLM review: 27-OrderChange.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/27-OrderChange.xml`, Git blob `e43fb0041dc6f797ab80a2e9f8efb406a7c4464c` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/27#F1 · High · "30 days after the invoice, as the contract says" is not what the contract says
- XPath: `/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`
- XPath: `/OrderChange/cac:TransactionConditions/cbc:Description` = `The framework contract's conditions apply.`
- Why: The note cites the contract for its term. The contract's term is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` (the same in 01–03). Thirty days from the invoice and thirty days from acceptance of the release are different due dates: the invoice of this release is dated 2026-03-31, before any acceptance is recorded (the installation was late, 34). The change misquotes the document it relies on, while its own transaction conditions say the contract's conditions apply.
- Condition: a payment term an order document attributes to the contract is the contract's term, or the order change carries no payment terms.
- Options: (a) remove `PaymentTerms` from the change, which alters only the colour, and leave the terms to the contract (preferred); (b) repeat the contract's wording; (c) if "after the invoice" is the story, change the contract and the notices (then a decision).
- Needs decision: no (the contract is unambiguous; broad said yes because the invoice and reminder depend on which term is the world's, which is option (c))
- From: broad (F1, yes), money (F1), context (F1)

### tender/27#F2 · High · The changed order still contains no installation, which the release's invoice bills
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: After this change the order stands at 40 benches plus the colour charge. The invoice of the order bills `32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`; recalculated, the difference of 720.00 is the installation of the 40 benches (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`), which neither the order nor this change orders. Same problem as 26#F3, here because this document states the buyer's latest view of the release.
- Condition: the order as changed contains every line the invoice of the release bills.
- Options: as 26#F3: (a) order the installation in the order (preferred; nothing then changes here if F3 option (a) is taken); (b) a separate order.
- Needs decision: yes
- From: money (F3, Medium)

### tender/27#F3 · Medium · The new total of the order given as "the amount of change"
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:ChargeTotalAmount` = `200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: In an order change `AnticipatedMonetaryTotal` is "The amount of change to the total cost of the order anticipated by the buyer". Recalculated: 20160.00 − 19960.00 (`26-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`) = 200.00 is the change; the element carries the whole new total. Stating the new total is common practice for order changes; under semantic conformance that does not change the UBL meaning.
- Condition: the amounts of `AnticipatedMonetaryTotal` equal the difference between the changed order and the order (payable 200.00, charge total 200.00, no line extension change).
- Options: (a) payable 200.00 with charge total 200.00 and no line extension amount (preferred, as the air merge decided for air/01-OrderChange); (b) keep the new total and record the gap between definition and practice for the TC write-up.
- Needs decision: no (money and context said yes; aligned with the air merge, which applied the definition without a decision)
- From: money (F2), context (F2)

### tender/27#F4 · Medium · The changed line does not identify the item, and the new colour is in free text only
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Park bench Serra 180, frame in moss green RAL 6005`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`
- Why: The purpose of the change is to replace the ordered variant. The order identifies it in structured form (`26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`, with PhysicalAttribute COLOUR/FRM/GRY and the property "Frame colour" = Ferro grey; ExtendedID is defined with the example "Item 123 Ext 45 = brown chair"), and the world's colour list has `GRN` ("Green, such as moss green (RAL 6005)."). The changed line has no item identification at all, so nothing structured tells the seller's system which article and variant are now wanted. Downstream the despatch advice, the customs declarations, the invoice and the credit note still identify the goods as GRY / "Frame in Ferro grey" (29–33; a finding of those examples). Broad and context rated it Low; Medium because the changed line lacks the identification the document's purpose depends on.
- Condition: the revised line identifies the item (VI-B180 / 771020000027) and its new variant in the same structured places the order used for the old one.
- Options: (a) SellersItemIdentification VI-B180 with the green variant's ExtendedID and a PhysicalAttribute with DescriptionCode GRN (preferred); (b) at least the item identifiers, with the colour in the description.
- Needs decision: no
- From: logistics (F1, Medium), broad (F4, Low), context (F6, Low)

### tender/27#F5 · Medium · A province in `Region`, twice
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries"; a province is `CountrySubentity`, as the Bayvarran addresses use. 219 in 104 files.
- Condition: provinces are in `CountrySubentity`; `Region` is absent or holds a region.
- Options: (a) move them to `CountrySubentity` (preferred).
- Needs decision: no
- From: broad (F3, part), parties (F2), context (F3)

### tender/27#F6 · Medium · Language code in `LocaleCode`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 code. 362 in 213 files.
- Condition: `LocaleCode` is absent or names a locale from a locale list.
- Options: (a) remove it (preferred); (b) `en-XB` from a locale list.
- Needs decision: no
- From: broad (F3, part), parties (F1), context (F4)

### tender/27#F7 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The buyer is a municipal department (ISIC 8411); a liquidation status and a "Commercial register" type do not fit a body that is not a company.
- Condition: neither on the public body.
- Options: (a) drop both (preferred); (b) reduce the legal entity to name and CompanyID.
- Needs decision: no
- From: broad (F7, part, Low), parties (F4, Low), context (F7, Low)

### tender/27#F8 · Low · Currency codes, three exchange rates and a forward contract in a change with no price and no conversion
- XPath: `/OrderChange/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderChange/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/OrderChange/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderChange/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/OrderChange/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderChange/cac:AllowanceCharge/cbc:Amount` = `200.00`
- Why: `PricingCurrencyCode` is "the currency that is used for all prices in the Order Change"; the change has no price (its line has quantity and amount only), no tax total and no payment currency, and every amount is in lume (`/OrderChange/cbc:RequestedInvoiceCurrencyCode` = `XBL`); nothing is converted by any rate. Broad read the 200.00 charge in XBL as contradicting the pricing currency; a charge is not a price, so the merge rates it as data without use. The forward purchase of ferra of 2026-01-02 has the problems stated in 26#F13 (attached to the pricing rate, dated before the procedure). `TaxCurrencyCode` may be kept as a request for the invoice (money's option).
- Condition: a currency code and exchange rate are present only where the document has an amount in, or a conversion into, that currency; the forward contract as decided in 26#F13.
- Options: (a) remove `PricingCurrencyCode` and the three rates (and with them the forward contract) from the change (preferred); (b) keep `TaxCurrencyCode` as the request for the invoice.
- Needs decision: yes (the forward contract follows the decision of 26#F13)
- From: broad (F2, Medium; F6, Low, yes), money (F4), context (F5, part)

### tender/27#F9 · Low · A freight forwarder is named who plays no part in the transport
- XPath: `/OrderChange/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `FreightForwarderParty` is "A freight forwarder or carrier." The order names none and the change is about colour; under the order's DAP terms (`26-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`) the seller arranges the carriage. The documents of the movement do not know Bayforth: the despatch advice is issued by `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`, and neither customs declaration names it. Bayforth appears otherwise only as the seller's tax representative (`32-Invoice.xml:/Invoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`; also 33–35). It is given by number and name only.
- Condition: a forwarder named in the order documents takes part in the transport or customs handling of the flow, compatibly with the delivery terms, and its addition is a stated change; otherwise none is named.
- Options: (a) remove it (preferred); (b) give Bayforth a visible role (e.g. the declarant of the import in 31) and say so, which changes 29–31.
- Needs decision: yes (who Bayforth is in this flow; logistics said no, parties, broad and context yes)
- From: parties (F7), logistics (F2), broad (F5, part), context (F5, part)

### tender/27#F10 · Low · Payment means and transaction conditions appear for the first time in a change of colour
- XPath: `/OrderChange/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`
- XPath: `/OrderChange/cac:TransactionConditions/cbc:Description` = `The framework contract's conditions apply.`
- Why: `PaymentMeans` in an order change is the "Expected means of payment". The order it changes has none, and nothing about the payment changes; the buyer states the seller's account (with branch and bank address) six days before the seller's invoice gives it. The transaction conditions only restate that the contract applies, which the contract reference already says. Neither is announced as a change.
- Condition: the order change carries payment means and conditions only if it changes them or the order had them.
- Options: (a) remove them from the change (preferred); (b) put expected payment means in the order.
- Needs decision: no
- From: money (F5), broad (F5, part), context (F5, part)

### tender/27#F11 · Low · The contract cited twice, once as an unexplained "originator document"
- XPath: `/OrderChange/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/OrderChange/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: As in 26#F14: "A reference to an originator document associated with this document" with the contract's ID only adds nothing to `Contract` and says not which document is meant.
- Condition: the originator reference names another document and says what it is, or is absent.
- Options: (a) remove it (preferred).
- Needs decision: no
- From: broad (F7, part), logistics (F4)

### tender/27#F12 · Low · Additional document reference with only an ID
- XPath: `/OrderChange/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COLOUR-RAL6005`
- Why: "A reference to an additional document associated with this document", without type or description, and in no other example (`grep -rl --include='*.xml' PWD-COLOUR-RAL6005 world/examples`: this file only). Broad and context refuted it (the ID names a colour specification, which fits as an annex); the reader still has to infer the kind of document from the ID.
- Condition: the reference states what the document is.
- Options: (a) add `DocumentType` (e.g. "Colour specification") (preferred).
- Needs decision: no
- From: logistics (F3); broad and context refuted it (carried)

### tender/27#F13 · Low · Party tax exemption reason worded as a transaction
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the text begins with a kind of sale; only its second half is the party's status.
- Condition: the party-level reason states the party's status.
- Options: (a) reword, e.g. "Public body: exempt from the state sales tax" (preferred).
- Needs decision: no
- From: parties (F3)

### tender/27#F14 · Low · Master data of the parties that the change does nothing with
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketName` = `Ferrano Stock Exchange`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: The change tells the seller a new colour; the seller's share capital, listing and warehouse provider (whose contact has no means of contact) and both parties' customs-trader numbers are not part of that. Parties refuted the listing (part of a listed company's description), carried.
- Condition: the parties carry what the change uses.
- Options: (a) leave these out (preferred); (b) keep those with a stated use.
- Needs decision: no
- From: broad (F7, part), parties (F6), context (F8); customs-trader numbers added in the merge

### tender/27#F15 · Low · Same Urvanian names tagged `en-XB` here and `en-XU` elsewhere; Italian names tagged as English
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CityName[2]` = `Ferrano`
- Why: The second renderings are tagged `en-XB` here and `en-XU` in the Urvanian-issued examples (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`); the text is identical, so the tag follows the issuer. The renderings are moreover Italian names ("Via", "Piazza") tagged as English; broad refuted that as the world's convention of Italianate English names for Urvanian places. Neither question can be settled from the XML; the earlier flows' merges kept both as Low/yes.
- Condition: the same text carries the same `languageID` in every example, and the tag names the language of the text, or the convention is documented.
- Options: (a) `en-XU` everywhere and the convention recorded in the story (preferred); (b) document the issuer rule.
- Needs decision: yes
- From: parties (F5, part); broad's refutation of the Italian names folded in by the merge

### tender/27#F16 · Low · Legal form of the Urvanian party in one untagged rendering
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Given in `qau` and `en-XU` in the Urvanian-issued examples (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`), here once and untagged.
- Condition: rendered like the address wherever the party is described in full.
- Options: (a) both renderings, tagged (preferred).
- Needs decision: no
- From: parties (F5, part; split off in the merge)

## Checked and consistent
- `OrderReference` `LPWD-PO-26-0212` is the order of 23 March 14:40; the change follows the next morning (24 March 08:06), sequence number 1, the only change of the flow, and is answered within its validity (to 2026-03-27) by 28 (25 March).
- Arithmetic (recalculated): line 40 × 499 = 19960.00, unchanged, status Revised; 19960.00 + 200.00 = 20160.00; 200.00 is 5 lume a bench. 28 and 32 carry the same charge, code and amount.
- Charge reason CAT is "Special colour service" (UNTDID 7161) and fits; RAL 6005 is moss green in the real RAL Classic collection (own knowledge).
- Payment means 30 (credit transfer); account XU79 0351 0416 0000 0000 2094 58 passes the IBAN-style check (`check_ids.py`), contains the branch number 03510-41600, holder name = Valdara's registered name, same account in 32, 35, 36.
- `RequestedInvoiceCurrencyCode` XBL = the invoice's document currency; rates 100 and 0.01 reciprocal.
- Parties: buyer and seller as in 26; Bayforth `20411644` the same in the 5 examples that carry it; the signatory is the issuing department (from parties).
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/OrderChange/cac:QuotationDocumentReference/cbc:ID`: VI-QT-26-0071 is no example and would have to come between order and change — refuted: a quotation for the surcharge the same afternoon is plausible, need not be a UBL document of the flow, and the response confirms "at the quoted charge" (from broad, logistics, context).
- `/OrderChange/cac:AdditionalDocumentReference/cbc:ID`: only an ID — refuted by broad and context; the merge keeps logistics' F12 (from broad, context).
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: CREVXUFR a real BIC — refuted: positions 5–6 `XU` are a user-assigned ISO 3166 code no real BIC carries (from broad, parties).
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]`: Italian-looking name tagged en-XB — refuted by broad as the world's convention; the merge folds it into F15 as a question to settle (from broad).
- `/OrderChange/cac:AllowanceCharge/cbc:Amount`: no tax category on the charge — refuted: the change has no tax total, and the category follows from the goods (from broad, money).
- `/OrderChange/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: a 7161 code without base or factor — refuted: a fixed charge needs neither (from money).
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode`: a ferra account for an order in lume — refuted: the invoice's payment currency is the ferra (from money; context had listed it as a money question).
- `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` — refuted: text element, same everywhere (from parties).
- `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: +999 — refuted, not assigned in E.164 (from parties).
- `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — refuted by parties; the merge keeps it in F14 (from parties).
- `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990` a real ICD — refuted (from parties).
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:Address/cbc:CityName[2]`: branch address too thin — refuted: the institution's address is complete and the branch is identified by number (from parties).
- `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount`: unchanged although the colour changed — refuted: the surcharge is a document-level charge (from logistics).
- `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: forward contract before the procedure — logistics raised it once in 26; the merge carries it into F8 by reference to 26#F13 (from logistics).
- `/OrderChange/cac:ValidityPeriod/cbc:EndDate`: a validity for a change — refuted: it says until when the buyer stands by it (from context).
- `/OrderChange/cac:Signature`: a signature on a change — refuted: a public buyer signing a change that costs money is plausible (from context).

## Changed in the merge
- broad/F1 (yes), money/F1, context/F1 → F1: High, Needs decision no.
- money/F3 (Medium) → F2: High, aligned with 26#F3.
- money/F2, context/F2 (yes) → F3: Needs decision no, aligned with the air merge (order change totals = amount of change).
- logistics/F1 (Medium), broad/F4, context/F6 (Low) → F4: Medium.
- broad/F3 → F5 and F6: split.
- broad/F7 → F7, F11, F14: split; public body raised to Medium (parties/F4, context/F7 also Low), aligned with the decisions file.
- broad/F2 (Medium), broad/F6, money/F4, context/F5 (part) → F8: Low (exchange rates with nothing to convert, as in the decisions file); broad's contradiction reading not followed (a charge is not a price).
- parties/F7, logistics/F2, broad/F5 and context/F5 (parts) → F9: Needs decision yes.
- money/F5, broad/F5 and context/F5 (parts) → F10.
- parties/F5 → F15 and F16: split; broad's refuted Italian-name question folded into F15.
