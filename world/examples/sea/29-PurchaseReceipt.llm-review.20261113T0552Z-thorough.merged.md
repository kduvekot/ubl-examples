# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/29#F1 · High · Emission value, factor and base do not agree (96 kg vs 0.82 × 1 EA)
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", and `ValueBaseMeasure` "The base quantity to which the value factor applies". Factor × base = 0.82 × 1 EA = 0.82, not the stated 96 kg CO2e (recomputed). Neither the bench's weight nor its material gives 96 with this factor either (96 / 0.82 = 117.1; 0.82 × (34 + 22.5) kg = 46.3 kg). The same triple occurs in 39 files (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples`).
- Condition: Where factor and base are given, factor × base = value.
- Options: (a) preferred: drop factor and base (the value is a cradle-to-gate figure per bench from the manufacturer's LCA); (b) a real factor with its base (e.g. per kg of steel) that gives 96.
- Needs decision: no
- From: added by the merge (no part raised it in 29), aligned with sea merges a/c, retail, road, rail

### sea/29#F2 · Medium · "Services outside scope of tax" used for a sale of goods
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: UNCL 5305 code O is "Services outside scope of tax" (listing; in UNCL 5305 "taxes are not applicable to the services"). The receipt sells two park benches, and the same tax category states `SupplyTypeCode` GOODS, so code and supply type contradict each other. Lisavu has no general sales tax, so the sale is indeed outside any tax, but the code names services. EN 16931 uses O for any supply not subject to VAT; under the agreed semantic-conformance rule that practice does not make the code fit (context only). The tax scheme is named "No general sales tax" without an identifier, a scheme that consists of the absence of tax. O with GOODS occurs in 5 files (cotton 01, 04, 05, 16, sea 29; money and context, parsing `ClassifiedTaxCategory`).
- Condition: A goods supply outside the scope of tax carries a category whose meaning covers goods (or no category), decided once for every Lisavan goods sale; or the use of O for goods is recorded as a deliberate deviation in the code-list decisions.
- Options: (a) preferred: decide at project level (a world code or documented exception for "outside the scope of tax" for goods, recorded in `analysis/codelist-decisions.md`); (b) keep O and add the case to the findings on EN 16931 practice; (c) leave tax category and tax total out of Lisavan receipts, which needs a decision under the "nothing implied by absence" rule; (d) give Lisavu a real scheme with an identifier.
- Needs decision: yes
- From: broad (F1), context (F1), money (F1)

### sea/29#F3 · Medium · An emission boundary code in an element for the fullness of transport equipment
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value is a system-boundary code ("Cradle to gate", list `EmissionBoundaryCode`) for a product footprint; no transport equipment is involved. A code from another list in this element (39 files carry it).
- Condition: `FullnessIndicationCode` is absent or states the fullness of transport equipment.
- Options: (a) preferred: drop it (the boundary is stated in `LifecycleStageDescription`); note for the TC write-up that UBL 2.5 has no element for the system boundary.
- Needs decision: no
- From: added by the merge (no part raised it in 29), aligned with sea merges a/c and retail

### sea/29#F4 · Medium · Lifecycle stage "Manufacturing" for a cradle-to-gate figure that starts at the mine
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". The code says manufacturing (EN 15804 A3), while the description and `Description` ("Mining, steel making, casting, galvanising, sawing and the transport between them") cover raw-material supply, transport and manufacturing (A1–A3). Code and text equivalent disagree (own knowledge of EN 15804 stages).
- Condition: The code covers the stages the description names, or the description is narrowed to the code.
- Options: (a) preferred: a code for the product stage A1–A3 (cradle to gate) from the world's list, or drop the code and keep the description; (b) narrow the figure to manufacturing only.
- Needs decision: no
- From: added by the merge (no part raised it in 29), aligned with sea merges a/c, retail, road, rail

### sea/29#F5 · Low · Catalogue data and search keywords on a till receipt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: A purchase receipt is "A receipt for a purchase made with cash or cash equivalents". `Keyword` is "A keyword (search string) for this item, assigned by the seller party", which means nothing on a receipt for a completed sale (broad, context). The merge extends the finding to the rest of the catalogue data on the line: the emission figure, the resource consumption and waste of the circularity profile, the load test with its standard and issuer, and the Urvanian national tariff code (a Lisavan retail sale uses no Urvanian tariff). They are product master data copied into a document that does not use them (section 4.8). Counter-arguments carried: warranty, fixing and maintenance information serves the buyer of a retail sale (broad, context refuted those); retail's merge noted that a consumer may be given footprint and repairability data; and the world has no Lisavan tariff list.
- Condition: The receipt's item carries what the buyer of the sale uses (name, identification, warranty, maintenance), not search strings or full catalogue data without a stated reason.
- Options: (a) preferred: drop the keywords, the emission, the resource and waste data, the load test and the XU tariff code; keep warranty, anchors and maintenance; (b) keep the footprint and repairability with a stated reason (e.g. a Lisavan disclosure rule).
- Needs decision: no
- From: broad (F5), context (F2, part); extended by the merge

### sea/29#F6 · Low · The farm's master data on a receipt for goods it collected itself
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[2]/cbc:Line` = `Farm track off Plantation Road at kilometre 4, past the cotton fields.`
- Why: The farm collected the benches itself ("Collected by the farm with its own trailer"), so nothing is delivered to its address; still the receipt carries its address with driving directions, coordinates, the physical location of its cotton fields, a contact and legal-entity data. Naming a business customer on a receipt (for its accounts) needs its name, identifier and perhaps its address once.
- Condition: The receipt carries the customer data a business customer needs on a receipt and no location data the sale does not use.
- Options: (a) preferred: keep identifier, name and structured address; drop coordinates and physical location.
- Needs decision: no
- From: context (F2, part)

### sea/29#F7 · Low · The farm's address lines repeat the structured address and mix two languages in one line
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: `AddressLine` is "a single address line expressed as unstructured text", and its `Line` may be repeated only to give the same content in several languages. The four lines repeat the structured street, description, district and town, and lines 1 and 4 put the Lisavan and English names into one line without `languageID`. The address is given twice, once structured and tagged, once unstructured in mixed languages.
- Condition: The address is given structured or in address lines, and each line is in one language (tagged where needed).
- Options: (a) preferred: drop the address lines; (b) one rendering per language without repeating the structured parts.
- Needs decision: no
- From: parties (F3)

### sea/29#F8 · Low · The point of sale named by company and street
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Velumi Trading, Reef Street, Selanu`
- Why: `PointOfSaleLocation` is "The location of the point of sale where this purchase took place"; a location's name is the place, not the company, and street and town belong in the location's address. The value strings together the seller's name and part of its postal address, which the supplier's address already gives; the shop or counter where register `T1` stands is not named.
- Condition: The point of sale is named as a place (shop or trade counter), its address, if needed, in `Location/Address`.
- Options: (a) preferred: a place name such as "Trade counter" with the address in `Address` if it differs from the party's; (b) drop the name and keep the cash register only.
- Needs decision: no
- From: broad (F3), context (F3), logistics (F1), parties (F4)

### sea/29#F9 · Low · The contacts' names, job titles and departments disagree with the roles
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Farm office`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi sells here, but its contact is named Purchasing (a customer service officer in Sales), the buying function. The farm's office is placed as a customer service officer in a Sales department, which a one-person farm buying two benches hardly has.
- Condition: Each contact's name, job title and department agree and fit the party's role (seller's sales counter; the farm's office).
- Options: (a) preferred: Velumi's sales counter or customer service; the farm office without sales title and department; (b) drop title and department where the functional name suffices.
- Needs decision: no
- From: broad (F4), parties (F2)

### sea/29#F10 · Low · The seller's customs trader number in a retail receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: The receipt records a domestic card sale of two benches on the island; Velumi's customs trader number plays no part in it (copied master data, section 4.8).
- Condition: The seller carries only the identifiers the receipt uses.
- Options: (a) preferred: drop the customs trader identifier.
- Needs decision: no
- From: parties (F5)

### sea/29#F11 · Low · Benches bought for the port sold "from stock" to a farm
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description[2]` = `The Serra park bench from Velumi Trading's stock, imported from Bayvarra, for island customers.`
- XPath: `22-Invoice.xml:/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- XPath: `22-Invoice.xml:/Invoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The 96 benches of the flow were ordered, invoiced and booked for the Port of Selanu (originator and beneficiary in order, invoice and statement; cost centre "Stock for municipal projects"). The receipt sells two Serra benches "from Velumi Trading's stock, imported from Bayvarra" three weeks later. Either they come from other stock, which nothing shows, or two of the port's benches went to a farm. Counter-arguments: the money part refuted a related suspicion (a trader may sell from its stock to other customers; the maker's trade-only conditions govern Lumeway's sales), and the context part put the stock question under "Outside this review". The merge cannot settle whether the flow implies a contradiction.
- Condition: The flow makes clear where the two benches come from.
- Options: (a) preferred: say in the description or a note that they are from general stock; (b) adjust the order (e.g. 98 benches, 96 for the port).
- Needs decision: yes
- From: broad (F2); context (Outside), money (considered and refuted, related)

### sea/29#F12 · Low · The cotton farm in a commercial companies register with a yearly expiring registration
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: Lisavu Cotton Farm is a sole proprietorship growing cotton (ISIC 0116). Its legal entity places it in the "Island companies register" of type COMMERCIAL, although the world's CorporateRegistrationTypeCode list has `FARM` (parties: the list holds COMMERCIAL, CHARITY, ASSOCIATION, FARM; only COMMERCIAL occurs, 633 times over `*.xml`). `RegistrationExpirationDate` is "the date upon which a registration expires (e.g., registration for an import/export license)"; an entry in a companies register does not expire at year end, a yearly farm registration would. The description is identical in `cotton/01-SelfBilledInvoice.xml`.
- Condition: Register, type code and expiration date describe one register in which such a registration exists and expires.
- Options: (a) preferred: a farm register with type `FARM`, keeping the yearly expiry; (b) keep the companies register and drop the expiration date.
- Needs decision: yes
- From: parties (F1)

### sea/29#F13 · Low · Tax category O with a percent of 0
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Category O means no tax applies, so there is no rate; a percent of 0 states a rate for a tax that is not applicable (IND6).
- Condition: An outside-scope category carries no percent.
- Options: (a) preferred: drop `Percent` (whatever F2 decides about the code).
- Needs decision: no
- From: added by the merge (no part raised it), aligned with cotton, utilities, road

### sea/29#F14 · Low · The bench's GTIN lies in Lumeway's company prefix, the brand is Valdara's
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Valdara`
- Why: GTINs are allocated by the brand owner from its own GS1 company prefix (own knowledge of the GS1 rules). The bench is a Valdara product (brand Valdara, manufacturer `XU-R-104274`), but its GTIN starts with `9520610`, the prefix of Lumeway's GLN `9520610900008` (`22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`). Check digit valid (`check_ids.py`).
- Condition: The GTIN comes from the brand owner's prefix, or the world states why the distributor allocated it.
- Options: (a) preferred: a GTIN from Valdara's own prefix everywhere; (b) record that Lumeway, as importer, allocated it.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail a/b/c

### sea/29#F15 · Low · World item number with a valid GS1 check digit
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: The world item number (`schemeID` `urn:ubl-examples:world:item`) is 12 digits with a valid GS1 (UPC-A) check digit (recomputed: 3 × (7+1+2+0+0+2) + (7+0+0+0+0) = 43, check digit 7 = last digit), so it reads as a real GTIN-12, which the rule "fictional values must not be mistaken for real ones" excludes. The merge could not check the real GS1 register. 39 files carry it.
- Condition: The world item number cannot be mistaken for a real GTIN, or the GS1 registers are checked and record it as unassigned.
- Options: (a) preferred: a format that is not a valid GTIN; (b) check and record it in the sources.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail a/b/c, rail, road, plastics

## Checked and consistent
- Arithmetic (recomputed): 2 × 289 = 578.000 XLC = line extension = tax exclusive = tax inclusive = payable = paid amount; tax 0.000; tax-inclusive price = price.
- Card payment: debit card (UNCL 4461 code 55) agrees with card type DEBIT; approved at 10:25, the transaction and issue time; issuer `BSELXLSL` (Bank of Selanu, Velumi's bank in `27-RemittanceAdvice.xml`); holder the farm; PAN masked; merchant ID carries Velumi's register number.
- Price plausibility: purchase 49920.00 / 96 = 520.00 XBL = 208.000 XLC at 0.4, plus a freight and insurance share of about 12.7 XLC, about 221 XLC landed; 289 XLC is a plausible margin (money, context).
- Physics: two benches of 1800 × 620 × 780 mm and about 41.5 kg gross each fit a farm trailer (logistics, broad); the farm's coordinates lie about 2.4 nm from the Port of Selanu, on the island (logistics).
- Sale on 2026-06-13, after receipt at Nalevi on 2026-05-21 (`21-ReceiptAdvice.xml`); "imported from Bayvarra" agrees with `14-BillOfLading.xml` and `19-ImportCustomsDeclaration.xml`.
- Velumi and the farm are described as in their other documents (parties, compared with a script; the farm identical to the cotton flow); Lisavan and English renderings carry `qal` and `en-XL`; GTIN passes `check_ids.py` (re-run).

## Considered and refuted
- `/PurchaseReceipt/cbc:Note[2]` = `Collected by the farm with its own trailer.`: two benches on a farm trailer — refuted: about 83 kg and 1.8 m length fit easily (from broad).
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`: master data copied into a receipt — refuted because the receipt is the buyer's proof of purchase for a warranty claim (from broad, context).
- `/PurchaseReceipt/cbc:ProfileExecutionID` = `SEA-2026-01`: the retail sale under the shipment's execution ID — refuted because every document of the flow shares it and the receipt sells goods from this shipment (from context).
- `/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:HolderName` = `LISAVU COTTON FARM`: a company as cardholder — refuted because business debit cards are issued in a company's name (from context).
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `2`: conflict with the maker's conditions (`21-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`) — refuted because those govern Lumeway's sales to traders, not Velumi's resale (from money).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Description`: driving directions in a postal address — refuted because the element is clarifying text for the address, and a farm on a track is found by it (from parties).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode`: a liquidation status for a sole proprietorship — refuted because a registered business can be wound up (from parties).

## Changed in the merge
- money/F1 → F2: Low → Medium, aligned with broad, context and the cotton merges (a code whose meaning does not fit the element's use); needs decision yes as all parts said.
- context/F2 → F5 and F6: split into the item's catalogue data (with broad/F5) and the farm's master data; F5 extended by the merge to the emission, circularity, load-test and tariff data on the line.
- context's "Outside this review" note on the stock and broad/F2 → F11 (Low, yes), with money's related refutation as counter-argument.
- F1, F3, F4, F13, F14, F15: added by the merge (verified against the XML; no part raised them in 29), to align with the other sea merges and the earlier flows where the same item data occurs.
