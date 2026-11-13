# LLM review: 09-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/09-ForwardingInstructions.xml`, Git blob `ba67389d2ddd1ff0fe54f4614822678c58b812b2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### sea/09#F1 · High · The insurer given as the party that holds the insurance; the bill of lading names Lumeway Distribution as policy holder
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:InsuranceParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: UBL defines `Consignment/InsuranceParty` as "The Party who holds the insurance for this Consignment", i.e. the insured or policy holder; the insurer is named separately in `InsurancePolicy/InsurerParty` ("The Party providing the insurance"). Here both are Wavesure Cargo Insurance. The bill of lading for the same consignment `LD-CS-26-0133` names Lumeway Distribution as the holder (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyHolderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`), which also fits the delivery term CIF (the seller insures, `05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`) and the instruction to the forwarder to "insure the cargo". The two examples contradict each other about who holds the insurance (section 6: High).
- Condition: `InsuranceParty` names the party that holds the cargo insurance, the same party as the policy holder in `14-BillOfLading.xml`, or is absent.
- Options: (a) preferred: Lumeway Distribution as `InsuranceParty` (CIF seller, policy holder in the bill of lading); (b) drop `InsuranceParty`, since `InsurancePolicy` already names the insurer.
- Needs decision: no (the bill of lading already settles the story; context asked for a decision)
- From: parties (F1, High), broad (F6, Low), context (F4, Low)

### sea/09#F2 · Medium · Forwarding instructions that do not describe the goods
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions` = `Book a 40-foot container on the next sailing to Selanu, arrange the truck to the port, declare the export and insure the cargo.`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:OriginalDespatchTransportationService/cbc:Name` = `Truck from Marrowdale to the port of Lumeport`
- Why: Forwarding Instructions are "A document issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein". Apart from the gross weight, nothing says what the goods are: no goods item, description, commodity code, number or kind of packages, volume or value per item. The forwarder is asked to book a container, declare the export (the declaration lists two goods items, `11-ExportCustomsDeclaration.xml`) and insure the cargo (59,155.80 XBL, insured as what?) without knowing the goods; the only hint is the buyer's order number, a document the forwarder does not receive. The places appear only in the names of the pre- and on-carriage services, and pickup date and sailing are not given ("the next sailing"). The forwarder's instructions to the carrier one day later do not describe the goods either (`12-ForwardingInstructions.xml`); the goods first appear in the packing list and the export declaration of 2026-05-12.
- Condition: the instructions describe the goods to be forwarded (at least goods items with description, quantity, packages, gross weight and commodity code), consistent with the packing list, and the places of pickup and delivery in structured elements.
- Options: (a) preferred: add the two goods items (benches, side frames) with quantities, pallets and weights as in the packing list, and pickup and delivery locations; (b) reference the commercial documents with a type code and state the pallet count (weaker: the packing list is issued three days later).
- Needs decision: no
- From: broad (F1), logistics (F2)

### sea/09#F3 · Medium · Shipment ID given as shipping order ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- Why: `ShippingOrderID` is a "Reference number to identify a Shipping Order" (logistics quoted the definition with "or Forwarding Instruction", which the UBL 2.5 model does not have); `Shipment/ID` identifies the shipment. The same number fills both, so an identifier of one kind is used as another. This instruction has its own ID `LD-FI-26-0131`, which the bill of lading records as the forwarder's reference (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`). Elsewhere in the flow the shipping order is `BF-FI-26-0137` (the forwarder's instruction to the carrier, in the bill of lading) and the consignment ID (port status), so three numbers name the shipping order of one shipment.
- Condition: `ShippingOrderID`, if present, identifies a shipping order or forwarding instruction, not the shipment or the consignment.
- Options: (a) preferred: drop it (Lumeway's instruction precedes the carrier booking, and the document's own `ID` identifies it); (b) a shipping order number of its own, used consistently.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1, High)

