# LLM review: 12-DespatchAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/12-DespatchAdvice.xml`, Git blob `d93dffcfbe79b292ad495776e25413987734c7cc` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/12#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". 0.82 × 1 EA = 0.82 kg CO2e, not 96 kg; 96 / 0.82 = 117.1 matches no quantity in the document. The values are copied from 02-Catalogue; the same factor is in 39 XML files (recounted in the merge).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) state the activity and its unit so that factor × activity = 96 kg; (c) drop the emission from the despatch advice (see F13).
- Needs decision: no
- From: broad, context, logistics

### retail/12#F2 · Medium · Each pallet lists itself as the one package it contains
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TransportHandlingUnitTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:DeliveredQuantity` = `4`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `095206100000122217`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:Quantity` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[2]/cac:ActualPackage/cbc:ID` = `095206100000122234`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:ActualPackage/cbc:ID` = `095206100000122251`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[4]/cac:ActualPackage/cbc:ID` = `095206100000122268`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[5]/cac:ActualPackage/cbc:ID` = `095206100000122285`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[6]/cac:ActualPackage/cbc:ID` = `095206100000122302`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks` = `One carton torn, the bench's armrest bent.`
- Why: `ActualPackage` is "A package contained in this transport handling unit" and its `Quantity` "The quantity of items contained in this package". Each handling unit is a pallet (`PX`, an SSCC) with `TotalPackageQuantity` 4 and four benches, but the one package listed inside it is again a pallet (`PX`), identified by a GRAI (the returnable pallet itself), holding one item. A pallet does not contain a pallet; the returnable pallet is the handling unit's own carrier, and the four packages it does contain are nowhere described. 17-ReceiptAdvice and 19-CreditNote speak of a torn carton, so the packages are cartons of one bench each. The same pattern is in all six handling units (verified in the merge; the broad part's "pallets 2 to 6 carry no such package" is not correct). Not High, as logistics proposed: `TotalPackageQuantity` 4 and one listed `ActualPackage` do not contradict each other by count (a handling unit need not list every package); the problem is the meaning of the listed package.
- Condition: in every handling unit, the packages listed are what the pallet carries, consistent with `TotalPackageQuantity` and the goods; the returnable pallet, if identified, is identified as the handling unit's own equipment, the same way on all six pallets.
- Options: (a, preferred) four `ActualPackage` per unit as cartons (Rec. 21 `CT`), one bench each, and the pallet's GRAI moved to the handling unit (e.g. as a returnable-equipment reference); (b) drop `ActualPackage` and keep `TotalPackageQuantity`; (c) if the benches travel unpacked (08's item mentions only "Stretch film and pallet straps" as packaging waste), no packages, and 17 and 19 must not speak of cartons.
- Needs decision: no
- From: broad, context, logistics (High there)

