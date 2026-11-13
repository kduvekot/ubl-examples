# LLM review: 12-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/12-ForwardingInstructions.xml`, Git blob `1f7cbe1f873685d1f9299ab7815123702e495ea9` (committed)
- Last commit changing the example: 62a1919 2026-11-12 sea/12 no longer declares a carriage value; emergency card on the secondary hazard decided
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/12#F1 · High · Shipping order given as the shipment ID, while the bill of lading names this document as the shipping order
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- Why: `ShippingOrderID` is a "Reference number to identify a Shipping Order" (logistics quoted the definition with "or Forwarding Instruction", which the UBL 2.5 model does not have). These instructions are the shipping order the carrier works under: the bill of lading gives this document's own ID as its shipping order. Here the element holds the shipment's ID instead, and the port's status message the consignment ID: one booking, three shipping order numbers, and this document contradicts the bill of lading that refers to it (section 6: High).
- Condition: the shipping order of this booking has one number throughout the flow, and it is not the shipment's or the consignment's ID.
- Options: (a) preferred: drop `ShippingOrderID` here (this document is the shipping order; its `ID` identifies it) and keep `BF-FI-26-0137` in the bill of lading; (b) set it to `BF-FI-26-0137`; (c) a separate shipping order number used in 12, 13 and 14.
- Needs decision: no
- From: logistics (F1, High), context (F1, High), broad (F2, Medium)

### sea/12#F2 · Medium · A booking request to the carrier that does not say what to carry, in what, or where
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the forwarding of goods described therein". Bayforth asks the carrier to confirm a booking, but the shipment has no goods item, description, packages or HS code, no equipment (Lumeway asked for "a 40-foot container on the next sailing", `09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions` = `Book a 40-foot container on the next sailing to Selanu, arrange the truck to the port, declare the export and insure the cargo.`), no port of loading or discharge and no sailing; only a weight and the consignee. A carrier cannot book a slot or plan stowage from it, yet the bill of lading later shows the booking on a named vessel and voyage.
- Condition: the instructions state at least the goods (description, packages, gross weight), the equipment (one 42G1 container), the ports (`XBLMP` to `XLSEL`) and the sailing or date wanted, consistent with the bill of lading.
- Options: (a) preferred: goods items (or a consignment summary), the requested transport equipment and a main-carriage stage Lumeport–Selanu with the requested departure; (b) reference the transport service description `TOL-DOC-26-0130` for the service and add the cargo.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F2)

### sea/12#F3 · Medium · Shipment gross weight without the transport equipment its definition includes
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus pallets; with the 40-foot box (tare 3,750 kg) the shipment weighs 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). Not High: this document names no container.
- Condition: the shipment's gross weight includes the transport equipment, or the goods' gross weight is carried in an element that excludes it (goods items, consignment).
- Options: (a) preferred: 4,106.4 kg on goods items or the consignment (with F2); (b) 7,856.4 kg.
- Needs decision: no
- From: logistics (F3), context (F3)

### sea/12#F4 · Medium · Language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) repeats the language. 362 occurrences in 213 examples.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` (preferred by broad and context).
- Needs decision: no
- From: broad (F3), parties (F1), context (F4)

### sea/12#F5 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address"; a gate is not a street, and a postal address has no use for it. 79 occurrences in 76 examples.
- Condition: no street element of the postal address holds a gate.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F4), parties (F2), context (F8, Low)

### sea/12#F6 · Low · Carrier's booking number in instructions that ask for the booking to be confirmed
- XPath: `/ForwardingInstructions/cbc:CarrierAssignedID` = `TWL-BK-26-55710`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: `CarrierAssignedID` is the "Reference number assigned by a carrier or its agent to identify a specific shipment, such as a booking reference number when cargo space is reserved"; the bill of lading carries it as the carrier's ID (`14-BillOfLading.xml:/BillOfLading/cbc:CarrierAssignedID` = `TWL-BK-26-55710`). If the carrier has already assigned the number, the space is reserved; a request that still asks for confirmation reads as if it has not. No earlier document of the flow shows the booking. Against this (context): a forwarder typically obtains the booking number first (by portal or phone) and then sends the shipping instructions for confirmation, which would explain both values. The documents do not say which; the merge cannot settle it.
- Condition: either the documents show or say that the booking was made before these instructions (and the note refers to the booked slot), or the instructions carry no carrier-assigned number.
- Options: (a) preferred: keep the number and word the note so it refers to the existing booking (e.g. "Please confirm the shipping instructions for booking TWL-BK-26-55710"); (b) drop the number and let the bill of lading carry it first.
- Needs decision: yes (whether the booking existed before these instructions)
- From: broad (F5), logistics (F4); context considered and refuted it

