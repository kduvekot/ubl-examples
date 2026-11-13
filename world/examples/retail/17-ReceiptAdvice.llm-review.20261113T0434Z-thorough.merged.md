# LLM review: 17-ReceiptAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/17-ReceiptAdvice.xml`, Git blob `47b28c9a1fccb7811613ffb860e40b9269d5dddc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### retail/17#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each, the factor says 0.82 kg CO2e per bench, the value 96 kg per bench. Recomputed in the merge: 0.82 × 1 = 0.82 ≠ 96; 96 / 0.82 = 117.1, which matches no quantity of the bench in the flow, so a per-kWh or per-kg reading does not rescue it either. The same triple occurs in 39 XML files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`), copied from 02-Catalogue.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure` (in the base's unit), or factor and base are absent.
- Options: (a, preferred) drop factor and base, as in road, rail and retail a/b: the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg; (c) drop the emission from the receipt advice altogether (context; see F17).
- Needs decision: no
- From: broad (F1), logistics (F2), context (F1)

### retail/17#F2 · Medium · A language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 362 occurrences in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files; recounted in the merge).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F2), parties (F1), context (F2, the LocaleCode half)

### retail/17#F3 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is a vehicle entrance of the distribution centre, not a street name. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address, give it where a vehicle needs it; (b) record it in Bayvarra's address format (finding then dismissed).
- Needs decision: no
- From: broad (F3), parties (F2)

### retail/17#F4 · Medium · Received on 30 April, while the carrier reported the truck on its way on 29 April, expected at 14:00
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- Why: at 11:49 on 2026-04-29 the truck was "on its way from the distribution centre" for a trip billed as 38 km (16-Invoice) and expected at 14:00; this receipt records arrival the next morning at 10:40, and no document explains the overnight delay (the timing complaint speaks only of "40 minutes into the slot"). Not High because the carrier's arrival time is an estimate; kept as a finding (broad and context had it under "Outside this review") because both documents describe the same delivery. Same problem as 15/F4; the decision is one for both.
- Condition: receipt time, the carrier's status and the despatch advice describe one consistent delivery.
- Options: (a, preferred) keep 2026-04-30 10:40 here and move the "on its way" status in 15 to that morning; (b) receipt on the afternoon of 2026-04-29.
- Needs decision: yes
- From: logistics (F3); broad and context (Outside this review)

### retail/17#F5 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle system boundary, from a world list (`EmissionBoundaryCode`) meant for another concept. The same code is in 39 XML files (`grep -rl --include='*.xml' 'CRADLETOGATE' world/examples | wc -l`, recounted in the merge). UBL has no element for the system boundary of an emission calculation, a candidate for the TC write-up.
- Condition: no system-boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it, and record the missing boundary element for the TC write-up; (b) express the boundary in the lifecycle stage description, which already says it.
- Needs decision: no
- From: context (F2, the FullnessIndicationCode half)

### retail/17#F6 · Medium · Lifecycle stage "Manufacturing" for an emission from ore to factory gate
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". The description, and the calculation description "Mining, steel making, casting, galvanising, sawing and the transport between them", cover raw material supply, transport and manufacturing (EN 15804 stages A1–A3, own knowledge); the code names only manufacturing. Code and text disagree. No part raised this in 17; the merge adds it for consistency with the earlier flows (road, rail, air) and retail a/b, where the same item data was reviewed.
- Condition: the lifecycle stage code covers the stages the description names, or is absent.
- Options: (a, preferred) omit the code and keep the description; (b) one emission entry per stage.
- Needs decision: no
- From: added by the merge

### retail/17#F7 · Low · "No status" as the status of an original receipt advice
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Receipt Advice with respect to its original state". This is the original receipt advice; it has no status to report against an original (IND6: nothing implied by absence, and nothing stated without a reason).
- Condition: no `DocumentStatusCode`, unless the advice is a copy, revision or replacement.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (F5, part)

