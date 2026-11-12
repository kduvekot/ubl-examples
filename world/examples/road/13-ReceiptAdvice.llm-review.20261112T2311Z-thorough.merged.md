# LLM review: 13-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/13-ReceiptAdvice.xml`, Git blob `604fd2f166bf65e6e949e78ef14e8423b7c4b8ad` (committed)
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

### road/13#F1 · High · Emission factor × base does not give the emission value
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA (one bench) the calculated value is 0.82 kg CO2e, not the stated 96 kg. Recalculated in the merge: 96 / 0.82 = 117.1, which is no quantity of the item or the flow; 0.82 × (34 kg steel + 22.5 kg hardwood of the `CircularityProfile`) = 46.3 kg, 0.82 × 34 kg = 27.9 kg. The three values contradict each other, which section 6 makes High. The same triple occurs in 39 examples, 9 of them in this flow (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × (activity quantity in the unit of `ValueBaseMeasure`) equals `ValueMeasure`, or factor and base are absent.
- Options: (a, preferred, as in the rail merges and context) drop `ValueFactorNumeric` and `ValueBaseMeasure`: the 96 kg is a per-item figure from the LCA and no factor is stated anywhere; (b, broad/logistics) give the factor and base the 96 kg are really calculated from (e.g. kg CO2e per kg of steel, base in KGM).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F4, Medium)

