# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/05#F1 · Medium · Province of Urvanian addresses in Region
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country … such as the name of its county, province, or state", i.e. `CountrySubentity` (+ code), as the Bayvarran addresses of the flow do (`Coastal State`). No `languageID`, unlike the other parts of these addresses. 219 occurrences in 104 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; where given, it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) drop where the postal code identifies the place; (c) keep only if Ferrano is an economic region, recorded.
- Needs decision: no
- From: broad, parties, context

### plastics/05#F2 · Medium · Goods item quantity is a weight, and packages and net mass are not declared
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `120480`
- Why: `GoodsItem/Quantity` is "The number of units making up this goods item". The value is 120 `TNE`, a mass, while the units of this goods item are 120 jumbo bags (item description "in jumbo bags of 1 tonne"; `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`). The net mass, which an export declaration needs next to the gross mass, is not in `NetWeightMeasure`, and the number and kind of packages, a standard item of a customs declaration (own knowledge of customs practice), are not declared at all. The import declaration of the same goods uses the tariff-quantity element for the mass (`09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsTariffQuantity` = `120000`).
- Condition: `Quantity` holds a count of units (or is absent), the net mass (120 000 kg) is in `NetWeightMeasure` (or a tariff quantity), and the 120 jumbo bags are declared (package count and type), consistent with 06 and 09.
- Options: (a) `NetWeightMeasure` = 120000 KGM, a `ContainingPackage` (type JB, 120), and `Quantity` dropped or expressed in bags (preferred); (b) move the tonnes to `CustomsTariffQuantity`, as 09 does, and add the packages.
- Needs decision: no
- From: logistics