### retail/17#F8 · Low · Two different photo references for the same damage, neither described nor matching the receipt date
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BM-GI-PHOTO-26-0510`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:DocumentReference/cbc:ID` = `BS-PHOTO-26-0118`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:DamageDocumentationAttachment/cac:ExternalReference/cbc:URI` = `https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg`
- Why: the damage on pallet 3 is documented by an attached photo (its folder `26-0510` matches the header reference). The receipt line refers to another document, `BS-PHOTO-26-0118`, with another prefix of the same party (BM-, BS-). Neither reference says what it is, neither exists elsewhere (searched over `*.xml`), and in this flow the four digits after `26-` usually follow the issue date (e.g. `BM-SIG-26-0424` on the order of 2026-04-24), so `0510` and `0118` read as 10 May and 18 January, while the goods were received on 2026-04-30. It is unclear whether there are one, two or three photo sets.
- Condition: the damage photo is identified one way (one ID of the party's own numbering that fits the receipt), and each reference says what it is.
- Options: (a, preferred) keep the attachment and one typed reference (e.g. DocumentType "Damage photos"), with the URI built from it, and drop the other; (b) drop both references and keep the attachment (context).
- Needs decision: no
- From: broad (F6), logistics (F5), context (F4)

### retail/17#F9 · Low · A signature without signature content
- XPath: `/ReceiptAdvice/cac:Signature/cbc:ID` = `BM-SIG-26-RA`
- Why: the signature has only an ID and a signatory party, no signature method, value or attachment, so it signs nothing; its ID is built from the document type ("RA"). The same pattern holds for 137 of 147 Signature aggregates over all examples (count by the air merge, lxml); the earlier flows and retail a/b treat it as a convention to decide once.
- Condition: a signature carries what makes it one (method, attachment or value), or is absent.
- Options: (a, preferred) drop it, as a receipt advice needs no signature here; (b) complete it.
- Needs decision: yes
- From: context (F5, part)

### retail/17#F10 · Low · Contacts that do not fit receiving and despatching
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- Why: the receipt reports what goods-in counted and checked ("Counted and checked at goods-in."). The delivery customer's contact is Brightmarket's buying office, with a job title and department (customer service officer, sales) that contradict its name; the order names the goods-in contact (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`). 41 XML files carry the "Buying office" contact with this job title (parties part, `grep -rl --include='*.xml'`). Lumeway as despatch supplier has its sales customer service, while the order names a dispatch office; the parties part refuted that half (the supplier's customer service handles the credit the receipt requests), which the merge keeps as the weaker part of the finding.
- Condition: Brightmarket's contact fits receiving, with name, job title and department that agree; Lumeway's contact fits what the receipt asks of it.
- Options: (a, preferred) Brightmarket's goods-in contact; for Lumeway the dispatch office or, following the parties part, keep customer service for the credit request; (b) make Brightmarket's master contact consistent (Buyer / Purchasing).
- Needs decision: no
- From: broad (F7), parties (F5)

### retail/17#F11 · Low · Party master data the receipt advice does nothing with
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: a receipt advice between trading partners does nothing with Brightmarket's logo, consumer web shop and social-media profile, with either party's share capital, or with Lumeway's customs trader number in a domestic flow without customs (section 4.8). `CorporateStockAmount` is moreover defined as "The number of shares in the capital stock of a corporation" while its data type is an amount: a conflict for the TC write-up; the parties part made it "Needs decision: yes", the merge sets no, as retail a/b.
- Condition: the parties carry only data the receipt advice uses.
- Options: (a, preferred) leave these out of the trade documents; keep the consumer-facing data for the purchase receipt and consumer order, the customs number for customs flows.
- Needs decision: no
- From: parties (F3, F4, F7), context (F5, part)

### retail/17#F12 · Low · "Carton torn", while the despatch advice and the item data describe no cartons
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks` = `One carton torn, the bench's armrest bent.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:Note` = `One bench arrived in a damaged carton and was refused.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cbc:TotalPackageQuantity` = `4`
- Why: for the same pallet (SSCC `095206102170000038`) the despatch advice lists one package, the pallet (`PX`), and the item's own packaging waste is stretch film and pallet straps; this receipt reports a torn carton. The despatch advice's four packages per pallet may be cartons, but it never says so. Logistics rated this Medium; the merge lowers it to Low because 12's `TotalPackageQuantity` 4 admits the carton reading, so the documents are incomplete rather than contradictory. The context part refuted it as a question of 12's package description; the merge keeps it here because the receipt and credit note are the documents that name the carton (the same text is in 19).
- Condition: the packaging the receipt reports as damaged is the packaging the despatch advice (and the item data) declares for that pallet.
- Options: (a, preferred) declare what the four packages are in 12 (cartons) and keep the carton here; (b) if the benches travel unboxed, describe the damage without a carton (e.g. "stretch film torn") here and in 19.
- Needs decision: no
- From: broad (F4), logistics (F4); context (Considered and refuted)

### retail/17#F13 · Low · The handling unit's receipt line reuses receipt line ID 1 with another quantity
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ReceivedQuantity` = `3`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- Why: `ReceivedHandlingUnitReceiptLine` is "A receipt line associated with this transport handling unit". Pallet 3's receipt line `1` has 3 received and 1 rejected; the document's receipt line `1` has 23 received and 1 rejected. The invoice and credit note refer to "receipt line 1 of BS-RA-26-0235" (`19-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cac:ReceiptLineReference/cbc:LineID` = `1`), which can be either. The despatch advice gives its pallet lines their own IDs (`12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:HandlingUnitDespatchLine/cbc:ID` = `3`). The logistics part rated it High; the merge lowers it to Low, aligned with retail b (08's substitute line): the pallet line can be read as the part of line 1 on pallet 3, so the IDs are ambiguous rather than contradictory.
- Condition: each receipt line ID identifies one line, or the handling-unit line is identifiable as a breakdown of line 1.
- Options: (a, preferred) an ID of its own for the pallet's line (e.g. `1-3`); (b) drop the pallet-level receipt line and keep the damage on the handling unit (remarks, status, attachment).
- Needs decision: no
- From: broad (F8), logistics (F1)

### retail/17#F14 · Low · "Late" for a delivery that arrived within a slot no document agreed
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaintCode` = `LATE`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaint` = `Arrived 40 minutes into the slot; unloading delayed the next truck.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- Why: `TimingComplaintCode` is "A complaint about the timing of delivery". No document of the flow sets a slot: the order has no requested delivery time (its delivery is only the location, `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`), the transport request gives a service period to 2026-05-02, and the carrier's last expectation was 2026-04-29 14:00. "40 minutes into the slot" is within the slot, which reads oddly as late, while the delay of almost a day against the carrier's announcement goes unmentioned. Code and text do not describe the same lateness, and the reader cannot verify the complaint.
- Condition: the slot the complaint refers to is stated in a document the delivery was based on (order, transport request or despatch advice), and the text says how the arrival relates to it.
- Options: (a, preferred) a delivery slot in 08 or 11 (e.g. 2026-04-30 10:00–10:30) and a text that says the truck arrived after its end; (b) complain about the arrival a day after the announced time; (c) drop the complaint.
- Needs decision: no
- From: broad (F5), logistics (F6), context (F3)

### retail/17#F15 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: Lumeway's GLN and the GTIN of Valdara's bench share the company prefix 9520610, which across the world is Lumeway's (its GLNs, and every SSCC, e.g. `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:ID` = `095206102170000038`). The item is Valdara's (brand, manufacturer, made in Urvania). Under the GS1 allocation rules (own knowledge) the brand owner allocates the GTIN from its own prefix. Check digits are correct (`check_ids.py`, rerun).
- Condition: Valdara's GTINs and Lumeway's GS1 keys are under different company prefixes, or the story states that Lumeway allocated the GTINs.
- Options: (a, preferred) a company prefix of Valdara's own for its GTINs; (b) state in the story that the distributor allocated them.
- Needs decision: yes
- From: parties (F6)

### retail/17#F16 · Low · The world item number has the form and check digit of a GTIN
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: the world's item number `771020000027` (scheme `urn:ubl-examples:world:item`) has twelve digits and a valid GS1 check digit (7, computed in the merge), so it reads as a GTIN-12 (UPC-A) with prefix 07, a range GS1 assigns in the US and Canada (own knowledge). A fictional identifier must not look like one from a real register. No part raised it here; the merge adds it as retail a, rail, road and plastics did.
- Condition: the world item number cannot be mistaken for a real GTIN, or the story records why it has that form.
- Options: (a, preferred) a format that is not a valid GTIN (other length, or a prefix such as 952); (b) record the choice in the identifier scheme.
- Needs decision: yes
- From: added by the merge

### retail/17#F17 · Low · The item's catalogue data copied into the receipt line
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CircularityProfile`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- Why: a receipt advice identifies what was received; the item's emissions, circularity data, load test, dimensions, sales conditions, Urvania's customs tariff code in a domestic Bayvarran delivery, and the distributor's wording in a document written by the buyer are catalogue data the receipt does not use (IND5/IND6).
- Condition: the received item carries its identifiers and what the receipt depends on.
- Options: (a, preferred) reduce the item to identifiers, name and the received variant.
- Needs decision: no
- From: broad (F9), context (F5, part)

## Checked and consistent
- Quantities (redone): 23 received + 1 rejected = 24 despatched (`12-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`) = ordered; on pallet 3: 3 + 1 = 4 = its despatch line in 12.
- The damaged handling unit `095206102170000038` is pallet "003 of 006" in 12 (`12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cbc:ShippingMarks` = `BRIGHTMARKET LUMEPORT / 003 of 006`), matching the photo `pallet-3.jpg`; shipment `LD-SH-26-0230` is that of 12 and 13.
- References: order `BS-PO-26-0224` line 1 and despatch advice `LD-DA-26-0229` line 1 resolve; issue time 15:21 is after the receipt at 10:40.
- Codes `PARTIAL`, `DAMAGED`, `CREDIT` and the type `Actual` agree with each other, with the notes and with 19-CreditNote, which credits one bench with discrepancy "Transport damage".
- Buyer's item ID `BM-551210` equals 08's and is the store's own number in 21.
- GS1 keys pass `check_ids.py` (rerun in the merge).

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`: suspected that "quantity received" should include the rejected bench (24) — refuted, received and rejected add up to the delivered quantity, and the definitions ("The quantity received", "The quantity rejected") allow the reading (from broad and logistics).
- `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`: a sales contact for the despatch party — refuted by the parties part because the supplier's customer service handles the requested credit; carried into F10 as the weaker half (from parties).
- `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted, the definition fits a business park (from parties).
- `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks`: "carton" against 12 — refuted by the context part as a question of 12's package description; the merge disagrees and keeps it as F12 (from context).

## Changed in the merge
- broad/F1, logistics/F2, context/F1 → F1: grouped; 96/0.82 recomputed.
- context/F2 → F2 and F5: split (LocaleCode and FullnessIndicationCode are different problems with different fixes).
- F6 (MANUFACTURING): added by the merge, Medium/no, aligned with retail a/b and road/rail/air.
- logistics/F3 → F4: kept Medium/yes; broad/context "Outside" placement recorded.
- context/F5 → F7, F9, F11, F17: split by problem (NoStatus, signature, party master data, item data); the signature set to "Needs decision: yes", aligned with retail a/b, air and utilities.
- broad/F7, parties/F5 → F10: grouped; the parties part's refutation of Lumeway's contact carried as the weaker half.
- parties/F3, F4, F7 (+ context/F5 part) → F11: one copied-master-data finding; parties/F4's "Needs decision: yes" set to no (aligned with retail a/b).
- logistics/F4 → F12: Medium lowered to Low (12's four packages admit the carton reading); broad's Low kept; context's refutation answered.
- logistics/F1 → F13: High lowered to Low (ambiguity, not contradiction), aligned with retail b.
- broad/F5, logistics/F6, context/F3 → F14: grouped.
- F16 (world item number): added by the merge, aligned with retail a.

## Outside this review
- Whether 12-DespatchAdvice should declare the cartons (or what its four packages per pallet are) is for 12's review; it bears on F12.
