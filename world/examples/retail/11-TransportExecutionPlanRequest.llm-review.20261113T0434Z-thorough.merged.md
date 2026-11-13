# LLM review: 11-TransportExecutionPlanRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/11-TransportExecutionPlanRequest.xml`, Git blob `43f5b79071571e3db0185c905bab61bd7c25ec4c` (committed)
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

### retail/11#F1 · Medium · The transport request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `996`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[6]/cbc:ShippingMarks` = `BRIGHTMARKET LUMEPORT / 006 of 006`
- Why: a TransportExecutionPlanRequest is "A document sent by a transport user to request a transport service from a transport service provider". Its consignment has only an ID, a gross weight and the consignee and consignor: no goods description, no number or kind of handling units, no dimensions or loading length. That the load is six pallets of four park benches 1.8 m long is known only from 12-DespatchAdvice, which Bayforth does not receive. The full-truck-load service does not replace it: the forwarder cannot plan loading or vehicle from a weight alone.
- Condition: the consignment states what is carried: at least a goods description and the number and type of transport handling units (six pallets), with the gross weight already given; dimensions where the pallets are not standard.
- Options: (a, preferred) `TotalTransportHandlingUnitQuantity` 6 and a goods item ("Park benches, 24 pieces on 6 pallets", 996 kg), with pallet dimensions; (b) at least a consignment-level description and package quantity.
- Needs decision: no
- From: broad, context, logistics

### retail/11#F2 · Medium · Language codes in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is a language code and names no locale. 362 such elements in 213 XML files (recounted in the merge).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list.
- Needs decision: no
- From: broad, context, parties

### retail/11#F3 · Medium · A gate in AdditionalStreetName, in Lumeway's postal address and in the pick-up address
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is the entrance of the distribution centre where the truck loads, not a street. In the postal address it has no place at all (it matters only to vehicles); in `FromLocation` it is useful information for the truck, but it is still not a street name and belongs to the place within the site. 79 occurrences in 76 XML files (recounted).
- Condition: no `AdditionalStreetName` holds the gate; where the transport needs it, it is given as part of the pick-up location (name, description or a sub-location).
- Options: (a, preferred) drop it from the postal address (party master data), and give it in the pick-up location, e.g. `FromLocation/Description` "Gate 3" or a name "Lumeway distribution centre, gate 3", with the address without the gate; (b) a subsidiary location for the gate.
- Needs decision: no
- From: broad, context, logistics, parties

### retail/11#F4 · Low · Origin and destination named after the companies, without the GLNs the flow uses
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Lumeway Distribution`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Brightmarket Stores`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Goods-in, garden department`
- Why: `FromLocation` and `ToLocation` are "The location of origin" and "The destination location for the transport service"; their names are companies, not places. The order asks for delivery at a specific goods-in (GLN `9522610900019`); the request sends the forwarder to the store's business address (Market Street 50) without it, so the driver is not told where to unload. The note speaks of the "distribution centre", which is the place to name; Lumeway's GLN is `9520610900008`.
- Condition: origin and destination are named as places (distribution centre, store goods-in), and the destination carries the goods-in GLN of the order.
- Options: (a, preferred) `ToLocation/ID` `9522610900019` with a name such as "Brightmarket Lumeport, goods-in, garden department"; `FromLocation` named "Lumeway distribution centre, Marrowdale", with its GLN; (b) keep the names and add the GLNs.
- Needs decision: no
- From: broad, context, logistics, parties

### retail/11#F5 · Low · Contacts that do not fit the parties' roles in the transport
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: in a transport request the transport user's contact arranges the transport, the provider's contact plans it, and the consignee's contact receives the goods. Lumeway is represented by its sales customer service, Bayforth by its "Export desk" (an operations planner) for a domestic haul from Marrowdale (Upland State) to Lumeport (Coastal State), and the consignee Brightmarket by its buying office, whose job title and department also contradict its name. The order names the fitting contacts (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`; `08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`). The same party contacts are used in every role in the flow (Bayforth's export desk in 25 places, parties part's count).
- Condition: each party's contact fits its role in this transport, and name, job title and department agree.
- Options: (a, preferred) Lumeway's dispatch office, a Bayforth road or domestic operations desk, Brightmarket's goods-in; (b) drop the contacts where they are only master data.
- Needs decision: no
- From: broad, parties

