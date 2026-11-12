# LLM review: 08-DespatchAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/08-DespatchAdvice.xml`, Git blob `40cea0e7c3b5f742441038658c674f3f93c6cc68` (committed)
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

### plastics/08#F1 · Medium · The despatch advice states neither when the goods left nor when they arrive
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-04-19`
- XPath: `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `RR-SH-26-0889`
- Why: A Despatch Advice is "A document used to describe the despatch or delivery of goods". This one has no despatch date or time, no estimated delivery and no delivery location: verified in the merge, the shipment holds only its ID, the gross weight and the consignment with the carrier. The consignee, asked to "check the goods on arrival", is not told that the barge left on 2026-04-19 at 15:10 (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`) and is due at the river quay in Lumeport on 2026-04-22 (04, 06). The issue date is not a despatch date (nothing implied by absence). The document's purpose depends on this information (section 6: Medium).
- Condition: the despatch advice states the actual despatch (date, time) and the expected delivery (date or period, and place), consistent with 04 and 06.
- Options: (a) `Shipment/cac:Delivery` with `cac:Despatch/cbc:ActualDespatchDate`/`Time` 2026-04-19 15:10, an `EstimatedDeliveryPeriod` ending 2026-04-22 and the river quay as `DeliveryLocation` (preferred: all the receiver plans on); (b) at least the despatch date and the estimated delivery date.
- Needs decision: no
- From: logistics (F1), context (F1), broad (F6, expected delivery part)

### plastics/08#F2 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the flow use CountrySubentity. The parts counted 219 occurrences in 104 example files.
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with a code if Urvania has a list).
- Options: (a) move it to CountrySubentity (preferred); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F1), parties (F1), context (F2)

### plastics/08#F3 · Medium · Language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. The parts counted 362 LocaleCode elements in 213 example files, all `en`.
- Condition: every LocaleCode holds a locale from a list its listID names, or is absent.
- Options: (a) drop it where the locale has no use (preferred, as parties and the wood merges); (b) `en-XB` with a locale list as listID (broad, context).
- Needs decision: no
- From: broad (F2), parties (F2), context (F3)

### plastics/08#F4 · Low · No reference to the consignment note and no package count
- XPath: `/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One barge load of recycled granulate in jumbo bags.`
- Why: The note sends the consignee to "the consignment note", but the despatch advice does not identify it (`FB-WB-26-0890`, 06). The goods are described only as "in jumbo bags": the advice does not say how many packages to check on arrival (120, from 06), which a receiving check counts. "One barge load" is not quite what happened: the consignment is a part load of the barge (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `FB4-26-031/2`).
- Condition: the advice references the consignment note and states the number and type of packages (120 × JB); the line note does not claim a full barge load unless it is one.
- Options: (a) an `AdditionalDocumentReference` to `FB-WB-26-0890` with its type, the 120 bags as a handling unit or package count of the shipment, and the line note "120 jumbo bags of recycled granulate" (preferred); (b) at least the waybill reference.
- Needs decision: no
- From: logistics (F2), broad (F6, packages and waybill part)

### plastics/08#F5 · Low · Lot number differs from the waybill's trace identifier for the same goods
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `RR-PE-0416`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-16`
- Why: The waybill traces the same goods as `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:TraceID` = `RR-PE-LOT-26-0416` and the bags as `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ID` = `RR-JB-0416`. Three forms point to the 0416 lot; a receiver matching the advice with the consignment note finds no common identifier. A TraceID need not be the lot number, but nothing links the two. (The same problem is plastics/06#F14 seen from the waybill.)
- Condition: the lot is identified the same way in 06 and 08, or the two identifiers are evidently different things and both documents say which.
- Options: (a) use `RR-PE-0416` as the waybill's trace ID too (preferred: the lot is the seller's identifier for recall); (b) keep both and let the waybill carry the lot in its item.
- Needs decision: no
- From: broad (F3), logistics (F3), context (F6)

### plastics/08#F6 · Low · Best-before and expiry date on polymer granulate
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:BestBeforeDate` = `2027-04-16`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:ExpiryDate` = `2027-04-16`
- Why: BestBeforeDate is "The date before which it is best to use this item instance", a notion from perishables; the lot's ExpiryDate repeats the same date, exactly one year after manufacture. PE granulate does not expire (own knowledge); recyclers sometimes recommend processing within a period (moisture, odour), but then one date with that meaning would do. An expiry date says the lot must not be used afterwards, stronger than any reason visible here. It looks like a default pair (IND5).
- Condition: at most one such date, with a business reason (e.g. a recommended processing period), or none.
- Options: (a) keep a best-before date as recommended processing period and drop the expiry date (broad's preference); (b) drop both (context's preference). The merge prefers (b) unless the world gives the granulate a processing period.
- Needs decision: no (context said yes; the change concerns the encoding of one lot, not the story)
- From: broad (F4), context (F5)

### plastics/08#F7 · Low · Status codes "NoStatus"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: A status code signifies the status of the document or line; `NoStatus` ("No status on document") says there is nothing to state, which absence would say as well (IND5/IND6). Context counted the document-level code 26 times in the examples (`grep -rho --include='*.xml'`).
- Condition: the status codes are absent, or carry a status with a reason (e.g. a replacement).
- Options: remove both (preferred).
- Needs decision: no
- From: broad (F5), context (F4)

### plastics/08#F8 · Low · Recycled-content certificate issued by a chamber of commerce
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: EnvironmentalCertificate/IssuerParty is "The authorised Organisation who issues this Certificate". In the world the Ferrano Chamber of Commerce issues certificates of origin and ATA carnets (`road/06-CertificateOfOrigin.xml`, `carnet/01-GoodsItemPassport.xml`, per parties). Recycled content is normally certified by an accredited certification body auditing the recycler, or supervised by the environment authority (own knowledge, e.g. EN 15343, ISO 14021 claims). The remark "Made entirely from sorted production waste recovered in Urvania" reads like an origin statement, which would fit the chamber, but the certificate type is RECYCLED.
- Condition: the issuer of the recycled-content certificate is an organisation the world authorises to certify recycled content, or the world records why the chamber does.
- Options: (a) a certification body or the Urvanian environment authority as issuer (preferred); (b) keep the chamber and record its role in the story.
- Needs decision: yes (changes who certifies)
- From: parties (F8), context (F11)

### plastics/08#F9 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: The ID has schemeID `urn:ubl-examples:world:item` but is 12 digits with a correct GS1 check digit (recalculated in the merge: weights 3/1 from the left over 7 7 1 0 3 0 0 0 0 0 4 give 52, check digit 8). As a GTIN-12 (UPC-A, GTIN-13 `0771030000048`) its GS1 prefix 077 lies in the range 060–139 that GS1 US issues to real companies (own knowledge). It could be taken for a real GTIN; the merge could not check the real register. The same number is in 01, 05, 09 and 10 (`grep -rl --include='*.xml' 771030000048 world/examples`).
- Condition: the item number cannot be mistaken for a real GTIN (another format, or a wrong-length/non-GS1 form), or its absence from the real register is verified and recorded.
- Options: (a) a non-GTIN format for the world's item scheme (preferred); (b) record the verification in the sources.
- Needs decision: yes
- From: broad (F10)

### plastics/08#F10 · Low · Rivermouth's bank account in a despatch advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". A despatch advice moves no money and has no amounts, payment means or terms; the account is copied master data (section 4.8). It has a purpose in `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
- Condition: the despatch advice carries no party financial account.
- Options: drop it (preferred).
- Needs decision: no
- From: broad (F7, first part), money (F1), parties (F4), context (F7)

### plastics/08#F11 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The permit to recover plastic waste (Basel Annex IV R3) has no role in announcing a delivery of a product (HS 390110). The recycled-content claim has its own certificate on the item (F8). Master data copied into every document of the flow (IND5).
- Condition: the permit appears only in documents that act on it, or the document says why it is relevant.
- Options: (a) remove it (preferred); (b) link it to the item's environmental certificate if the claim is to rest on it.
- Needs decision: no (parties said yes; aligned with context and 06)
- From: broad (F7, second part), parties (F5), context (F8)

### plastics/08#F12 · Low · Contacts do not fit the role the party has in this document
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The despatch party's contact is the one who despatched (shipping), the delivery customer's contact receives and checks the goods (the note asks it to); a sales customer service and a sales order desk are neither.
- Condition: each contact handles the task the party has in this document, or is absent.
- Options: (a) role-specific contacts (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad (F8), parties (F3), context (F9)

### plastics/08#F13 · Low · All three companies registered on 1 January 1996
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Three companies in two registers registered on New Year's Day 1996; the parts counted 271 occurrences in 181 example files. A default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained in the story, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (parties said no; aligned with broad, context and the wood merges)
- From: broad (F9), parties (F6), context (F10)

### plastics/08#F14 · Low · Italian text tagged as English
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: Renderings tagged `en-XU` are Italian street names, and the English legal form is Italian with a gloss; a world convention of Italianate exonyms is not visible, and the legal form is not a proper name. Parties counted the pattern in 101 of 250 examples.
- Condition: every rendering tagged `en-…` is English or a proper name used as such, and the convention is recorded.
- Options: (a) record the convention and render the legal form in English (preferred, aligned with the wood flow); (b) translate; (c) drop the second rendering.
- Needs decision: yes
- From: parties (F7)

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `RP-PO-26-0882` and order line 1 resolve to 01; 120 t despatched = 120 t ordered = invoiced in 10, which references this advice (all parts; flow index re-run in the merge).
- Shipment `RR-SH-26-0889`, consignment `RR-CS-26-0885`, gross weight 120 480 kg and carrier Fiumella agree with 05, 06 and 09 (broad, logistics, context).
- Issued 2026-04-19 17:57, after the despatch at 15:10 (06); lot manufactured 2026-04-16, between order (04-13) and despatch (04-19) (broad, logistics, context).
- Type DELIVERY fits a single complete delivery (context). Melt flow index 0.9 g/10 min plausible for film-grade LDPE recyclate; density 0.92 fits "density below 0.94" in the description (broad; the merge).
- The advice carries no prices or values (money). Parties identical across the flow apart from language renderings; IBAN-like account passes `check_ids.py` (parties; re-run in the merge).

## Considered and refuted
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` could be a real ISO 6523 ICD — refuted: the real register's ICDs stay far below 0990 (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `BLUMXBLX` could be real — refuted: positions 5–6 carry a fictional country's code (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: the buyer's customs-trader ID copied from master data — refuted: plausible commercial data in a cross-border trade, needed for the declarations (from parties).
- `/DespatchAdvice/cac:DespatchLine/cac:Item`: item details repeated from the order — refuted: the receiver checks the goods against them (from context).

## Changed in the merge
- logistics/F1, context/F1, broad/F6 → F1 and F4: broad's Low finding split; its expected-delivery part joins the Medium finding on the dates (the document's purpose depends on them), its packages/waybill part joins logistics/F2 (Low).
- broad/F4, context/F5 → F6: Needs decision no (context said yes), preferred option (b) with broad's (a) kept.
- broad/F7 → F10 and F11: split into the account and the permit, combined with money/F1, parties/F4, context/F7 and parties/F5, context/F8.
- parties/F5 → F11: Needs decision changed from yes to no.
- broad/F9, parties/F6, context/F10 → F13: Needs decision yes (parties said no).
- broad/F2, parties/F2, context/F3 → F3: preferred option set to dropping LocaleCode.
- broad/F10 → F9: check digit recalculated and the GS1 prefix range added.
- parties/F7 → F14: preferred option aligned with the wood flow.
- Combined without change of severity: broad/F1, parties/F1, context/F2 → F2; broad/F3, logistics/F3, context/F6 → F5; broad/F5, context/F4 → F7; parties/F8, context/F11 → F8; broad/F8, parties/F3, context/F9 → F12.
