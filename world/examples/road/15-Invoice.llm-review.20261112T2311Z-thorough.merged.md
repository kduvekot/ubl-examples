# LLM review: 15-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/15-Invoice.xml`, Git blob `8fdcb4b50214e654097ed80dd7c97b81f9267569` (committed)
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

### road/15#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With 0.82 per 1 EA the calculated value is 0.82 kg CO2e per bench, not 96 kg. Recalculated in the merge: 96 / 0.82 = 117.1, no quantity of the item or the flow; 0.82 × 56.5 kg of materials = 46.3 kg. The values contradict each other (High). The triple occurs in 39 files, 9 in this flow (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`).
- Condition: `ValueFactorNumeric` × (activity quantity in the unit of `ValueBaseMeasure`) equals `ValueMeasure`, or factor and base are absent.
- Options: (a, preferred, as in the rail and road 01-12 merges and context) drop factor and base, the value being a per-item LCA figure; (b, broad/logistics) state the factor and base the 96 kg is really calculated from.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F3, Medium)

### road/15#F2 · High · Payment exchange rate to a currency that is not the payment currency
- XPath: `/Invoice/cbc:DocumentCurrencyCode` = `XUF`
- XPath: `/Invoice/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:SourceCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01`
- Why: `Invoice/PaymentExchangeRate` is "The exchange rate between the document currency and the payment currency"; `PaymentCurrencyCode` is "A code signifying the currency used for payment in the Invoice". Both currencies are XUF, and the payment really is made in XUF into an XUF account (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`; `17-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `4862160`, in XUF), yet the rate converts XUF into XBL, a currency that is neither. The rate contradicts the payment currency in the same document (High). Refutation tried in the merge: XBL is Lumeway's home currency and the currency of its paying account (`17-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`), and the import declaration converts the invoice values at this rate (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00` = 4 790 400 × 0.01), but neither use is what the element defines: the payer's conversion is between Lumeway and its bank, and customs conversion has its own elements in the declaration. Of the 10 files with a `PaymentExchangeRate` (lxml over `*.xml`), this is the only one whose target currency differs from its own `PaymentCurrencyCode`.
- Condition: the invoice carries no payment exchange rate, or its source is the document currency and its target the payment currency stated in `PaymentCurrencyCode`, with payee account and remittance in that currency.
- Options: (a, preferred: broad, money) remove `PaymentExchangeRate`, since payment is in XUF (story unchanged); (b) make XBL the payment currency, which needs an XBL payee account and a remittance in XBL (a change of the story).
- Needs decision: no
- From: money (F1), broad (F2, Medium)