### sea/09#F4 · Medium · Shipment gross weight without the transport equipment its definition includes
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus pallets (the goods items in `10-PackingList.xml`: 3,984 + 122.4 = 4,106.4). The 40-foot container these instructions ask to book weighs 3,750 kg tare; loaded it is 4,106.4 + 3,750 = 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). The semantic-conformance rule applies the UBL definition even where practice reads the shipment's gross weight without the box. The same value is in 10, 11, 12, 14 and 15.
- Condition: the shipment's gross weight includes the transport equipment, or the weight of goods and packaging is given in an element whose definition fits it (goods items' or consignment's gross weight).
- Options: (a) preferred: carry 4,106.4 kg as goods-item (or consignment) gross weight and leave the shipment's gross weight out at this stage, when no box is assigned; (b) 7,856.4 kg once the container is known.
- Needs decision: no
- From: logistics (F3), context (F2)

### sea/09#F5 · Medium · Language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is the language code itself and repeats `Language/ID`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, files with `grep -rl`).
- Condition: each `LocaleCode` is absent or a locale code from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode` (nothing in the document depends on a locale; as all earlier flows); (b) a locale such as `en-XB` from a locale list (preferred by broad and context).
- Needs decision: no
- From: broad (F3), parties (F2), context (F3)

### sea/09#F6 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate of the business park is not a street name, and a postal address has no use for it. Here the gate does matter, for the truck that collects the goods, but then it belongs in the pre-carriage pickup location. 79 occurrences in 76 examples, 25 sea examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street element of the postal address holds a gate; where the gate matters it is given with the pickup location.
- Options: (a) preferred: drop it from the postal address and, if needed, give it in the pickup location of the pre-carriage.
- Needs decision: no
- From: broad (F4), parties (F3), context (F9, Low)

### sea/09#F7 · Low · Final delivery haulage in the seller's instructions under CIF
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:FinalDeliveryTransportationService/cbc:Name` = `Truck from the port of Selanu to the 3PL`
- Why: `FinalDeliveryTransportationService` is "The service for delivery to the consignee under the transport contract for this consignment". The sale is CIF Port of Selanu (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`): the seller's contract of carriage ends at the port of destination, and the bill of lading has the buyer's 3PL as on-carrier (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`). The forwarder's service instructions do not ask for on-carriage either. The parties part found the service consistent with the order's delivery party Nalevi; the destination agrees, but who contracts the haulage does not follow from the trade term.
- Condition: the seller's instructions cover only the transport the seller contracts under the trade term, or the documents say that Lumeway arranges on-carriage on Velumi's behalf.
- Options: (a) preferred: drop the final delivery service; (b) state that the forwarder arranges it on behalf and for the account of Velumi, and add it to the service instructions.
- Needs decision: yes (who arranges the on-carriage in Selanu)
- From: broad (F5), context (F5)

### sea/09#F8 · Low · Exchange rate the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ExchangeRate` is "information about the rate of exchange (conversion) between two currencies". The only amount is the insured value in lume (`/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`); nothing is stated in or to be converted to coral, and the rate has no `Date`. It looks like master data copied in (no fillers).
- Condition: an exchange rate appears only where an amount of the document is in, or must be converted to, the target currency, and then with its date.
- Options: (a) preferred: drop it; (b) keep it with an amount that needs it (e.g. a value to declare in coral) and a date.
- Needs decision: no
- From: broad (F7), money (F1), context (F6)

### sea/09#F9 · Low · Reference to the purchase order with only an ID
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID; the forwarder cannot tell that `VT-PO-26-0127` is the buyer's purchase order (it resolves to `05-Order.xml`). The checklist asks that "a reference with only an ID says what it refers to where that is not obvious".
- Condition: the reference states its document type (type code or description).
- Options: (a) preferred: a `DocumentTypeCode` for an order (e.g. UN/EDIFACT 1001 `220`) or a `DocumentType`.
- Needs decision: no
- From: logistics (F4), context (F7)