### road/13#F2 · Medium · Language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (e.g. `en-XB`, the form the examples already use in `languageID`); the bare ISO 639 code `en` with `listID` `ISO 639` only repeats `Language/ID` next to it and names no locale. Section 6 lists "a language code in LocaleCode" as Medium. Recounted in the merge: 364 occurrences in 213 files (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `-rl` for files); the parts said 362.
- Condition: `LocaleCode` is absent or holds a locale (language plus region) from a list of locales named in its listID.
- Options: (a, preferred: broad, parties) drop `LocaleCode`, since `Language/ID` already says English and nothing in the document needs a region; (b, context's preference) a locale such as `en-XB` with a locale list (BCP 47) as listID.
- Needs decision: no (parties said yes because the value looks deliberate; the fix is encoding only, as decided in all earlier flows)
- From: broad (F2), parties (F1), context (F6)

### road/13#F3 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance of the business park, information for vehicles, not a street name; in Lumeway's business address it says nothing about where mail goes. The flow itself names other entrances (`Gate B`, `dock 4`) as delivery instructions. Recounted: 79 occurrences in 76 files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance; where a delivery needs the gate, it is in an element meant for it (a delivery location or its description).
- Options: (a, preferred) drop the gate from the party address; a receipt advice needs no gate; (b) keep it only in delivery addresses, in a location description, not as a street name.
- Needs decision: no
- From: broad (F3), parties (F2)

### road/13#F4 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address in the same document puts its state there (`/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Recounted: 219 occurrences in 104 files (`grep -rho --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with `CountrySubentityCode` where a list exists).
- Options: (a, preferred) move it to `CountrySubentity`, as Bayvarra does; (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no
- From: broad (F4), parties (F3), context (F5)

### road/13#F5 · Medium · The carrier's CMR waybill referenced as a delivery note
- XPath: `/ReceiptAdvice/cac:Shipment/cac:Delivery/cac:DeliveryNoteDocumentReference/cbc:ID` = `TH-WB-26-0159`
- XPath: `08-Waybill.xml:/Waybill/cbc:ID` = `TH-WB-26-0159`
- Why: `DeliveryNoteDocumentReference` is "A reference to a Delivery Note associated with this Delivery". TH-WB-26-0159 is the carrier's CMR consignment note, a transport contract document issued by Trasvia, not the supplier's delivery note; the supplier's document accompanying the goods is the despatch advice, already referenced (`/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`). A reference element of one document kind is used for another (meaning other than the definition: Medium). Refutation tried in the merge: a signed CMR copy often serves the consignee as proof of delivery, but that makes it a transport document referenced for delivery, not a delivery note. The same reference is in `11-ReceiptAdvice.xml`.
- Condition: `DeliveryNoteDocumentReference`, if present, refers to a delivery note; the waybill, if referenced, is referenced through an element or document type that says it is a transport document.
- Options: (a, preferred) move the waybill reference to an `AdditionalDocumentReference` with the waybill's document type; (b) remove it.
- Needs decision: no
- From: logistics (F2)

### road/13#F6 · Medium · Lifecycle stage code MANUFACTURING for a cradle-to-gate figure
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies", `LifecycleStageDescription` the same "expressed as a text". In the world list `LifecycleStageCode` (checked in the merge), `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the description cover A1 to A3, so the code names only part of what the figure covers. Same occurrence count as F1 (39 files with `MANUFACTURING`, `grep -rl --include='*.xml' 'LifecycleStageCode[^>]*>MANUFACTURING<'`).
- Condition: the lifecycle stage code and text name the same stage(s), and the figure covers exactly what they name.
- Options: (a, preferred) omit the code and keep the cradle-to-gate text (or one entry per stage, SOURCING and MANUFACTURING, with split figures if the LCA gives them); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no
- From: context (F1, High)

### road/13#F7 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (system boundary of a product figure), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 files do the same (`grep -rl --include='*.xml' 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'`).
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the boundary, if kept, is stated in text.
- Options: (a, preferred) drop it and state the boundary in `LifecycleStageDescription`; (b) in addition, record the missing boundary element as a finding for the UBL TC write-up.
- Needs decision: no
- From: context (F3)

### road/13#F8 · Low · Revised receipt advice does not refer to the advice it revises
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `Revised`
- XPath: `/ReceiptAdvice/cbc:ID` = `LD-RA-26-0164`
- XPath: `/ReceiptAdvice/cbc:Note` = `Recounted: all benches received; one box of side frames over.`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:ID` = `LD-RA-26-0162`
- XPath: `12-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:ReceiptDocumentReference/cbc:ID` = `LD-RA-26-0162`
- Why: `Revised` says the document has been revised, but this advice has a new ID and refers neither to the receipt advice it replaces (LD-RA-26-0162, cancelled by `12-FulfilmentCancellation.xml`, whose note says "A corrected receipt advice follows.") nor to the cancellation. The despatch party cannot tell from this document which earlier figures it replaces. Low rather than context's Medium: the link exists in the flow, through the cancellation, and the receipt itself (what arrived) is complete.
- Condition: the corrected receipt advice identifies the receipt advice it replaces (and may refer to the cancellation), or its status says it is a new original.
- Options: (a, preferred) an additional document reference to LD-RA-26-0162 with its document type; (b) status `NoStatus` and the cancellation's note as the only link; (c, logistics) the ID LD-RA-26-0162 with a higher version, which makes the cancellation unnecessary and changes the flow.
- Needs decision: no
- From: broad (F5), logistics (F3), context (F2, Medium)

### road/13#F9 · Low · The accepted extra side frame is never billed, returned or declared
- XPath: `/ReceiptAdvice/cbc:DeliveryAcceptanceCode` = `ACCEPTED`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `13`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:OversupplyQuantity` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box more than despatched: picked twice at the 3PL.`
- XPath: `15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `12`
- XPath: `17-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:Quantity` = `12`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `717.60`
- Why: `OversupplyQuantity` is "The quantity over-supplied, i.e., the quantity over and above the quantity ordered." The corrected receipt accepts the whole delivery, including one side frame (5 980 XUF at the order price) picked twice at the 3PL. No document of the flow settles it: the invoice bills 12, the remittance pays the invoice in full, no return, debit note or correction follows, and the import declaration declares 12 units (717.60 XBL = 12 × 5 980 × 0.01, recomputed), so one unit crossed into Bayvarra without customs value. The documents do not contradict each other on their own terms; the flow leaves the accepted unit unaccounted for.
- Condition: the flow says what happens to the over-supplied side frame: it is billed (and declared), returned, or the acceptance excludes it, and receipt advice, invoice and import declaration agree with that.
- Options: (a, preferred) the receipt does not accept the extra unit and says it is held for return to the 3PL (fits "picked twice", needs no further document); (b) Valdara bills the 13th unit and the import declaration is corrected to 13; (c) the receipt records the unit as kept free of charge, with a note.
- Needs decision: yes
- From: money (F1)

### road/13#F10 · Low · Contacts that do not fit a receipt advice
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: a receipt advice comes from goods-in; the delivery customer's contact should be the receiving function, but it is Lumeway's customer service desk in Sales. Castrano's contact is named `Warehouse office` but titled `Customer service officer` in `Sales`, so name, job title and department disagree. Each party carries one fixed contact in every role of the flow.
- Condition: the delivery customer's contact is its goods-in function; the despatch supplier's contact has a name, job title and department that agree and fit the warehouse.
- Options: (a, preferred) role-specific contacts (goods-in for Lumeway, a warehouse title and department for Castrano); (b) drop job titles and departments that do not fit.
- Needs decision: no
- From: broad (F6), parties (F4), context (F7)

### road/13#F11 · Low · Italian street names tagged as English, with the issuer's region subtag
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: both renderings carry `languageID` `en-XB` (English as used in Bayvarra) but are Italian text; the same Urvanian addresses are tagged `en-XU` in the documents Urvanian parties issue (e.g. `15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`, tagged en-XU). The parties part refuted it: English text keeps foreign street names unchanged, and the region subtag follows the sender. Against that: `languageID` names the language of the content, which is Italian here, and the same party's address is tagged differently depending on who sends the document. The merge cannot settle which convention the world wants; aligned with the utilities and rail merges, which made the same question a Low finding needing a decision. Counted: 217 street renderings beginning with an Italian street word tagged en-XU or en-XB, in 102 files (`grep -rho --include='*.xml' 'StreetName languageID="en-X[UB]">\(Via\|Viale\|Piazza\|Corso\|Largo\|Strada\|Banchina\|Valico\)'`).
- Condition: the world has one stated rule for the language tag of Urvanian names rendered in English, and every rendering of the same address follows it.
- Options: (a, preferred) document the rule that English renderings keep Urvanian proper names and use the party's own variety (en-XU) whoever sends the document; (b) document that the tag follows the issuer, as now.
- Needs decision: yes
- From: merge (from the parties' "Considered and refuted")

### road/13#F12 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Castrano Logistics SRU carries 1 January 1996, a public holiday; recounted, `1996-01-01` occurs 271 times in 181 files for many different companies (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway (1988-10-03) and Valdara (1962-04-12) have their own dates. It reads as a filler (IND5).
- Condition: each party's `RegistrationDate` is its own plausible date, or the element is absent.
- Options: (a, preferred) give Castrano its own date from its history (a subsidiary of Valdara); (b) leave the element out.
- Needs decision: yes (parties said no; aligned with the earlier flows and road merges a and b: dates are part of company histories)
- From: parties (F5)

### road/13#F13 · Low · Urvanian legal forms in one untagged rendering
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: in documents issued by Urvanian parties the same legal forms come in two tagged renderings (Urvanian `qau` and `en-XU`, e.g. `14-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`); here, in a Bayvarran-issued document, there is one rendering without `languageID`, while the addresses of the same parties are rendered in both languages. The same party is described differently by issuer. No part raised it; added by the merge for consistency with the rail, air, wood and plastics merges.
- Condition: the legal form of each Urvanian party is rendered as its address is (both renderings, tagged), or the difference is a stated convention.
- Options: (a, preferred) both renderings with `languageID`, as in the Urvanian-issued documents; (b) one rendering, tagged.
- Needs decision: no
- From: merge

### road/13#F14 · Low · Party master data the receipt advice does nothing with
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: section 4.8: Valdara's `SecurityListing` ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") has no part in reporting what arrived. Context also listed Castrano's `ShareholderParty`; the merge took it out (see "Considered and refuted"): it explains why Castrano, as Valdara's subsidiary, despatches on Valdara's behalf.
- Condition: every optional party aggregate present has a reason in this document's purpose.
- Options: (a, preferred) leave the listing out of this document; (b) state the reason if the story gives one.
- Needs decision: no
- From: parties (F6), context (F8, party part)

### road/13#F15 · Low · Recount yields one package more than the carrier took over
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedQuantity` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `13`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box more than despatched: picked twice at the 3PL.`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalPackagesQuantity` = `108`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:Note` = `One pallet held three benches and a box of side frames: mis-picked at the 3PL.`
- Why: after the recount, 96 benches and 13 boxes arrived, i.e. 109 packages; the carrier took over 108 (24 pallets of 4 benches + 1 pallet of 12 boxes, 25 handling units, checked in the waybill) without reservation. The first receipt explained the extra box as standing in place of a bench (108 packages, consistent with the waybill); the corrected one changes the explanation without saying that the carrier's package count was then one short. Logistics refuted it: the despatch advice and waybill record what was believed to be loaded, and reporting the difference on receipt is the purpose of the receipt advice. Partly survives: the receipt does report the difference, but against the despatch line only; that the CMR count (and its "apparent good order") was wrong is stated nowhere. Whether that needs saying is a story question, so it stays Low with a decision.
- Condition: the recount, the waybill's package count and the explanation of the extra box are consistent, or the discrepancy with the carrier's count is stated.
- Options: (a, preferred) say in the line note that the carrier's count of 108 was one short (an extra box on the side-frame pallet); (b) keep the first receipt's explanation and correct only the bench count.
- Needs decision: yes
- From: broad (F7); refuted by logistics (its "Considered and refuted")

### road/13#F16 · Low · Catalogue and product-passport data in the receipt line
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a receipt advice reports what was received against what was despatched. Search keywords, warranty, the circularity profile and the product's emission figure (F1, F6, F7) play no part in that (section 4.8, IND5); item identification and description are what the receipt needs. Split from the party master data of context's F8, as in the rail merges.
- Condition: item data in the receipt advice has a use in reporting the receipt.
- Options: (a, preferred) drop keyword, warranty, circularity profile and emission from the receipt line; (b) keep them only if the story uses the receipt for them.
- Needs decision: no
- From: context (F8, item part)

### road/13#F17 · Low · Item number looks like a real GTIN-12
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- Why: the numbers of scheme `urn:ubl-examples:world:item` are 12 digits with a valid GS1 mod-10 check digit (recomputed in the merge: 7 and 4), so a scanner or GS1 check reads them as GTIN-12s; GTIN-12s are the UPC range administered by GS1 US, and `771` is also a GS1 prefix (GS1 Colombia). This rests on knowledge of the GS1 prefix allocation; whether the numbers are assigned could not be checked. The rule that fictional values must not be mistakable for real register entries applies. Only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither. 39 files carry `771020000027`.
- Condition: the item numbers cannot be read as validly check-digited GTINs, and both items of the scheme are described the same way.
- Options: (a, preferred) change the world item scheme's format so it is not a valid GTIN; (b) use the GS1 prefix reserved for demonstrations (952, as for the GLNs), if the scheme is meant to mimic GTIN; in either case drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role.
- Needs decision: yes
- From: broad (F8)

### road/13#F18 · Low · Received side frames not identified as the substituted 2026 casting
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- Why: the order response replaced the ordered side frame by the 2026 casting (`ExtendedID` 2026); the receipt line records only VI-C180, so the receipt does not show which casting arrived, and the invoice response's "Matched to the substituted 2026 casting" (`16-ApplicationResponse.xml`) has nothing in the goods documents to match against. Verified in the merge: `ExtendedID` 2026 occurs only in `02-OrderResponse.xml` in this flow.
- Condition: the receipt line identifies the casting version received as the order response identifies the substitute.
- Options: (a, preferred) `ExtendedID` 2026 on the item, as in the order response; (b) drop the version distinction everywhere if it has no role.
- Needs decision: no
- From: logistics (F4)

## Checked and consistent
- References: order `LD-PO-26-0149` (`01-Order.xml`), despatch advice `CL-DA-26-0153` with lines 1 and 2 (`04-DespatchAdvice.xml`), shipment and waybill resolve.
- Quantities: line 1, 96 received = 96 despatched (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:DeliveredQuantity` = `96`); line 2, 13 received = 12 despatched + `OversupplyQuantity` 1; no shortage, as the cancellation says (`12-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The recount found the bench reported short; the shortage did not exist.`). Header note and line notes agree.
- Times: issued 2026-03-26 10:48, two minutes after the cancellation (10:46) that announces it; actual delivery 2026-03-25 09:40, as in `11-ReceiptAdvice.xml` and `14-Invoice.xml`.
- Waybill packages recalculated: 24 handling units × 4 benches + 1 × 12 boxes = 108 packages on 25 handling units (`08-Waybill.xml`).
- Money: all 96 benches received are invoiced (`15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `96`), 12 side frames as despatched.
- Parties: Lumeway, Valdara and Castrano are described as in the other examples of the flow apart from the language tags (F11, F13); Castrano's `ShareholderParty` (Valdara, 100 %) agrees with Valdara's `ServiceProviderParty` (Castrano, warehousing and despatch).
- Check digits (`check_ids.py`): GLN `9520610900008` (GS1 prefix 952, reserved for examples) and ISIN `XU0001042501` are correct.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:Note` = `All 96 benches, after the recount.` against the first advice's "one pallet held three benches": suspected a contradiction — refuted because the corrected receipt is meant to supersede the first count (from broad).
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box more than despatched: picked twice at the 3PL.`, another reason than the cancelled advice's "The mis-picked box, in place of the missing bench": suspected a contradiction between examples — refuted because the first explanation depended on the shortage the recount disproved; the corrected document may correct the reason too (from context). The package-count side of it is F15.
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity`: 109 packages against 108 on the CMR — refuted by logistics (reporting the difference found on receipt is the purpose of this document); not followed in full, kept as F15 with both arguments.
- `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian street name tagged as English — refuted by parties (English keeps foreign street names; the subtag follows the sender); not followed, made F11.
- `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be a real one — refuted because prefix 952 is reserved by GS1 for demonstrations and examples, and the check digit is correct (from parties).
- `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because country code +999 is reserved in ITU-T E.164 and assigned to no country (from parties).
- `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number — refuted because "An identifier for this Service Provider" does not say who assigns it; a number Valdara assigns to its provider is a legitimate reading (from parties).
- `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`: listed by context as master data without use — refuted in the merge because it explains why Castrano, the despatch supplier, acts for the seller Valdara (its sole shareholder) in this receipt, which the parties part checked as consistent (from context F8; the rest of that finding is F14 and F16).

## Changed in the merge
- broad/F1, logistics/F1, context/F4 → F1: combined; context's Medium raised to High (arithmetic that does not hold, section 6); preferred option set to dropping factor and base, as in the rail and road 01-12 merges, the parts' "real factor" kept as option (b).
- broad/F2, parties/F1, context/F6 → F2: combined; parties' "Needs decision: yes" set to no (encoding only, as in all earlier flows); count corrected to 364.
- context/F1 → F6: High lowered to Medium, aligned with the rail and road 01-12 merges: code and text are both present and the code names a narrower stage of the same figure, read as a code that does not fit the element's value rather than a contradiction of two statements.
- broad/F5, logistics/F3, context/F2 → F8: combined; context's Medium lowered to Low because the link exists in the flow through `12-FulfilmentCancellation.xml`; logistics' version option kept as (c).
- broad/F6, parties/F4, context/F7 → F10: combined; context's F8 split: party data → F14 (without the ShareholderParty, refuted), item data → F16.
- parties/F5 → F12: needs decision no → yes, aligned with the earlier flows and road merges a and b.
- F11 and F13 added by the merge (F11 from a refutation of the parties part not followed).
- broad/F8 → F17: preferred option reworded (format change), aligned with the rail and plastics merges.

## Outside this review
- `14-Invoice.xml` (issued 2026-03-25 11:07) refers to this receipt advice, issued 2026-03-26 10:48; the finding is road/14#F1.
- `11-ReceiptAdvice.xml` references the same waybill as delivery note (F5 here); a finding of that example's review.
