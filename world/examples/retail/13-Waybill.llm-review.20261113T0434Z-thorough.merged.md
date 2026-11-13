# LLM review: 13-Waybill.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/13-Waybill.xml`, Git blob `0e28ae8a70150ecfdb1e12ab9527a6f9336f5e5e` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
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

### retail/13#F1 · High · "Three originals: consignor, consignee, carrier", but the distribution gives the consignor an electronic copy
- XPath: `/Waybill/cbc:Note` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyIdentification/cbc:ID` = `20410274`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: `DocumentDistribution` is "A list of interested parties to whom this document is distributed". The note says the consignment note exists in three originals, for consignor, consignee and carrier (as a CMR note does, art. 5; own knowledge). The distribution sends the consignee's original with the goods and gives the consignor, Lumeway (`20410274`), only an electronic copy; the carrier's original is not listed (it may be the issuer's own, but nothing may be implied by absence). For the consignor the two statements contradict each other. The merge tried the reading that an electronic copy is sent in addition to a paper original handed over at loading: the distribution then still omits the consignor's original while listing the consignee's, so the list is not the set of originals the note describes. High, as the parts broad and parties had it and as in rail and cotton ("distribution vs note"); logistics (Low) and context (Medium) rated it lower.
- Condition: the distribution list and the note describe the same set of originals and copies.
- Options: (a, preferred) list the consignor's original (and the carrier's, if the list is meant to be complete), keeping the electronic copy if wanted; (b) change the note, if in the world the electronic copy replaces the consignor's paper original.
- Needs decision: no
- From: broad, context (Medium), logistics (Low), parties

### retail/13#F2 · High · Three different carrier references for the same shipment
- XPath: `/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: `CarrierAssignedID` is "An identifier (in the form of a reference number) assigned by a carrier or its agent to identify a specific shipment". All three documents concern consignment `LD-CS-26-0228`, carried by Bayforth: here the reference is `BF-CMR-26-0217`, Lumeway's status request quotes the waybill's document ID, and Bayforth's own status report uses a third value. A shipment has one carrier reference; the forwarder would not recognise its own shipment from 14.
- Condition: the carrier-assigned shipment reference is the same in 13, 14 and 15, or each value is a different kind of reference in an element that fits it.
- Options: (a, preferred) keep `BF-CMR-26-0217` (the waybill, issued first, is where the carrier assigns it) and use it in 14 and 15; (b) another single value in all three.
- Needs decision: no
- From: broad, logistics (aligned with retail merge c for 15)

### retail/13#F3 · Medium · Consignment note without goods, packages and places and dates of taking over and delivery
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `996`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`
- Why: a Waybill is "A transport document describing a shipment"; this one presents itself as a CMR consignment note, whose particulars include the place and date of taking over, the place designated for delivery, the description of the goods, the number of packages with their marks and the gross weight (CMR art. 6(1); own knowledge). Only the gross weight is present: no goods item or description, no handling units (12 has six pallets marked "BRIGHTMARKET LUMEPORT / 001 of 006" …), no pick-up or delivery location, no date of taking over. The consignee is named, but not where the goods are to be delivered, and damage (which 12 asks to be reported "on the consignment note") cannot be recorded against goods the note does not describe.
- Condition: the waybill describes the goods (description, number and kind of handling units, marks), the place and date of taking over and the place of delivery.
- Options: (a, preferred) a goods item and the six pallets (with SSCCs and marks, or a package count), the delivery with the goods-in `9522610900019`, and the pick-up at the distribution centre with its date; (b) at least goods description, number of pallets and both places.
- Needs decision: no
- From: broad, context, logistics

### retail/13#F4 · Medium · The consignment ID given as shipping order ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: `ShippingOrderID` is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". `LD-CS-26-0228` is the consignment's ID (same document, `Consignment/ID`). The forwarding instruction of this shipment is Lumeway's transport request 11. Medium, not High: no example of the flow states a different shipping-order ID (aligned with rail b and road b). The same value is in 14.
- Condition: `ShippingOrderID` is the identifier of the shipping order or forwarding instruction, or absent.
- Options: (a, preferred) `LD-TR-26-0227`; (b) drop it, the consignment ID is already given.
- Needs decision: no
- From: broad, context, logistics

### retail/13#F5 · Medium · Language codes in LocaleCode
- XPath: `/Waybill/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is a language code and names no locale. 362 such elements in 213 XML files (recounted in the merge).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list.
- Needs decision: no
- From: broad, context, parties

