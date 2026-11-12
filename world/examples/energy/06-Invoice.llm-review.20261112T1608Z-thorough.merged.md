# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/06-Invoice.xml`, Git blob `7c0dad8fdbb0040b1dab2a0e3035fb59f281af39` (committed)
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

### energy/06#F1 · Medium · Pricing exchange rate from lume on a price that the note says is set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`
- Why: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". It says the price was converted from another currency. Here the price, the document, the payment and the line are all in XUF, the note says the contract sets the price in ferra, and the document has no exchange rate of its own that this one could differ from. So one of two things holds. Either the price really is a lume price (36 XBL/MWh) converted at 100, which contradicts the note; the rate's date, 2026-01-02, would fit a rate fixed at the start of the contract year. Or the rate serves another purpose. The likely one is the seller's own books and tax reporting: Kelpstone's tax scheme is kept in lume, and the export declaration states the value in lume (`04-ExportCustomsDeclaration.xml`, 1411200 XBL for 06's and 07's gas together). UBL has `TaxCurrencyCode` and `TaxExchangeRate` ("The exchange rate between the document currency and the tax currency") for that. The same pattern occurs in `07-Invoice.xml`.
- Condition: an exchange rate on the price is present only if the price was converted from another currency, and then the note agrees. A rate the seller needs for its tax reporting is at document level in `TaxCurrencyCode`/`TaxExchangeRate`. Otherwise there is no rate.
- Options: (a) preferred: drop `PricingExchangeRate` and, if the seller reports in lume, add `TaxCurrencyCode` XBL with `TaxExchangeRate`, because that matches the note; (b) if the contract really fixes the price in lume, keep the rate and change the note to say so; (c) drop the rate if it has no use in the invoice. Resolve it together with `07-Invoice.xml`, so that both invoices of the same contract tell the same story.
- Needs decision: yes (which story: a price set in ferra or in lume)
- From: broad (F1), money (F1), context (F1)

### energy/06#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language code that repeats `Language/ID`, not a locale such as `en-XB`. The same value occurs 362 times in 213 of the 250 XML examples (the parts counted with `grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` and with lxml).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB`, with a locale list ID; (b) leave it out.
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### energy/06#F3 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is a political or administrative division and belongs in `CountrySubentity`, as the supplier's bank address in this invoice has it (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). It is a convention of the world: 219 occurrences in 104 of the 250 XML examples (counted by the parts over `*.xml`).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense, and record why.
- Needs decision: no
- From: broad (F3), parties (F2)

### energy/06#F4 · Low · Kelpstone's plant location copied into the invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: the invoice bills gas measured at the border station. The location of the producer's treatment plant (description and coordinates) plays no part in that, and the item already carries its origin (`OriginCountry`, `OriginAddress`). The location looks copied from master data. Its `InformationURI` ("a document providing information about this location") is the company's home page, the same as `WebsiteURI`.
- Condition: the supplier carries no physical location the invoice does not use, and any `InformationURI` is about the location itself.
- Options: (a) preferred: leave `PhysicalLocation` out of the commercial documents 06–09, keep it in the customs documents, and drop the home-page URI there; (b) keep it only for a stated purpose (a place of supply would belong in a delivery element).
- Needs decision: no
- From: parties (F4), context (F3)