### retail/11#F6 · Low · Party master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- Why: a domestic truck booking uses neither the parties' share capital and tax registrations, nor the consignee's logo, web shop and social-media profile, nor Lumeway's customs trader number (no customs in this flow) (IND5/IND6). The bill-to party is Lumeway (DDP), so the booking's billing does not depend on the consignee's tax data. `CorporateStockAmount`'s definition ("The number of shares …") against its amount type is a candidate for the TC write-up (parties part).
- Condition: the parties carry what the booking uses (identification, name, address, contact).
- Options: (a, preferred) drop them here; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context, parties

### retail/11#F7 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is shared by 25 different companies of the world in three countries (parties part, lxml: distinct registration names per date; 271 occurrences in 181 files, earlier merges' count), among them Bayforth, while the other parties have dates of their own (Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January for unrelated companies looks like a filler.
- Condition: each party's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) a date from Bayforth's history; (b) leave the date out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties

### retail/11#F8 · Low · Document status "No status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Transport Execution Plan Request"; `NoStatus` ("No status on document") states that there is nothing to state. A first, ordinary request (`VersionID` 1) needs no status code (IND5/IND6). The broad part refuted this ("an explicit 'no special status' is a statement"); the merge does not follow it, as in the earlier flows: a code that says there is no status carries no information the document's absence of a status code would not.
- Condition: `DocumentStatusCode` only when the request is cancelled, revised or disputed.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (broad: considered and refuted)

## Checked and consistent
- Parties: Lumeway is sender, transport user, consignor and bill-to party (it sells DDP, so it pays the carriage; 16-Invoice is addressed to Lumeway); Bayforth is receiver and transport service provider; Brightmarket consignee.
- Dates: issued 2026-04-25 10:28, response deadline 2026-04-26, service from 2026-04-29 to 2026-05-02 — after the catalogue's earliest delivery (2026-04-27), before the promotion (2026-05-11); despatch (12), waybill (13) and status (15) on 2026-04-29 and receipt (17) on 2026-04-30 lie within it.
- Consignment `LD-CS-26-0228` and 996 kg are the same in 12 and 13; the consignment ID recurs in 14, 15 and 16.
- Physics, redone in the merge: 996 kg / 6 pallets = 166 kg per pallet; with a long wooden pallet of about 25–30 kg (own estimate) that leaves 34–35 kg per bench, plausible for a 1.8 m bench whose material consumption is 34 kg steel and 22.5 kg hardwood before casting and sawing losses. Six pallets fit a 13.6 m trailer whichever way they are loaded (even lengthwise in one row: 6 × 1.8 m = 10.8 m).
- From and to addresses equal the parties' business addresses in every retail example.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: a full truck load for six pallets of about one tonne — refuted because FTL describes the booking (the whole vehicle for this consignment), not the fill rate, and a dedicated truck for a promotion delivery is a commercial choice (from broad, context, logistics).
- `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: checked whether the bill-to party fits — it does: DDP, and 16-Invoice is addressed to Lumeway (from parties).
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted because the definition fits it (from parties).
- The broad part's refutation of `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus` was not followed; see F8.

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1; broad/F2, context/F2, parties/F1 → F2: combined.
- broad/F3, parties/F2 (postal address and FromLocation) with context/F5 (Low) and logistics/F2 (Medium) (FromLocation) → F3: one Medium finding with one XPath line per place, as in road and air; context's Low raised (element meaning, section 6).
- broad/F4, context/F4, logistics/F3, parties/F8 → F4: combined.
- broad/F5, parties/F5, F7, F10 → F5: all contacts of the example in one finding (as retail a/c, cotton).
- context/F6, parties/F3, F4, F9 → F6: one master-data finding; parties/F4 Needs decision yes → no with its TC note.
- context/F3 → F8: kept Low/no; broad's refutation recorded as not followed.
