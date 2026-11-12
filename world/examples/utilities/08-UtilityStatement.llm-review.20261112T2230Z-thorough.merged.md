# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/08-UtilityStatement.xml`, Git blob `2ad70d0c87bdcb2a69e49f63c3882af20185d03e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/08#F1 · High · Monthly payments on account that invoice 09 neither deducts nor collects that way
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- XPath: `/UtilityStatement/cac:MainOnAccountPayment/cbc:EstimatedConsumedQuantity` = `14`
- XPath: `/UtilityStatement/cac:MainOnAccountPayment/cbc:Note` = `The basis of the direct debit limit.`
- XPath: `09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- Why: OnAccountPayment is "The planned prepayments (on account) regarding this subscription". The statement says the household pays on account every month by direct debit on the first working day, and that the bill settles these payments against the reading. Its parent invoice `09-Invoice.xml` for the same month bills the full 38.78 XBL (water 14 × 2.35 = 32.90 + levy 14 × 0.42 = 5.88) with no PrepaidAmount, and collects it by one direct debit 21 days after the invoice date (2026-04-23), not on the first working day. `10-Reminder.xml` then treats the returned debit of 23 April for the full 38.78 as the only collection (`10-Reminder.xml:/Reminder/cac:ReminderLine[1]/cbc:DebitLineAmount` = `38.78`), and `11-CreditNote.xml` credits part of the full amount. Had about 14 m³ (≈ 38.78 with the levy) been collected on account on 2 March, the March bill would settle to about 0, not 38.78. Either the household pays twice (on account and in full), or there are no payments on account. Verified in the merge against 09, 10 and 11; no reading reconciles them (09 has no PrepaidAmount, no settlement note, and its only collection date is 2026-04-23).
- Condition: Statement 08, invoice 09 and reminder 10 describe the same payment arrangement: either payments on account that the invoice deducts (PrepaidAmount, with the balance collected), or monthly billing on the reading collected 21 days after the invoice, with no payments on account.
- Options: (a, preferred) remove OnAccountPayment and MainOnAccountPayment, because 09, 10 and 11 all follow monthly billing on the actual reading; the mandate's limit can be explained in the mandate or the terms; (b) keep the on-account scheme and give invoice 09 a PrepaidAmount and a settlement amount, reworking 10 and 11 to match.
- Needs decision: yes
- From: broad (F1), money (F1), context (F1); logistics (under "Outside this review")

### utilities/08#F2 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale (a locale is a language in a region, like the world's `en-XB` language tags). Recounted in the merge: 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'` over `world/examples`, and `grep -rl` for the files).
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a, preferred) drop `LocaleCode` (`Language/ID` already says English); (b) a locale value such as `en-XB` with a list that defines it.
- Needs decision: no
- From: broad (F6), parties (F1), context (F5)

### utilities/08#F3 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Both are Robin Ashdale, so the condition of the definition is not met. `03-UtilityStatement.xml` uses the element as defined (receiver Castrano Logistics, customer Valdara Industries).
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a, preferred) remove `CustomerParty` (its absence means that the receiver is the buyer); (b) keep it only if the story gives the statement a different receiver.
- Needs decision: no
- From: broad (F4), parties (F2), context (F3)

