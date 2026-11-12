# LLM review: 03-ForwardingInstructions.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/03-ForwardingInstructions.xml`, Git blob `0b8c1e57de771a3aa28a4f5ad2687ce72817a1ac` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/03#F1 · High · The referenced order VT-PO-26-0319 does not exist
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `01-OrderChange.xml:/OrderChange/cbc:ID` = `VT-OC-26-0320`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderReference/cbc:ID` = `VT-PO-26-0127`
- Why: No example has the document ID `VT-PO-26-0319`: `flow_index.py air` resolves it to nothing, and over `*.xml` it occurs only as a reference, here and as the OrderReference of `06-DespatchAdvice.xml` and `08-DespatchAdvice.xml` (`grep -rln --include='*.xml' VT-PO-26-0319 world/examples`, re-run in the merge: 3 files). The goods are the 8 side frames that order `VT-PO-26-0127` (`sea/05-Order.xml`) as changed by `VT-OC-26-0320` (`01-OrderChange.xml`, accepted by `02-OrderResponse.xml`) asks for; the number looks like a separate air purchase order that the flow never issues. The reference has no DocumentTypeCode either, so it does not even say it is an order. Merge check: refutation attempted (an order in another flow, a different ID style); none found, and `07-FulfilmentCancellation.xml` cites `VT-OC-26-0320` and `VT-PO-26-0127` for the same goods.
- Condition: the reference resolves to the order or order change these instructions execute, and says what kind of document it is.
- Options: (a) preferred: `VT-OC-26-0320` (the change that asked for the air delivery) and/or `VT-PO-26-0127`, with a DocumentTypeCode, as `07-FulfilmentCancellation.xml` does; (b) add an air purchase order `VT-PO-26-0319` to the flow, which changes the story (a separate order instead of an order change).
- Needs decision: no
- From: broad, logistics, context

### air/03#F2 · High · The box cannot hold the goods: 0.072 m³ of box for 0.42 m³ of frames
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cbc:Quantity` = `8`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[1]/cbc:Measure` = `800`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[2]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[3]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetVolumeMeasure` = `0.42`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- Why: The one package LD-AIR-BOX holds 8 items (Package/Quantity is "The quantity of items contained in this package") and measures 800 × 300 × 300 mm = 0.072 m³ (MeasurementDimension is "A measurable dimension … of this package"). The consignment's net volume, excluding packaging, is 0.42 m³, almost six times the box. The waybill's gross volume, 0.576 m³, is exactly 8 × 0.072 m³, so the dimensions seem to describe one box per frame; as encoded, the consignment does not fit its package. In addition, a Serra 180 bench is 620 mm deep and 780 mm high (item dimensions in `sea/05-Order.xml`); an end frame spanning these (own reading of what a side frame is) cannot lie in a 300 × 300 mm cross-section. Merge check: redone (0.8 × 0.3 × 0.3 = 0.072; 8 × 0.072 = 0.576; 0.42 / 0.072 = 5.8); a reading in which frames nest cannot make the goods' own volume larger than the box that holds them.
- Condition: the packages' number and dimensions can hold the stated net volume and the frame size, and their total agrees with the waybill's gross volume (and hence its chargeable weight).
- Options: (a) preferred: describe the packing as it must be for 8 frames: 8 boxes of one frame each (Package/Quantity 1 and the box count stated), or one crate of about 0.576 m³ on the skid, either matching the waybill's 0.576 m³; (b) lower the net volume if the frames really fit into 0.072 m³; then the waybill's gross volume and chargeable weight and the invoice change too.
- Needs decision: no
- From: broad, logistics