### retail/12#F3 · Medium · The despatch advice gives no despatch date, delivery place or expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0230`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-04-29`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: a despatch advice tells the receiver what was despatched and when and where it will arrive, so that goods-in can prepare the receipt (the note asks the receiver to check the goods on arrival). Neither the document nor the shipment has a `Delivery` or `Despatch`: no actual despatch date, no delivery location (the order asked for goods-in `9522610900019`), no estimated delivery. The only date is the issue date, and nothing may be implied by absence.
- Condition: the despatch advice states when the goods were despatched, and where and when they are expected (delivery location with the order's GLN, estimated delivery date or period).
- Options: (a, preferred) `Shipment/Delivery` with `DeliveryLocation` `9522610900019`, `Despatch/ActualDespatchDate` (and time) and an estimated delivery period; (b) at least the delivery location and an estimated delivery date.
- Needs decision: no
- From: logistics

### retail/12#F4 · Medium · Issued after the forwarder's expected arrival, and the delivery day differs between the documents
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:34:00`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: by 11:49 on 2026-04-29 the truck was on its way and expected at the store at 14:00 (15). This despatch advice, which should reach the receiver by the time of despatch so that goods-in can prepare, is issued at 15:34, after that expected arrival. 17-ReceiptAdvice then records receipt on 2026-04-30, which does not fit a 14:00 arrival on the 29th for a 38 km trip (`16-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`). Either the goods left on the morning of the 29th and arrived that afternoon (then this advice is late and 17's date is wrong), or they arrived on the 30th (then 15 does not fit). The broad part put this under "Outside this review" (timeline); the merge keeps it as a finding, as logistics did and as retail merge c does for 15 and 17, because it is one consignment and the despatch advice's own issue time is involved. A despatch advice issued after despatch is not wrong by itself, which is why it is not High.
- Condition: the despatch advice is issued no later than the despatch, and despatch, the forwarder's status and the receipt describe one consistent sequence.
- Options: (a, preferred) issue the despatch advice at loading (before the "on its way" status of 11:49) and make the delivery day the same in 15 and 17; (b) if delivery was on 2026-04-30, move the departure and the status 15 to that day.
- Needs decision: yes (which day the benches were delivered is part of the story)
- From: logistics (broad: under "Outside this review")

### retail/12#F5 · Medium · Language codes in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is a language code and names no locale. 362 such elements in 213 XML files (recounted in the merge).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list.
- Needs decision: no
- From: broad, context, parties

### retail/12#F6 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; "Gate 3" is a vehicle entrance of the distribution centre, not a street name. 79 occurrences in 76 XML files (recounted).
- Condition: no `AdditionalStreetName` of Lumeway holds the gate; where the despatch needs it, it is given in a despatch or pick-up location.
- Options: (a, preferred) drop it from the postal address (party master data); (b) if Bayvarra's address format makes the gate part of the postal address, record that and dismiss the finding.
- Needs decision: no
- From: broad, parties

### retail/12#F7 · Medium · A life-cycle boundary code in FullnessIndicationCode
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty". In a despatch advice with a truck the element could carry a real fullness, but here it carries the footprint's system boundary (list `EmissionBoundaryCode`; 39 XML files). UBL 2.5 has no element for the boundary: a candidate for the TC write-up.
- Condition: `FullnessIndicationCode` holds no system-boundary code.
- Options: (a, preferred) drop it; record the missing element for the TC write-up.
- Needs decision: no
- From: context

### retail/12#F8 · Medium · Life-cycle stage code says manufacturing (A3), the description says ore to factory gate (A1–A3)
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: the world's list defines `MANUFACTURING` as "Making the product (EN 15804 module A3)" and `SOURCING` as "Raw material supply and its transport (EN 15804 modules A1 and A2)"; the description covers A1 to A3. Code and text describe different stages.
- Condition: stage code and stage description cover the same stage(s).
- Options: (a, preferred) omit the code; (b) two emission entries with their shares.
- Needs decision: no
- From: added by the merge (no part raised it), aligned with retail merges a and c, road and rail

### retail/12#F9 · Low · Despatch line ID 1 used twice, with 4 and with 24 benches
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:HandlingUnitDespatchLine/cbc:DeliveredQuantity` = `4`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cac:DespatchLineReference/cbc:LineID` = `1`
- Why: both are despatch lines ("An identifier for this despatch line"). The six handling units carry despatch lines `1` to `6` with 4 benches each (each referring to order line 1), and the document-level despatch line is also `1`, with 24. The receipt advice, invoice and credit note refer to "despatch line 1 of LD-DA-26-0229", which can be read as either. The logistics part rated this High. The merge lowered it: the quantities agree (6 × 4 = 24), `LineCountNumeric` 1 counts the document's despatch lines, and the per-pallet lines can be read as the breakdown of line 1, so no value contradicts another; what remains is an ambiguous ID. Aligned with retail merge c (17's receipt line IDs) and 08's substitute line.
- Condition: every despatch line ID in the document identifies one line, or the handling-unit lines are recognisably the breakdown of line 1.
- Options: (a, preferred) IDs such as `1-1` … `1-6` for the per-pallet lines; (b) drop the per-pallet lines and state the content per pallet through `TotalPackageQuantity`.
- Needs decision: no
- From: broad, context, logistics (High there)

### retail/12#F10 · Low · Truck and an empty goods item on one of six pallets
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `BV LP 2203`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:GoodsItem/cbc:ID` = `1`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[2]/cbc:TotalGoodsItemQuantity` = `1`
- Why: the truck (BV LP 2203 with trailer BV TR 0817) carries all six pallets, but `TransportMeans` ("A means of transport associated with this transport handling unit") is given on the first pallet only. Pallets 2 to 6 each declare `TotalGoodsItemQuantity` 1 but contain no goods item, and pallet 1's goods item has only an ID. The reader cannot tell what pallets 2 to 6 travel on or what their goods item is.
- Condition: data that apply to the whole shipment are given once for it (or on every unit); each declared goods item exists and is described.
- Options: (a, preferred) move the vehicle to the shipment (e.g. `ShipmentStage/TransportMeans`) and drop the empty goods item and the units' `TotalGoodsItemQuantity`; (b) repeat vehicle and a described goods item on every pallet.
- Needs decision: no
- From: broad, context, logistics

### retail/12#F11 · Low · The shipping-document reference points to the transport request, not to the consignment note
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ShipmentDocumentReference/cbc:ID` = `LD-TR-26-0227`
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`
- Why: `ShipmentDocumentReference` is "A reference to a shipping document associated with this transport handling unit". The referenced document is 11-TransportExecutionPlanRequest, Lumeway's booking request, which Brightmarket never receives. The shipping document that travels with the goods, and that the note asks the receiver to use, is the consignment note 13-Waybill, issued at 08:56 the same day. The reference is also on one of six pallets only.
- Condition: the shipping-document reference, if present, refers to the document that accompanies the goods, at shipment level or on every handling unit.
- Options: (a, preferred) reference `BF-WB-26-0231` at shipment or consignment level; (b) drop it and let the note name the consignment note's number.
- Needs decision: no
- From: broad (logistics and context had it inside F10's problem; split, because the reference has the wrong target as well as the wrong place)

### retail/12#F12 · Low · Contacts that do not fit the parties' roles in the despatch
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- Why: the delivery customer's contact receives and checks the goods, as the note asks; the order names that contact (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`), but here Brightmarket's buying office is given, with a job title and department that also contradict its name. Lumeway as despatch party is represented by its sales customer service, although the order names its `Dispatch office`. Bayforth, the carrier of a domestic haul (Marrowdale to Lumeport), is represented by its "Export desk".
- Condition: each party's contact fits its role in the despatch, and name, job title and department agree.
- Options: (a, preferred) Brightmarket's goods-in, Lumeway's dispatch office, a Bayforth domestic or road desk.
- Needs decision: no
- From: broad, parties

