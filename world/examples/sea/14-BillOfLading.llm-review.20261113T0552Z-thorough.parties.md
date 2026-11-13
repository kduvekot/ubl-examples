# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 01cf804 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/14#F1 · High · Final delivery party is the buyer, while the goods are delivered to its 3PL Nalevi Warehousing
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:FinalDeliveryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:LogisticsOperatorParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: UBL defines `Consignment/FinalDeliveryParty` as "The final delivery party for this consignment", the party to which the goods are finally delivered (the consignee is a separate element). The goods go from the port of Selanu to the warehouse of Nalevi Warehousing, which in this very document carries them on (on-carriage carrier, with a warehousing and a receipt event) and operates the logistics. The order names Nalevi as the party receiving the goods (`05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`) and the packing list says `10-PackingList.xml:/PackingList/cac:Shipment/cbc:DeliveryInstructions` = `Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.`. Naming Velumi Trading (the consignee, whose address is its office in Reef Street) as final delivery party contradicts this example’s own on-carriage and the two other examples.
- Condition: `FinalDeliveryParty` is the party where the consignment is finally delivered, consistent with the on-carriage of this example and with 05-Order.xml and 10-PackingList.xml.
- Options: Preferred: Nalevi Warehousing as final delivery party; Velumi Trading stays consignee. Alternative: drop `FinalDeliveryParty` if the bill of lading need not name it (the on-carriage stage already does).
- Needs decision: no

### sea/14#F2 · Medium · Bill of lading holder given as the consignee, while the three originals go to the forwarder
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:BillOfLadingHolderParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cbc:ToOrderIndicator` = `true`
- XPath: `/BillOfLading/cbc:OtherInstruction` = `Three originals issued.`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- Why: `BillOfLadingHolderParty` is "The Party who holds the Bill of Lading for this Consignment". This bill is issued to order, in three originals, and the originals are sent by courier to Bayforth Forwarding, as 12-ForwardingInstructions.xml asked ("Send the bill of lading to the forwarder"). At the time of issue the holder is therefore the forwarder (for the shipper), not Velumi Trading; Velumi becomes holder only when the originals are endorsed and handed over to it. The holder role contradicts the distribution in the same document, unless the element is meant as the intended final holder, which its definition does not say.
- Condition: The bill of lading holder named in the document is the party that holds the originals at the time the document states, consistent with `DocumentDistribution`.
- Options: Preferred: name the party that holds the originals at issue (Bayforth Forwarding, or Lumeway Distribution as shipper if the forwarder holds them on its behalf). Alternative: keep Velumi Trading and change the distribution and story so that the originals go to Velumi.
- Needs decision: yes

### sea/14#F3 · Medium · A language code in LocaleCode
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/14#F4 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/14#F5 · Low · Lumeway Distribution’s sales customer-service contact used in a transport role
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: In this example Lumeway Distribution is the consignor (shipper) of the bill of lading. Its only contact is the sales department’s customer service, the same as in the catalogue and the order documents. For the questions this document raises (cargo, pickup, export formalities) the carrier, forwarder or authority needs Lumeway’s shipping or despatch contact; the checklist asks that a contact fit the party’s role in the document.
- Condition: The contact given for Lumeway Distribution in this example is one that handles the shipment (despatch, shipping or export), or there is none.
- Options: Preferred: give Lumeway Distribution a despatch or shipping contact for its transport roles. Alternative: leave the contact out of the transport documents where nobody needs to reach Lumeway about the shipment.
- Needs decision: no

### sea/14#F6 · Low · Velumi Trading and Nalevi Warehousing described differently from 05-Order.xml (English renderings tagged en-XB, legal form only in English)
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by Tidewell Ocean Lines) the English renderings of Velumi Trading’s (and the notify party Nalevi Warehousing’s) street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself Velumi Trading has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example. Nalevi Warehousing has the en-XL form there: `05-Order.xml:/Order/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`.
- Condition: Velumi Trading and Nalevi Warehousing carry the same address renderings, `languageID` values and legal-form renderings in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/14#F7 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. In this example Velumi Trading is the consignee, so its contact should be whoever receives the goods or handles their arrival, not purchasing. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/14#F8 · Low · The notify party’s contact: goods inwards described as a sales customer-service officer
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Department` = `Sales`
- Why: The notify party is notified on arrival; its contact `Goods inwards` fits that, but its job title and department are the sales customer-service pair the world uses for sellers. Goods receipt is a warehouse operations function; name, title and department do not agree. The same contact is used in 05-Order.xml.
- Condition: Name, job title and department of Nalevi Warehousing’s contact agree with each other and with goods receipt.
- Options: Preferred: a warehouse or goods-receipt title and department (e.g. operations). Alternative: keep only the functional name.
- Needs decision: no

### sea/14#F9 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Bayforth Forwarding (freight forwarder), Velumi Trading (consignee), Nalevi Warehousing (notify party) and Wavesure Cargo Insurance (insurer). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

### sea/14#F10 · Low · One cargo insurance split over two policies: holder, broker and beneficiary in one, insurer in the other
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyHolderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: The consignment’s policy `WS-CP-26-4471` names the policy holder (Lumeway Distribution), the broker (Bayforth Forwarding) and the beneficiary (Velumi Trading) but no insurer; the shipment carries a second policy without ID, with the same insured value and excess, which names only the insurer (Wavesure Cargo Insurance) and again the broker. There is one cargo insurance in the flow (09-ForwardingInstructions.xml: "insure the cargo"); split like this, the insurer cannot be linked to the policy number and the holder, and the broker is given twice.
- Condition: The cargo insurance appears once, with its ID, insurer, holder, broker and beneficiary in the same `InsurancePolicy`, or the two aggregates are clearly two different policies.
- Options: Preferred: one `InsurancePolicy` (at consignment level, where the certificate `WS-CERT-26-0884` belongs) with all its parties. Alternative: if both levels are wanted, give the shipment-level policy the same ID and the same parties.
- Needs decision: no

## Checked and consistent
- Consignor Lumeway Distribution, carrier and signatory Tidewell Ocean Lines, freight forwarder Bayforth Forwarding and consignee Velumi Trading agree with 09-ForwardingInstructions.xml, 10-PackingList.xml and 12-ForwardingInstructions.xml; the original despatch party is the consignor; the equipment supplier is the carrier (container prefix of Tidewell).
- Verified gross mass: weighing party, shipper party and responsible party are all Lumeway Distribution, which fits SOLAS method 2 (the shipper weighs the contents and adds the tare) and the shipper’s own scale `LD-SCALE-03`.
- Insurance parties: policy holder Lumeway Distribution (the CIF seller), beneficiary Velumi Trading (the buyer, to whom risk passes on board), broker Bayforth Forwarding (instructed in 09 to insure the cargo) — consistent with the delivery terms of this example.
- The scanned copy goes to Nalevi Warehousing, the notify party and on-carriage carrier, which needs the bill to collect the container.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty` = the freight forwarder Bayforth Forwarding (ISIC `5229`) as road carrier — refuted: 09-ForwardingInstructions.xml instructs Bayforth to "arrange the truck to the port", and a forwarder that contracts the haulage in its own name is the carrier of that stage.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty` = Nalevi Warehousing, a warehouse company — refuted: a 3PL that collects containers from the port with its own trucks is a normal set-up, and the final delivery service in 09 is "Truck from the port of Selanu to the 3PL".