### sea/12#F7 · Low · Exchange rate the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: "information about the rate of exchange (conversion) between two currencies"; the instructions contain no amount apart from the parties' share capital, and the freight is prepaid in lume by the shipper (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Ocean freight and bunker surcharge prepaid by the shipper.`). No `Date` either. Same unused rate in `09-ForwardingInstructions.xml`.
- Condition: an exchange rate only with an amount that needs it, and then dated.
- Options: (a) preferred: drop it; (b) keep it with charges collect in coral, dated.
- Needs decision: no
- From: broad (F7), money (F1), context (F5)

### sea/12#F8 · Low · Reference to the buyer's order with only an ID, sent to the carrier
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID; the carrier has no relation to the buyer's purchase order (`05-Order.xml`) and cannot tell what the reference is. The bill of lading does carry the order number as the consignor's reference (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `VT-PO-26-0127`, see its review), so the number may be wanted on the bill.
- Condition: the reference states its document type, or is absent from the carrier's instructions.
- Options: (a) preferred: a `DocumentTypeCode` for an order if the order number is wanted on the bill; (b) drop it (context's preference).
- Needs decision: no
- From: logistics (F5), context (F6)

### sea/12#F9 · Low · Contacts whose function does not fit the role
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: the carrier needs the consignor's shipping contact and the consignee's receiving contact; the consignor's is Sales' customer service, the consignee's is called Purchasing with the job title and department of a seller's customer service. (The carrier's "Bookings" contact and the forwarder's "Export desk" fit their roles.)
- Condition: contacts with agreeing name, title and department that fit the role, or none.
- Options: (a) preferred: shipping and goods-inwards contacts.
- Needs decision: no
- From: broad (F9), parties (F3, F5), context (F7, contact part)

### sea/12#F10 · Low · Party master data a booking does nothing with
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ForwardingInstructions/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ForwardingInstructions/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: share capital and state sales-tax registrations play no role in a booking with the carrier; they look copied from the parties' master data (section 4.8). The customs-trader numbers of consignor and consignee are left out of the finding: a carrier may need them for its cargo declarations.
- Condition: the parties carry only what the carriage uses.
- Options: (a) preferred: drop share capital and tax schemes.
- Needs decision: no
- From: context (F7, legal-data part; extended by the merge to the carrier and forwarder)

### sea/12#F11 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: tagged `en-XB` here, `en-XL` in the order Velumi sent (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`); the tag follows the issuer across the flow, a convention no document records.
- Condition: the same `languageID` in every example, or the issuer rule recorded.
- Options: (a) preferred: `en-XL` everywhere; (b) record the rule.
- Needs decision: yes (one rule for the world)
- From: broad (F10), parties (F4, address part)

### sea/12#F12 · Low · Velumi's legal form given once, in English, without its Lisavan form
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: the order gives it in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); here only the English, untagged.
- Condition: the same renderings in every example.
- Options: (a) preferred: both renderings, tagged.
- Needs decision: no
- From: parties (F4, legal-form part; split by the merge)

### sea/12#F13 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Bayforth (Bayvarra) and Velumi (Lisavu) share New Year's Day 1996, while Lumeway (`1988-10-03`) and Tidewell (`1974-03-01`) have their own; 271 occurrences in 181 examples.
- Condition: own dates, or absent.
- Options: (a) preferred: own dates; (b) leave the element out.
- Needs decision: yes
- From: parties (F6)

### sea/12#F14 · Low · Document status "NoStatus"
- XPath: `/ForwardingInstructions/cbc:DocumentStatusCode` = `NoStatus`
- Why: "A code signifying the status of the Forwarding Instructions with respect to its original state"; `NoStatus` states nothing a receiver acts on (no fillers). Not raised by any part; added by the merge, as in 09 and the earlier flows.
- Condition: absent or a status that matters.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: merge