### utilities/08#F4 · Medium · Energy consumer level in a water report, and "Low consumer" against the figures
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevelCode` = `LOW`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevel` = `Low consumer`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidentOccupantsNumeric` = `2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `14`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidenceTypeCode` = `APT`
- Why: ConsumersEnergyLevel is "The level of energy consumed, compared to the average for this residence type and the number of people living in the residence"; the report is about 14 m³ of drinking water, not energy, so the element carries a meaning other than its definition. Read as a water level, the value does not fit either: 14,000 l / 31 days / 2 residents = 226 l per person per day (recalculated in the merge), against typical household use of about 120–150 l (own knowledge); that is a high, not a low consumer. The history in the same report calls the earlier months (15 and 13 m³) "Normal".
- Condition: No energy level in a water report, or (if a water-use level is wanted) the level stated agrees with the consumption per resident, with the lack of a water-level element in UBL recorded.
- Options: (a, preferred) remove ConsumersEnergyLevel and ConsumersEnergyLevelCode; (b) keep a level and make it agree with the figures (three or four occupants give 113–151 l per person and day; or a lower consumption with readings, history and invoice to match; or level normal/high), and record the missing water-level element as a UBL finding.
- Needs decision: no
- From: broad (F3, Medium), context (F7, Low), logistics (F5, Low)

### utilities/08#F5 · Medium · A district-heating cooling correction in the water company's water statement, priced per m³ with a rate defined per MWh
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionTypeCode` = `COOL`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:MeterNumber` = `CSW-H-71844`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `Poor cooling makes the network pump more water; the shortfall is charged on the annual account.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `0.80`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionWaterQuantity` = `6.2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `19.84`
- XPath: `/UtilityStatement/cbc:UtilityStatementTypeCode` = `WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ContractType` = `Water supply`
- XPath: `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3600`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:HeatingTypeCode` = `DH`
- Why: The statement is a drinking-water statement (type WATER, contract "Water supply", one water meter CSW-W-71844) of Coastal State Water Company (ISIC 3600 "Water collection, treatment and supply"). A cooling correction belongs to a district-heating supply: it penalises a too-small temperature drop of the heating water at a heat meter. The meter CSW-H-71844 appears nowhere else in the world (`grep -rl --include='*.xml' 'CSW-H-71844'`: only this file) and is not a meter of this consumption point; neither the statement nor invoice 09 has a heat supply, contract or line, no other example has district heating (`grep -rli --include='*.xml' 'district heating'`: only this file), and the amount is "charged on the annual account", so this document does nothing with it. The residence's heating type explains why the flat has a heat meter, not why the water company corrects its cooling. In addition, CorrectionUnitAmount is defined as "Correction per MWH per degree C", but the amount works out per cubic metre: 0.80 × 6.2 m³ × 4 °C = 19.84 (recalculated in the merge; the only product of the stated figures that gives 19.84). With a rate per MWh the heat quantity in MWh would be needed (ConsumptionEnergyQuantity), not the water volume. (Physics, own knowledge, logistics: 6.2 m³ cooled by 31 K carry 6.2 × 1.163 × 31 ≈ 224 kWh.)
- Condition: A cooling correction appears only in a statement of the party that supplies the district heat, for a supply that statement covers (heat meter at the consumption point, contract or supplier for heat), and its unit amount × the quantity in the unit the definition names × the temperature difference = the correction amount; otherwise the water statement carries no such correction.
- Options: (a, preferred) remove the correction from the water statement (and the HeatingType, unless it explains the water use); (b) if Coastal State Water Company also supplies district heat in the world, add that supply (heat meter, contract, a separate SupplierConsumption or statement) and express the correction per MWh per °C with the energy quantity.
- Needs decision: yes (whether the water company also supplies district heat changes the story)
- From: broad (F2), money (F3), context (F2), logistics (F1)

### utilities/08#F6 · Medium · The payable amount for the consumption leaves out the sewage levy invoice 09 charges on it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- XPath: `/UtilityStatement/cbc:Note` = `This statement explains the consumption behind your bill.`
- XPath: `09-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `5.88`
- Why: Invoice 09 bills the city's sewage levy per cubic metre of the same 14 m³ (14 × 0.42 = 5.88), so the bill comes to 38.78. The statement says it explains the consumption behind the bill, but shows 32.90 as the total payable on this consumption and never mentions the levy. The merge checked whether the statement may deliberately cover the supplier's own supply only: nothing says so, and the levy is charged on this consumption point's metered quantity.
- Condition: The statement accounts for everything invoice 09 charges for this consumption point, or says that the levy of 5.88 is added on the invoice.
- Options: (a, preferred) add a consumption line for the levy and set the payable totals to 38.78; (b) add a note naming the levy of 5.88.
- Needs decision: yes
- From: money (F2)

### utilities/08#F7 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- Why: Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "The consumption in case the consumption is from more than one supplier". The flat has one water supplier, and both alternatives are present with identical totals. ConsumptionLine is only reachable under SupplierConsumption, which is why the model pushes this use.
- Condition: Only the alternative matching the number of suppliers is used, or the model limitation is recorded as a finding for the TC.
- Options: (a) Consumption only (coverage of the consumption line is then lost here); (b) SupplierConsumption only, with a real second supplier; (c) record the UBL model limitation (consumption lines only under SupplierConsumption).
- Needs decision: yes
- From: broad (F5), context (F4)