### sea/09#F10 · Low · Contacts whose function does not fit the role
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:Name` = `Cargo claims`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: the consignor gives forwarding instructions through Sales' customer service, the same contact as in the catalogue and order, while the forwarder's questions (cargo, pickup, export) go to shipping or despatch; the consignee's contact, who should receive the goods, is called Purchasing, with the job title and department of a seller's customer service; the insurer's "Cargo claims" contact is a client relationship manager in client services. Name, job title, department and role do not agree.
- Condition: each contact's name, job title and department agree with each other and fit the party's role in this document, or the contact is absent.
- Options: (a) preferred: a shipping contact for the consignor, a goods-in or import contact for the consignee (or its 3PL), a claims handler for the insurer; (b) leave out contacts nobody needs here.
- Needs decision: no
- From: broad (F9), parties (F4, F6), context (F8)

### sea/09#F11 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: the English renderings carry `languageID="en-XB"` (English as used in Bayvarra); the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`, with `languageID` `en-XL`). Across the flow the tag follows the issuer's country (parties: Bayvarran issuers 01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26; Lisavan issuers 05, 17, 19, 21, 24, 27–29). Whether a rendering is tagged with the issuer's or the place's variety of English is a convention of the world that no document records.
- Condition: Velumi's address renderings carry the same `languageID` in every example, or the world records the rule that the tag follows the issuer.
- Options: (a) preferred: `en-XL` everywhere (broad, parties), as in the order; (b) record the issuer rule.
- Needs decision: yes (one rule for the world; as cotton, road, rail and air)
- From: broad (F10), parties (F5, address part)

### sea/09#F12 · Low · Velumi's legal form given once, in English, without its Lisavan form
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: in the order Velumi issued, its legal form is given in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`, and `[2]` = `Island limited company` tagged `en-XL`); here the Lisavan form is missing and the English one is untagged, while the address next to it is given in both languages. The same party is described differently in the flow.
- Condition: Velumi's legal form is given the same way (renderings and `languageID`) in every example.
- Options: (a) preferred: both renderings, tagged, as in the order.
- Needs decision: no
- From: parties (F5, legal-form part; split by the merge)

### sea/09#F13 · Low · The same registration date 1996-01-01 for unrelated companies in two countries
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Bayforth Forwarding, Wavesure Cargo Insurance (federal business register of Bayvarra) and Velumi Trading (island companies register) share New Year's Day 1996, while parties with a known history have their own dates (Lumeway `1988-10-03`). 271 occurrences in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, files with `grep -rl`). It reads as a default value, not a fact of the world (no fillers).
- Condition: every `RegistrationDate` is that party's registration date in the world, or absent where the world has none.
- Options: (a) preferred: own dates from the parties' histories; (b) leave the element out where the world does not know the date.
- Needs decision: yes
- From: parties (F7)

### sea/09#F14 · Low · Party master data the instructions do nothing with
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234521`
- Why: forwarding instructions carry no tax and no capital; the consignor's share capital and the state sales-tax registrations of consignor, forwarder and insurer look copied from the parties' master data (section 4.8, no fillers). Not raised by any part; added by the merge for consistency with the earlier flows. The customs-trader numbers of consignor (`XB-TR-410274`) and consignee (`XL-TR-041859`) are not part of this finding: the forwarder is asked to declare the export and needs the exporter's customs number.
- Condition: the parties carry only the data the forwarder uses (identification, address, contact, customs number).
- Options: (a) preferred: drop share capital, fully-paid indicator and the tax schemes.
- Needs decision: no
- From: merge