### road/15#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address in the same invoice uses `CountrySubentity` (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Recounted: 219 occurrences in 104 files.
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with a code where a list exists).
- Options: (a, preferred) move it to `CountrySubentity`, as Bayvarra does; (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no
- From: broad (F3), parties (F1), context (F4)

### road/15#F4 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats `Language/ID` and names no locale (section 6: Medium). Recounted: 364 occurrences in 213 files; the parts said 362.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales named in its listID.
- Options: (a, preferred: broad, parties) drop `LocaleCode`; (b, context's preference) `en-XB` with a locale list as listID.
- Needs decision: no (parties said yes; encoding only, as in all earlier flows)
- From: broad (F4), parties (F2), context (F5)

### road/15#F5 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance for vehicles, not a street name, and an invoice address has no use for it. Recounted: 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop the gate from the party address; (b) keep it only in delivery addresses, in a location description.
- Needs decision: no
- From: broad (F5), parties (F3)

### road/15#F6 · Medium · Lifecycle stage code MANUFACTURING for a cradle-to-gate figure
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". In the world list (checked in the merge) `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. Text and description cover A1 to A3, so the code names only part of what the figure covers.
- Condition: the lifecycle stage code and text name the same stage(s), and the figure covers exactly what they name.
- Options: (a, preferred) omit the code and keep the cradle-to-gate text (or one entry per stage with split figures); (b) keep `MANUFACTURING` and reduce figure and texts to module A3.
- Needs decision: no
- From: context (F1, High)

### road/15#F7 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `EmissionCalculationMethod/FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode`, unrelated to the load of transport equipment (semantic conformance, UBL 2.5 §4.7); 39 files do the same.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the boundary, if kept, is stated in text.
- Options: (a, preferred) drop it and state the boundary in `LifecycleStageDescription`; (b) in addition, record the missing boundary element for the UBL TC write-up.
- Needs decision: no
- From: context (F2)

### road/15#F8 · Low · Italian names and legal form tagged as English
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: the renderings carry `languageID` `en-XU` but are Italian text (the legal form with an English gloss). The parties part refuted it for the street name: English keeps foreign street names unchanged. Against that: `languageID` names the language of the content, and a legal form is not a proper name. The same Valdara street is tagged `en-XB` in the Bayvarran-issued documents of the flow (e.g. `16-ApplicationResponse.xml`). The merge cannot settle which convention the world wants; aligned with the utilities and rail merges (Low, decision). 217 such street renderings in 102 files.
- Condition: the world has one stated rule for the language tag of Urvanian names and legal forms rendered in English, and every rendering follows it.
- Options: (a, preferred) document that English renderings keep Urvanian proper names, tagged with the party's own variety; give the legal form an English rendering; (b) document the present practice as the convention.
- Needs decision: yes
- From: merge (from the parties' "Considered and refuted")

### road/15#F9 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: section 4.8: Valdara's stock-exchange listing has no part in billing; its logistics provider Castrano neither: the despatch advice is referenced, and the invoice bills the goods, not Castrano's service. Refutation tried in the merge: in the receipt advice Castrano's role is explained by these data (road/13), but in the invoice Castrano has no role at all.
- Condition: every optional party aggregate present has a reason in the invoice's purpose.
- Options: (a, preferred) leave listing and service provider out of the invoice; (b) state a reason if the story gives one.
- Needs decision: no
- From: parties (F4), context (F8, party part)

### road/15#F10 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the supplier's contact handles billing questions (accounts receivable) and the customer's contact receives and checks invoices (accounts payable); Valdara gives its order desk in Sales, Lumeway its customer service desk in Sales. Each party carries one fixed contact in every role of the flow.
- Condition: the accounting parties' contacts are their billing / accounts functions.
- Options: (a, preferred) accounts receivable and accounts payable contacts; (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F6), parties (F5), context (F7)

### road/15#F11 · Low · Catalogue and product-passport data in the invoice line
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: the invoice bills the goods; search keywords, the circularity profile and the product's emission figure (F1, F6, F7) play no part in billing or paying (section 4.8, IND5). Warranty text can belong on an invoice in some practice (as proof of purchase), but nothing in the flow refers to it. Split from the party master data of context's F8, as in the rail merges.
- Condition: item data in the invoice has a use in billing or paying.
- Options: (a, preferred) drop keyword, circularity profile and emission; (b) keep the warranty only if the story uses the invoice as warranty proof.
- Needs decision: no
- From: context (F8, item part)

### road/15#F12 · Low · Item number looks like a real GTIN-12
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- Why: the world item numbers are 12 digits with a valid GS1 mod-10 check digit (recomputed in the merge: 7 and 4), so they read as GTIN-12s in the UPC range administered by GS1 US; `771` is also a GS1 prefix (GS1 Colombia). Own knowledge of the GS1 allocation; whether the numbers are assigned could not be checked. Only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`.
- Condition: the item numbers cannot be read as validly check-digited GTINs, and both items of the scheme are described the same way.
- Options: (a, preferred) change the world item scheme's format so it is not a valid GTIN; (b) use the GS1 prefix reserved for demonstrations (952) if the scheme is meant to mimic GTIN; in either case drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role.
- Needs decision: yes
- From: broad (F7)

### road/15#F13 · Low · Invoice line 2 does not identify the substituted 2026 casting
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- XPath: `16-ApplicationResponse.xml:/ApplicationResponse/cac:DocumentResponse/cac:LineResponse/cac:Response/cbc:Description` = `Matched to the substituted 2026 casting.`
- Why: the order response replaced line 2 by the 2026 casting (VI-C180, `ExtendedID` 2026). The invoice line bills VI-C180 with the ordered description and no extension, yet Lumeway's invoice response says it matched line 2 to the substituted 2026 casting, information not in the invoice. Verified: `ExtendedID` 2026 occurs only in `02-OrderResponse.xml` in this flow.
- Condition: invoice line 2 identifies the substituted 2026 casting (e.g. `ExtendedID` 2026), consistent with the order response and the invoice response.
- Options: (a, preferred) `ExtendedID` 2026 on line 2, as in the order response; (b) a line note naming the substitution.
- Needs decision: no
- From: broad (F8), context (F6)

## Checked and consistent
- Lines (redone): 96 × 49 900 = 4 790 400 = `/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`; 12 × 5 980 = 71 760 = `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `71760`; both per 1 EA, equal to the order price (`01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900`) and the substituted price (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Price/cbc:PriceAmount` = `5980`).
- Totals (redone): 4 790 400 + 71 760 = 4 862 160 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `4862160` = `TaxExclusiveAmount` = `TaxInclusiveAmount` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160`; taxable amount the same, tax 0.
- Tax: header and both line categories `G`, 0 %, `EXP`; the seller is the exporter of record (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`) and the goods go to Bayvarra (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FinalDestinationCountry/cbc:IdentificationCode` = `XB`).
- Payment terms (redone): 2 % of 4 862 160 = 97 243.2, rounded to `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `97243`; settlement period 2026-03-24 to 2026-04-03 (10 days); due date 2026-03-24 + 30 = `/Invoice/cbc:DueDate` = `2026-04-23`, the same in `PaymentMeans` and `PaymentTerms`; penalty interest 8 % a year, simple.
- What follows: the remittance pays 4 862 160 XUF, after the discount period and before the due date, quoting `RF78VIINV260166` into the payee account given here (`17-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160`). `PaymentID` and the payee account pass `check_ids.py`.
- References: order `LD-PO-26-0149` and despatch advice `CL-DA-26-0153` resolve; quantities 96 and 12 equal the order and the despatch advice; the 13th side frame received (`13-ReceiptAdvice.xml`) is not invoiced (its settlement is road/13#F9).
- Bank identifiers `CREVXUFR`, `BLUMXBLX` cannot be real BICs: XU and XB are not ISO 3166 codes in use (own knowledge, from money).

## Considered and refuted
- `/Invoice/cbc:IssueDate`: invoice issued 2026-03-24, before the receipts showed one bench short (later withdrawn) and one side frame over, and before the goods arrived on 2026-03-25 — refuted because under FCA the seller delivers by handing the goods to the buyer's carrier on 2026-03-23, so the invoice follows the delivery and bills the despatched quantities (from broad, logistics).
- `/Invoice/cac:Delivery/cac:DeliveryParty`: a delivery without date or place — refuted because the despatch advice reference carries the delivery details and an invoice needs no more (from logistics).
- `/Invoice/cbc:TaxPointDate` = `2026-03-24`: suspected the tax point should be the day of supply (2026-03-23) — refuted because the element is "The date of the Invoice, used to indicate the point at which tax becomes applicable", and many VAT systems let the invoice date be the tax point when the invoice follows the supply within a short period; with a 0 % export nothing depends on it (from money).
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: suspected that shared charges reduce what the seller receives — refuted because SHAR means each party pays its own bank's charges; the remittance reports the amount sent (from money).
- `/Invoice/cbc:AccountingCostCode` = `4410`: suspected copied without reason — refuted because the order gave the seller this code (`01-Order.xml:/Order/cbc:AccountingCostCode` = `4410`) and the invoice returns it for the buyer's booking of the goods (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian street name tagged as English — refuted by parties; not followed, made F8.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be real — refuted because prefix 952 is reserved by GS1 for examples and the check digit is correct (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because +999 is reserved in ITU-T E.164 (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number — refuted because the definition does not say who assigns the identifier (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F3 → F1: combined; context's Medium raised to High; preferred option set to dropping factor and base, as in the rail and road 01-12 merges.
- money/F1, broad/F2 → F2: combined at money's High (the rate contradicts `PaymentCurrencyCode` in the same document, section 6); broad had Medium.
- broad/F4, parties/F2, context/F5 → F4: parties' "Needs decision: yes" set to no; count corrected to 364.
- context/F1 → F6: High lowered to Medium, aligned with the rail and road 01-12 merges.
- context/F8 split: party data → F9 (with parties/F4), item data → F11.
- broad/F6, parties/F5, context/F7 → F10: combined.
- broad/F7 → F12: preferred option reworded (format change), aligned with the rail and plastics merges.
- broad/F8, context/F6 → F13: combined.
- F8 added by the merge (from a refutation of the parties part not followed).