### retail/12#F13 · Low · The despatch line carries the item's full catalogue description
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:EnvironmentalEmissionTypeCode` = `CO2E`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a despatch advice identifies what is shipped; the lot and manufacture date (`ItemInstance`) belong here. The seller's sales conditions, the footprint, circularity profile, load test, dimensions and Urvania's customs tariff code (in a domestic Bayvarran delivery) do not, and nothing in the despatch uses them.
- Condition: the despatched item carries its identifiers, the lot data and what despatch and receipt depend on.
- Options: (a, preferred) drop the catalogue data from the item.
- Needs decision: no
- From: broad, context (context had it together with the party master data; split, as in road and rail)

### retail/12#F14 · Low · Party master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: a domestic despatch advice uses neither the parties' share capital, nor Brightmarket's logo, web shop and social media, nor Lumeway's customs trader number (no customs in this flow) (IND5/IND6). `CorporateStockAmount`'s definition ("The number of shares in the capital stock of a corporation") against its amount type is a candidate for the TC write-up (parties part).
- Condition: the parties carry what despatch and receipt use.
- Options: (a, preferred) drop them here; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context, parties

### retail/12#F15 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:ID` = `095206102170000014`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: Lumeway's GLN, its SSCCs in this document and the GTIN of Valdara's bench share the company prefix 9520610. The item is Valdara's (brand, manufacturer in Urvania); under GS1's allocation rules (own knowledge of the parties part) the brand owner allocates the GTIN from its own prefix. All check digits are correct (`check_ids.py`, run in the merge).
- Condition: Valdara's GTINs and Lumeway's GLNs/SSCCs/GRAIs are under different company prefixes, or the story states that Lumeway allocated the GTINs.
- Options: (a, preferred) give Valdara its own company prefix; (b) state in the story that the distributor allocated the GTINs.
- Needs decision: yes
- From: parties

