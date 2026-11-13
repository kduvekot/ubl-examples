# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/10-GoodsCertificate.xml`, Git blob `a573492644f6156f64f31e963d3578b9c5d69634` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/10#F1 · High · First version of the certificate with an "original" and a "previous version" that are other documents
- XPath: `/GoodsCertificate/cbc:VersionID` = `1`
- XPath: `/GoodsCertificate/cac:OriginalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cac:PreviousDocumentReference/cbc:ID` = `SCC-PH-25-0198`
- Why: in a Goods Certificate, `OriginalDocumentReference` is "A reference to the original version of the goods certificate" and `PreviousDocumentReference` "A reference to the previous version of the goods certificate". This is version 1, so it has neither. The "original" is the cotton-classing certificate of the lint (cited as such in the goods item, `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`), and the "previous version" is a 2025 phytosanitary certificate (SCC-PH-25-…), i.e. another certificate for another shipment.
- Condition: original and previous-version references are absent in version 1, or point to earlier versions of this same certificate (with `VersionID` raised accordingly); related certificates are additional document references with a type.
- Options: (preferred) drop both; cite the classing certificate (already in the item) and, if relevant, last year's certificate as additional document references with a description; or make this a version 2 that replaces SCC-PH-25-0198 only if that is really an earlier version of this certificate.
- Needs decision: no

### cotton/10#F2 · High · "10 bales sampled out of 80" for a shipment of 27 bales
- XPath: `/GoodsCertificate/cac:Attestation/cbc:Note` = `10 bales sampled out of 80.`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: the certificate is issued for the shipment SCG-SH-26-0200: 6129 kg of lint in bales of 227 kg, i.e. 27 bales (6129 / 227 = 27, as in the order 08). The attestation says 10 of 80 bales were sampled. 80 bales would be 18160 kg of lint, about three times the shipment, and three times the lint that the 18000 kg of seed cotton in 03 can yield. If the gin's whole stock was sampled, the certificate does not say so, and it does not certify these 27 bales as a sample of that stock.
- Condition: the sampling statement refers to the bales of this shipment (27), or says explicitly that the shipment was drawn from a larger sampled lot and identifies the lot.
- Options: (preferred) "3 bales sampled out of 27" (or whatever sample rule XB-PH-07 sets for 27 bales), and the criterion text adapted; or describe the 80-bale lot from which the 27 bales come.
- Needs decision: no

### cotton/10#F3 · Medium · A phytosanitary certificate issued by a chamber of commerce
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:Contact/cbc:Name` = `Carnet office`
- XPath: `/GoodsCertificate/cac:LegalAuthorityParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: under the International Plant Protection Convention, phytosanitary certificates are issued by the exporting country's national plant protection organisation, a public authority (own knowledge, IPPC Art. IV and V). A chamber of commerce, a membership organisation (ISIC 9411), issues certificates of origin and carnets, not plant-health certificates; here the contact is even its carnet office. The legal authority named is the customs service, not a plant-health authority. A real phytosanitary certificate issued like this would not be accepted at import.
- Condition: the phytosanitary certificate is issued (or sanctioned, as `LegalAuthorityParty`) by Lisavu's plant-protection authority, with a contact that deals with plant health.
- Options: (preferred) a Lisavan plant-protection service as issuer, with the chamber at most as the body that classed the lint; or change the certificate type, if the chamber's document is meant to be a private quality/fumigation attestation rather than a phytosanitary certificate.
- Needs decision: yes

### cotton/10#F4 · Medium · A goods-processing code as criterion type
- XPath: `/GoodsCertificate/cac:GoodsProcessing/cac:CriterionItem/cbc:TypeCode` = `PROCESSING`
- Why: `CriterionItem/TypeCode` is "A code describing the type of criteria". The code is taken from the goods-processing type list (`listID` `urn:ubl-examples:world:codelist:GoodsProcessingTypeCode`, the same list as `GoodsProcessing/TypeCode` GINNING), so a processing type stands where a criterion type is expected. A code from a list meant for another element.
- Condition: the criterion's type code comes from a list of criterion types (or is absent).
- Options: (preferred) a criterion-type list with a code for "processing criterion" (or reuse the attestation-type list if it is meant for criteria); or drop the type code, the description is clear.
- Needs decision: no

### cotton/10#F5 · Medium · Language code in `LocaleCode`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/10#F6 · Low · No number of bales on a certificate based on bale sampling
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Description` = `Cotton lint, compressed bale`
- XPath: `/GoodsCertificate/cac:Attestation/cac:AttestationLine/cac:CriterionItem/cbc:CriterionDescription` = `No live insects in a sample of 10 bales.`
- Why: the certificate attests freedom from pests by sampling bales, but nowhere states how many bales it covers (no package or handling-unit count); the importing authority cannot check the sample against the consignment.
- Condition: the number of bales certified is stated as a count.
- Options: (preferred) a goods-item or package quantity of 27 bales.
- Needs decision: no

### cotton/10#F7 · Low · Classing results in the applicant's remarks
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as cotton/02#F5.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark.
- Needs decision: no

### cotton/10#F8 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: as cotton/02#F6.
- Condition: the north coast in the same element everywhere.
- Options: (preferred) `District`.
- Needs decision: no

### cotton/10#F9 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1`
- Why: as cotton/02#F7.
- Condition: the bale weight is not carried as a count.
- Options: (preferred) drop the pack elements and count the bales (F6).
- Needs decision: no

### cotton/10#F10 · Low · The importer's contact is its purchasing desk in sales
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- Why: as cotton/02#F3; for an import certificate the relevant contact is the mill's import or goods-in desk.
- Condition: name, title and department agree and fit the importer role.
- Options: (preferred) an import / goods-in contact.
- Needs decision: no

## Checked and consistent
- Validity 28 February – 14 March 2026 covers loading (2 March, 13) and import (6 March, 15); the attestation ends on the same day.
- Ginning period 7–22 February starts after the seed-cotton delivery (5 February, 03); "Seed removed; lint only" fits HS 5201.
- Declared value 6055.452 XLC and gross weight 6190.29 kg agree with 08, 09, 11 and 16; the goods-item gross weight "excluding the carrier's equipment" is used correctly here.
- Applicable territory Bayvarra matches the pests "named by Bayvarra's plant health rules"; criterion XB-PH-07 is a Bayvarran rule.
- Exporter, importer, consignor, consignee and forwarder are the same parties as in 09, 11, 13 and 15.

## Considered and refuted
- `/GoodsCertificate/cac:WarehouseParty`: the ginnery as warehouse — refuted: the note says the bales were inspected at the ginnery's warehouse.
- `/GoodsCertificate/cac:FreightForwarderParty`: a forwarder on a plant-health certificate — refuted only weakly; the definition (consolidator) does not fit Bayforth exactly, but naming the forwarder that receives the original certificate is common. Not raised.