### sea/09#F15 · Low · Document status "NoStatus"
- XPath: `/ForwardingInstructions/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Forwarding Instructions with respect to its original state"; `NoStatus` states nothing a receiver would act on, so the element has no business reason (no fillers). Not raised by any part; added by the merge, as in retail and cotton.
- Condition: `DocumentStatusCode` is absent or states a status that matters (e.g. a replacement).
- Options: (a) preferred: drop it.
- Needs decision: no
- From: merge

### sea/09#F16 · Low · A signature with an ID and the signatory only, its ID carrying the example number
- XPath: `/ForwardingInstructions/cac:Signature/cbc:ID` = `LD-SIG-FI-09`
- XPath: `/ForwardingInstructions/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the signature has no method, date, signature attachment or signing person, so it states no signature beyond the issuer; its ID ends in `09`, the position of this example in the flow rather than a number of Lumeway's. Not raised by any part; added by the merge, aligned with retail, air and utilities (empty signature) and cotton/road (example number in the ID).
- Condition: a signature, where present, says how and when the document was signed, and its ID is the signer's own reference.
- Options: (a) preferred: drop the signature; (b) complete it (method, time, signer) with an ID of Lumeway's numbering.
- Needs decision: yes (whether the world's documents are signed at all; as retail/air)
- From: merge

## Checked and consistent
- Insured value: CIF value 50,688.00 goods + 2,950.00 freight + 140.00 premium (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`, `22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`) = 53,778.00 (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`; `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:Amount` = `53778.00`); × 1.10 = 59,155.80 = `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` (recomputed). The same insured value is in the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:InsuranceValueAmount` = `59155.80`).
- Gross weight 4,106.4 kg agrees with the packing list and the bill of lading (but see F4).
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` are the same in 10, 11, 12 and 14; consignee/importer Velumi, consignor/exporter Lumeway and forwarder Bayforth agree with the order and the later documents; Wavesure is described identically in 14.
- "Send the bill of lading to the forwarder." agrees with the bill of lading's distribution of the originals (`14-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`, `ORIGINALCOURIER`).
- A 40-foot container on the next sailing agrees with the service offered (`08-TransportServiceDescription.xml`) and the bill of lading; "Load the castings last, behind the doors" agrees with the packing list's "Castings pallet at the doors." and with the frames being pallet `025 of 025` on the bill of lading. `ConsolidatableIndicator` false fits a full container.
- Issued 2026-05-09 16:45, after the order response (2026-05-08) and the transport service description (2026-05-09 12:03), before the forwarder's booking (`12-ForwardingInstructions.xml`, 2026-05-10).
- GLN check digit correct (`check_ids.py`, from broad).

## Considered and refuted
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `true` with a named consignee — refuted because a bill of lading "to the order of" a named consignee is a common form, and the bill of lading has the same indicator (from broad, context).
- `/ForwardingInstructions/cbc:AdValoremIndicator` = `false` — refuted because no value is declared, and an explicit false states that nothing is charged on the value (IND6: an explicit statement is not a filler). The UBL definition speaks of ad valorem duties ("certain duties … levied on commodities at certain rates per centum on their value"), which a forwarding instruction does not set either way (from broad, context; the merge notes the definition).
- `/ForwardingInstructions/cbc:IssueDate` = `2026-05-09` after the service's nomination deadline 10:00 that day — not a problem of this example; see `08-TransportServiceDescription.xml` (from broad).
- `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`: suspected that on 2026-05-09 the shipper could not yet know the CIF value, which contains freight and premium only fixed in the bill of lading of 2026-05-14 — refuted because the ocean freight is a published box rate under the carrier's tariff (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:TariffCode` = `TWL-T-0940`) and the premium a known rate (from money).

## Refuted in the merge
### broad/F8 · Low · Distribution of the instructions to their own addressee
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cbc:DocumentTypeCode` = `ForwardingInstructions`
- Why (broad): `DocumentDistribution` is "A list of interested parties to whom this document is distributed"; it names the forwarder, the party the instructions are addressed to, for this very document type, and adds no interested party. Condition: document distribution names parties other than the addressee that receive a copy, or is absent.
- Refuted because: Forwarding Instructions have no receiver element; `FreightForwarderParty` names the forwarder's role, and the distribution list is where the document says to whom and how (`ELECTRONIC`) it is sent. The parties and context parts refuted the same candidate on these grounds; the definition does not exclude the main addressee.

## Changed in the merge
- parties/F1 (High), broad/F6 (Low), context/F4 (Low, yes) → F1: High kept (contradiction with `14-BillOfLading.xml`, same consignment); needs decision set to no, because the bill of lading already says who holds the policy.
- context/F1 (High) → F3: Medium, with broad and logistics. 09 is Lumeway's instruction to its forwarder; a different shipping order number in the bill of lading (the forwarder's instruction to the carrier) is not a contradiction of this document, so the misuse of the element (Medium) remains.
- context/F9 (Low) → F6: Medium, aligned with broad and parties and all earlier flows.
- parties/F5 → F11 and F12: split into the tag question (Low, yes) and the missing Lisavan legal form (Low, no), as in cotton, road, rail and air. broad/F10 (no) aligned to yes for the tag rule.
- LocaleCode: preferred option set to drop (parties), broad's and context's locale kept as option (b).
- F14, F15, F16 added by the merge (no part raised them), for consistency with the earlier flows' merges.

## Outside this review
- These instructions (2026-05-09 16:45) and the forwarder's instructions to the carrier (`12-ForwardingInstructions.xml`, 2026-05-10 09:15) precede the packing list (`10-PackingList.xml`, 2026-05-12) and the export declaration (`11-ExportCustomsDeclaration.xml`, 2026-05-12); the numbering of IDs (0131, 0134, 0135, 0137) does not follow the issue order. A timeline question across documents (from context).
