# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/05-UtilityStatement.xml`, Git blob `f5bb8506980bfe0a7e311a1ed3ba8b85f0c771d7` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
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


### utilities/05#F1 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 82 m³.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Amount` = `190.35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Amount` = `185.65`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `202.10`
- Why: AverageAmount is "The average monetary amount of the consumption". Redone by the merge: (81 + 79 + 86) / 3 = 82 m³, right; (190.35 + 185.65 + 202.10) / 3 = 578.10 / 3 = 192.70 XBL (= 82 × 2.35). The value 202.10 is March's amount (86 × 2.35). Same pattern as 01 and 03 (in 08 the two coincide; money part).
- Condition: AverageAmount is the average of the amounts of the months the description averages (192.70), or the description states another basis.
- Options: (a, preferred) 192.70; (b) drop AverageAmount.
- Needs decision: no
- From: broad (F1), money (F1), context (F1); logistics (outside its lens)

### utilities/05#F2 · Medium · CustomerParty repeats the receiver, though its definition is "the buyer, if different from the receiver"
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `20410411`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `20410411`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: UtilityStatement/CustomerParty is "The buyer, if different from the receiver of the document." Both are Brightmarket Stores, so the condition is not met; `03-UtilityStatement.xml` uses the element as defined. Same as utilities/01#F4.
- Condition: CustomerParty is present only when the buyer differs from the receiver.
- Options: (a, preferred) leave CustomerParty out; (b) keep it only if the story gives the statement another receiver.
- Needs decision: no
- From: broad (F2), parties (F2), context (F3)

### utilities/05#F3 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- Why: SubscriberConsumption/Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "The consumption in case the consumption is from more than one supplier". The only supplier is Coastal State Water Company (the city's sewage levy in invoice 06 is collected for a third party, not supplied by a second utility supplier; broad). Both alternatives are present with identical totals. Same as utilities/01#F5.
- Condition: Only the alternative that matches the number of suppliers is used.
- Options: (a) Consumption only; (b) SupplierConsumption only with a real second supplier; (c) record for the TC that consumption lines are only reachable under SupplierConsumption. Preference: (c) with (a) or (b).
- Needs decision: yes
- From: broad (F3), context (F2)

### utilities/05#F4 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID ISO 639 is a language code, the same as Language/ID, and names no locale (language in a region, e.g. en-XB as in the world's languageID attributes). Recounted by the merge: 364 occurrences of `LocaleCode listID="ISO 639">en<` in 213 files (`grep -rh`/`grep -rl --include='*.xml'`; the parts counted 362, the rail merges 364).
- Condition: LocaleCode holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop LocaleCode (Language/ID says English); (b) a locale such as en-XB with a fitting list.
- Needs decision: no
- From: broad (F4), parties (F1), context (F4)

### utilities/05#F5 · Low · Payable amount of the consumption leaves out the sewage levy billed per cubic metre of it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cbc:Note` = `This statement explains the consumption behind your bill.`
- XPath: `06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `36.12`
- XPath: `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `238.22`
- Why: The Consumption's LegalMonetaryTotal is "the total amount payable on this consumption, including any allowances, charges, or taxes". Invoice 06 bills for the same 86 m³ the city's sewage levy, 86 × 0.42 = 36.12 (redone), and totals 238.22 = 202.10 + 36.12; the statement, which says it explains the bill, shows 202.10 and does not mention the levy (money). Against it (broad, logistics, context, which refuted it): the levy is collected for the city (CollectionInvoiceLine), not a consumption supplied by the sender, and a statement may explain only the supplier's own supply. Whether a third-party levy is "payable on this consumption" cannot be settled from the definition; the merge lowers it to Low with Needs decision: yes. The same occurs in 08 (levy of invoice 09).
- Condition: The statement accounts for the whole amount the invoice charges for this consumption point, or states that the levy is added on the invoice.
- Options: (a) a second ConsumptionLine for the levy (ParentDocumentLineReferenceID of the collection line) with the totals at 238.22; (b, preferred) keep the totals at the water company's own supply and say in a note that the city's levy of 36.12 is added on the invoice, which needs no new modelling.
- Needs decision: yes
- From: money (F2, Medium); broad, logistics and context refuted it