### utilities/08#F8 · Low · Statement issued before the invoice it supplements
- XPath: `/UtilityStatement/cbc:IssueTime` = `15:10:00`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `CSWC-INV-26-0319`
- XPath: `09-Invoice.xml:/Invoice/cbc:IssueTime` = `15:44:00`
- Why: A Utility Statement is "A supplement to an Invoice or Credit Note", and ParentDocumentReference is "A reference to the parent Invoice or Credit Note". Both are dated 2026-04-02, but the statement is issued 34 minutes before its parent invoice. In the other four statement/invoice pairs of the flow the statement follows its invoice (01 and 03 after 02, 05 after 06, 12 after 13), and the numbering (statement 0320 after invoice 0319) also puts the invoice first.
- Condition: The statement's issue date and time are not earlier than those of its parent invoice.
- Options: (a, preferred) an issue time after 15:44 for the statement (matches the numbering); (b) an earlier invoice time.
- Needs decision: no
- From: broad (F7), context (F8), logistics (F2)

### utilities/08#F9 · Low · Signature without method or reason
- XPath: `/UtilityStatement/cac:Signature/cbc:ID` = `CSW-SIG-26-0401`
- Why: The signature has only an ID and the signatory; nothing says how or why the statement is signed (no fillers). This is a convention across the world: 137 of the 147 Signature aggregates in `world/examples/*/*.xml` hold only ID and SignatoryParty (counted with lxml in the merge), so changing it is a decision for all examples.
- Condition: A signature carries the data that make it one (method, reason, attachment), or is absent.
- Options: (a, preferred) remove it; (b) add the signature method and reason.
- Needs decision: yes
- From: broad (F9, part)

### utilities/08#F10 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport, with its own meter network); a water utility serving a state's capital is a large organisation, so `SMALL` ("Small enterprise") is implausible. 25 companies of the world are registered on 1 January 1996 (parties' count over the `PartyLegalEntity` elements); recounted in the merge: 271 occurrences of `<cbc:RegistrationDate>1996-01-01<` in 181 files over `world/examples/*/*.xml`. Both values look like a default description, not the company's story (no fillers).
- Condition: Size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a, preferred) a size that fits a state water utility (medium or large) and a registration date of its own; (b) drop the two elements where the documents do not need them.
- Needs decision: yes
- From: parties (F3)

### utilities/08#F11 · Low · The household's bank account in a statement that collects nothing
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerFinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: A utility statement explains consumption; it carries no payment means. The account is the payer account of the mandate in invoice 09, so here it reads as copied from the customer's master data. The parties part refuted this because the statement's on-account terms say "By direct debit", so the account shows the household which account is debited. That argument holds only as long as the on-account payments of F1 stay; with F1's preferred option the account has no use here, and even with on-account payments the statement does not say that this account is the one debited.
- Condition: The statement carries the account only if it uses it (and then says for what).
- Options: (a, preferred) leave the account out of this statement.
- Needs decision: no
- From: broad (F9, part), money (F4), context (F10); refuted by parties (argument above)

### utilities/08#F12 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-311790`
- Why: `SubscriberID` is "An identifier for the subscriber responsible for the consumption at this consumption point", but holds the supply contract's number (`09-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:ID` = `CSW-C-311790`, described as "Supply contract"). Whether the world treats the subscription number and the contract number as one cannot be settled from the examples: context rated it Medium (an identifier of another kind), parties and logistics Low. Same pattern in all five statements of the flow.
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number serves as the subscriber number.
- Options: (a, preferred) a customer number of Robin Ashdale at the water company; (b) record that the contract number serves as the subscriber number; (c) remove SubscriberID.
- Needs decision: yes
- From: parties (F4, Low/yes), context (F6, Medium/no), logistics (F3, Low/no)

