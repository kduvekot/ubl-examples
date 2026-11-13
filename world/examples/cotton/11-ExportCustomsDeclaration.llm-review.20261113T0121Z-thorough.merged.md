# LLM review: 11-ExportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/11-ExportCustomsDeclaration.xml`, Git blob `6a4c14a5a30406d882ebdc39fccad12bc46c7e0e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/11#F1 · Medium · Shipment gross weight without the container
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment"; the goods item's `GrossWeightMeasure` is the weight of the goods item "excluding the carrier's equipment". The same figure in both elements cannot fit both definitions. The same shipment SCG-SH-26-0200 travels in container TWLU4123110, whose verified gross mass, weighed the same afternoon, is 9940.29 kg (12): 6190.29 kg goods with packaging + 3750 kg tare. Customs practice declares the gross mass without the container; under the agreed rule of semantic conformance the UBL definition applies. Medium, not High: this document declares no equipment, so the value contradicts the definition and 12's description of the shipment rather than another value of this declaration (logistics had Low).
- Condition: the shipment gross weight includes the transport equipment, or only the goods-item gross weight is given.
- Options: (a, preferred) drop the shipment gross weight and keep the goods-item figure, which is what customs needs; (b) 9940.29 kg with the container declared.
- Needs decision: no
- From: broad (F1), logistics (F2)

### cotton/11#F2 · Medium · The customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Island Customs Service is a public authority (ISIC `8411`, general public administration). `CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `CompanyLiquidationStatusCode` the party's liquidation status: a government agency is not registered in a commercial companies register and cannot be in liquidation. The values contradict the party's own classification. All 6 example files that give this authority's `RegistrationName` also carry a liquidation status (parties' count over *.xml).
- Condition: the authority's legal entity carries no commercial registration scheme and no liquidation status; an identifier, if any, is from a register of public bodies.
- Options: (a, preferred) keep only `RegistrationName` (and an identifier from a register of public bodies, if the world has one); (b) drop the authority's `PartyLegalEntity`.
- Needs decision: no
- From: parties (F1)

### cotton/11#F3 · Medium · Language code in `LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F2), parties (F2)

### cotton/11#F4 · Low · `PackQuantity` 1 / `PackSizeNumeric` 227: the nominal bale weight as a pack size
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count; 227 is the nominal bale weight in kilograms ("compressed bales of about 227 kg"). Logistics and context read it as a weight in a count element (Medium). Counter-argument (merge): the item is traded and declared per kilogram (`Quantity` 6129 KGM), so "227 one-kilogram units per pack" is a possible reading, though the bale weight is only "about". Cannot be settled from the definition alone. Same in 02, 07, 08, 10, 15 and 16.
- Condition: the pack elements, where present, state a count whose unit is clear; otherwise the bale weight is carried where a weight belongs, and the bale count as in F5.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric`, with the nominal bale weight as an item property with a KGM quantity if needed; (b) keep them and record the reading as a convention.
- Needs decision: yes
- From: logistics (F1), context (F1), broad (F8)

### cotton/11#F5 · Low · The number of bales is not declared
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- Why: an export declaration normally states the number and kind of packages, which customs checks at exit (own knowledge of customs data models). The goods item states the net quantity in kilograms only; the 27 bales (6129 / 227 = 27) are not counted.
- Condition: the declaration states the number of bales as a package count.
- Options: (a, preferred) a package of the goods item with `Quantity` 27 and a bale packaging type.
- Needs decision: no
- From: broad (F4), context (F2), logistics (inside F1)

### cotton/11#F6 · Low · The phytosanitary certificate of the shipment is not referred to
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cbc:ID` = `SCC-GC-26-0202`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: a customs declaration for exporting plant products lists the supporting documents presented with it; the phytosanitary certificate SCC-GC-26-0202, issued the day before for this shipment, is not referenced, while the buyer's order is. Logistics refuted it: the certificate is required by the importing country (its applicable territory is XB), so the export declaration need not carry it. Not followed: export declarations commonly declare the phytosanitary certificate among the documents produced (own knowledge, e.g. the EU document code N851 used at export), because the exporting authority's certificate accompanies the goods from export onward.
- Condition: the declaration references the plant-health certificate of the shipment, or the story says why it is not needed at export in Lisavu.
- Options: (a, preferred) an `AdditionalDocumentReference` to SCC-GC-26-0202 with its document type.
- Needs decision: no
- From: broad (F4), context (F2); refuted by logistics (argument carried)

### cotton/11#F7 · Low · Exit office only by name; no container or transport at exit
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4123110`
- Why: the exit office is named only by text, while the port of Selanu is identified elsewhere in the flow as `XLSEL`. The declaration, made "before the goods leave", does not say how they leave: no container (TWLU4123110, weighed the same afternoon, 12), no mode or means of transport at the border, which an export declaration normally carries. Details the document could carry, not contradictions. (Parties noted that a customs office is identified by a customs office code rather than a LOCODE; either would identify it.)
- Condition: the exit office location carries an identifier (customs office code, or the port's identifier used elsewhere); the container and the transport mode at exit are stated, or their absence is deliberate.
- Options: (a, preferred) an identifier for the exit office and a transport handling unit with the container in the shipment; optionally the main-carriage mode (sea).
- Needs decision: no
- From: logistics (F3); parties (considered)

### cotton/11#F8 · Low · The customs authority's contact for an export is its import office
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Import office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:ElectronicMail` = `import@customs-xl.example`
- Why: the customs party is "The Authority who processes this Customs Declaration", an export declaration with exit at the port of Selanu; its contact is the service's import office.
- Condition: the customs party's contact is the office that handles exports (or the exit office at the port), or is absent.
- Options: (a, preferred) an export or port office contact; (b) drop the contact.
- Needs decision: no
- From: broad (F3), parties (F3)

