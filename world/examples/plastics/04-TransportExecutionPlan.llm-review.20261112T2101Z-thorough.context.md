# LLM review: 04-TransportExecutionPlan.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/04-TransportExecutionPlan.xml`, Git blob `dc8723ba3179d86f1689569b00ab4ceab21fea05` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/04#F1 · High · FromLocation contradicts the loading place of the same plan
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`
- Why: FromLocation is "The location of origin of the transport service". The plan gives the carrier's business address under the carrier's name, while its only shipment stage loads at Rinova's quay (and the note says "from the quay next to the recovery plant"). The service therefore begins at a place other than the one FromLocation names. ToLocation in the same way names the consignee and its business address, while the stage unloads at the river quay of Lumeport.
- Condition: FromLocation and ToLocation name the places where the service begins and ends, in agreement with LoadingPortLocation and UnloadingPortLocation.
- Options: Make From and To the loading and unloading quays (preferred); or drop them and let the stage carry the places.
- Needs decision: no

### plastics/04#F2 · Medium · AtLocation without a stationary service
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Fiumella Barges`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does not require transport movement." The plan contains no such service: the main service is the barge (`/TransportExecutionPlan/cac:MainTransportationService/cbc:TransportServiceCode` = `RIVERBARGE`) and the only additional one is the pre-arrival notice. The value is the carrier's name, not a place.
- Condition: AtLocation is absent, or names the place of a service without movement that the plan contains.
- Options: Remove it (preferred); or add the stationary service (e.g. storage at the quay) it belongs to.
- Needs decision: no

### plastics/04#F3 · Medium · Late-payment percentage used for a late-delivery penalty
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:Note` = `5 % of the freight per day late, at most 25 %.`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PenaltyPaymentTerms/cbc:PenaltySurchargePercent` = `5`
- Why: PenaltySurchargePercent is "The penalty for payment after the settlement period, expressed as a percentage of the payment." The penalty of this plan is for late delivery by the carrier (5 % of the freight per day late), not for late payment. The same note and percentage occur 3 times in the examples (`grep -rh --include='*.xml' -B3 'PenaltySurchargePercent' world/examples`).
- Condition: PenaltySurchargePercent, if present, is a surcharge for paying after the settlement period; the late-delivery penalty is stated where its meaning fits (the note of the penalty terms).
- Options: Keep the late-delivery penalty in the note and remove the percentage (preferred); or, if a late-payment surcharge is meant as well, state that one.
- Needs decision: no

### plastics/04#F4 · Medium · The plan does not say what is carried
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- XPath: `/TransportExecutionPlan/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: The Transport Execution Plan is "used in the negotiation of a transport service between a transport user and a transport service provider"; this one confirms the barge, but its consignment has only an ID and a gross weight: no description of the goods and no packages (120 jumbo bags of granulate in 06-Waybill.xml). The plan the carrier commits to does not say what it commits to carry.
- Condition: The plan states what is carried: at least a description of the goods and the number and kind of packages.
- Options: Add a goods item or handling-unit description to the consignment (preferred, mirrors the waybill).
- Needs decision: no

### plastics/04#F5 · Medium · A province is held in Region
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/04#F6 · Medium · A language code is held in LocaleCode
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/04#F7 · Low · Brokerage commission without a broker
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:CommissionPaymentTerms/cbc:Note` = `Brokerage of 1.25 % of the freight, paid by the barge operat…`
- Why: CommissionPaymentTerms are "Terms of payment applying to a commission specified in the transport execution plan." The note describes a brokerage paid by the barge operator to "the barge broker that found the barge for this voyage", but Rinova asked Fiumella's chartering desk directly (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Chartering desk`) and no broker appears in any document of the flow. A commission between the carrier and a third party is also no term between the transport user and the carrier.
- Condition: Either the flow contains the broker that found the barge (and the commission is a term between the parties of the plan), or the plan carries no commission terms.
- Options: Remove the commission terms (preferred: nothing in the story needs a broker); or add the broker to the story and the plan.
- Needs decision: yes