### utilities/08#F13 · Low · Password of the reading website in clear text
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:WebSiteAccess/cbc:Password` = `RD-4K7-918`
- Why: WebSiteAccess has a business reason here (the household submits its own readings, method CUSTOMER). Sending the password itself in a business document is poor practice; a login and a link suffice, the password being given separately, and as an example it teaches the wrong practice. The context part refuted it: UBL provides the element for exactly this access, and the household needs it to submit readings. Both arguments hold; the merge cannot settle whether the world wants the password in the statement.
- Condition: The statement carries no password, or the story explains why it must (e.g. a one-time activation code).
- Options: (a, preferred) keep URI and Login, drop the password; (b) describe it as a one-time activation code.
- Needs decision: yes
- From: broad (F8); refuted by context (argument above)

### utilities/08#F14 · Low · "Maximum flow" of 2.5 m³/h is the meter's permanent flow rate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:Name` = `Maximum flow`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `2.5`
- Why: (own knowledge) 2.5 m³/h is the permanent flow rate Q3 of a standard domestic water meter (ISO 4064 / OIML R49); its maximum (overload) flow is Q4 = 1.25 × Q3 = 3.125 m³/h. The same property is in 05.
- Condition: Property name and value agree (permanent flow rate 2.5 m³/h, or maximum flow 3.125 m³/h).
- Options: (a, preferred) rename to permanent flow rate (Q3); (b) give 3.125 m³/h.
- Needs decision: no
- From: logistics (F4)