### air/03#F3 · High · AdValoremIndicator false here, true in the air waybill for the same shipment
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00`
- XPath: `04-Waybill.xml:/Waybill/cbc:AdValoremIndicator` = `true`
- Why: AdValoremIndicator is "A term used in commerce in reference to certain duties, called ad valorem duties, which are levied on commodities at certain rates per centum on their value". The goods, the shipment `LD-SH-26-0323` and the declared value (512.00 XBL) are the same in both documents, so whether ad valorem duties apply cannot change between the shipper's instructions and the carrier's waybill. Read in air-freight practice as the valuation charge on a declared value for carriage (context part, own knowledge), the two documents disagree as well: here a value is declared but the indicator is false. Merge check: refutation attempted (the two documents mean different things by the indicator); refuted, because the definition is the same in both document types and, under either reading, one consignment gets two values.
- Condition: both documents carry the same AdValoremIndicator for this shipment, chosen according to the UBL definition, or neither carries it.
- Options: (a) preferred: leave it out of both, as neither document deals with duties (a valuation charge is not what the definition means; if the story wants one, it belongs in the waybill's charges); (b) the same value in both, set by whether Lisavu's import duty on HS 7325.99 is ad valorem.
- Needs decision: no
- From: money, context (Medium there); broad refuted it here and recorded it in 04

### air/03#F4 · Medium · The instructions do not say how, from where or to where the goods are to be forwarded
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the shipment to the island.`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-14`
- Why: Forwarding Instructions give instructions "regarding the action to be taken for the forwarding of goods". This one has no transport mode, no shipment stage, no origin or destination location, no delivery address and no delivery terms: the forwarder learns that 8 frames are ready at a dispatch area and must be delivered on 2026-05-14, but not that they go by air (the reason for the whole flow), from which airport, to which airport, or to whom at delivery (Nalevi Warehousing in `01-OrderChange.xml` and the despatch advices, Velumi Trading as consignee here, Selanu airport cargo terminal as the CPT place in 01). "To the island" is the only hint; the destination is left to be implied by absence.
- Condition: the instructions state at least the transport mode (air), the place of departure and the destination (Selanu airport XLSLA and/or the delivery party), in the structured elements for them.
- Options: (a) preferred: a main-carriage ShipmentStage (mode 4, loading XBLMA, unloading XLSLA) and the delivery terms CPT Selanu airport, matching `04-Waybill.xml`; (b) a Delivery with DeliveryLocation and DeliveryParty.
- Needs decision: no
- From: broad, logistics

### air/03#F5 · Medium · Instruction to send a bill of lading in an air shipment, to the instructions' own addressee
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `04-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `AWB`
- Why: OtherInstruction holds "other free-text instructions to the forwarders or carriers related to the shipment". The goods go by air under an air waybill (`04-Waybill.xml`, "Air waybill under the Montreal Convention"), not a bill of lading and not a document of title (own knowledge: air waybills are non-negotiable). And the instruction is addressed to the forwarder (FreightForwarderParty and DocumentDistribution are Bayforth Forwarding), telling it to send a document to itself. Counted over `*.xml` in the merge: the same text occurs in 4 files (`grep -rln --include='*.xml' 'Send the bill of lading' world/examples`: air/03, cotton/09, sea/09, sea/12), the other three in sea transport, where it may be right (the logistics part counted 2).
- Condition: the instruction names the transport document of this shipment and a recipient other than its addressee, or is absent.
- Options: (a) preferred: remove it (the waybill goes to the forwarder anyway, `04-Waybill.xml` ReceiverParty); (b) an instruction that fits, e.g. "Send the air waybill copy to the consignor".
- Needs decision: no
- From: broad, logistics, context

### air/03#F6 · Medium · A transport event with date and time but no type and no place
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceTime` = `19:00:00`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:CompletionIndicator` = `false`
- Why: Consignment/TransportEvent is "any additional significant occurrences or happenings related to the transportation of goods not specified elsewhere in this Consignment". Without TransportEventTypeCode, Description or Location the event says nothing: 13 May 19:00 could be a cut-off for acceptance, a pickup or a departure. It matches no other time of the flow: the requested despatch is 13 May (no time), the waybill's flight is 14 May 07:00, and the order response speaks of a "morning flight". UBL has dedicated events for the likely meanings (Consignment/RequestedPickupTransportEvent, ShipmentStage/AcceptanceTransportEvent).
- Condition: the event says what happens and where, preferably in the dedicated element for it, or it is absent.
- Options: (a) preferred: the dedicated element for what is meant (e.g. the acceptance cut-off at the origin cargo terminal for the 14 May flight) with its location; (b) a TransportEventTypeCode and Location on the generic event; (c) drop it.
- Needs decision: no
- From: broad (Low), logistics, context