### utilities/05#F6 · Low · Receiver's marketing data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The receiver's logo, online shop and photo-sharing profile matter where Brightmarket presents itself to its customers, not in a water statement it receives; they are part of the block repeated in all 41 examples with Brightmarket's full data (parties). Copied master data (section 4.8).
- Condition: Logo, additional web site and social media profile appear only with a use in this statement.
- Options: (a, preferred) drop them; (b) keep them only with a stated reason.
- Needs decision: no
- From: broad (F6, part), parties (F4), context (F8, part)

### utilities/05#F7 · Low · Receiver's contact: buying office with a sales job title and department
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Name says buying office, job title and department say customer service in Sales; they contradict each other. For a statement on the shop's water, facilities or accounts payable is the fitting addressee (broad, context); the buying office buys goods for resale (context), though parties thought it acceptable if its title and department agreed. The contact is the same in all 41 examples with Brightmarket's full data.
- Condition: Name, job title and department agree, and the function fits the receiver of a utility statement.
- Options: (a, preferred) a facilities or accounts payable contact; (b) a purchasing title and department for the buying office; (c) drop title and department.
- Needs decision: no
- From: broad (F6, part), parties (F5), context (F8, part)

### utilities/05#F8 · Low · The water company described as a small enterprise registered on the world's default date
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with a meter network); a utility serving a state's capital is not plausibly a small enterprise (parties). The broad part refuted the size (a small private company serving one city is plausible). The registration date is shared by 25 companies of the world, every other date by one (parties); recount: 271 occurrences in 181 files. Both look like default values. Aligned with the earlier flows' merges (registration date Low, yes).
- Condition: Size and registration date of the water company are values of its own story, the same in every example, or absent.
- Options: (a, preferred) a size that fits a state water utility and a registration date of its own; (b) drop the two elements where the documents do not need them; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F3); broad refuted the size

### utilities/05#F9 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-260118`
- Why: SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point"; the value is the water supply contract's ID. An identifier of one kind is used as another (logistics, context); whether the world's subscription number is the contract number cannot be settled (broad's refutation in 01). Same as utilities/01#F12.
- Condition: SubscriberID holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a, preferred) a customer number of Brightmarket at the water company; (b) drop SubscriberID; (c) record the convention.
- Needs decision: yes
- From: parties (F6), logistics (F1, no), context (F5, Medium, no)

### utilities/05#F10 · Low · Subscriber type of the utility item is "Water", the consumption point's is "Commercial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Commercial`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `COM`
- Why: Under UtilityItem the text is "Identification of the subscriber type, expressed as text" and the code "The code identifying for the service type"; UBL's definitions disagree. "Water" fits only the code's definition; the same subscriber is "Commercial" at the consumption point. Same as utilities/01#F13.
- Condition: Text and code describe one thing according to their definitions, or the reading is recorded as a TC finding.
- Options: (a) record the UBL inconsistency and keep; (b) drop the text; (c) the subscriber type in both.
- Needs decision: yes
- From: broad (F7), context (F6); parties refuted it

### utilities/05#F11 · Low · Whole shop's water booked to the garden department
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `6120`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Garden department`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:Description` = `Shop, Lumeport`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". The consumption point is the whole shop, not a garden department; booking all of it there only makes sense if the garden department is the main user (plant watering), which nothing says. Recounted: `<cbc:AccountingCost>Garden department` 16 times in 12 files, Brightmarket's purchasing default (copied). Against it (money, which refuted it): a store's garden department is a plausible user of water, and invoice 06 carries the same code. Aligned with the packaging merges ("cost centre fixed per party": Low, no); broad's "yes" not followed, since changing a cost centre does not change the story.
- Condition: The cost centre fits the shop's utility costs (the same in statement and invoice 06), or is absent, or the story gives the reason.
- Options: (a, preferred) a facilities or building cost centre of the shop, in 05 and 06 alike; (b) keep it with a stated reason.
- Needs decision: no
- From: broad (F5, yes), context (F7); money refuted it

