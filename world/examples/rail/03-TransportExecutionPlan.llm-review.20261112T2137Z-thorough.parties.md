# LLM review: 03-TransportExecutionPlan.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/03-TransportExecutionPlan.xml`, Git blob `10a1218954b5cf3553a1e440bbc205476072297d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/03#F1 · Medium · Province in Region of four Urvanian addresses
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The Bayvarran consignee's address in the same document uses CountrySubentity (`/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where the province is given, it is in cbc:CountrySubentity.
- Options: (a) move the province to CountrySubentity (preferred); (b) drop it where postal zone and city already locate the address.
- Needs decision: no

### rail/03#F2 · Medium · Language code in LocaleCode of the consignee
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language. Locale Code is "A code signifying the locale in which this language is used." `en` (listID ISO 639) is a language code and repeats `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`; a locale names language and region. The value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the consignee's Language has no LocaleCode, or one that names a locale from a list of locales.
- Options: (a) drop it (preferred); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### rail/03#F3 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the site, not a street name; and the plan delivers by rail to the siding (`/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`), so the gate is not even the delivery point.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) remove it from the postal address (preferred); (b) state a gate, where needed, at a delivery location.
- Needs decision: no

### rail/03#F4 · Medium · AtLocation names the carrier, not a place
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- Why: Transport Execution Plan. At_ Location is "The location of a transport service (e.g., terminal handling service) that does not require transport movement." Its only content is the name of the transport service provider (`/TransportExecutionPlan/cac:TransportServiceProviderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`), a company, with no address or identifier. It names no place where a stationary service is performed, and the plan's services (collection, rail carriage, pre-arrival notice) all involve movement between From and To.
- Condition: AtLocation, if present, names a place (with address or identifier) where a service without transport movement is performed under this plan.
- Options: (a) drop AtLocation (preferred: no stationary service is planned); (b) if terminal handling at the hub is part of the service, name the hub's terminal there and describe that service.
- Needs decision: no

### rail/03#F5 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings next to them are different names, so the Italian text is neither the local name nor English. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/03#F6 · Low · Transport user's contact is the sales order desk
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the plan as transport user and has to respond to it by `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-09`. That response, and the arrangements for collection, belong to Valdara's shipping or logistics function, not to the order desk that takes customer orders.
- Condition: the transport user's contact is a shipping, logistics or transport-buying function of Valdara.
- Options: (a) a shipping/logistics contact (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/03#F7 · Low · Consignee's contact is its sales customer service
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Section 5: a consignee's contact receives goods. The plan makes the consignee unload (`/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`) and counts free time at its siding; the carrier needs Lumeway's goods-in or siding contact, not the sales customer service.
- Condition: the consignee's contact is Lumeway's goods-receiving (warehouse, siding) function.
- Options: (a) a goods-in contact (preferred); (b) role-specific contacts in Lumeway's master data.
- Needs decision: no

### rail/03#F8 · Low · Origin location named after a company
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- Why: Section 5: the name of a location is the place, not the company. The waybill calls the same place `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`, so the place has two names in the flow, and no identifier links them.
- Condition: the origin location's name names the warehouse, the same way in every example of the flow.
- Options: (a) "Castrano Logistics warehouse, Ferrano" everywhere (preferred); (b) add a location identifier used wherever the warehouse occurs.
- Needs decision: no

### rail/03#F9 · Low · Legal-entity master data the plan does nothing with
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: a transport plan does nothing with the transport user's stock-exchange listing or with the share capital of the transport user or the consignee.
- Condition: every legal-entity element present has a purpose in the plan.
- Options: (a) drop SecurityListing and CorporateStockAmount here (preferred); (b) a reduced party description for transport documents.
- Needs decision: no

## Checked and consistent
- Roles agree with the request it answers (`02-TransportExecutionPlanRequest.xml`): Ferrano Rail Cargo sender, signatory and transport service provider; Valdara receiver, transport user and bill-to party; Lumeway consignee. Sender and receiver are swapped against the request, as a reply should be.
- Full descriptions of Ferrano Rail Cargo, Valdara and Lumeway are identical to the other examples of the flow (value by value).
- FromLocation and ToLocation addresses are identical to those in the request; the ToLocation address is the hub's postal address (`04-TransportProgressStatusRequest.xml`).
- The notified party, Ferrano Intermodal Hub, has the same register ID `XU-R-105096` as the hub in `04-TransportProgressStatusRequest.xml`, `05-TransportProgressStatus.xml` and `07-TransportationStatus.xml`.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotifyParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: the pre-arrival notice should go to the consignee who unloads at the destination — refuted because the plan's remark "Collection as requested; notice two hours before arrival." and the note on carrier haulage to the hub make the arrival of the tractor at the hub a legitimate subject of the notice, and the notification location is the hub; the reading is consistent.
- `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: master data copied — refuted because Castrano Logistics is the collection place of the plan (FromLocation).
- `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: implausible size for a rail freight operator — refuted because no value in the flow (staff, turnover, fleet) contradicts it.
- `/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Valdara Industries`: bill-to party under the delivery terms — refuted: the order is DAP (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`), so the seller pays the carriage, and `10-Invoice.xml` bills Valdara.