### energy/06#F5 · Low · "Four kilometres" to the field, but the field's coordinates are 6.1 km from the plant
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `18.00`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `16.20`
- Why: calculated: the plant is at 39°52.80′ S 15°18.00′ W and the field (the item's origin) at 39°49.80′ S 15°16.20′ W. The latitude difference is 3.00′ = 5.56 km; the longitude difference is 1.80′ × cos 39.85° × 1.852 km = 2.56 km; together that is about 6.1 km, not four. The platform need not stand at the field's grid coordinates, so this is a plausibility remark. The parts of 04 and 05 found the same distance in those examples.
- Condition: the distance in the description agrees with the coordinates of the plant and the field, or the description no longer gives a distance.
- Options: (a) preferred: correct the text or the coordinates, the same way in every example that carries them; (b) drop the distance from the text.
- Needs decision: no
- From: merge (found while verifying parties F4 and context F3)

### energy/06#F6 · Low · The customer's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: the English renderings of Montebrio Power's street and town carry `languageID="en-XB"`. The same texts are `en-XU` in `03-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`, in 05 and in 09. The legal form is given in `qau` and `en-XU` there, but is one untagged text here. The tag follows the issuer's country (04, 06, 07 and 08 are issued from Bayvarra), not the rendering. The parts counted 107 Urvanian addresses with an `en-XB` rendering in 39 `*.xml` files (lxml count).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag the English renderings of Urvanian names `en-XU` and keep the `qau` legal form; (b) record an issuer-locale rule and apply it consistently.
- Needs decision: no
- From: broad (F4), parties (F3)

## Checked and consistent
- Line and totals: 36800 × 3600 = 132480000 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `132480000` = LineExtensionAmount, TaxExclusiveAmount and TaxInclusiveAmount = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`; tax 0 (broad, money, context, logistics; recalculated in the merge).
- Tax: category G with exemption reason EXP ("Export outside Bayvarra") under Bayvarra's STT, in the subtotal and on the item; supply type GOODS fits gas (own knowledge). The gas leaves Bayvarra under 04 and is imported by this buyer under 05 (broad, money, context).
- Penalty: 1.5 % of 132480000 = 1987200 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1987200`. The penalty period starts on 2026-05-04, the day after the due date 2026-05-03, and runs one month. The reminder 08 charges exactly this (19872.00 XBL × 100), and the remittance advice 09 pays it on line 2 (broad, money).
- Follow-up documents: 08 and 09 refer to KG-INV-26-0157 with this amount and due date. 09 pays 132480000 + 1987200 = 134467200 XUF, quoting `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157`, to this payee account (money, context).
- Against 05: the quantity is `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`, and the customs value is `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000` (context, logistics, parties).
- Rate: 1 XBL = 100 XUF agrees with 04 (39200 MWh × 36 XBL = 1411200 XBL), 08 and 09 (money, logistics).
- Item: the same item (KG-NG, 772060000015, HS 271121, CPC 12020, origin XB) and field coordinates as 04 and 07 (logistics).
- Dates: `InvoicePeriod` March 2026 lies before the issue date 2026-04-03 (logistics).
- Parties: Kelpstone Gas and Montebrio Power are the exporter and importer of 04/05. Kelpstone is described identically in 04–09 (59 leaf values). Montebrio's identifiers, legal entity, tax scheme and contact match 03, 05 and 09, apart from the tags of F6. The seller's contact (gas sales) and the buyer's (energy trading) fit a wholesale gas contract. `BuyerCustomerParty`/`SellerSupplierParty` repeat the accounting parties, and their definitions have no "if different" condition. The payee account holder is the supplier's registration name, at its Gullhaven branch (parties).
- `check_ids.py`: RF41KGINV260157 and the payee account pass their check digits (broad, money, logistics).

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XBL` against `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected a contradiction between a payee account in lume and payment in ferra. Refuted because a cross-currency credit transfer is normal: the banks convert, and ChargeBearerCode SHAR settles the charges (from broad, money).
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected to repeat DocumentCurrencyCode for no reason. Refuted because the payee account is held in lume, so the statement that payment is in ferra tells the payer something (from context).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`: suspected master data without use. Refuted because the invoice of an export is evidence for the importer's customs declaration (05), where this number matters (from broad).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`: suspected copied master data. Refuted because the exporter's customs number is commonly given on an export invoice and links it to the export declaration (from context).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cbc:ID` = `33/03`: suspected unused data. Refuted because origin information on an export invoice supports the customs declarations (from context).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`: suspected a trading contact on an invoice. Refuted because, for a wholesale gas contract, the buyer's trading desk is the counterpart of the seller's gas sales contact (from broad).
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`: suspected because its definition speaks of "payment after the settlement period", and the terms have no settlement period. Refuted because the due date and the penalty period (from 2026-05-04) make the point clear (from money).
- `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`: suspected because the note says "per month" and the structured period covers only the first month. Refuted because the penalty amount is for that first month, and that is what the reminder charges (from money).
- No `TaxPointDate`, while 02 and 03 carry one: refuted because an export with no tax charged needs no tax point in the invoice, and the definition makes it optional (from money).
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`: suspected that the invoice should identify the delivery (border station, shipment KG-SH-26-0154 or the import declaration). Refuted because a monthly invoice for one gas flow to one buyer is unambiguous with the period and the measuring point named (from logistics).

## Changed in the merge
- broad/F1, money/F1, context/F1 → F1: combined. Needs decision is yes (broad and money said yes, context no), because the fix decides which story is true, a price set in ferra or in lume. The rate's date and the supplier's tax-scheme currency are added as evidence.
- broad/F2, parties/F1, context/F2 → F2: combined, no change.
- broad/F3, parties/F2 → F3: combined. Needs decision is no (broad said yes), because moving the province to `CountrySubentity` changes the encoding, not the story. Section 6 gives "a province in Region" as a Medium example, not as a decision. The merge of energy 01–05 makes the same choice.
- parties/F4, context/F3 → F4: combined; the option of keeping the location in the customs documents is from parties.
- F5: new in the merge. It came up while verifying F4: the description's "four kilometres" was recalculated against the coordinates, and the same result is in the parts of 04 and 05.
- broad/F4, parties/F3 → F6: combined; the untagged `CompanyLegalForm` line comes from parties.

## Outside this review
- Shipment KG-SH-26-0154 is declared with 39200 MWh in 04 and 36800 MWh in 05. That problem lies in 04/05 and belongs to their reviews.
- Whether the 2400 MWh of 07 can be followed through customs is a finding in 07's review.
