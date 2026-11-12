# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/10#F1 · High · Declaration issued after the status report says it was accepted and the goods released
- XPath: `/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:IssueTime` = `09:10:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- Why: this, the only import declaration of the consignment, is issued at 09:54; the carrier's status of 09:10 already reports it accepted and the goods released at the border crossing completed at 08:55. A release cannot precede the declaration it rests on. The same contradiction is a finding of `09-TransportationStatus.xml`; the fix is one change in either document.
- Condition: the import declaration is issued before the time at which the flow reports it accepted and the goods released.
- Options: (a, preferred) issue it before the border crossing (pre-lodged on 2026-03-23 after despatch or early on 2026-03-24), which fits the waybill's "the import by the distributor at the border"; (b) move the release to a later status report.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### road/10#F2 · High · Emission value is not factor × base
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as in `07-CertificateOfOrigin.xml`: 0.82 per 1 EA gives 0.82 kg, not 96; 96 / 0.82 = 117.1 matches nothing, nor does 0.82 × 56.5 kg of material = 46.3 kg (recalculated in the merge). 39 examples carry the triple (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` equals `ValueMeasure`, or factor and base are absent.
- Options: (a, preferred, as rail and air) drop factor and base; (b) a factor and base the 96 kg are calculated from.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F6, Medium)

### road/10#F3 · High · Certificate reference resolves to two documents
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- Why: the reference carries only an ID, which both the submitted application (06, endorsement pending) and the approved certificate (07) have, with the same version. Without type, version, UUID or date the declaration cannot be linked to the approved certificate that the preference requires; one of the two candidates is not a valid certificate. Kept High as in `07-CertificateOfOrigin.xml` F1 (a reference that does not resolve to one document); context had Medium, logistics Low.
- Condition: the reference identifies exactly one document, the approved certificate, and says that it is a certificate of origin.
- Options: (a, preferred) resolve the duplicate ID in 06/07 and add `DocumentTypeCode` here; (b) add the UUID or issue date (2026-03-22) of 07 to the reference, which works even if the IDs stay.
- Needs decision: no
- From: broad (F3, High), context (F3, Medium), logistics (F3, Low)

### road/10#F4 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Customs and Border Service of Bayvarra (ISIC 8411, public administration) is a state authority; it is not in the commercial register and cannot go into liquidation ("A code signifying the party's liquidation status"). The register identifier is reused as its `PartyIdentification`.
- Condition: the customs party carries no commercial-register scheme and no liquidation status.
- Options: (a, preferred) keep only `RegistrationName`, or drop `PartyLegalEntity`; (b) a public-bodies register, if the world has one.
- Needs decision: no
- From: broad (F7), context (F4), parties (F4)

### road/10#F5 · Medium · Lifecycle stage code MANUFACTURING for a cradle-to-gate figure
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `MANUFACTURING` is module A3 in the world list; the texts cover A1–A3 (cradle to gate). Code and text name different stages.
- Condition: code and text name the same stage(s), and the figure covers exactly them.
- Options: (a, preferred) omit the code (or two entries); (b) reduce figure and texts to A3.
- Needs decision: no
- From: context (F2, High)

### road/10#F6 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty …"; the value is from the world's `EmissionBoundaryCode` list (semantic conformance).
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is.
- Options: (a, preferred) drop it, state the boundary in text, and record the missing element for the UBL TC.
- Needs decision: no
- From: context (F5)

### road/10#F7 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 occurrences in 213 files.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F4), context (F8), parties (F1, yes)

### road/10#F8 · Medium · Gate number in AdditionalStreetName of the importer's postal address
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is an entrance, and an import declaration has no use for it.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop it from the address.
- Needs decision: no
- From: broad (F5), parties (F2)

### road/10#F9 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address uses (`/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`).
- Condition: the province is in `CountrySubentity`.
- Options: (a, preferred) move it; (b) define Urvanian provinces as economic regions in the world's rules.
- Needs decision: no
- From: broad (F6), context (F7), parties (F3)

### road/10#F10 · Low · Urvanian national tariff codes in Bayvarra's import declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the goods are declared for free circulation in Bayvarra, but the national subheadings are from Urvania's tariff (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`); an import is classified in the importing country's tariff, on which duty and statistics depend (own knowledge). The world has only the Urvanian list (context), so either the accord has a common tariff, which the list's name does not say, or the code has no role here. Merge: Low rather than Medium (broad), because the code is used as its element defines (a commodity code from a named list); what does not fit is its presence in this document. Aligned with air (copied XU tariff code, Low).
- Condition: the national commodity code is from the tariff the importing country applies, or is absent (leaving the HS code).
- Options: (a, preferred) drop the national code and keep the HS code; (b) a Bayvarran or Trade Accord tariff list.
- Needs decision: yes (whether the accord has a common tariff is story)
- From: broad (F8, Medium, no), context (F9, Low, yes)