### plastics/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language, already in `Language/ID`. All 362 `LocaleCode` elements, in 213 of the 250 XML examples, carry this value.
- Condition: a locale such as `en-XB` from a locale list named in `listID`, or no `LocaleCode`.
- Options: (a) drop it (preferred); (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### plastics/05#F4 · Medium · Customs administration described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyIdentification/cbc:ID` = `XU-R-105507`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CustomsParty` is "The Authority who processes this Customs Declaration": the Customs Administration of Urvania, a public body (ISIC `8411`). Its legal entity says it is registered in the commercial register (type `COMMERCIAL`) and gives a company liquidation status ("A code signifying the party's liquidation status", `ACTIVE`). A state administration is established by law, not entered in a commercial register, and cannot be liquidated like a company (checklist). Its identifier and `CompanyID` use the commercial-register scheme (`urn:ubl-examples:world:XU:register`) for the same reason. The values contradict the party's own classification as public administration.
- Condition: the customs authority's legal entity carries no company liquidation status and no commercial-register registration; if it is identified, the identifier comes from a scheme for public bodies.
- Options: (a) reduce the legal entity to the registration name (or drop it) and identify the authority by a public-body scheme (preferred); (b) if Urvania registers public bodies, use a register of another type than `COMMERCIAL` and drop the liquidation status.
- Needs decision: no
- From: broad, parties, context

### plastics/05#F5 · Low · Italian text tagged as English
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- Why: these `en-XU` renderings are Italian ("Via del Riciclo", "Recycling street"; "Banchina del Fiume", "River quay"; "Valico di Confine", "Border crossing") and the legal form is Italian with an English gloss, while Bayvarran streets are English. 101 of the 250 XML examples show the pattern (parties part). Counter-argument (the broad and context parts refuted the same candidate in `01-Order.xml`): Italianate exonyms are the world's convention for Urvanian names in English. The merge cannot settle it for street names; the legal form is a description, not a name, and is the stronger case.
- Condition: every rendering tagged `en-…` is English or a proper name used as such in English, and the convention is recorded in the world story if meant.
- Options: (a) record the convention and render the legal form in English (preferred); (b) translate all renderings; (c) drop the second rendering where the local form suffices.
- Needs decision: yes
- From: parties

### plastics/05#F6 · Low · All three companies registered on 1 January 1996
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Three companies in two registers share New Year's Day 1996; 271 occurrences in 181 of the 250 XML examples (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`). A default value (IND5) unless the story explains it.
- Condition: individual registration dates, or the shared date explained in the world's history, or the element absent.
- Options: (a) individual dates (preferred); (b) record a general (re-)registration in the story; (c) drop where no history is known.
- Needs decision: yes
- From: broad, parties, context

### plastics/05#F7 · Low · Exporter's and consignee's contacts do not fit the customs roles
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: customs contacts the exporter about the declaration (shipping or customs), not sales customer service; the consignee's sales order desk has no role toward the Urvanian customs. The parties carry one generic contact in every document of the flow.
- Condition: each contact handles the task the party has in this document, or is absent.
- Options: (a) role-specific contacts (preferred); (b) drop contacts the declaration does not need (the consignee's in particular).
- Needs decision: no
- From: broad, parties, context

### plastics/05#F8 · Low · Rinova's waste-recovery permit in an export declaration for a product
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: the permit (Basel Annex IV R3) is irrelevant for the export of a product (HS 390110), and in an export declaration it could suggest a transboundary waste shipment, which would need its own procedure. It is in 14 XML examples, all 11 of this flow: master data copied into every document (IND5).
- Condition: the permit does not appear in the export declaration, unless the declaration acts on it.
- Options: (a) remove it (preferred); (b) if the recycled-content claim is to rest on it, tie it to the item's certificate.
- Needs decision: no
- From: broad, parties, context

### plastics/05#F9 · Low · No mode or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `RR-SH-26-0889`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`
- Why: the goods leave by barge through a river border post, but the declared shipment has no shipment stage: no mode of transport (inland water, `8`) and no identity of the barge (`Fiumella IV`, in 04 and 06), which export declarations normally carry so that the exit office can match goods and vessel (own knowledge of customs practice). The carrier is named, the vessel is not.
- Condition: the declared shipment states the mode and means of transport at the border, matching 04 and 06, or the story says why the exit office does not need them.
- Options: (a) add a main-carriage `ShipmentStage` with `TransportModeCode` 8 and the barge (`TransportMeans/MaritimeTransport` with name and ID as in 06) (preferred); (b) the mode only.
- Needs decision: no
- From: broad, logistics

### plastics/05#F10 · Low · Export value includes the freight beyond the export border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9984000`
- XPath: `09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:FreeOnBoardValueAmount` = `98046.00`
- Why: the declared value is the full `CPT` price (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000`), which includes the barge to the river quay in Lumeport (`07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `179400`). Export values for customs and statistics are normally taken at the export border (FOB/FCA-type; own knowledge of EU and WCO practice). The import side of the flow splits the freight off: 98 046.00 `XBL` = (9 984 000 − 179 400) / 100 (recomputed in the merge, at the 100 `XUF` = 1 `XBL` rate of the examples). Counter-argument (broad part, which refuted it): the world's export valuation rule is not visible, and declaring the invoice value is common practice for export statistics. The merge cannot settle which rule the world applies, so it stays Low with a decision.
- Condition: the export customs value follows a stated valuation basis, consistent with the FOB value used in 09 (the price at the border, or a documented rule that the full `CPT` price is declared).
- Options: (a) declare the value at the border (the price less the transport beyond the river border) (preferred: how real export declarations value goods); (b) keep the full price and record the Urvanian rule in the world.
- Needs decision: yes
- From: money (broad refuted it)

### plastics/05#F11 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8, recomputed in the merge), so it has the form of a GTIN-12 (UPC-A) and could be taken for a real one although its scheme is the world's own (same value in `01-Order.xml`). Whether it is assigned could not be checked.
- Condition: the number cannot be mistaken for a real GTIN, or it is verified as unassigned and the verification documented.
- Options: (a) a non-GTIN format for world item numbers (preferred); (b) document the verification.
- Needs decision: yes
- From: broad

### plastics/05#F12 · Low · Chamber of commerce as issuer of a recycled-content certificate
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: `EnvironmentalCertificate/IssuerParty` is "The authorised Organisation who issues this Certificate". In the world the Ferrano Chamber of Commerce issues certificates of origin and ATA carnets (`road/06-CertificateOfOrigin.xml`, `carnet/01-GoodsItemPassport.xml`); recycled content is normally certified by an accredited certification body or the environment authority supervising the plant (own knowledge, e.g. EN 15343 / ISO 14021). The remark reads like an origin statement, which would fit the chamber, but the type is `RECYCLED`.
- Condition: the issuer of the recycled-content certificate is an organisation the world authorises to certify recycled content, or the world states why the chamber does so.
- Options: (a) a certification body or the Urvanian environment authority as issuer (preferred); (b) keep the chamber and record its role in the world story.
- Needs decision: yes
- From: parties, context

### plastics/05#F13 · Low · Consignee's bank account in an export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". An export declaration by Rinova to the Urvanian customs involves no payment to or from the foreign consignee; its account at a Bayvarran bank is copied master data (section 4.8). It appears in 14 XML examples.
- Condition: the consignee party in the export declaration carries no financial account.
- Options: (a) drop it (preferred).
- Needs decision: no
- From: broad, money, parties, context

### plastics/05#F14 · Low · Customs authority's VAT registration copied into the declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: the authority's own VAT registration plays no part in a declaration it processes (it neither supplies nor buys anything here): data copied from master data into a document that does not use it (section 4.8). Counter-argument (broad part, which refuted it): public bodies can be VAT-registered. The merge agrees that the registration is possible, which is why this is not part of F4, but that does not give it a use in this declaration.
- Condition: the customs party carries no `PartyTaxScheme` in this declaration, unless the declaration uses it.
- Options: (a) drop it (preferred); (b) keep it only with a reason in the document.
- Needs decision: no
- From: parties (broad refuted it)

### plastics/05#F15 · Low · Reference to the order with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `RP-PO-26-0882`
- Why: `AdditionalDocumentReference` is "A reference to additional documents relevant or related to this customs declaration". With no document type, customs cannot tell that `RP-PO-26-0882` is the buyer's order (`01-Order.xml`) rather than a contract, invoice or licence. The order is the commercial document available at declaration time (the invoice `10-Invoice.xml` is issued 2026-04-20, after this declaration).
- Condition: the reference states what it refers to (a document type code or description identifying the order).
- Options: (a) add `DocumentTypeCode` (e.g. the world's UBL document type code for an order, as 06 and 11 use that list) and the issue date (preferred); (b) `DocumentDescription`.
- Needs decision: no
- From: broad, logistics, context

### plastics/05#F16 · Low · Signature ID contains the example flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `RR-SIG-EX-plastics`
- Why: `Signature/ID` is "An identifier for this signature". The value ends in `plastics`, the name of the example flow in the repository, not something the signatory would assign; it reads as a generator artefact. Signature IDs ending in a lower-case flow name occur in 14 XML examples (`grep -rlE --include='*.xml' -- '-SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: the signature ID is an identifier the signatory could assign, without reference to the example flow.
- Options: (a) derive it from the declaration number or the party's own numbering (preferred).
- Needs decision: no
- From: broad, context

## Checked and consistent
- Consignment `RR-CS-26-0885`, shipment `RR-SH-26-0889`, carrier Fiumella Barges, gross weight 120 480 kg, 120 t, HS 390110, origin XU agree with 03, 04, 06 and 08 (and 09 for the shipment).
- Shipment gross weight equal to the goods-item gross weight: correct, since no transport equipment is declared (bags loose in the barge hold).
- Declared value 9 984 000 XUF = order and goods invoice total (01, 10) (but see F10 on the valuation basis).
- The export underpins the zero-rating of the goods invoice (`10-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`); exporter and seller are the same party. Currency `XUF` here and `XBL` in 09 at 100 `XUF` = 1 `XBL`, the rate of the exchange-rate aggregates of the other examples.
- Export type permanent, reason sale; exporter, consignor and signatory Rinova (customs-trader ID `XU-TR-104548`), consignee Rivermouth, carrier Fiumella, Customs Administration of Urvania (ISIC 8411): fit an export lodged by the exporter.
- Timeline within the flow: declared 2026-04-19 16:08, after loading (13:30) and before the exportation event 2026-04-20 16:00 (04, 06).
- HS 390110, density 0.92 g/cm³ and section VII are consistent. `check_ids.py`: the IBAN-like account passes.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: the declared value includes carriage beyond the border — refuted by broad (valuation rule not visible; invoice value is common for statistics). The merge cannot settle it; kept as F10 with "Needs decision: yes". (from broad)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID`: VAT registration of a customs administration — refuted by broad: public bodies can be VAT-registered. The merge agrees on that point but keeps F14 on another ground (no use in this document). (from broad)
- `/ExportCustomsDeclaration/cbc:Note[2]` = `Declared electronically before the goods leave.` against the despatch at 15:10 (06) before the issue at 16:08 — refuted because "leave" means leave the customs territory, which happens on 2026-04-20 (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`). (from context; broad listed the same under "Outside this review")
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `120480` equal to the goods gross weight although the shipment weight includes transport equipment — refuted: no equipment is used. (from context, logistics, broad)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate`: a recycled-content certificate in a customs declaration — refuted because recycled content can matter for Trade Accord rules or plastic levies, so it is not clearly without use. (from context)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`: a location without identifier — refuted: no other example identifies the post either, so there is nothing it fails to match. (from logistics)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` could clash with a real ICD — refuted: not assigned in the real register (own knowledge). (from parties)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped identifier (`BLUMXBLX`) could be a real BIC — refuted: positions 5–6 carry the user-assigned code `XB`. (from parties)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox`: a postal address with both a post box and a street and building number — refuted: a post-box address may name the delivery office's street. (from parties)
- `/ExportCustomsDeclaration/cac:ExporterParty`: no separate declarant — refuted: the exporter lodges and signs the declaration itself (`/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Rinova Recovery`). (from parties)

## Changed in the merge
- broad/F2, parties/F1, context/F2 → F1: combined.
- logistics/F1 → F2: wording; the import declaration's use of `CustomsTariffQuantity` added as evidence and as option (b).
- broad/F3, parties/F2, context/F3 → F3: combined; preferred option "drop".
- broad/F1, parties/F3, context/F1 → F4: combined, with the register-scheme identifier from parties; the VAT registration (parties/F10) kept separate as F14 (Low), unlike the other merges of this run, because it does not contradict the party's nature.
- parties/F8 → F5: counter-argument from the refutations in `01-Order.xml` added; preferred option changed.
- broad/F9, parties/F7, context/F9 → F6: combined; "Needs decision" yes.
- broad/F7, parties/F4, context/F8 → F7: combined.
- broad/F6 (part), parties/F6, context/F5 → F8: combined; "Needs decision" no instead of yes (parties); broad's grouping with the bank account split into F8 and F13.
- broad/F5, logistics/F2 → F9: combined.
- money/F1 → F10: broad's refutation added as counter-argument; FOB arithmetic recomputed.
- broad/F10 → F11: check digit recomputed; wording.
- parties/F9, context/F10 → F12: combined.
- broad/F6 (part), money/F2, parties/F5, context/F4 → F13: combined.
- parties/F10 → F14: broad's refutation added as counter-argument.
- broad/F4, logistics/F3, context/F6 → F15: combined.
- broad/F8, context/F7 → F16: combined; context's citation of `FB-SIG-882` in 04 as the party's own numbering not repeated, as the merge of 04 finds that ID unrelated to its document (04 F13).

## Outside this review
- Timeline across documents (from broad): the note says the goods are "Declared electronically before the goods leave", but the declaration is issued at 16:08 on 2026-04-19, after the despatch stated in `06-Waybill.xml` (15:10 the same day), though before the exit from Urvania (2026-04-20 16:00). Context refuted it as a contradiction (see "Considered and refuted"); whoever checks the flow's timeline may still look at it.