### retail/12#F16 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is shared by 25 different companies in three countries (parties part; 271 occurrences in 181 files, earlier merges' count), among them Bayforth, while other parties have dates of their own. It looks like a filler.
- Condition: Bayforth's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) a date from Bayforth's history; (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties

### retail/12#F17 · Low · "No status" codes on the document and the line
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "the status of the Despatch Advice with respect to its original state" and `LineStatusCode` "the status of this despatch line with respect to its original state". An original despatch advice has no status to report; `NoStatus` states nothing (IND5/IND6). The broad part refuted the line code as an explicit default; the merge does not follow it, as in the earlier flows.
- Condition: status codes only for a revised, cancelled or disputed document or line.
- Options: (a, preferred) drop both.
- Needs decision: no
- From: context (broad: line code considered and refuted)

### retail/12#F18 · Low · World item number that is a valid GTIN-12
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: the world item number (`urn:ubl-examples:world:item`) has a valid GS1 mod-10 check digit (recomputed: 7) and reads as a GTIN-12 in GS1's US/Canada range; fictional values must not be mistaken for real ones. Not checked against GS1's register.
- Condition: the world item number cannot be mistaken for a real GTIN, or its absence from GS1's register is recorded.
- Options: (a, preferred) a world item-number format that is not a valid GTIN; (b) record a register check in the sources.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail merges a and c, rail, road and plastics

## Checked and consistent
- Counts, redone in the merge: 6 handling units × 4 benches (`HandlingUnitDespatchLine` 4 each, `TotalPackageQuantity` 4 each) = 24 = `DespatchLine/DeliveredQuantity` = order line 1 of 08-Order = invoiced quantity of 18; shipping marks "001 of 006" to "006 of 006"; six SSCCs and six GRAIs.
- Weight: 996 kg / 6 = 166 kg per pallet; less a long wooden pallet of about 25–30 kg (own estimate), 34–35 kg per bench in its carton, plausible for a 1.8 m cast-steel and hardwood bench (material consumption 34 kg + 22.5 kg before losses). Four benches of 1800 × 620 × 780 mm per pallet, stacked two by two: about 1800 × 1240 mm, 1560 mm plus pallet, which fits a trailer's inner height of about 2.6 m (own knowledge). Six such pallets need 6 × 1.24 m = 7.4 m of loading length crosswise, or 10.8 m lengthwise; the stated 13.6 m is enough either way.
- `TransportMeansTypeCode` 395 (Rec. 28 "Truck, with trailer") agrees with the separate trailer plate.
- Shipment `LD-SH-26-0230`, consignment `LD-CS-26-0228`, 996 kg and carrier Bayforth agree with 11 and 13; order reference `BS-PO-26-0224` and order line `1` resolve to 08-Order; buyer's item ID `BM-551210` and the grey variant are the ordered ones, not the substitute.
- SSCCs `095206102170000014` … `095206102170000069`, the GRAIs, GLNs and the GTIN pass their check digits (`check_ids.py`, run in the merge); the SSCC of pallet 3 (`095206102170000038`) is the one 17 reports as damaged.
- Parties are described identically in every retail example (parties part); register IDs agree with `CompanyID` and endpoint IDs.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:TraceID` = `095206102170000014`: suspected a filler repeating the SSCC — refuted: the SSCC is the trace identifier GS1 logistics labels carry (from broad).
- `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cac:ActualPackage/cbc:ID` = `095206100000122217`: its digits after the leading 0 begin with the bench's GTIN `9520610000012` — refuted as a finding because GRAI and GTIN are different GS1 keys; noted because it may confuse a reader (from logistics).
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`: refuted because the world's list distinguishes despatch types and a delivery to the customer is the intended type (from context).
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `996`: the shipment weight "plus transport equipment" equal to the consignment weight in 11 — refuted: with the pallets counted as packaging and no other equipment, the figures can coincide (from context).
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted because the definition fits a business park (from parties).
- The broad part's refutation of `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus` was not followed; see F17.

## Changed in the merge
- broad/F1, context/F1, logistics/F3 → F1: combined.
- broad/F2 (Medium), context/F2 (Medium), logistics/F2 (High) → F2: Medium; broad's statement that pallets 2–6 carry no package corrected (all six do); logistics' carton argument and option added, plus option (c).
- logistics/F4 → F3: kept Medium.
- logistics/F5 → F4: kept Medium/yes, aligned with retail merge c (15, 17); broad's "Outside this review" note folded in as the counter-argument.
- broad/F3, context/F3, parties/F1 → F5; broad/F4, parties/F2 → F6: combined.
- context/F4 → F7: kept.
- F8 (MANUFACTURING) and F18 (world item number): added by the merge.
- logistics/F1 (High), broad/F7, context/F5 (Low) → F9: Low, with the reason.
- broad/F6, context/F6 and logistics/F6 (vehicle and goods item) → F10; broad/F5 with the reference halves of context/F6 and logistics/F6 → F11.
- broad/F8, parties/F6, F8, F10 → F12: all contacts of the example in one finding.
- broad/F9, context/F8 (item half) → F13; context/F8 (party half), parties/F4, F5, F7 → F14; parties/F5 (CorporateStockAmount) Needs decision yes → no with its TC note.
- context/F7 → F17: kept Low/no; broad's refutation recorded as not followed.

## Outside this review
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-26`: the lot was made by Valdara in Urvania on Sunday 2026-04-26, three days before despatch from Lumeway's stock in Marrowdale, while the item is described as "from the distributor's stock"; whether manufacture, the cross-border transport and stocking fit in three days is a timeline question across flows (from broad, context, logistics).
