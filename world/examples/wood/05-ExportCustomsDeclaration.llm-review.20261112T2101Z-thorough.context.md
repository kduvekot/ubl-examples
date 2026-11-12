# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/05#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/05#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:ID` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/05#F3 · Low · The supporting document is the order, not the commercial invoice
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `/ExportCustomsDeclaration/cbc:IssueTime` = `09:25:00`
- XPath: `08-Invoice.xml:/Invoice/cbc:IssueTime` = `08:56:00`
- Why: The declared customs value (34 560.00 XBL) and the transaction are evidenced by the commercial invoice, which the exporter had issued half an hour before this declaration (both on 2026-02-26). The declaration refers instead to the buyer's purchase order, by ID only and without a document type, and does not refer to the invoice at all.
- Condition: The declaration refers to the commercial invoice it is based on, and every reference says what kind of document it is.
- Options: Preferred: refer to MS-INV-26-0635 with its document type (keeping the order reference if the world's customs require it).
- Needs decision: no

### wood/05#F4 · Low · The customs authority is described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The customs authority is a public administration (its ISIC code is 8411, General public administration activities). `CompanyLiquidationStatusCode` is "the party's liquidation status" and `CorporateRegistrationTypeCode` "the type of this registration scheme": a public authority is not registered as a company in a commercial register and cannot be in liquidation, so "Active, not in liquidation" and "Commercial register" do not fit the kind of party.
- Condition: The authority's `PartyLegalEntity` carries no liquidation status and no commercial-register scheme; it is either absent or describes the authority's legal basis as a public body.
- Options: Preferred: drop `PartyLegalEntity` for public authorities (the declaration does not need it). Alternative: a registration scheme for public bodies, if the world has one.
- Needs decision: no

### wood/05#F5 · Low · The signature ID contains the name of the example flow
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `MS-SIG-EX-wood`
- Why: `Signature/ID` is "An identifier for this signature", assigned in the world by the signing party. Its last part `wood` is the name of the example flow in this repository, not a number a trader or customs system would assign; the other signatures of the flow have world-style IDs (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Signature/cbc:ID` = `VI-SIG-26-RFQ`). The pattern occurs in 14 examples (`grep -rlE --include='*.xml' 'SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: The signature ID follows the signing party's own numbering and contains nothing from the repository's structure.
- Options: Preferred: number signatures like the other documents of the party (e.g. year and running number).
- Needs decision: no

### wood/05#F6 · Low · `Shipment/GrossWeightMeasure` equals the goods' gross weight
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", while the goods item's gross weight is "including packing and packaging but excluding the carrier's equipment". Both carry the same 21600 kg, so the shipment value is the goods weight and does not meet the shipment definition (the truck's trailer is the transport equipment). The value of the goods (4800 slats of 1.8 × 0.095 × 0.038 m = 31.2 m³, i.e. about 690 kg/m³ including bundling and pallets, plausible for kiln-dried ash or oak) fits the goods item, not the shipment.
- Condition: `Shipment/GrossWeightMeasure` either includes the transport equipment (and so exceeds the goods' gross weight) or is absent.
- Options: Preferred: drop the shipment gross weight and keep it on the goods item (and the consignment) where its definition fits. Alternative: add the trailer's tare.
- Needs decision: no

### wood/05#F7 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the exporter's contact is the one customs asks about the export (shipping or customs clerk); the consignee's contact receives the goods. A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/05#F8 · Low · Party master data this document does nothing with
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[2]/cbc:Name` = `Thickness tolerance`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:TestMethod` = `Oven-dry method on samples from each kiln charge`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. An export declaration needs the parties' identities and the goods' classification, value, origin and quantity; the commercial specification of the slats (thickness tolerance, test method of the moisture content, standard property identifier) is also carried and does nothing for customs. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

### wood/05#F9 · Low · A validity period on the property "Planed on four sides"
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A surface that has been planed on four sides stays planed; nothing in the document says what would stop the property being valid after 12 months, or from when the months are counted. The property that does change over time is the moisture content (`AdditionalItemProperty[1]`), which carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with a reason the document makes clear, or it is absent.
- Options: Preferred: drop it from the surface property. Alternative: if the world needs one, move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no

## Checked and consistent
- Shipment `MS-SH-26-0632` and consignment `MS-CS-26-0629` are the same as in `04-TransportExecutionPlanRequest.xml` and `06-DespatchAdvice.xml`.
- The carrier is the haulier the transport was requested from (Trasvia Haulage); its permit is relevant to the authority here.
- The note "Declared electronically before the goods leave" agrees with the issue time and the exit office being the Bayvarran border post.
- HS 440799 with NatureCode IX (HS section IX, wood) agree.

## Considered and refuted
- The forestry certificate on the item: refuted as copied data — timber regulations commonly require proof of legal and sustainable harvest at the border.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `90`: suspected filler — refuted because an export declaration is commonly valid for a limited period within which the goods must exit.
