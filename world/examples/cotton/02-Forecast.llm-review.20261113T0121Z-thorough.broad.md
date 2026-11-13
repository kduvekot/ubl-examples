# LLM review: 02-Forecast.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/02-Forecast.xml`, Git blob `564d177fc853a93d7bb7f285f6471573cea2ed35` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/02#F1 · High · Forecast cites a classing certificate signed eighteen days after the forecast
- XPath: `/Forecast/cbc:IssueDate` = `2026-02-02`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: the forecast is issued on 2 February and describes demand for a period starting 16 February, but it attaches to the item a cotton-classing certificate whose signature is dated 20 February, with measured results (grade, staple, micronaire) of a specific lot. Seed cotton was only delivered to the gin on 5 February (`03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`) and ginned from 7 to 22 February (`10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:StartDate` = `2026-02-07`). A document cannot carry a certificate that does not exist yet, and a forecast of future supplies has no classed lot to certify.
- Condition: the forecast carries no certificate dated after its issue time; any quality requirement for the forecast quantity is stated as a requirement (grade, staple), not as a lot certificate.
- Options: (preferred) drop the `Certificate` from the forecast item and keep the grade and staple properties; or, if the mill forecasts against a lot already classed, give it a certificate issued before 2 February.
- Needs decision: no

### cotton/02#F2 · Medium · Language code in `LocaleCode`
- XPath: `/Forecast/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used". `en` with `listID` "ISO 639" is a language code and repeats `Language/ID`; it names no locale (a region or country where the language is used). The same value occurs in 213 of the 250 examples (`grep -l --include='*.xml' -r '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: `LocaleCode` is absent or holds a locale code from a list of locales (e.g. language plus region) that differs from the language identifier.
- Options: (preferred) drop `LocaleCode` where it only repeats the language; or use a locale list (e.g. a BCP 47 tag such as `en-XB`) with its own `listID`.
- Needs decision: no

### cotton/02#F3 · Low · Purchasing contact described as a sales customer-service officer
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the mill sends the forecast as buyer; its contact is named "Purchasing" but is placed in the sales department with a customer-service title. Name, department and title contradict each other.
- Condition: the buyer's contact has a name, job title and department that agree and fit a buyer.
- Options: (preferred) department "Purchasing" and a buyer's job title; or a sales contact under another name, if the forecast really comes from sales planning.
- Needs decision: no

### cotton/02#F4 · Low · The ginnery's English address is tagged as Bayvarran English
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: here the English names of the ginnery's Lisavan address carry `languageID="en-XB"` (English as used in Bayvarra); in the ginnery's own documents (01, 03, 04, 10, 11, 12, 16) the same names carry `en-XL`. The text is the same, so the tag follows the sender rather than the address. The item description and name are also tagged `en-XB` here and `en-XL` in 10, 11 and 16. Seven examples of the flow use `en-XB` for these renderings (`grep -l 'en-XB' world/examples/cotton/*.xml`).
- Condition: the same rendering of the same address (and of the same item text) carries the same language tag in every example.
- Options: (preferred) tag the English forms of Lisavan addresses `en-XL` everywhere, because the rendering belongs to the address; or use plain `en` throughout.
- Needs decision: no

### cotton/02#F5 · Low · Classing results in the applicant's remarks
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for this certificate". The text is the classer's result, signed by the chamber's classer, not a remark of the applicant.
- Condition: the classing result is not carried as an applicant's remark (or the remark is really the applicant's).
- Options: (preferred) keep the results in the item properties (grade and staple are already there) and drop the remark; or move them to the certificate's own description, if the model offers one.
- Needs decision: no

### cotton/02#F6 · Low · Origin area in `Region` here, in `District` in the farm's address
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". The north coast is a part of Lisavu that the farm's address places in `District` ("The district or geographical division of a country or region"). The same area is put in two different elements.
- Condition: the north coast of Lisavu is carried in the same address element in the item's origin and in the farm's address.
- Options: (preferred) `District` in both, because it is a division of one country; or `Region` in both, if the north coast is a recognised economic region of the island.
- Needs decision: no

### cotton/02#F7 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count; 227 is the bale's weight in kilograms, as the description says ("compressed bales of about 227 kg"). `PackQuantity` 1 EA ("the number of subunits making up this item") adds nothing.
- Condition: the bale weight is not carried as a count of items, and the pack data say what a pack contains in units that fit the element.
- Options: (preferred) drop both elements and keep the bale weight in the description (or as an item property with a weight unit); or state the pack size as a count only if the item is defined per kilogram and that is made explicit.
- Needs decision: no

### cotton/02#F8 · Low · Tax registration of the sender in a forecast
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: a forecast carries no amounts and no taxes; the mill's state sales-tax registration has no use here and looks copied from master data.
- Condition: the forecast carries no tax registration of its parties, or a reason in the document for carrying it.
- Options: (preferred) drop `PartyTaxScheme` from the forecast's parties.
- Needs decision: no

## Checked and consistent
- The forecast revision 07 revises this forecast: `07-ForecastRevision.xml:/ForecastRevision/cac:OriginalDocumentReference/cbc:ID` = `LTM-FC-26-0192`, with matching source issue date and time (2026-02-02, 09:00:00).
- Staple length 28.6 mm equals 1-1/8 inch (28.575 mm), as in the certificate remark.
- 24000 kg is about 106 bales of 227 kg; as a forecast quantity it need not be a whole number of bales.
- Parties: the mill (20412603) and the ginnery (IC42681) are described with the same identifiers, register and legal data as in 01, 08 and 16.

## Considered and refuted
- `/Forecast/cbc:BasedOnConsensusIndicator`: consensus in a one-sided forecast — refuted: the forecast is shared with the supplier under a season agreement; consensus is plausible.
- `/Forecast/cac:AdditionalDocumentReference/cbc:ID`: the ginnery's season agreement with the farms in the mill's forecast — refuted only partly; the mill may know the reference, but the reference has no type or description. Not raised: an ID-only reference to an external agreement is readable.
- `/Forecast/cac:SenderParty/cbc:IndustryClassificationCode`: a weaving mill (ISIC 1312) buying raw lint — refuted: an integrated mill spins and weaves; the code is a plausible main activity.