### plastics/04#F8 · Low · Post-event delay and notification place do not fit a pre-arrival notice
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:NotificationTypeCode` = `PREARRIVAL`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cbc:PostEventNotificationDurationMeasure` = `1`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Rivermouth Packaging`
- Why: PostEventNotificationDurationMeasure is "The length of time between the occurrence of a given event and the issuance of a notification"; a pre-arrival notice is issued before the event, which the plan states with the pre-event duration of two hours. Nothing in the plan (remarks, additional service) speaks of a second notice after arrival. NotificationLocation is "A location at which a notification will be issued"; the notice is issued from the barge, while the value names the company that is notified.
- Condition: The notification requirement carries only the delays and locations that a pre-arrival notice has: the pre-event delay, and as location the place the notice is issued from (or none).
- Options: Remove the post-event duration and the notification location (preferred); or add the after-arrival notice the post-event duration would belong to.
- Needs decision: no

### plastics/04#F9 · Low · The request's "Please confirm by return." is repeated in the confirmation
- XPath: `/TransportExecutionPlan/cbc:TransportUserRemarks` = `Please confirm by return.`
- Why: TransportUserRemarks are "Remarks from the transport user regarding the transport operations referred to in the Transport Execution Plan." The remark is a request to answer the request (03), not a remark on the transport operations, and this plan is the answer to it (status Confirmed).
- Condition: The plan carries only remarks of the transport user that concern the transport operations.
- Options: Leave the remark out of the plan (preferred).
- Needs decision: no

### plastics/04#F10 · Low · Rivermouth Packaging's bank account in a document that does not use it
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". The plan settles the barge between Rinova and Fiumella, and the freight is invoiced to Rinova (07); the consignee's bank account plays no part in it. The account (with its branch and bank address) reads as copied from the party's master data into a document that does nothing with it (section 4.8 of the review rules; IND5, no fillers).
- Condition: Rivermouth Packaging's FinancialAccount appears only in documents of the flow that pay or are paid through it (as `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` does).
- Options: Remove it here (preferred); or, if the document has a use for it, make that use visible.
- Needs decision: no

### plastics/04#F11 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in a transport plan for granulate depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/04#F12 · Low · Contacts do not fit the role the party has in this document
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Rinova receives the plan as transport user, so its contact arranges transport; "Customer service" in Sales is the contact for buyers. The consignee unloads and receives the pre-arrival notice, so its contact is goods receipt, not an "Order desk" in Sales.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/04#F13 · Low · Every party registered on 1 January 1996
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

## Checked and consistent
- `/TransportExecutionPlan/cac:TransportExecutionPlanRequestDocumentReference/cbc:ID` = `RR-TR-26-0884` resolves to 03; contract, parties, service period and consignment agree.
- Events in time order and within the validity and service period: takeover 2026-04-19 09:00, loading 13:30, exportation 2026-04-20 16:00, discharge 2026-04-22 08:00; an estimated transit of 3 days fits.
- DocumentStatusCode Confirmed with reason "As requested" agrees with the provider's remark "Collection as requested".
- Waiting-time terms in the provider's special terms and in the service-charge terms agree (beyond two hours).
- Vessel, journey and master are the same as in 06-Waybill.xml.

## Considered and refuted
- `/TransportExecutionPlan/cac:TransportUserResponseRequiredPeriod/cbc:EndDate` = `2026-04-16` in a confirmed plan — refuted because in the UBL transport execution plan process the transport user still accepts or rejects the plan the provider returns.
- `//cac:MainCarriageShipmentStage/cac:ExportationTransportEvent` in main carriage — refuted because the barge leaves Urvania during main carriage.
- `//cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:CompletionIndicator` = `false` — refuted because the discharge lies in the future of the plan (issued 2026-04-15).
- `//cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport` for a river barge — refuted because the aggregate is defined as "A vessel used for transport by water (not only by sea)".