### sea/12#F15 · Low · A signature with an ID and the signatory only, its ID carrying the example number
- XPath: `/ForwardingInstructions/cac:Signature/cbc:ID` = `BF-SIG-FI-12`
- XPath: `/ForwardingInstructions/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: no method, date, attachment or signing person; the ID ends in `12`, this example's position in the flow. Not raised by any part; added by the merge, as in 09.
- Condition: a signature, where present, says how and when the document was signed, with the signer's own reference.
- Options: (a) preferred: drop it; (b) complete it.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- The booking number is the one on the bill of lading, which references these instructions (`14-BillOfLading.xml:/BillOfLading/cac:DocumentReference/cbc:ID` = `BF-FI-26-0137`) and quotes their ID as shipping order.
- Consignor Lumeway, forwarder Bayforth (issuer and signatory), carrier Tidewell and consignee Velumi agree with 09 and 14; shipment `LD-SH-26-0132`, consignment `LD-CS-26-0133` and the gross weight 4,106.4 kg agree with 09, 10, 11 and 14.
- "Send the bill of lading to the forwarder." asks the carrier to send it to Bayforth, which the bill of lading does (`14-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`).
- Issued 2026-05-10 09:15, the morning after Lumeway's instructions (2026-05-09 16:45), before the cargo acceptance at the port.
- GLN check digit correct (`check_ids.py`, from broad).

## Considered and refuted
- Forwarding instructions sent by the forwarder to the carrier — refuted because UBL defines the document as used by any party who gives instructions for the transportation services to any party contracted to provide them, carriers included (from broad).
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `true` with a named consignee — refuted: "to the order of" a named consignee is a common form (from broad).
- `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.` in a document the forwarder issues — refuted: the forwarder asks the carrier to send the bill to itself, which `14-BillOfLading.xml` does (from parties, context).
- `/ForwardingInstructions/cbc:Description`: the same name, description and note as Lumeway's instructions in 09 — refuted: the forwarder passing on the instructions in the same words is plausible (from context).
- `/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`, dated 2026-05-10, while the forwarder's export declaration `BF-EX-26-0135` is dated 2026-05-12 — refuted: the flow's numbers form one running counter over all issuers (from logistics).
- `/ForwardingInstructions/cbc:CarrierAssignedID`: the booking number on instructions that ask for confirmation — refuted by context (number obtained first). Not followed: kept as F6, Low/yes, with both arguments.

## Refuted in the merge
### broad/F6 · Low · Text copied from the consignor's instructions
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the shipment to the island.`
- Why (broad): name, description, note and other instruction are word for word those of `09-ForwardingInstructions.xml`; nothing replaces the consignor's service instructions with what the carrier must do. Condition: the free texts are those of the forwarder's instructions to the carrier.
- Refuted because: each text fits the forwarder's instructions to the carrier as well (the bill is to go to Bayforth, and does; the description is neutral), as the parties and context parts found; what the carrier must do is missing, but that is F2 (no goods, equipment, ports), not a problem of the free texts.

### broad/F8 · Low · Distribution of the instructions to their own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Tidewell Ocean Lines`
- Why (broad): the distribution list names the carrier, the party the instructions are addressed to, for this very document. Condition: distribution names parties other than the addressee, or is absent.
- Refuted because: Forwarding Instructions have no receiver element; the distribution list is where the document says to whom and how it is sent, and the definition ("A list of interested parties to whom this document is distributed") does not exclude the main addressee. Context checked the distribution to the carrier as fitting. Same as in `09-ForwardingInstructions.xml`.

## Changed in the merge
- logistics/F1, context/F1 (High), broad/F2 (Medium) → F1: High kept (contradiction with `14-BillOfLading.xml`, which refers to this document).
- broad/F5, logistics/F4 (Low, no) → F6: needs decision set to yes, because context's refutation (booking number obtained before the instructions) is a legitimate reading the merge cannot exclude.
- context/F7 → F9 and F10: split into contacts and copied party data; F10 extended to the carrier's share capital and all three tax schemes.
- context/F8 (Low) → F5: Medium, aligned.
- parties/F4 → F11 and F12 (split); broad/F10 (no) aligned to yes.
- LocaleCode: preferred option set to drop.
- F14, F15 added by the merge (no part raised them).

## Outside this review
- Timeline: issued on a Sunday (2026-05-10, recomputed), while the parties' contacts work "Weekdays 08:00–17:00"; and after the service's nomination deadline of 2026-05-09 10:00 in `08-TransportServiceDescription.xml` (see its review) (from broad, logistics, context).
- Issued before the packing list and the export declaration it would rely on (2026-05-12) (from context).