### retail/13#F6 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; "Gate 3" is a vehicle entrance of the distribution centre, not a street name. 79 occurrences in 76 XML files (recounted). The waybill does need the gate, but as part of the place of taking over (see F3), not of Lumeway's postal address.
- Condition: no `AdditionalStreetName` of Lumeway holds the gate; where the waybill needs it, it is given in the pick-up location.
- Options: (a, preferred) drop it from the postal address (party master data) and give it in the place of taking over; (b) if Bayvarra's address format makes the gate part of the postal address, record that and dismiss the finding.
- Needs decision: no
- From: broad, parties

### retail/13#F7 · Low · A CMR consignment note for a domestic carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:Description` = `The forwarder's truck from the distribution centre to the store.`
- Why: the CMR convention applies to carriage by road where the places of taking over and delivery are in two different countries (CMR art. 1; own knowledge). This carriage runs from Marrowdale (Upland State) to Lumeport (Coastal State), both in Bayvarra (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CityName` = `Marrowdale`). Some countries apply the CMR rules to domestic carriage by national law; the documents do not say that Bayvarra does. The world's `WaybillTypeCode` list defines `CMR` as "A consignment note under the Convention on the Contract for the International Carriage of Goods by Road" and has no national road consignment note type (checked in the merge), so option (a) needs a new list entry.
- Condition: the waybill type and name fit a domestic Bayvarran road carriage, or the world states that Bayvarra applies the CMR domestically.
- Options: (a) a national road consignment note type (new entry in the world's list); (b, preferred) record in the story that Bayvarra applies the CMR to domestic road carriage, and say so in the name (no new list entry, no change to other examples).
- Needs decision: yes
- From: broad, context, logistics

### retail/13#F8 · Low · Issue location named after the company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeway Distribution`
- Why: `IssueLocation` is "The location where this waybill was issued"; the name is the consignor's company, without address or identifier. The place is Lumeway's distribution centre in Marrowdale, where the goods are taken over (CMR art. 6(1)(a) requires the place of issue; own knowledge).
- Condition: the issue location names the place (and may carry its address or GLN).
- Options: (a, preferred) "Lumeway distribution centre, Marrowdale" with its address or GLN `9520610900008`; (b) the city.
- Needs decision: no
- From: broad, context, logistics, parties

### retail/13#F9 · Low · Contacts that do not fit the parties' roles in the carriage
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Bayforth, the carrier, is represented by its "Export desk" for a domestic haul; Lumeway, the consignor, by its sales customer service; Brightmarket, the consignee who receives the goods and signs for them ("Deliver against signature of the consignee"), by its buying office, whose job title and department also contradict its name. The flow names fitting contacts (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`; `08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`).
- Condition: each party's contact fits its role in the carriage, and name, job title and department agree.
- Options: (a, preferred) a Bayforth domestic or road desk, Lumeway's dispatch office, Brightmarket's goods-in.
- Needs decision: no
- From: broad, parties

### retail/13#F10 · Low · Party master data the waybill does nothing with
- XPath: `/Waybill/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: a domestic consignment note uses neither a customs trader number, nor the parties' share capital, nor the consignee's logo, web shop and social media (IND5/IND6). `CorporateStockAmount`'s definition ("The number of shares in the capital stock of a corporation") against its amount type is a candidate for the TC write-up (parties part).
- Condition: the parties carry what the consignment note uses.
- Options: (a, preferred) drop them here; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context (with the signature, split in the merge), parties

### retail/13#F11 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is shared by 25 different companies in three countries (parties part; 271 occurrences in 181 files, earlier merges' count), among them Bayforth. It looks like a filler.
- Condition: Bayforth's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) a date from Bayforth's history; (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties

### retail/13#F12 · Low · The carrier's signature has an ID and a signatory only, and the consignor does not sign
- XPath: `/Waybill/cac:Signature/cbc:ID` = `BF-SIG-BF-WB-26-0231`
- Why: a consignment note is signed by consignor and carrier (CMR art. 5; own knowledge), and the consignee signs on delivery ("Deliver against signature of the consignee"). The only signature here has no method, attachment or date, and its ID repeats the issuer's prefix (`BF-SIG-` + the waybill number `BF-WB-26-0231`). Signatures with ID and signatory only are a world-wide convention (137 of 147, lxml count of the air merge), so the change is a decision; on a waybill, where the signatures matter, completing it is preferred over dropping it (as in air).
- Condition: the waybill's signatures carry what makes them signatures, for the parties that sign, or none is given.
- Options: (a, preferred) complete the carrier's signature (method or attachment) and add the consignor's; (b) drop it.
- Needs decision: yes
- From: context (Needs decision no there; set to yes, aligned with retail merges a and c, air and utilities)

## Checked and consistent
- Shipment `LD-SH-26-0230`, consignment `LD-CS-26-0228` and gross weight 996 kg agree with 11 and 12.
- Parties: sender and carrier Bayforth (the carrier issues the waybill), receiver and consignor Lumeway, consignee Brightmarket, as in 11 and 12; described identically in every retail example (parties part).
- Times: issued 2026-04-29 08:56, on the day of pick-up and within 11's service period; before Lumeway's status request 14 (10:59) and the "on its way" status 15 (11:49).
- `AdValoremIndicator` `false` fits a carriage without declared value; `ConsolidatedIndicator` `false` fits a dedicated full truck load.
- 16-Invoice refers to this waybill (`16-Invoice.xml:/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `BF-WB-26-0231`).

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: suspected filler in a domestic carriage — refuted because it states that no value was declared for carriage, a real statement on a consignment note (from context; broad listed it as consistent).
- `/Waybill/cbc:Description` = `The forwarder's truck from the distribution centre to the store.`: describes the transport rather than the contents — refuted because "Text describing the contents of the Waybill" refers to the document's content, which is this carriage (from context).
- `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: suspected that the consignor lacks the address a CMR note needs — refuted because the same party (register ID 20410274) is described in full in `ReceiverParty` (from parties).
- `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted because the definition fits a business park (from parties).

## Changed in the merge
- broad/F1 (High), parties/F1 (High), context/F3 (Medium), logistics/F4 (Low) → F1: High, with the merge's check of the "copy in addition" reading; aligned with rail b and cotton.
- broad/F2, logistics/F1 → F2: combined.
- broad/F3, context/F1, logistics/F2 → F3; broad/F4, context/F2, logistics/F3 → F4; broad/F5, context/F4, parties/F2 → F5; broad/F6, parties/F3 → F6: combined.
- broad/F7, context/F5, logistics/F5 → F7: combined; the world's waybill-type list checked, and the preference set to (b) (story statement), because the list has no national type and (a) needs a new entry; the parts had preferred (a) or none.
- broad/F8, context/F6, logistics/F6, parties/F4 → F8: combined.
- broad/F9, parties/F6, F9, F11 → F9: all contacts in one finding.
- context/F7 → split into F10 (master data) and F12 (signature); parties/F7, F8, F10 folded into F10; parties/F8 (CorporateStockAmount) Needs decision yes → no with its TC note. F12: Needs decision no → yes; the doubled prefix and the missing consignor's signature added in the merge.