### road/10#F11 · Low · Duties said to be paid on goods that claim preferential origin
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: the note says duties are paid, while the declaration claims preferential origin under the accord with the certificate, which normally reduces the duty to zero (own knowledge). Money refuted the part of the suspicion that the declaration should state the duty amounts (the UBL 2.5 Import Customs Declaration has no element for them, so the note is the only place); the tension between "duties paid" and the preference is not answered by that, and whether Bayvarra levies any duty or import tax on accord goods is a judgment on the world's tax treatment.
- Condition: the note and the preferential claim agree (duty-free under preference, or the duty that remains named in the note).
- Options: (a, preferred) say in the note what is paid (e.g. Bayvarra's import tax, no duty under the accord); (b) drop the note.
- Needs decision: yes
- From: broad (F9); money considered and refuted the structured-duty part

### road/10#F12 · Low · Validity period of 30 days on a release for free circulation
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `30`
- Why: a declaration for free circulation takes effect on release; nothing in the flow uses a 30-day validity (IND5). Context refuted it because UBL defines the element as "A period, assigned by the issuer, during which the information in the declaration is valid", which a declarant may set. The merge keeps it as Low with a decision: the definition allows the value, but no business reason is given, and whether the world's customs rules give declarations a validity cannot be settled.
- Condition: the declaration carries a validity only if the procedure gives it one, stated in the world's customs rules.
- Options: (a, preferred) drop it; (b) keep it and record the rule.
- Needs decision: yes
- From: broad (F10, validity part); context considered and refuted it

### road/10#F13 · Low · Contacts that do not fit an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: customs contacts the importer's import or customs function, not its customer service in Sales; the consignor's order desk plays no part in Bayvarra's import; the customs contact has the generic title `Public service officer` in `Public services`.
- Condition: the importer's contact handles imports or customs; the consignor has no contact or a fitting one; the customs contact's title and department fit a customs office.
- Options: (a, preferred) an import/customs contact for Lumeway, no consignor contact, a customs officer title; (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F11), context (F10), parties (F5)

### road/10#F14 · Low · Border office hours exclude the time the truck was at the border
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Period/cbc:StartTime` = `07:30:00`
- Why: the authority's border office is reachable on weekdays 08:00–17:00, but the truck was at the border from 07:30 on 2026-03-24; a road border post is normally staffed around the clock (own knowledge).
- Condition: the customs contact's hours cover the time the consignment was at the border, or the contact is one reachable then.
- Options: (a, preferred) hours fitting a road border post (e.g. 24 hours); (b) move the border passage into the stated hours.
- Needs decision: no
- From: parties (F7)

### road/10#F15 · Low · Party master data the import declaration does nothing with
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's stock-exchange listing and its 3PL play no part in Bayvarra's import clearance (section 4.8, IND5). Unlike in the certificate of origin, nothing here needs the warehouse the goods left from.
- Condition: every optional party aggregate present has a reason in the declaration's purpose.
- Options: (a, preferred) drop them.
- Needs decision: no
- From: parties (F6), context (F11, listing)

### road/10#F16 · Low · Product passport and catalogue data copied into the declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: an import declaration needs description, classification, origin, quantity, weight and value; keywords, warranty, load test and colour properties, emission, circularity and repairability play no part (section 4.8).
- Condition: the item carries what the declaration needs; the rest is absent unless used.
- Options: (a, preferred) reduce the item to description, name, identifiers, origin and classification.
- Needs decision: no
- From: broad (F12), context (F11, item part)

### road/10#F17 · Low · Item number reads as a real GTIN-12
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: 12 digits with a valid GS1 mod-10 check digit (recomputed: 7; and 4 for the side frame's 771020000034), so they read as GTIN-12s of a real GS1 prefix range (own knowledge). Only the bench carries symbology and issuer scope.
- Condition: the item numbers cannot be read as check-digit-valid GTINs of a real GS1 prefix, and both items are described alike.
- Options: (a, preferred) a non-GS1 structure or the example prefix 952; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where unused.
- Needs decision: yes
- From: broad (F13)

### road/10#F18 · Low · Signature ID built from the flow name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LD-SIG-IM-road`
- Why: `road` is the name of this example flow in the repository and means nothing to Lumeway or customs; the other signers of the flow number their signatures (`FCC-SIG-26-0309`). Context counted 14 signature IDs ending in a flow name over `*.xml`.
- Condition: the signature ID follows the signer's own numbering, without flow names.
- Options: (a, preferred) a Lumeway number after the declaration ID; (b) drop the signature.
- Needs decision: no
- From: broad (F14), context (F12)

## Checked and consistent
- Customs values: 4 790 400 XUF × 0.01 = 47 904.00 XBL and 71 760 × 0.01 = 717.60 XBL, the rate of `15-Invoice.xml:/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01` on the same date; the XUF values are those of the export declaration and the invoice lines; XBL is right for values on which Bayvarran duties are assessed (money, broad; recalculated in the merge).
- Quantities 96 and 12, gross weights 3984 and 122.4 kg (total 4106.4), shipment CL-SH-26-0154 agree with 04, 05 and 08; despatch line references 1 and 2 of CL-DA-26-0153 resolve to `04-DespatchAdvice.xml` (broad, logistics, context).
- `PreviousCustomsDeclaration` VI-CD-26-0156 is the export declaration of `05-ExportCustomsDeclaration.xml` (broad, logistics, context).
- Roles: importer, consignee, notifier and signatory Lumeway; consignor Valdara; customs the Bayvarran service; consistent with the waybill's instruction that the distributor declares the import (broad, parties, logistics).
- `TypeCode` IMPORT, `SubTypeCode` FREECIRC, `NatureOfTransactionCode` PURCHASE fit a distributor buying for resale; `NotifierParty` = importer fits (context).
- Party identity, GLN and ISIN check digits (parties).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0156`: a previous declaration of another customs territory — refuted because the definition is "A reference to a previously sent customs declaration" and linking import to the partner's export is plausible under the accord (from broad).
- Customs value equal to the FCA price without freight to the border — refuted because the world's valuation basis is not stated and the WTO Valuation Agreement (Art. 8.2) leaves inclusion of transport to each member (from broad and money).
- `/ImportCustomsDeclaration/cbc:Note`: should state the duties in structure — refuted because the UBL 2.5 Import Customs Declaration has no duty or tax element (from money); the preference question remains F11.
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`: wrong office for an import — refuted because the document has only `CustomsExitOfficeLocation` ("Customs exit office of the goods being declared"), and the Urvanian exit post is that office (from logistics and context; the merge follows them, see "Refuted in the merge").
- `/ImportCustomsDeclaration/cac:ValidityPeriod`: meaningless for an import — refuted by context (the issuer may set it); the merge does not follow and keeps F12.
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XB` — refuted, English keeps foreign street names and the subtag follows the sender (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN could be real — refuted, prefix 952, check digit correct (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Telephone`: could be real — refuted, +999 reserved (from parties).
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01` as a contract number — refuted, the definition does not say who assigns it (from parties); its presence is F15.

## Refuted in the merge
### broad/F10 · Low · Export-side office and a validity period in an import declaration (exit-office part)
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why (broad): `CustomsExitOfficeLocation` is the "Customs exit office of the goods being declared"; for goods imported into Bayvarra the Urvanian exit post belongs to the export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`), while the Bayvarran office of entry is missing.
- Condition (broad): the import declaration names the Bayvarran office where the goods enter (or none).
- Refuted because: the UBL 2.5 Import Customs Declaration has no office-of-entry element (logistics checked the model), and the definition names the exit office "of the goods being declared", which for this movement is the Urvanian post; the value is a legitimate reading and the missing entry office cannot be carried. The validity part of broad/F10 is kept as F12.

## Changed in the merge
- broad/F3, context/F3, logistics/F3 → F3: High (context Medium, logistics Low), aligned with 07 F1.
- context/F2 → F5: High lowered to Medium, aligned with rail and air.
- broad/F8, context/F9 → F10: Low and Needs decision yes (broad Medium, no).
- broad/F9 → F11: money's refutation of the structured-duty part recorded; the preference tension kept.
- broad/F10 split: exit office refuted in the merge, validity period kept as F12 (Low, yes).
- broad/F11, context/F10, parties/F5 → F13: the three parts' contacts combined.
- context/F11 split into F15 (party, with parties/F6) and F16 (item, with broad/F12).
- parties/F1 → F7: Needs decision no, aligned.

## Outside this review
- The declaration (2026-03-24 09:54) is issued before the commercial invoice on which a customs value is normally based (`15-Invoice.xml:/Invoice/cbc:IssueTime` = `11:41:00`, same day), so the values rest on the order (money): a question of the order of documents across the flow.