### air/03#F7 · Medium · LocaleCode holds a language code
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en` (Bayforth Forwarding)
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language, not a locale, and repeats Language/ID. Counted over `*.xml`: 362 such elements in 213 files.
- Condition: every LocaleCode holds a locale from a locale list, or is absent.
- Options: (a) preferred: drop it; (b) a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### air/03#F8 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street. Here the gate would matter, because the forwarder picks the goods up (Package/Pickup `BF-PU-26-0611`), but then it belongs to the pickup location, not to the consignor's postal address. Counted over `*.xml`: 79 occurrences in 76 files.
- Condition: no gate in a street-name element of the postal address; if the forwarder needs the gate, it is given with the pickup.
- Options: (a) preferred: move it to a pickup location (Package/Pickup/PickupLocation, with the dispatch area's address); (b) drop it.
- Needs decision: no
- From: parties, context

### air/03#F9 · Low · Gross minus net weight leaves 5.6 kg for skid, box and bags
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetNetWeightMeasure` = `76`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cbc:TransportHandlingUnitTypeCode` = `SI`
- Why: Shipment gross weight is the weight of the goods plus packaging plus transport equipment. 81.6 − 76 = 5.6 kg is left for a skid, the box or boxes and 8 bags. Broad (own knowledge): a corrugated box of 0.8 × 0.3 × 0.3 m weighs about 0.5–0.7 kg (4–5.6 kg for eight, if F2 is resolved that way), and a wooden skid another 5–15 kg, so the gross looks like goods plus boxes only. Against (logistics, own estimates): a small skid of 3–4 kg, one box of 1–1.5 kg and light bags fit 5.6 kg. Which holds depends on how F2 is resolved; the merge cannot settle it now. Gross per frame 81.6 / 8 = 10.2 kg equals `sea/10-PackingList.xml` (122.4 kg for 12 frames), so the figure is the flow's own.
- Condition: after F2 is resolved, gross minus net weight covers the skid and the packaging as described, at plausible tare weights, here and in `04-Waybill.xml` (same 81.6 kg).
- Options: recheck the tare once the packing is described; raise the gross weight (and what follows from it) if eight boxes and a skid are meant, or state a light skid.
- Needs decision: yes (cannot be settled before F2)
- From: broad; logistics refuted it

### air/03#F10 · Low · Shipping order ID equals the shipment ID, and the flow quotes another value
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `04-Waybill.xml:/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324`
- Why: ShippingOrderID is "Reference number to identify a Shipping Order"; the value is the shipment's own ID, and no shipping order exists in the flow. The later documents put yet another value, the consignment ID `LD-CS-26-0324`, in ShippingOrderID (04, 05, 09), so the shipping order reference has no stable meaning. Against (logistics): a consignor may number its shipping order with its shipment number, and it is a reference the forwarder can quote. That makes the value possible, not distinguishable; the contradiction with 04 and 05 is recorded as High there.
- Condition: ShippingOrderID identifies a shipping order (or these instructions as the order to ship), and the waybill and status reports quote the same value; or it is absent.
- Options: (a) preferred: drop ShippingOrderID here and let 04, 05 and 09 quote these instructions, `LD-FI-26-0322`, which the Waybill definition of ShippingOrderID allows ("Shipping Order or Forwarding Instruction"); (b) keep `LD-SH-26-0323` as a real shipping order number and use it in 04, 05 and 09.
- Needs decision: no
- From: broad, context; logistics refuted it

### air/03#F11 · Low · An exchange rate the instructions do nothing with, without a date
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: Every amount in the instructions is in XBL (declared values 512.00); no amount, charge or collect instruction is in XLC, and no instruction asks for conversion. The rate has no Date ("the date on which the exchange rate was established"), so it does not say when it applies. The rate 0.4 agrees with the world's other XBL→XLC rates (e.g. `cotton/09-ForwardingInstructions.xml:/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`).
- Condition: the exchange rate is absent, or the document uses it (an amount or charge in XLC) and dates it.
- Options: (a) preferred: remove it (nothing in forwarding instructions for a CPT shipment is settled in XLC); (b) keep it with a Date and a stated use (charges collect at Selanu, a value for the Lisavan import).
- Needs decision: no
- From: broad, money, context

### air/03#F12 · Low · Document distribution to the document's own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed". The only entry is the forwarder to whom the instructions are issued (FreightForwarderParty); it adds nothing, and no real copy recipient (carrier, consignee) is listed.
- Condition: DocumentDistribution lists only parties other than the addressee that receive a copy, or is absent.
- Options: (a) preferred: drop it; (b) distribute to a party that needs a copy.
- Needs decision: no
- From: broad, context

### air/03#F13 · Low · English renderings of the island consignee's address tagged en-XB here, en-XL elsewhere
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB` (`Reef Street`, Velumi Trading)
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Velumi Trading)
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Velumi Trading)
- Why: The same text of the same party carries `en-XL` elsewhere in the flow (`01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`, `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); the tag follows the issuer's country. Counted over `*.xml`: `en-XB">Port Wrenfield` in 35 files, `en-XL">Port Wrenfield` in 27. A rule "the writer's English" would be a legitimate reading of languageID (broad's argument in 02 and 05); the merge cannot settle which rule the world follows.
- Condition: the same rendering of the same address carries the same languageID throughout the flow, by a stated rule.
- Options: (a) preferred: `en-XL` for island names everywhere; (b) the writer's variety, recorded with the world's language conventions.
- Needs decision: yes (which convention the world follows)
- From: parties

### air/03#F14 · Low · The island consignee's legal form in one untagged rendering
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi Trading's legal form appears once, in English, without languageID, while island-issued examples give it in Lisavan and English, each tagged (`04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`), and its address is rendered in both languages here. Raised by parties only as a remark inside its language-tag finding; made a finding of its own for consistency with the wood and plastics merges.
- Condition: the legal form is rendered like the party's address (both languages, tagged), or one documented rule explains the difference.
- Options: render it like the address (preferred).
- Needs decision: no
- From: parties (remark)

### air/03#F15 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Bayforth Forwarding)
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- Why: RegistrationDate is "The registration date of the CompanyID." `1996-01-01` is the date of 25 different companies in three countries and registers (lxml over `*.xml`), in 181 example files, while other companies have individual dates (Lumeway Distribution `1988-10-03`). It reads as a default value ("no fillers").
- Condition: each company's RegistrationDate is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) preferred: a date per company from its history; (b) drop it where unknown; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes (company histories)
- From: parties

### air/03#F16 · Low · The consignee's contact does not fit its name or receiving goods
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: A consignee's contact takes delivery or arranges it. Here it is `Purchasing`, a customer service officer in Sales: name, title and department contradict each other and the role (52 occurrences of this pair over `*.xml`).
- Condition: the consignee's contact fits receiving goods, with name, title and department in agreement.
- Options: (a) preferred: an import or goods-receiving contact with matching title and department; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad, parties

### air/03#F17 · Low · Signature aggregate without a signature
- XPath: `/ForwardingInstructions/cac:Signature/cbc:ID` = `LD-SIG-FI-03`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with nothing that could be verified. Counted with lxml over `*.xml` in the merge: 137 of 147 Signature aggregates are like this (context counted 131 of 133). The ID also ends in the example's sequence number (`FI-03`) rather than the signatory's own numbering, like the IDs the wood and plastics merges flagged.
- Condition: either a verifiable signature is present, or there is no Signature aggregate; a Signature ID, where kept, is the signatory's own.
- Options: (a) preferred: drop it; (b) add signature data where the story needs a signed instruction.
- Needs decision: yes (a convention across many examples)
- From: context

### air/03#F18 · Low · DocumentStatusCode NoStatus says nothing
- XPath: `/ForwardingInstructions/cbc:DocumentStatusCode` = `NoStatus`
- Why: DocumentStatusCode signifies the status of the document "with respect to its original state"; the UBL code NoStatus states that there is no status to give, i.e. the element carries no information, which the rule "no fillers" excludes. Not raised by any part; added by the merge because the wood and plastics merges (and the parallel air merge for 06 and 08) record the same code as a Low finding.
- Condition: DocumentStatusCode is absent, or holds a status the document actually has.
- Options: drop it (preferred).
- Needs decision: no
- From: merge

## Checked and consistent
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross 81.6 kg, net 76 kg, net volume 0.42 m³ and declared value 512.00 XBL are the same in `02-OrderResponse.xml`, `04-Waybill.xml` and `06-DespatchAdvice.xml`; the declared value equals the goods value 8 × 64 = 512.00 of `01-OrderChange.xml` (`01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`) and `04-Waybill.xml:/Waybill/cbc:DeclaredCarriageValueAmount` = `512.00`.
- DeclaredStatisticsValueAmount 512.00: one goods item under one heading (HS 732599), so the statistical value is the value of all goods.
- SSCC `095206103190000015`: check digit correct (check_ids.py); company prefix 9520610 is that of Lumeway's GLN 9520610900008, in GS1's demonstration range 952.
- Weight per frame 76 / 8 = 9.5 kg, about 1.3 dm³ of cast iron at 7.2 kg/dm³ (own knowledge), within an envelope of 0.0525 m³ per frame (0.42 / 8).
- Package quantity 8, BatchQuantity 8 and the 8 items of 06 agree; TotalGoodsItemQuantity 1 and ConsignmentQuantity 1 match the one goods item and the one consignment.
- Dates: earliest pickup 2026-05-12, requested despatch 2026-05-13, requested delivery 2026-05-14, in order and not before the issue date (2026-05-12 13:44, after the order response of 10:46).
- Parties: Lumeway (consignor and signatory), Bayforth (`20411644`, Coastal State tax number matching `XB-CO`, address `LUM-ADR-953846`, contact `Export desk`, Operations planner, Operations, fitting an export booking) and Velumi (consignee, buyer of 01 and consignee of `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `IC41859`) carry the same identifiers as elsewhere in the flow.

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: an air waybill is never to order, suspected filler — refuted because `false` is correct and states explicitly that a straight consignment is wanted (from broad, context).
- `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`: against "the forwarder is booked" in `02-OrderResponse.xml` — refuted because confirming in writing a booking made on a quote is normal practice (from broad, context).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredStatisticsValueAmount` = `512.00`: a statistical value in a forwarding instruction — refuted because the forwarder may lodge the export declaration and needs it (from broad, context); under CPT it might have to include freight to the border — refuted because the price is unchanged by the change of terms and the world's statistical valuation rule is not stated (from money).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00`: pointless below the Montreal Convention limit (26 SDR/kg × 81.6 kg, own knowledge) — refuted because XBL is fictional with no SDR conversion in the world (from money).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:SplitConsignmentIndicator` = `false`: a state that cannot be known before transport — refuted because at issue time the consignment has not been split (from context).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty`: Velumi as consignee while the order names Nalevi as delivery party — refuted because under CPT Selanu airport the goods are consigned to the buyer and the warehouse collects them (from parties).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:FreightForwarderParty`: repeats the document-level forwarder — refuted: same party, identifier only (from parties).
- Bayforth's address register `urn:ubl-examples:world:XB:lumeport:address-register` (a city) against Lumeway's state register: suspected to break "address registers by country level" — refuted because the pattern is the same in all examples and the city of Lumeport may have its own register; not decidable from the examples (from parties).
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:ContainedPackage/cbc:Quantity` = `8`: one bag of 8 frames inside a box of 8 frames looked odd — refuted because both count the same 8 items (from logistics); the box's size is F2.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Pickup/cbc:ID` = `BF-PU-26-0611`: a forwarder's pickup number before the booking is confirmed — refuted because it shares 0611 with the forwarder's quote cited in 02, so the forwarder assigned it when quoting (from logistics).
- `/ForwardingInstructions/cbc:AdValoremIndicator` = `false` (from broad, refuted here as about duties and recorded in 04): the merge does not follow it; see F3.
- `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323` (from logistics): the merge does not follow it; see F10.
- Gross minus net 5.6 kg (from logistics): the merge does not follow the refutation with certainty; see F9.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; occurrence count re-run.
- broad/F2, logistics/F2 → F2: combined, with the frame-size argument and both options.
- money/F1 (High), context/F4 (Medium, needs decision yes) → F3: High, because one consignment has two values in two examples of the flow (section 6); needs decision no, because the preferred option (leave it out of both) changes no story; the valuation-charge reading of context is kept in "Why" as context, not as the meaning (semantic conformance).
- broad/F4, logistics/F3 → F4: combined.
- broad/F3, logistics/F5, context/F2 → F5: combined; the occurrence count corrected from 2 to 4 files.
- broad/F7 (Low), logistics/F4, context/F3 (Medium) → F6: Medium, as two parts; the event is meaningless without type and place, and the dedicated elements exist.
- broad/F5, parties/F1, context/F5 → F7; parties/F2, context/F6 → F8: combined.
- broad/F6 → F9: kept as Low with "Needs decision: yes" because logistics refuted it with other tare estimates and the answer depends on F2.
- broad/F8, context/F7 → F10: combined, logistics' refutation carried as the counter-argument; preferred option chosen to match 04 and 05 (see air/04#F1).
- broad/F9, money/F2, context/F8 → F11; broad/F10, context/F9 → F12; broad/F11, parties/F5 → F16: combined.
- parties/F3 → F13 and F14 (legal form split off, for consistency with wood and plastics).
- context/F10 → F17: count re-made; the signature-ID remark added for consistency with wood and plastics.
- F18 added by the merge.

## Outside this review
- The frames are made in Urvania (ManufactureDate 2026-05-10 in `06-DespatchAdvice.xml`) and are ready at the distributor's dispatch area in Marrowdale, Bayvarra, on 2026-05-12; whether that transfer is possible in two days is a cross-flow timeline question (from logistics).