### utilities/08#F15 · Low · Document references with only an ID, one of them in an element whose definition does not fit
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:GuidanceDocumentReference/cbc:ID` = `CSW-SAVE-WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:DocumentReference/cbc:ID` = `CSW-QUALITY-2026-Q1`
- Why: GuidanceDocumentReference is "A reference to a document providing an explanation of this kind of report"; the ID suggests a water-saving leaflet, which explains how to save water, not how to read the report. ConsumptionReport/DocumentReference is "A reference to some other document (for example, this report in another format)"; a quarterly water-quality report is neither this report nor about the consumption. Neither reference has a type, description or URI saying what it is.
- Condition: Each reference is in an element whose definition fits, and says what it refers to; the guidance reference refers to a document that explains the report.
- Options: (a, preferred) give each a DocumentTypeCode/DocumentDescription, point the guidance reference to an explanation of the statement, and move the water-saving guide and the quality report to the statement's AdditionalDocumentReference; (b) remove the references the report does nothing with.
- Needs decision: no
- From: broad (F9, part), context (F9), logistics (F6)

### utilities/08#F16 · Low · Filler descriptions and a delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: The history descriptions say nothing the periods next to them do not; the delivery location has no identifier or address, only a pointer to consumption point CSW-CP-38516-57 already identified in the statement (no fillers, IND5).
- Condition: Each description carries information of its own, and Delivery is absent or identifies the location.
- Options: (a, preferred) remove them; (b) give the delivery location the consumption point's ID.
- Needs decision: no
- From: broad (F11), context (F11, part), logistics (F7)

### utilities/08#F17 · Low · Subscriber type of the utility item is "Water", the consumption point's is "Household"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `HH`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text", while SubscriberTypeCode is "The code identifying for the service type". The code's definition supports a utility code (parties refuted the code on that ground), but the text gives the utility where its definition asks for the subscriber type, and the consumption point says Household. UBL's two definitions disagree; the same occurs in 01, 03, 05 and 12.
- Condition: The text and the code each match their definitions (text consistent with the consumption point's subscriber type), or the service-type reading is recorded as deliberate together with the UBL definition inconsistency.
- Options: (a) record the UBL definition inconsistency for the TC and keep the code; (b) drop the text SubscriberType (context's preference); (c) leave both out.
- Needs decision: yes
- From: broad (F10, Low/yes), context (F11, part, Low/no)

## Checked and consistent
- Meter: 1844 − 1830 = 14 m³ × MeterConstant 1 = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity; customer readings on 2026-02-28 and 2026-03-31, consistent with the WebSiteAccess for readings; the Login equals the consumption point ID.
- Amounts (redone in the merge): 14 × 2.35 = 32.90 = `09-Invoice.xml` line 1 (meter CSW-W-71844, contract CSW-C-311790, exempt E/WATER, tax 0.00); history 15 × 2.35 = 35.25 and 13 × 2.35 = 30.55.
- AverageAmount: (35.25 + 30.55 + 32.90) / 3 = 98.70 / 3 = 32.90 and (15 + 13 + 14) / 3 = 14 m³, as the description says. Unlike 01, 03 and 05 the average here is a true three-month average; it equals March's amount only because March is the average month.
- ConsumptionReportReference CSW-CP-38516-57-2602 (13 m³, February) agrees with ConsumptionHistory[2].
- Correction temperatures: 31 − 35 = −4 °C (DifferenceTemperatureReductionQuantity); arithmetic 0.80 × 6.2 × 4 = 19.84 (unit problem in F5).
- Mandate: the MainOnAccountPayment note on the debit limit agrees with 09's MaximumPaidAmount 150.00, well above 14 m³ ≈ 38.78 with the levy.
- Robin Ashdale (receiver, customer, subscriber, utility customer) is described identically in 08–11 (residential address Gull Lane 57, Old town, 38516 Lumeport, `LUM-ADR-934215`); a private person without legal entity, tax scheme or register identifier, with Person first and family name. The consumption point address equals the postal address, typed RESIDENTIAL, subscriber type Household.
- Sender, signatory and UtilitySupplierParty are Coastal State Water Company (`20412192`), the supplier of `09-Invoice.xml`.
- check_ids.py: account XB64BLUM38010007251840 correct.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount`: the correction of 19.84 is not in the payable amount — refuted because the description says it is charged on the annual account (from broad). (Whether it belongs in this statement at all is F5.)
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:DifferenceTemperatureReductionQuantity`: the sign of −4 °C — refuted, actual 31 °C − normal 35 °C = −4 °C, a shortfall that makes a charge (from broad and money).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ActualTemperatureReductionQuantity`: a temperature difference in CEL rather than kelvin — refuted because a difference of 1 °C equals 1 K and CEL is commonly used for cooling values in district-heating billing (from logistics).
- `/UtilityStatement/cac:Signature/cbc:ID`: CSW-SIG-26-0401 looks dated 1 April while the statement is of 2 April — refuted because the number need not be a date (from logistics).
- `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Robin Ashdale`: a party without identifier — refuted, a household subscriber has no register number; name, subscriber ID and address identify it (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `WATER`: refuted as in 05, because UBL defines the code in UtilityItem as "The code identifying for the service type" (from parties; the text SubscriberType stays a finding, F17).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidentOccupantsNumeric`: the number of occupants — refuted because it is the basis of the consumption comparison the report gives (from context).
- `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID`: refuted by parties as copied master data — the merge disagrees and keeps it as F11 (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:WebSiteAccess/cbc:Password`: refuted by context — the merge cannot settle it and keeps it as F13 (from context).

## Changed in the merge
- broad/F9 split into F9 (signature), F11 (bank account) and F15 (references): different elements, fixes and decision status.
- broad/F9 (signature part): Needs decision no → yes, aligned with the air, rail and utilities 01–07 merges (a convention across 137 of 147 Signature aggregates).
- broad/F3, context/F7, logistics/F5 → F4: one finding at Medium (broad's): the element carries the meaning of an energy level for water (definition), and the "low" against 226 l per person and day is part of the same problem; context and logistics had Low.
- broad/F11, context/F11 (description part), logistics/F7 → F16: grouped as one filler finding; the SubscriberType part of context/F11 went to F17.
- parties/F4, context/F6, logistics/F3 → F12: Low with Needs decision yes (parties), aligned with merger A (01–07); context had Medium/no.
- broad/F8 → F13: Needs decision no → yes, because context refuted the same value with a valid argument and the merge cannot settle it.
- broad/F10, context/F11 (SubscriberType part) → F17: Low/yes, aligned with merger A; context's "drop the text" kept as option (b).
- parties/F3 → F10: count recalculated and added (271 in 181 files).
- broad/F6, parties/F1, context/F5 → F2: count re-made (362 in 213 files).

## Outside this review
- `09-Invoice.xml`: PayerParty of the mandate is the debtor Robin Ashdale (that example's review, 09#F3).