### cotton/11#F9 · Low · The consignee's contact: Purchasing, Customer service officer, Sales
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: a consignee's contact receives goods; here the name says buying and job title and department say selling, so the three also contradict each other. The combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: a receiving (goods-in / import) contact whose name, job title and department agree.
- Options: (a, preferred) the mill's goods-in or import desk; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F5), parties (F4)

### cotton/11#F10 · Low · Consignee's Bayvarran sales-tax registration in the Lisavan export declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: the declaration is made to the Island Customs Service for a permanent export from Lisavu; the consignee's registration for the Coastal State sales tax of Bayvarra is assessed nowhere in it. It has its use at import (15), not here (section 4.8, master data copied into a document that does not use it).
- Condition: the export declaration carries a party tax registration only if Lisavu customs uses it.
- Options: (a, preferred) drop the consignee's `PartyTaxScheme`.
- Needs decision: no
- From: money (F1)

### cotton/11#F11 · Low · Classing results carried as the applicant's remarks
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for the certificate"; the text is the classer's result, and grade and staple are already item properties of the same item.
- Condition: the classing result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark.
- Needs decision: no
- From: broad (F6)

### cotton/11#F12 · Low · Origin area in `Region` here, in `District` in the farm's address
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: the same area is a `District` in the farm's address and a `Region` here; a consistency remark (`Region` can be read as a geographic region).
- Condition: the north coast is in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in the origin address.
- Needs decision: no
- From: broad (F7), context (F3)

### cotton/11#F13 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Ginnery and mill, in different registers, share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F5)

### cotton/11#F14 · Low · Signature ID built from the flow name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `SCG-SIG-EX-cotton`
- Why: the signature's identifier ends in the name of the example flow ("cotton"), a name that exists in the repository, not in the world; the ginnery would number its signatures in its own series (as its other signatures do: SCG-SIG-26-0001, SCG-SIG-VGM). No part raised it; added by the merge for alignment with the earlier flows (road: VI-SIG-EX-road). The pattern `SIG-…-<flow>` is in 8 example files (`grep -rl --include='*.xml' 'SIG-[A-Z]*-\(cotton\|road\|rail\|sea\|air\)<'`), in this flow also 13 and 15.
- Condition: the signature ID is an identifier of the signer's own numbering, with no repository or flow name in it.
- Options: (a, preferred) an ID in the ginnery's signature series.
- Needs decision: no
- From: merge

## Checked and consistent
- The customs declaration ID SCG-CD-26-0204 is the one the import declaration cites as previous declaration (`15-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`).
- Declared customs value 6055.452 XLC = 6129 kg × 0.988 XLC, the order (08) and invoice (16) value; under FOB Port of Selanu (08) the price is the export value at the frontier (recalculated: 6129 × 0.988 = 6055.452).
- Shipment SCG-SH-26-0200 and consignment LTM-CS-26-0201 are those of 09, 10, 12, 13 and 15; goods item gross 6190.29 kg and quantity 6129 kg agree with 10 and 15.
- Issued 2026-03-01 13:33, before the weight statement (12, 15:19) and the bill of lading (13, 2026-03-02), as the note ("Declared electronically before the goods leave") says; validity 90 days.
- Exporter and consignor are the ginnery (IC42681, customs trader XL-TR-042681), consignee the mill (customs trader XB-TR-412603); both trader numbers have a use in a customs declaration. Their descriptions match 10 block by block.
- The customs party's address (Wharf Road 53, Selanu) is on the same street as the port (`12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`).
- Function code 9 (Original) of UN/EDIFACT 1225; permanent export, reason sale. `AdditionalDocumentReference` LTM-PO-26-0198 resolves to 08.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 90 days of validity — refuted: a plausible period within which the goods must leave (from broad).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`: customs value supported by the order rather than by the invoice 16 — refuted because the invoice is issued on 2026-03-02, after this declaration; the order states the same price and amount (from money).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`, different from the document ID `SCG-EX-26-0203`: a duplicate identifier — refuted because `CustomsDeclaration/ID` is "an identifier associated with customs related procedures", distinct from the message ID, and 15 refers to it (from logistics).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`: a commercial classing certificate in a customs declaration — refuted because the grade affects the export value and cotton exports are commonly declared with their class (from context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:FunctionCode` = `9`: a message function code for a declaration — refuted because "Original" is the function of a first declaration (from context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: the port has a UN/LOCODE in 12 — not kept by parties (a customs office has its own code); the identification point is part of F7 (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Cotton sales`: the exporter's sales desk for an export sale — acceptable (from parties).
- Phytosanitary certificate not referenced: refuted by logistics (required by the importing country); not followed, kept as F6 with both arguments.

## Changed in the merge
- logistics/F2 (Low) + broad/F1 (Medium) → F1: Medium, because the value misfits the element's definition and 12's description of the same shipment; not High, as this document declares no equipment.
- logistics/F1, context/F1 (Medium) + broad/F8 (Low) → F4: Low with "Needs decision: yes" (reading of the item as traded per kilogram; same as cotton/10#F7).
- broad/F4 and context/F2 split into F5 (bale count) and F6 (phytosanitary certificate), because logistics refuted only the certificate part.
- F14 added by the merge (no part raised it), for alignment with the signature-ID findings of earlier flows.
- broad's "as cotton/02#F…" / "as cotton/09#F7" findings written out in full (F3, F9, F11, F12, F4).
