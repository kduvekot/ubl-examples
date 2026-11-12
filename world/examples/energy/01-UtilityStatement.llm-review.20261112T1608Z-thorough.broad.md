# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/01-UtilityStatement.xml`, Git blob `ddb038e38819569df4aa78c5bfc77925766f9bb9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/01#F1 · High · Amount payable on the consumption is zero, but the parent invoice bills this consumption
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`
- Why: `Consumption/LegalMonetaryTotal` is "The total amount payable on this consumption, including any allowances, charges, or taxes." The statement's parent invoice (02-Invoice.xml, the Utility Statement is "a supplement to an Invoice") bills exactly this consumption point's 61 200 kWh as gas network use, 61 200 × 1.9 = 116 280 XUF net, 139 536 XUF with 20 % VAT. The statement says nothing is payable on the same consumption. Tried to refute: the statement could be meant as pure metering data; but then the definition of the mandatory total still asks for the amount payable on this consumption, which the parent invoice fixes.
- Condition: the amount payable on this consumption in the statement agrees with what the parent invoice charges for it (net or gross, stated consistently).
- Options: (a, preferred) state the network charge for the consumption (116 280 net / 139 536 gross, with LineExtensionAmount/TaxInclusiveAmount as needed), because the parent invoice is the grid operator's bill for it; (b) if the statement is meant to cover only the retailer's own billing, change the parent reference and the story so that the zero has a reason.
- Needs decision: no

### energy/01#F2 · Medium · CustomerParty is the same party as the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- Why: `UtilityStatement/CustomerParty` is "The buyer, if different from the receiver of the document." Here it is Ferrano Energy, the receiver itself, so the condition of the definition is not met.
- Condition: CustomerParty is absent, or names a party different from ReceiverParty.
- Options: (a, preferred) omit CustomerParty, since the receiver is the buyer of the network service; (b) if another buyer is meant (e.g. Valdara as buyer of the gas), name it, but Valdara is already SubscriberParty.
- Needs decision: no

### energy/01#F3 · Medium · Province given in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "the political or administrative division of a country", which is `CountrySubentity`. The Urvanian address format code (AddressFormatCode `XU`, world list) puts `Region` on the last line, so the use is a world convention; the value still names an administrative division. The same value occurs 219 times in 104 of the 250 XML examples (`grep -rh --include='*.xml' -o '<cbc:Region>[^<]*'`).
- Condition: the province of an Urvanian address is in `CountrySubentity` (or the world states that Urvanian provinces are economic regions, not administrative divisions).
- Options: (a, preferred) move it to `CountrySubentity` (with a code, like Bayvarra's states) and update the XU address format; (b) keep `Region` and document why a province is not an administrative division in Urvania.
- Needs decision: yes

### energy/01#F4 · Medium · ConsumptionEnergyQuantity is defined for district heating, used for gas
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `61200`
- Why: the UBL 2.5 definition of `ConsumptionEnergyQuantity` in Consumption Correction is "Your consumpt for district heating energy." The statement is for gas (`UtilityStatementTypeCode` `GAS`). Under the semantic-conformance rule the element is used outside its definition, even though the definition looks like a drafting defect (it may be a finding for the UBL TC). The element also occurs in utilities/03-UtilityStatement.xml (count over `*.xml`: 2 files).
- Condition: either the element is not used for gas, or the deviation is recorded as a finding on the UBL definition in `analysis/codelist-decisions.md`.
- Options: (a) drop the element; the energy is already in `ConsumptionReport/TotalConsumedQuantity` and the correction's `Description`; (b, preferred if the owner agrees the definition is a defect) keep it and record the definition problem as a finding for the TC.
- Needs decision: yes

### energy/01#F5 · Low · Statement issued before the invoice it supplements
- XPath: `/UtilityStatement/cbc:IssueDate` = `2026-04-02`
- XPath: `02-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-03`
- Why: the statement is "A supplement to an Invoice" and references FG-INV-26-0150, which is issued the next morning (08:20). An invoice number can be reserved in advance, so this is not a contradiction, but the order is unusual for a supplement.
- Condition: the statement is issued with or after its parent invoice, or the order has a stated reason.
- Options: (a, preferred) issue the statement on the invoice's date/time or later; (b) leave as is.
- Needs decision: no

### energy/01#F6 · Low · Subscriber master data the statement does nothing with
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why: the subscriber's stock-exchange listing, its logistics service provider (warehousing and despatch) and its customs-trader number have no role in a meter-reading statement from the grid operator to the retailer. They look copied from the party's master data (section 4.8).
- Condition: every aggregate of SubscriberParty has a use in this statement.
- Options: (a, preferred) leave them out of this document; (b) give a reason in the story.
- Needs decision: no

### energy/01#F7 · Low · Contacts do not fit the roles in a metering statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cbc:Name` = `Order desk`
- Why: the receiver (the retailer) uses the statement for billing; its contact would be billing/metering data, not customer service in Sales. The subscriber's contact for its gas connection is its order desk in Sales, which takes orders from Valdara's customers. The sender's metering office fits.
- Condition: the receiver's and subscriber's contacts are ones that deal with metering or billing of the connection.
- Options: (a, preferred) role-specific contacts (retailer's billing, subscriber's facility/energy management); (b) omit the subscriber contact.
- Needs decision: no

### energy/01#F8 · Low · Grid operator's industry code covers electricity only, but it reads a gas meter
- XPath: `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is "Electric power generation, transmission and distribution"; gas distribution through mains is 3520 (own knowledge of ISIC). Ferrano Grid owns and reads the gas meter here and bills gas network use (02-Invoice.xml line 3).
- Condition: the party's industry classification covers its gas network activity.
- Options: (a, preferred) add 3520 (the element repeats); (b) leave as is if gas is a minor activity.
- Needs decision: no

## Checked and consistent
- Meter arithmetic: 29 760 − 28 410 = 1 350 m³ (`DeliveredQuantity`, meter `TotalDeliveredQuantity`, `TotalMeteredQuantity`).
- Volume correction: (4 + 1.01325) / 1.01325 = 4.9477 for 4 bar gauge; 1 350 × 4.9477 = 6 679 m³; × 9.163 kWh/m³ = 61 200 kWh, equal to `TotalDeliveredQuantity`, `TotalConsumedQuantity` and 02-Invoice.xml line 3 `InvoicedQuantity`.
- Periods: reading dates 2026-02-28 → 2026-03-31, MainPeriod and ConsumptionReport period March 2026, same as the parent invoice's InvoicePeriod.
- Parent reference FG-INV-26-0150 resolves to 02-Invoice.xml, issued by the same sender to the same receiver.
- Party identifiers, addresses and legal data of Ferrano Grid and Ferrano Energy agree with 02-Invoice.xml; ISIN XU0001042501 check digit OK (`check_ids.py`).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description`: suspected the calorific value 9.163 kWh/m³ is implausibly low — refuted: it is within the range of low-calorific natural gas (about 9–10 kWh/m³, own knowledge), and the Kelpstone gas of 04/06 (75 kg/MWh, i.e. 13.3 kWh/kg) gives a density of about 0.69 kg/m³ at that calorific value, lean but possible.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID`: suspected an ID of the retailer (FE-C-…) in a grid operator's statement — refuted: the definition asks for "the subscriber responsible for the consumption", and the retailer's customer number is a legitimate identifier of it known to both parties.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:TotalDeliveredQuantity`: suspected unit mismatch with the meter (KWH vs MTQ) — refuted: the point's total is the energy after conversion, the meter's is volume; both agree via the volume conversion above.
