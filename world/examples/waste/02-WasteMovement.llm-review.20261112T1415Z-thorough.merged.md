# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/02-WasteMovement.xml`, Git blob `32c42c37c829fb72899a0b9b0b8748b5caf542d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit e6f29b5 2026-11-12 Reviews of the waste flow, run 20261112T1415Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

This merged file combines the parts broad, money, parties, logistics and context of run
`20261112T1415Z-thorough`; all five parts reviewed the same Git blob as this file.

## Findings

### waste/02#F1 · High · The weight statement the movement refers to does not exist
- XPath: `/WasteMovement/cac:WeightStatementDocumentReference/cbc:ID` = `RR-WB-26-0412`
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: `WeightStatementDocumentReference` is "A reference to a Weight Statement document", a UBL 2.5 document type of which the repository has an example (`cotton/12-WeightStatement.xml`). No example has the ID `RR-WB-26-0412` (`grep -rl --include='*.xml' 'RR-WB-26-0412'` finds only this file, re-checked in the merge; `flow_index.py` resolves it to `?`). The weight statement is the source of the only weight in this document and, through it, of the quantity billed in `03-Invoice.xml` (`03-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`), so the figure, and whether it is gross or net (F3, and F1 of 03's review), cannot be traced.
- Condition: the reference resolves to a Weight Statement example of the flow whose weights (gross, tare, net) agree with this movement and with the invoiced quantity; or the reference is not a `WeightStatementDocumentReference` (a plain, typed `DocumentReference` to a document the flow does not model), and the weights are stated in this document.
- Options: (a) preferred: add a Weight Statement (Rinova's weighbridge ticket, gross/tare/net) to the flow, because the flow bills by weight and it settles the gross/net question; (b) describe the weighbridge ticket as a plain `DocumentReference` with its type and date, if the world's weighbridge issues no UBL weight statements, and give the weights here.
- Needs decision: yes
- From: broad (F1), logistics (F1), context (F7, Low, together with `RR-REC-26-0412`)

### waste/02#F2 · Medium · A report of the transport of waste that says neither when nor where the waste moved
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cbc:IssueDate` = `2026-04-02`
- Why: the WasteMovement is "A document used to report the transport of waste". It is issued by the recovery facility and references a weighbridge statement and a further document `RR-REC-26-0412`, so it reports a movement that has taken place; but the shipment has no `ShipmentStage` (loading, departure, arrival), no `Delivery` (e.g. `ActualDeliveryDate`, "The actual date of delivery"), no transport means (vehicle registration) and no place of loading or delivery. The only date is the issue date. When the waste left the producer and when the facility received it are the core of a movement document (Basel Annex V B; own knowledge), and they are needed to check the movement against the notified period and the consent.
- Condition: the shipment states at least when and where the waste was taken over and when it was delivered at the recovery facility, all no later than the issue time 2026-04-02 12:34, and preferably the vehicle used; or, if the document is meant to be issued before departure, it gives planned dates and drops the references to weighing and receipt.
- Options: (preferred) add `cac:Shipment/cac:Delivery` with `cbc:ActualDeliveryDate`/`ActualDeliveryTime` and `DeliveryLocation` at Rinova, and a main-carriage `ShipmentStage` with the road vehicle and loading/departure (pickup) at Valdara, the dedicated elements; alternatively at least the delivery.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F1)

### waste/02#F3 · Medium · Only a gross weight is reported; the net quantity of waste is missing
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: `GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The quantity of waste moved, which the movement report exists to state and which the invoice bills "per tonne collected" (`03-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`), is the weight without packaging and equipment: `cac:Shipment/cbc:NetWeightMeasure`, `NetNetWeightMeasure`, or the goods item's net weight. None is given, nor the number of big bags (`TotalTransportHandlingUnitQuantity`, a package or handling-unit count). The invoice bills exactly 38.2 t, the gross figure (finding F1 in 03's review).
- Condition: the document states the net weight of the waste (and preferably the number of bags), and the net weight is lower than the gross weight by the weight of bags and transport equipment.
- Options: (preferred) add `NetWeightMeasure` (and `GrossWeightMeasure`/`NetWeightMeasure` on the goods item) taken from the weight statement, plus the bag count; alternatively, if 38 200 kg is in fact the net weight of the waste, move it to the net element and give a gross weight that includes bags and equipment (then see F7).
- Needs decision: no
- From: logistics (F3); see also money's refuted candidate under "Considered and refuted"

### waste/02#F4 · Medium · A domestic movement reported to the customs administration's border office
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-WasteNotification.xml:/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: the waste moves from Valdara (Ferrano, XU) to Rinova (Ferrano, XU); no border is crossed and no other country is named, yet the movement is reported to the customs "Border office". The notification it refers to names the same customs administration as `CustomsParty`, "The competent authority granting a permit to export or import the waste", for a movement without export or import (F1 of 01's review). The receiver is therefore not an authority that fits the movement. The carrier's "International road haulage" licence adds to the impression of a cross-border story (`/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`), but its scope is not itself wrong (see F17).
- Condition: the receiver of the movement document is the authority the notification names as competent for this movement, and that authority fits the movement (an export/import authority only for a transboundary movement), in agreement with `01-WasteNotification.xml`.
- Options: follow the decision taken for the notification: (a) make the movement transboundary (facility or route in another country), so document type, receiver and authorisation fit (preferred by context and the merge, as in 01); (b) a competent Urvanian waste/environment authority as receiver, the same party as in the notification (preferred by parties for a domestic story); (c) keep customs only if the world makes it the competent authority for waste, and say so in the world. This finding resolves with 01's F1.
- Needs decision: yes
- From: broad (F3), parties (F2), context (F3)

### waste/02#F5 · Medium · Rinova named as disposal facility for a recovery movement
- XPath: `/WasteMovement/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY`
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material". The movement is of type Recovery, and Rinova's permit covers recovery operation R3 only; no disposal is reported. Naming Rinova as disposal facility as well as recovery facility says something the type code and the permit deny (same as F2 of 01's review, `01-WasteNotification.xml:/WasteNotification/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`).
- Condition: `DisposalFacilityParty` is present only for a disposal operation that is part of this movement, naming the party that performs it; otherwise only `RecoveryFacilityParty` identifies Rinova.
- Options: remove `DisposalFacilityParty` (preferred), consistently with the notification; or name a separate disposal party with its own authorisation if residues are disposed of.
- Needs decision: no
- From: broad (F4), parties (F3), context (F4, Low)

### waste/02#F6 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`, as the world does for Bayvarra's states (799 occurrences over `*.xml`, parties part). `<cbc:Region>Province of` occurs 219 times in 104 examples (re-counted in the merge with `grep -ro`/`grep -rl --include='*.xml'`).
- Condition: no address in this example carries a province in `Region`; a province, where given, is in `CountrySubentity`.
- Options: move the province to `CountrySubentity` for all Urvanian addresses, as for Bayvarra (preferred); or drop it where the postal zone suffices.
- Needs decision: no
- From: broad (F5), parties (F1), context (F2)

### waste/02#F7 · Low · 38 200 kg for one road load of bagged polyethylene waste is hardly plausible
- XPath: `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `4923`
- Why: one movement by a road haulier (ISIC 4923) is one lorry load. Figures (own knowledge): gross combination weight limit 40 t (44 t in some countries); tractor about 7.5 t, curtain-side semi-trailer about 7 t, payload about 25 t; trailer inner space 13.6 × 2.45 × 2.7 m = 90 m3; big bag about 0.89 m3; bulk density of sorted PE production waste 0.05–0.2 t/m3 (film, offcuts) to 0.25–0.45 t/m3 (regrind, lumps). Calculation (logistics, redone in the merge): 60 bags = 53 m3 × 0.45 t/m3 = 24 t of waste at most. 38.2 t gross less the trailer (which UBL counts as transport equipment) leaves 31.2 t: above the payload, and needing 69 m3 (78 bags where 60 fit). If 38.2 t is the net waste (as the invoice treats it), it needs 85 m3 even at 0.45 t/m3, and 38.2 + 14.5 t vehicle = 52.7 t exceeds the limit. Counter-argument (broad part): if the 38 200 kg is the whole loaded vehicle including the tractor, the load is about 23–24 t, plausible for dense PE scrap at about 0.3–0.45 t/m3 in large bags. Only that reading passes, and the document does not say which applies; hence a decision.
- Condition: the weights of one movement fit one road vehicle's payload and loading space at the bulk density of the described waste (for bagged PE waste roughly 10–24 t net), and the invoice quantity follows the corrected net weight.
- Options: (preferred) about 20–24 t net with a consistent gross, and `03-Invoice.xml` adjusted; alternatively describe the waste as denser (baled, compacted) with a bag/bale count that makes the weight fit.
- Needs decision: yes
- From: logistics (F5); broad (physics under "Checked and consistent", as counter-argument)

### waste/02#F8 · Low · Shipment and consignment IDs of the notification reused for the first of twelve movements
- XPath: `/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteMovement/cbc:SequenceNumberID` = `1`
- XPath: `01-WasteNotification.xml:/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- Why: the notification plans 12 shipments (`01-WasteNotification.xml:/WasteNotification/cbc:ConsignmentQuantity` = `12`) under the shipment `01-WasteNotification.xml:/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205` with 40 000 kg; this movement, number 1 of 12, uses the same shipment and consignment IDs with 38 200 kg. Either the notification's shipment is the planned pattern for all twelve (then movements 2–12 would share these IDs, and the ID does not identify this movement) or it is this actual shipment (then the notification described one of twelve).
- Condition: each movement can be told apart from the notification's planned shipment and from the other movements by its shipment/consignment identifier, its relation to the notification carried by `WasteNotificationDocumentReference` and `SequenceNumberID`; or the documents say that the notification's weight is a planned value for this same load.
- Options: (preferred) give the movement its own shipment/consignment ID; alternatively keep the IDs and mark the notification's weight as planned. Resolve together with F6 of 01's review.
- Needs decision: yes
- From: broad (F6), logistics (F6)

### waste/02#F9 · Low · The second document reference does not say what it is and cannot be linked
- XPath: `/WasteMovement/cac:DocumentReference/cbc:ID` = `RR-REC-26-0412`
- Why: `DocumentReference` is "A reference to a relevant document associated with this Waste Movement". It carries only an ID, no `DocumentTypeCode`, `DocumentType` or issue date, and no example has this ID (re-checked over `*.xml`; `flow_index.py`: `?`). From the prefix it may be a receipt (Receipt Advice, a UBL document type) or a certificate of recovery; neither exists in the flow. If it is a certificate of recovery, it would normally follow the recovery, later than receipt; with no dates in the document this cannot be checked.
- Condition: the reference states its document type (and its date), and either resolves to an example of the flow or is a document type the flow does not model, said so in `cbc:DocumentType`.
- Options: (preferred) state the type (`cbc:DocumentType`, e.g. "Certificate of recovery") and its issue date; if it is a Receipt Advice, add it to the flow; or remove the reference if it has no role here.
- Needs decision: yes
- From: broad (F7), logistics (F4, Medium), context (F7, together with `RR-WB-26-0412`)

### waste/02#F10 · Low · The movement shows no consent of the competent authority
- XPath: `/WasteMovement/cac:WasteNotificationDocumentReference/cbc:ID` = `VI-DOC-26-0204`
- Why: a movement under a notification takes place only after the competent authority has consented to the notification (Basel/OECD procedure; own knowledge). The movement refers to the notification only; no document of the flow and no reference here records a consent or its number, so the movement 10 days after the notification has no visible authorisation. Broad noted the same in its 01 review (F1 there).
- Condition: either the flow shows the consent (a referenced document or authorisation with its ID and validity covering 2026-04-02), or the story states that no consent is needed (a domestic movement, or green-listed waste for which information suffices).
- Options: (preferred) add a `DocumentReference` to the consent with `cbc:DocumentType` and issue date; alternatively make the story explicit (depends on 01's F1).
- Needs decision: yes
- From: logistics (F8)

### waste/02#F11 · Low · The goods item does not identify the waste by code
- XPath: `/WasteMovement/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: the goods item description is "Text describing this goods item to identify it for customs, statistical, or transport purposes"; a waste movement document identifies the waste by its classification code (Basel/national waste list; own knowledge), which the facility checks against its R3 permit. Only free text is given, here and in the notification (F4 of 01's review).
- Condition: the goods item carries the same structured waste code as the notification.
- Options: (preferred) add `cac:Item/cac:CommodityClassification` with the waste code, identical in both documents.
- Needs decision: no
- From: logistics (F7)

### waste/02#F12 · Low · Notifier's capital-market and service-provider master data copied into the movement document
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the notifier's share capital, stock-exchange listing and warehousing-and-despatch provider (Castrano Logistics, neither carrier nor any other party of the movement; the carrier is Trasvia Haulage) have no function in reporting a waste transport. The same Valdara blocks occur in 75 examples each (`grep -rl --include='*.xml' -F 'VI-SP-2026-01'`, `'XU0001042501'`), i.e. master data copied into every document (section 4.8).
- Condition: every party detail present has a use in the movement document.
- Options: (preferred) leave these elements out, or reduce `NotifierParty` to identification and name as for `WasteProducerParty`; if Castrano acts in the movement, give it a role the document uses, consistent with the carrier.
- Needs decision: no
- From: broad (F8), parties (F5), context (F5)

### waste/02#F13 · Low · Contacts that do not fit the authority, the notifier and the reporting facility
- XPath: `/WasteMovement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteMovement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the movement report is handled by the authority's office for waste-movement consents, not a border office (no border is crossed, F4). The notifier's contact is Valdara's sales order desk, the same contact Valdara carries in all its 75 examples whatever its role ("Order desk" in 87 examples, `grep -rl --include='*.xml'`); questions about the notified waste go to whoever answers for it (environment/HSE, plant). The reporting facility's contact is "Customer service" in Sales; broad and context expected the people responsible for receipt (goods-in, weighbridge, plant), while parties argued that Rinova's customer service deals with its customers' waste deliveries. The merge keeps that place as the weakest line (see "Considered and refuted").
- Condition: the authority's contact handles waste movements; the notifier's contact answers for the notified waste; the facility's contact answers for the receipt of the waste.
- Options: (preferred) role-specific contacts (waste-permits office, environmental officer, goods-in/weighbridge); or omit the contacts.
- Needs decision: no
- From: broad (F8), parties (F7), context (F5)

### waste/02#F14 · Low · Customs administration described as a company in the commercial register
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the receiver is a public administration (ISIC 8411). A government authority is not entered in the commercial register and has no liquidation status. All four public bodies of the world are described this way, in 23 examples (parties part).
- Condition: the authority's legal entity, if present, has no commercial-register scheme and no liquidation status, or a scheme that fits public bodies.
- Options: (preferred) keep only the registration name and identifier; or drop `PartyLegalEntity` for the authority.
- Needs decision: no
- From: parties (F6), context (F6)

### waste/02#F15 · Low · VAT registrations of every party in a movement document that does nothing with tax
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007337656`
- Why: the movement document carries no amount, price or tax. `PartyTaxScheme` ("A tax scheme applying to this party") is given in full for four parties, including the receiving authority itself, and nothing in the document uses it; the parties are identified by register and customs trader IDs. The invoice that bills this movement (`03-Invoice.xml`) carries the VAT registrations where they are needed. Of the 241 examples with `cac:PartyTaxScheme`, 154 are of non-financial document types (money part; the 241 re-counted in the merge).
- Condition: every `PartyTaxScheme` in the movement document has a stated reason in this document, or is absent.
- Options: (a) preferred: remove `PartyTaxScheme` from all parties; (b) keep it only where the world's waste-movement rules ask for a tax ID, and remove it from the authority and the carrier.
- Needs decision: no
- From: money (F1), parties (F5, the authority's VAT number), context (F6, the authority's VAT number)

### waste/02#F16 · Low · Recovery facility and carrier both registered on 1 January 1996
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The same New Year's Day date is given to 25 different legal entities (parties part; the date occurs in 181 files, re-counted in the merge), while others have individual dates (Valdara `1962-04-12`). It looks like a default (rule "no fillers").
- Condition: each `RegistrationDate` is the party's own registration date in the world, or is absent.
- Options: (preferred) individual plausible dates; or remove the element. If the world has all registers re-founded on 1996-01-01, record that and dismiss.
- Needs decision: yes
- From: parties (F4)

### waste/02#F17 · Low · Carrier's authorisation is a general international haulage licence, not a waste-carrier authorisation
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: for a waste movement the relevant authorisation of the carrier is its permission to carry waste (Basel movement document; own knowledge). The general road haulage licence is the one copied into all 15 Trasvia examples (`grep -rl --include='*.xml' -F 'International road haulage'`). Context read the word "International" as a claim of international carriage that this domestic movement does not use; as in 01's review, the merge treats the scope as not wrong in itself (an international licence covers domestic carriage) and the kind of licence as the finding.
- Condition: the carrier's authorisation here permits it to carry this waste, or is absent.
- Options: (preferred) a waste-carrier registration for Trasvia in the world, shown here; or omit it.
- Needs decision: yes
- From: parties (F8), context (F3, the word "International")

## Checked and consistent
- `WasteNotificationDocumentReference` `VI-DOC-26-0204` resolves to `01-WasteNotification.xml` (a Waste Notification, as the element requires), issued 2026-03-23, before this document (2026-04-02 12:34).
- `ConsignmentQuantity` `12` ("Estimated total number of shipments for the Waste Notification document") equals `01-WasteNotification.xml:/WasteNotification/cbc:ConsignmentQuantity` = `12`; `SequenceNumberID` 1 lies within 1..12.
- `WasteMovementTypeCode` `RECOVERY` uses the list `WasteOperationCategoryCode`, which the world's CVA binds to this element; it agrees with the notification's type and the facility's R3 authorisation.
- Every party shared with `01-WasteNotification.xml` and `03-Invoice.xml` (Valdara XU-R-104274, Rinova XU-R-104548, Customs XU-R-105507, Trasvia XU-R-104822) is described identically (parties part, c14n comparison); goods description and `HazardousRiskIndicator` `false` are the same as in the notification; the carrier's licence `XU-HAUL-2020-0877` is valid to 2030-06-30.
- Sender and signatory are Rinova, the recovery facility that received the waste: a legitimate issuer of a movement report on receipt.
- `DocumentDistribution` to Valdara, "Electronic copy: the producer must keep it with the notification", fits the producer's record-keeping; `DocumentTypeCode` `WasteMovement` names this document.
- Rinova's permit `XU-ENV-2024-0311` is valid until 2029-12-31; R3 fits plastic recovery.
- Gross weight 38 200 kg equals 38.2 t (`TNE`) in `03-Invoice.xml` (unit conversion checked); whether that is right is F3 and F1 of 03's review.
- Money lens: no amounts, prices, taxes, payment means or terms; tax currency XUF matches country XU; the parties billed in 03 are the recovery facility and the producer/notifier here, with the same VAT registrations.
- `check_ids.py`: ISIN `XU0001042501` check digit correct.
- Bilingual renderings (`qau`, `en-XU`) carry the same content.

## Considered and refuted
- `/WasteMovement/cac:SenderParty/cac:PartyName/cbc:Name` = `Rinova Recovery`: the facility, not the notifier or carrier, sends the movement report — refuted because the facility confirms receipt in the movement document (Basel Annex V B) (from broad).
- `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY`: a different list than the notification's `WasteNotificationTypeCode` — refuted because the CVA binds `WasteOperationCategory` to this element and both lists contain `RECOVERY` with the same meaning (from broad, logistics, context).
- `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200` against the notification's 40 000 kg: a contradiction — refuted because the notification gives an estimate, this movement a weighed figure; the identifier question is F8 (from broad, context).
- `/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`: the invoice bills per tonne on this gross weight, which includes the bags' tare — refuted by money because big bags weigh about 2–3 kg each, which does not change the figure at 0.1 t precision. The merge does not share the refutation: the document states no number of bags (money's "12 big bags" confuses the 12 notified shipments with bags; a full load would be about 60 bags, about 150 kg), and by its definition the gross weight also includes the transport equipment (at least the trailer, several tonnes). The candidate is therefore part of F3 here and of F1 in 03's review.
- `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: share capital in a non-financial document — refuted for the money lens (not a transaction amount); it is part of F12 (from money).
- `/WasteMovement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`: a contact unfit for the reporting facility — refuted by parties because Rinova's customer service deals with customers' waste deliveries. Broad and context flagged it; the merge keeps the place in F13 as its weakest line, with both arguments.
- `/WasteMovement/cac:NotifierParty/cbc:IndustryClassificationCode` = `3100`: mismatch with polyethylene production waste — refuted, a furniture maker produces such waste (from parties).
- `/WasteMovement/cac:DisposalFacilityParty/cac:PartyIdentification/cbc:ID` = `XU-R-104548`: whether the facility roles point to other parties than in the notification — they are the same as in `01-WasteNotification.xml`; the role problem is F5 (from parties).
- `/WasteMovement/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`: a customs-trader ID with no use — refuted while the document goes to the customs administration, which knows the trader ID; it falls with F4 (from parties).
- `/WasteMovement/cbc:ConsignmentQuantity` = `12`: should count this movement's consignments — refuted because the element is defined as "Estimated total number of shipments for the Waste Notification document" (from logistics).
- `/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`: a consignment ID used as a document number — refuted: it is used only as the consignment's identifier; F8 is about reuse (from logistics).
- `/WasteMovement/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`: the facility's permit as master-data filler — refuted because a movement report shows that the receiving facility is authorised for the operation (from context).
- `/WasteMovement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Rinova Recovery`: signed by the facility rather than the notifier — refuted because the sender of this report is the facility confirming receipt (from context).
- `/WasteMovement/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: a distribution to a party already in the document — refuted because the distribution states a distinct purpose, the producer's record-keeping (from context).

## Changed in the merge
- broad/F1 + logistics/F1 + context/F7 (`RR-WB-26-0412` part, Low) → F1: High kept (a referenced document that does not exist, section 6); context/F7 split into F1 and F9 because the two references have different problems and severities; the gross weight added as an XPath line for traceability.
- broad/F2 + logistics/F2 + context/F1 → F2: grouped; condition combines logistics' issue-time limit and vehicle with context's alternative (a document issued before departure).
- logistics/F3 → F3: unchanged in substance; money's refuted candidate (bag tare) linked to it.
- broad/F3 + parties/F2 + context/F3 → F4: grouped; the carrier's "International" licence from context/F3 moved to "Why" as context and to F17, because its scope is not wrong in itself.
- context/F4 (Low) → F5: raised to Medium with broad/F4 and parties/F3, because the element names a party in a role its definition does not cover.
- logistics/F5 → F7: broad's physics check (plausible if the gross includes the tractor) added as counter-argument; "Needs decision" changed from no to yes because the merge cannot settle which reading applies.
- broad/F6 (Needs decision: no) + logistics/F6 (yes) → F8: grouped; "Needs decision: yes", because one option changes what the notification's shipment means.
- logistics/F4 (Medium) + broad/F7 (Low) + context/F7 (`RR-REC-26-0412` part) → F9: Low, because the document may be one the flow does not model (a certificate of recovery), so a missing type and date is a completeness remark, not a broken reference; "Needs decision: yes" kept from logistics because one option adds a Receipt Advice to the flow.
- broad/F8 + parties/F5 + context/F5 → F12 (master data) and F13 (contacts): broad/F8 and context/F5 combined both; split so each finding has one condition; the authority's VAT number from parties/F5 moved to F15.
- parties/F7 + broad/F8 + context/F5 (contact parts) → F13: grouped; the facility's `Sales` line kept despite parties' refutation, with both arguments.
- parties/F6 + context/F6 → F14: grouped; the authority's VAT registration from context/F6 moved to F15.
- money/F1 → F15: the authority's VAT number from parties/F5 and context/F6 joined.
- parties/F8 → F17: context/F3's reading of "International" noted; finding limited to the kind of authorisation.

## Outside this review
- Whether the movement on or before 2026-04-02 could take place only 10 days after the notification of 2026-03-23 (time for the authority's consent) is a timeline question across documents (broad, context); the missing consent itself is F10.
- Whether Trasvia Haulage's vehicles, as described in the road flow, could carry this load on the movement date is a cross-flow capacity and timeline question (logistics).