### utilities/05#F12 · Low · "Maximum flow" of 2.5 m³/h is the meter's permanent flow rate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:Name` = `Maximum flow`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `2.5`
- Why: (Own knowledge.) 2.5 m³/h is a standard small water meter size: the permanent flow rate Q3 of ISO 4064 / OIML R49 (formerly the nominal flow Qn). Its maximum (overload) flow is Q4 = 1.25 × Q3 = 3.125 m³/h (old scheme Qmax = 2 × Qn = 5 m³/h). The size fits the use (86 m³ / 744 h = 0.12 m³/h on average, about 5 % of Q3), but the label is wrong. The broad and context parts read the value as the maximum flow and found it plausible, which does not settle the label.
- Condition: Property name and value agree with the rating they state (Q3 2.5 m³/h, or a maximum flow of 3.125 m³/h).
- Options: (a, preferred) rename the property to the permanent flow rate (Q3); (b) keep "Maximum flow" with 3.125 m³/h. Same property in 08.
- Needs decision: no
- From: logistics (F2)

### utilities/05#F13 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: The delivery location only points back to the consumption point CSW-CP-38510-411 the statement already identifies; "Earlier month." repeats the Period. No fillers (IND5).
- Condition: Each description carries information of its own, or is absent (the Delivery aggregate goes if it has nothing else).
- Options: (a, preferred) leave them out; (b) give the location the consumption point's ID.
- Needs decision: no
- From: broad (F8), logistics (F3), context (F9)

## Checked and consistent
- Meter: 4298 − 4212 = 86 m³ × constant 1 = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity; invoice 06 line 1 bills 86 m³ for meter CSW-W-55102, and its levy line also uses 86 m³.
- Amounts: 86 × 2.35 = 202.10; history 81 × 2.35 = 190.35 and 79 × 2.35 = 185.65; average quantity 82 m³ right; exempt (E, 0 %, reason WATER), tax 0.00, TaxInclusiveLineExtensionAmount = line amount, as in the invoice.
- Parent CSWC-INV-26-0317 is `06-Invoice.xml` (09:13, before this statement at 11:55); consumption line 1 is its line 1 (86 m³, price 2.35, contract CSW-C-260118).
- ConsumptionReportReference February (79 m³) agrees with ConsumptionHistory[2]; reading dates enclose March; units MTQ and MQH.
- Consumption point address equals Brightmarket's postal address (Market Street 50, 38515 Lumeport, Coastal State, XB-CO in CountrySubentity), matching "Shop, Lumeport".
- Parties match invoice 06; ISIC 3600 and 4719 fit; both parties under the Coastal State's sales tax (STT, STATE).
- check_ids.py: GLN 9522610900002 check digit correct.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: total lacks the sewage levy of invoice 06 — refuted by broad, logistics, context (levy collected for the city). The merge cannot settle it: kept as F5, Low, yes (from broad, logistics, context).
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: SMALL for a state's water company — refuted by broad; parties' finding kept as F8 with this argument (from broad).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID`: ID contains 38510 while the postal code is 38515 — refuted, the supplier's own identifier need not contain the postal code (from broad, logistics).
- `/UtilityStatement/cbc:AccountingCost`: "Garden department" copied — refuted by money (plausible water user, same as invoice 06). Kept as F11 with this argument (from money).
- `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID`: a real GLN — refuted, GS1 prefix 952 is reserved for demonstrations and examples, check digit valid (from parties).
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm`: a private company for a state's water supply — refuted, a utility can be a (state-owned) private limited company (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode`: utility type in a subscriber type — refuted by parties on the code's definition; the text element remains F10 (from parties).
- `06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `36.12`: the statement does not explain the levy — refuted by context (see F5) (from context).

## Changed in the merge
- money/F2 (Medium, yes) → F5 Low, yes: three parts refuted it with a defensible reading; the merge can neither confirm nor refute it. Preference changed to option (b) (note), which needs no new modelling.
- broad/F6 and context/F8 → F6 and F7: marketing data and contact split, as parties had them.
- context/F5 (Medium, no), logistics/F1 (no) → F9 Low, yes: aligned with utilities/01#F12.
- broad/F5 (yes) → F11, Needs decision: no: aligned with the packaging merges; money's counter-argument added.
- F4: count corrected to 364 occurrences in 213 files.

## Outside this review
- The same "Maximum flow" property occurs in `08-UtilityStatement.xml` (for merger B's review of 08).
