# LLM review: 06-Waybill.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/06-Waybill.xml`, Git blob `98b3edab06331ce10e3457361c14ccae3bf60af1` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/06#F1 · High · Actual despatch after the waybill was issued
- XPath: `/Waybill/cbc:IssueDate` = `2026-04-19`
- XPath: `/Waybill/cbc:IssueTime` = `09:38:00`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchDate` = `2026-04-19`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`
- Why: ActualDespatchDate and ActualDespatchTime are "The actual despatch (pickup)" date and time. The waybill is issued at 09:38 and reports as actual a despatch at 15:10 the same day, five and a half hours later, and after the loading at 13:30 which it gives without saying planned or actual. A document cannot report as done what happens after it is issued.
- Condition: Every actual time in the waybill is at or before its issue time.
- Options: Issue the waybill after loading and despatch (preferred: under the CMNI the consignment note follows taking over and loading); or report the despatch as planned (earliest/latest pickup) instead of actual.
- Needs decision: no

### plastics/06#F2 · Medium · ReturnableQuantity counts the bags, not returnable goods
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ReturnableQuantity` = `120`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:ReturnableMaterialIndicator` = `true`
- Why: GoodsItem/ReturnableQuantity is "The number of units in the goods item that may be returned." The granulate is sold, not returnable; what is returnable is the packaging, which the package already states. The value 120 EA counts the jumbo bags, a unit of the package, in an element about the goods.
- Condition: ReturnableQuantity is absent, or counts units of the goods that may be returned.
- Options: Remove it and keep the returnable packaging on the package (preferred); or, if the bags are to be counted for return, state it on the package.
- Needs decision: no

### plastics/06#F3 · Medium · The consignment ID is given as shipping order ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `RR-CS-26-0885`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment." The value is the consignment's identifier, not that of an instruction; the instruction behind this carriage is the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `RR-TR-26-0884`).
- Condition: ShippingOrderID holds the identifier of a shipping order or forwarding instruction of the flow, or is absent.
- Options: Use the number of the transport request if the world treats it as the forwarding instruction (preferred); or remove the element.
- Needs decision: no

### plastics/06#F4 · Medium · BaseAmount holds the rate per tonne
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:BaseAmount` = `1495`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`
- Why: BaseAmount is "The monetary amount to which the multiplier factor is applied in calculating the amount of this allowance or charge." 1495 XUF is the freight rate per tonne (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `1495`); the charge is 1495 × 120 t = 179400, so the "factor" would be the quantity, and no MultiplierFactorNumeric is given.
- Condition: BaseAmount, if present, is an amount to which a stated multiplier factor applies to give Amount.
- Options: Remove BaseAmount and leave the rate to the freight invoice (preferred); or state the charge as a real base and factor.
- Needs decision: no

### plastics/06#F5 · Medium · A province is held in Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/06#F6 · Medium · A language code is held in LocaleCode
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/06#F7 · Low · Value for duties in a transport document
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ValueAmount` = `9984000`
- Why: GoodsItem/ValueAmount is "The amount on which a duty, tax, or fee will be assessed." The waybill assesses nothing; the customs values are declared in 05 and 09, and the carrier's liability is covered by DeclaredForCarriageValueAmount.
- Condition: The waybill carries no value for duties, unless a duty or fee is assessed on it in this document.
- Options: Remove it (preferred).
- Needs decision: no

### plastics/06#F8 · Low · OriginAddress is the plant's street address
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cac:OriginAddress/cbc:BuildingNumber` = `31`
- Why: GoodsItem/OriginAddress is "The region in which the goods have been produced or manufactured, according to criteria laid down for the purposes of application of the customs tariff ...". It is a region of origin, not the street and building of the recycling plant.
- Condition: OriginAddress names the region of origin (country, and subdivision where the tariff needs it), or is absent.
- Options: Reduce it to the region (preferred); or leave it out, as the items of 05 and 09 already give the country of origin.
- Needs decision: no

### plastics/06#F9 · Low · IssueLocation names a company, not a place
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Fiumella Barges`
- Why: IssueLocation is "The location where this waybill was issued." The value is the carrier's name with no address, so it does not say where (office, or Rinova's quay at loading).
- Condition: IssueLocation names a place.
- Options: Name the place of issue (preferred); or remove it.
- Needs decision: no

### plastics/06#F10 · Low · The consignor's original is not in the distribution
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`
- Why: The note gives three originals (consignor, consignee, carrier), but the distribution sends the consignee its original with the goods and the consignor only an electronic copy ("the original is held or sent elsewhere", in the world's list); the consignor's original does not appear.
- Condition: The distribution and the note agree on what the consignor receives.
- Options: Give the consignor an original in the distribution (preferred, as the note says); or change the note.
- Needs decision: no

### plastics/06#F11 · Low · Rivermouth Packaging's bank account in a document that does not use it
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". A waybill is the carrier's contract document; the freight is invoiced to Rinova (07), and the consignee's bank account plays no part in it. The account (with its branch and bank address) reads as copied from the party's master data into a document that does nothing with it (section 4.8 of the review rules; IND5, no fillers).
- Condition: Rivermouth Packaging's FinancialAccount appears only in documents of the flow that pay or are paid through it (as `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` does).
- Options: Remove it here (preferred); or, if the document has a use for it, make that use visible.
- Needs decision: no

### plastics/06#F12 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in a waybill for granulate depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/06#F13 · Low · Contacts do not fit the role the party has in this document
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Rinova receives the waybill as consignor, so its contact is shipping, not "Customer service" in Sales; the consignee's contact signs for the goods (the instruction is "Deliver against signature of the consignee"), not an "Order desk" in Sales.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/06#F14 · Low · Every party registered on 1 January 1996
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

## Checked and consistent
- References resolve: order line 1 of 01-Order.xml; ShipmentDocumentReference and DocumentReference to 04-TransportExecutionPlan.xml.
- Freight: 1495 XUF × 120 t = 179400 XUF, the line of 07-Invoice.xml.
- Pickup window 2026-04-19 08:00–16:00 contains takeover 09:00 and despatch 15:10; events agree with 04.
- Packaging: JB jumbo bags of woven polypropylene with lifting loops, returnable, fit the item description.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:DeclaredForCarriageValueAmount` with `/Waybill/cbc:AdValoremIndicator` = `false` — refuted because the indicator, as UBL defines it, concerns ad valorem duties, and a declared value raises the carrier's liability under the CMNI (own knowledge, art. 20); the goods are uninsured (`09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:InsuranceValueAmount` = `0.00`), which gives the consignor a reason.
- `/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23` against the plan's service end 2026-04-22 — refuted because one is the latest date the buyer allows, the other the carrier's commitment; they do not contradict.
- `/Waybill/cbc:CarrierAssignedID` and `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` — refuted as duplicates: one identifies the shipment, the other the consignment on the voyage.
