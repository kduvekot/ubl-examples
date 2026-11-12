# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/07-Invoice.xml`, Git blob `c9439fcedf37997f7173ad361e9246f5cc5439d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/07#F1 · High · Gas sold to Ferrano Energy as an export is consigned to Montebrio Power on export and imported by nobody
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `8640000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `XU-R-105918`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: this invoice bills Ferrano Energy for 2400 MWh of Kelpstone gas "measured at the border station" and exempts it from tax as an export. The flow's only export declaration (04) declares 39200 MWh, which is 36800 (06) + 2400 (this invoice), with a value of 1411200 XBL, exactly both invoices at 36 XBL/MWh. Its only consignee is Montebrio Power. The flow's only import declaration (05) is Montebrio Power's, for its own 36800 MWh and 132480000 XUF. So the 2400 MWh sold here are declared on export as delivered to another party and are not declared on import at all. The customs value and the import VAT of this purchase appear nowhere in the flow, and the export exemption claimed here cannot be linked to a customs document that names this buyer. A consignee may differ from the buyer, and Ferrano Energy's import might lie outside the flow (money's reading). But nothing in the flow says either, and the invoice and 04 then describe the same gas as going to different parties. No import declaration in the examples names Ferrano Energy (XU-R-105781) as importer (logistics, counted over `world/examples/*/*.xml`; confirmed in the merge with `grep -l 'XU-R-105781' --include='*ImportCustomsDeclaration.xml'`). Whether the gas reaches Ferrano Energy is itself sound: it resells 61.2 MWh of March gas to Valdara Industries in 01, within the 2400 MWh bought here.
- Condition: the 2400 MWh billed here are covered by customs documents that name Ferrano Energy (or a stated agent) as consignee and importer, with a customs value of 8640000 XUF; or the flow states how the gas reaches Ferrano Energy otherwise, and this invoice (seller, tax treatment) agrees with that.
- Options: (a) preferred: split the export declaration 04 by buyer (two consignees or goods items) and add Ferrano Energy's import (its own import declaration, or a second goods item in 05 if the world's customs allow it), because this keeps the two direct sales; (b) let Montebrio Power import all 39200 MWh and resell 2400 MWh to Ferrano Energy, which replaces this invoice with a domestic Montebrio invoice with Urvanian VAT; (c) state in the documents that Ferrano Energy's share is delivered through Montebrio's import. Resolve together with the findings on the consignee of 04 and on shipment KG-SH-26-0154 in 04/05.
- Needs decision: yes (adds or changes documents of the flow)
- From: logistics (F1), context (F1), broad (F1), money (F2), parties (F3)

### energy/07#F2 · Medium · Pricing exchange rate from lume on a price that the note says is set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`
- Why: as in `06-Invoice.xml`. `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole", that is, a price converted from another currency. The note says the price is set in ferra, all currencies of the invoice are XUF, and there is no document-level rate. If the rate is there for the seller's books in lume (its tax scheme's currency is XBL), the elements for that are `TaxCurrencyCode` and `TaxExchangeRate`.
- Condition: an exchange rate on the price is present only if the price was converted, and then the note says so. A rate to the seller's tax currency is at document level. Otherwise there is no rate.
- Options: (a) preferred: `TaxCurrencyCode` XBL with `TaxExchangeRate` if the seller needs it, and `PricingExchangeRate` dropped; (b) a price set in lume: keep the rate and correct the note; (c) drop the rate. Resolve together with `06-Invoice.xml`.
- Needs decision: yes (which story: a price set in ferra or in lume)
- From: broad (F2), money (F1), context (F2)

### energy/07#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language code that repeats `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 of the 250 XML examples (counted by the parts over `*.xml`).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB`, with a locale list ID; (b) leave it out.
- Needs decision: no
- From: broad (F3), parties (F1), context (F3)

### energy/07#F4 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division and belongs in `CountrySubentity`, as in the supplier's bank address in this invoice (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). It is a world convention: 219 occurrences in 104 of the 250 XML examples.
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense, and record why.
- Needs decision: no
- From: broad (F4), parties (F2)

### energy/07#F5 · Low · Buyer's contact is the customer service of its Sales department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys 2400 MWh of wholesale gas here. Its customer service in Sales serves its own retail customers, not procurement or payables. Montebrio, buying the same gas in 06, gives its trading desk.
- Condition: the accounting customer's contact deals with buying or paying for wholesale gas.
- Options: (a) preferred: a procurement or accounts-payable contact (also in 03); (b) leave the contact out.
- Needs decision: no
- From: broad (F6), parties (F5)

### energy/07#F6 · Low · Industry classification of the gas buyer leaves out gas
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is electric power generation, transmission and distribution. Ferrano Energy buys gas here for its gas customers (01), which is ISIC 3520, distribution of gaseous fuels through mains (own knowledge).
- Condition: Ferrano Energy's classification covers its gas activity, the same way in every example.
- Options: (a) preferred: add 3520 next to 3510; (b) keep the main activity only, if that is the world's rule.
- Needs decision: no
- From: parties (F6)

### energy/07#F7 · Low · Kelpstone's plant location copied into the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: the plant's location (description and coordinates) plays no part in billing gas measured at the border station, and the item carries its origin already. It looks copied from master data. The `InformationURI` ("a document providing information about this location") is the company's home page, as in `WebsiteURI`.
- Condition: the supplier carries no physical location the invoice does not use, and any `InformationURI` is about the location itself.
- Options: (a) preferred: leave `PhysicalLocation` out of 06–09; (b) keep it only for a stated purpose.
- Needs decision: no
- From: parties (F7), context (F4)

### energy/07#F8 · Low · "Four kilometres" to the field, but the field's coordinates are 6.1 km from the plant
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- Why: calculated as in `06-Invoice.xml`: the plant is at 39°52.80′ S 15°18.00′ W and the field at 39°49.80′ S 15°16.20′ W. That gives 5.56 km north–south and 2.56 km east–west, about 6.1 km in all, not four. The platform need not stand at the field's grid coordinates, so this is a plausibility remark.
- Condition: the distance in the description agrees with the coordinates, or the description gives no distance.
- Options: (a) preferred: correct the text or the coordinates, the same way everywhere; (b) drop the distance from the text.
- Needs decision: no
- From: merge

### energy/07#F9 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Ferrano Energy's English address renderings carry `languageID="en-XB"`. The same texts are `en-XU` in `02-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`, in 01 and in 03. The legal form is given in `qau` and `en-XU` there, but is one untagged text here. The parts counted 107 Urvanian addresses with an `en-XB` rendering in 39 `*.xml` files.
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag the English renderings of Urvanian names `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no
- From: broad (F5), parties (F4)

## Checked and consistent
- Line and totals: 2400 × 3600 = 8640000 = LineExtensionAmount, TaxExclusiveAmount, TaxInclusiveAmount and PayableAmount; tax 0 under category G, exemption EXP, STT; supply type GOODS (all parts; recalculated in the merge).
- Penalty: 1.5 % of 8640000 = 129600 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `129600`, with the penalty period from the day after the due date, as in 06 (broad, money, context).
- Quantities: 2400 + 36800 (06) = 39200 MWh, the quantity in 04. Price: 3600 XUF = 36 XBL × 100, which is 06's price and the export value per MWh (1411200 / 39200 = 36). Implied weight: 2400 MWh × 75 kg/MWh = 180000 kg, the difference between 04 (2940000 kg) and 05 (2760000 kg) (logistics).
- Item and origin are the same as in 04 and 06; HS 271121 and CPC 12020 fit natural gas. `InvoicePeriod` March 2026 lies before the issue date 2026-04-03; due date 2026-05-03 (logistics).
- Payment: RF14KGINV260158 passes its check digits, and the payee account is Kelpstone's lume account, as in 06, 08 and 09 (check passes). No reminder or remittance advice refers to this invoice, and nothing says it was paid late, so its absence from the follow-up documents is consistent (money, broad, logistics).
- Parties: Kelpstone is described identically in 04–09. Ferrano Energy's identifiers, legal entity, tax scheme and contact match 01, 02 and 03, apart from the tags of F9. `BuyerCustomerParty`/`SellerSupplierParty` repeat the accounting parties without an "if different" condition. The payee account holder is the supplier's registration name. Ferrano Energy as a wholesale gas buyer fits its role as retailer (02 and 01) (parties, context, broad).

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF` against `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XBL`: suspected a contradiction between payment in ferra and a payee account in lume. Refuted because a cross-currency credit transfer with bank conversion is normal, and ChargeBearerCode SHAR settles the charges (from broad, money).
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected to repeat DocumentCurrencyCode for no reason. Refuted because the payee account is held in lume (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`: suspected copied master data. Refuted because the exporter's customs number is relevant on an export invoice (from context).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`: suspected as a finding of its own, an export exemption for a buyer who is not the consignee on the export declaration. Money refuted it as a separate finding, because the goods do leave Bayvarra under 04, which is what the exemption reason states. The merge agrees that the category is not wrong on its own terms; the consignee question is F1, which cites the category (from money).

## Changed in the merge
- logistics/F1 (High), context/F1 (High), broad/F1 (Medium), money/F2 (Low), parties/F3 (Low) → F1, High. Section 6 makes a statement contradicted by another example of the flow High: this invoice sells the 2400 MWh to Ferrano Energy, while 04 consigns them to Montebrio Power. The five parts of 04 rate the same problem High. Money's "not necessarily a contradiction" reading is kept in "Why", but nothing in the flow supports it. The options of all parts are combined. Needs decision stays yes.
- broad/F2, money/F1, context/F2 → F2: combined. Needs decision is yes (context said no), as in 06/F1, because the fix chooses the story.
- broad/F3, parties/F1, context/F3 → F3: combined, no change.
- broad/F4, parties/F2 → F4: Needs decision is no (broad said yes), because this is an encoding change; the same choice is made across the flow.
- broad/F6, parties/F5 → F5: combined, no change.
- parties/F7, context/F4 → F7: combined.
- F8: new in the merge (see 06/F5).
- broad/F5, parties/F4 → F9: combined; the untagged legal form comes from parties.

## Outside this review
- Shipment KG-SH-26-0154 is declared with 39200 MWh in 04 and 36800 MWh in 05. That problem lies in 04/05 and belongs to their reviews (F1 here covers only what this invoice contradicts).
