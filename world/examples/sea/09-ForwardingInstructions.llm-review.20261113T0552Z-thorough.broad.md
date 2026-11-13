# LLM review: 09-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/09-ForwardingInstructions.xml`, Git blob `ba67389d2ddd1ff0fe54f4614822678c58b812b2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/09#F1 · Medium · Forwarding instructions that do not describe the goods
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions` = `Book a 40-foot container on the next sailing to Selanu, arrange the truck to the port, declare the export and insure the cargo.`
- Why: the document is "issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein". Apart from the gross weight, nothing says what the goods are: no goods item, no description, no commodity code, no number of pallets or packages, no volume. The forwarder is asked to book a container, declare the export and insure the cargo without knowing the goods, their HS codes or their value per item; the only hint is the order number (`/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`), a document between buyer and seller that the forwarder does not receive. The forwarder's instructions to the carrier one day later do not describe them either (`12-ForwardingInstructions.xml`); the goods first appear in the packing list and the export declaration of 2026-05-12.
- Condition: the instructions describe the goods to be forwarded (at least goods items with description, quantity, packages, weight and commodity code), consistent with the packing list.
- Options: (a) preferred: add goods items for the benches and the side frames (as in the packing list); (b) attach the commercial invoice/packing list by reference with a type code and state the pallet count.
- Needs decision: no

### sea/09#F2 · Medium · Shipment ID given as shipping order ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- Why: `ShippingOrderID` is "Reference number to identify a Shipping Order", i.e. a booking document; `Shipment/ID` identifies the shipment. The same number fills both, so either the shipment number is passed off as a shipping order, or the shipping order and the shipment are one thing; the identifier's prefix (`SH`) and the shipment element suggest the former.
- Condition: `ShippingOrderID` identifies a shipping order (booking), distinct from the shipment ID, or is absent.
- Options: (a) preferred: drop `ShippingOrderID` (Lumeway has issued no shipping order; these instructions are the request); (b) a shipping order number of its own if one exists.
- Needs decision: no

### sea/09#F3 · Medium · Language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/09#F4 · Medium · A gate in AdditionalStreetName
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in the postal address. Here the gate does matter, for the truck that collects the goods, but then it belongs in the pickup location, not in the consignor's postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate; where the gate matters it is given with the pickup location.
- Options: (a) preferred: drop it from the postal address and give it in the pre-carriage pickup location.
- Needs decision: no

### sea/09#F5 · Low · Final delivery haulage instructed by the seller under CIF
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:FinalDeliveryTransportationService/cbc:Name` = `Truck from the port of Selanu to the 3PL`
- Why: `FinalDeliveryTransportationService` is "The service for delivery to the consignee under the transport contract for this consignment". The sale is CIF Port of Selanu (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`): the seller's transport contract ends at the port of destination, and the bill of lading has the consignee's 3PL as on-carrier (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`). The forwarding service instructions do not ask for it either. Lumeway naming the on-carriage as part of its transport contract contradicts the trade term.
- Condition: the seller's instructions cover only the transport the seller contracts under the trade term, or the documents say that Lumeway arranges on-carriage on Velumi's behalf.
- Options: (a) preferred: drop the final delivery service; (b) state that the forwarder arranges it on behalf and for the account of Velumi.
- Needs decision: yes (who arranges the on-carriage)

### sea/09#F6 · Low · Insurer given as the party that holds the insurance
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:InsuranceParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: `InsuranceParty` is "The Party who holds the insurance for this Consignment", i.e. the policyholder; the insurer is named separately in `InsurerParty`. Under CIF the seller takes out the insurance, and the instructions ask the forwarder to "insure the cargo"; the holder is Lumeway (or the forwarder on its behalf), not the insurer.
- Condition: `InsuranceParty` is the policyholder (Lumeway, or the forwarder if it insures in its own name), or absent.
- Options: (a) preferred: Lumeway as `InsuranceParty`; (b) drop it, since `InsurancePolicy` already names the insurer.
- Needs decision: no

### sea/09#F7 · Low · Exchange rate the document does not use
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the only amount in the instructions is the insured value in lume; nothing is stated or to be converted in coral. The rate looks like master data copied in.
- Condition: an exchange rate appears only where an amount of the document is converted with it.
- Options: (a) preferred: drop it; (b) state why the forwarder needs it (e.g. a value to declare in coral), with that value.
- Needs decision: no

### sea/09#F8 · Low · Distribution of the instructions to their own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cbc:DocumentTypeCode` = `ForwardingInstructions`
- Why: `DocumentDistribution` is "A list of interested parties to whom this document is distributed"; it names the forwarder, the party the instructions are addressed to (`FreightForwarderParty`), for this very document type. It adds no interested party.
- Condition: document distribution names parties other than the addressee that receive a copy, or is absent.
- Options: (a) preferred: drop it; (b) name a real copy recipient (e.g. the insurer).
- Needs decision: no

### sea/09#F9 · Low · Contacts whose function does not fit
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:Name` = `Cargo claims`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: the consignor gives forwarding instructions through Sales' customer service; the consignee's contact (who receives goods) is purchasing, with the job title of a seller's customer service; the insurer's "Cargo claims" contact is a client relationship manager in client services. Name, job title, department and role do not agree.
- Condition: each contact's name, job title and department agree with each other and fit the party's role in the document.
- Options: (a) preferred: a shipping contact for the consignor, a goods-in contact for the consignee (or its 3PL), a claims handler for the insurer.
- Needs decision: no

### sea/09#F10 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (16 × `en-XB`, 8 × `en-XL` over `world/examples/sea/*.xml`).
- Condition: Velumi's address renderings carry the same `languageID` in every example.
- Options: (a) preferred: `en-XL` everywhere.
- Needs decision: no

## Checked and consistent
- Insured value: CIF value 50,688.00 goods + 2,950.00 freight + 140.00 insurance (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`, `…[2]` = 140.00) = 53,778.00 × 110 % = 59,155.80 XBL = `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount`.
- Gross weight 4106.4 kg agrees with the packing list and the bill of lading.
- Consignment `LD-CS-26-0133` is the consignment the port's status refers to (`13-TransportationStatus.xml`); consignee and importer Velumi, exporter Lumeway agree with the order.
- A 40-foot container on the next sailing agrees with the service offered (`08-TransportServiceDescription.xml`, 42G1, sailing 2026-05-14) and with the bill of lading's 42G1.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `true` with a named consignee — refuted because a bill of lading "to the order of" a named consignee is a common form, and the bill of lading has the same indicator.
- `/ForwardingInstructions/cbc:AdValoremIndicator` = `false` — refuted because no value is declared for ad valorem freight; the indicator then legitimately says so.
- `/ForwardingInstructions/cbc:IssueDate` = `2026-05-09` after the service's nomination deadline 10:00 that day — not a problem of this example; see `08-TransportServiceDescription.xml`.
