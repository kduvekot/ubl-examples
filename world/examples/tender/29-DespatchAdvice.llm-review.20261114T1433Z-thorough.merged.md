# LLM review: 29-DespatchAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/29-DespatchAdvice.xml`, Git blob `79edc7989dc6f0f5e4d8a3b040fb4fdfaa8e1ecc` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/29#F1 · High · The line says moss green, the item on the same line is identified and described as Ferro grey
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The release was changed to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`) and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). The line's own note confirms green benches, while the item on that line is the grey variant: ExtendedID "identifies the item with specific properties" (the model's own example is a chair's colour), the colour code GRY ("Grey, such as Ferro grey (RAL 7011)"; the world list has GRN, "Green, such as moss green (RAL 6005)."), and the property "Frame colour" = Ferro grey. The structured data and the note describe different goods; a receiver checking against the structured data would reject them.
- Condition: variant identifier, colour attribute and colour property describe what was despatched (moss green, RAL 6005), in agreement with the note.
- Options: (a) the green variant (ExtendedID, DescriptionCode GRN, "Frame in moss green (RAL 6005)", property value) here and in the documents that follow (preferred); (b) remove the colour data where the document does not need it.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### tender/29#F2 · High · Emission factor × base does not give the emission value
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: As 25#F2: recalculated, 0.82 × 1 EA = 0.82, not 96 kg CO2e (96 / 0.82 = 117.07 of an unstated activity). Same triple in 39 files.
- Condition: factor × base = value, or factor and base are absent.
- Options: (a) drop factor and base (preferred; also resolved by F16); (b) the base the factor refers to.
- Needs decision: no
- From: logistics (F2, High), broad (F5, Medium); context listed it under "Outside this review"

### tender/29#F3 · Medium · "Outstanding" 200 benches that were never ordered
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingQuantity` = `200`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingReason` = `Later releases under the framework contract.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `40`
- Why: `OutstandingQuantity` is "The quantity outstanding (which will follow in a later despatch)" against the referenced order line (`/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` of `LPWD-PO-26-0212`), which orders `26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `40`; 40 are delivered, nothing is outstanding. The 200 (240 − 40) are the estimated rest of the framework, which nobody has ordered and the buyer need not order (minimum 120, maximum 288); a logistics provider cannot announce them as following. (Money found the same 200 in the invoice's annotation "First release: 40 benches; 200 remain.", where it is a remark, not a quantity.)
- Condition: the outstanding quantity is the part of the referenced order line not yet despatched (0), or is absent.
- Options: (a) remove quantity and reason (preferred); (b) set it to 0.
- Needs decision: no
- From: broad (F3), logistics (F3), context (F3)

### tender/29#F4 · Medium · The advice says neither when the goods left nor when and where they arrive
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `CL-CS-26-0217`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` = `Civic Square`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Department` = `Procurement office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and services". This one has no `Delivery` on shipment or line: no actual despatch date or time, no estimated delivery, no despatch or delivery address. The only address of the receiving side is the department's office, room 2.14 for the head of procurement, while the order names `26-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Public works depot, Lumeport`; 40 benches cannot be received in an office. The note asks the receiver to check the goods "on arrival" (`/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`), and the debit note for lateness (34) depends on dates no document of the release states.
- Condition: the advice states the despatch date (and time), the expected arrival and the delivery location (the depot, with address), agreeing with the order.
- Options: (a) `Shipment/Delivery` with ActualDespatchDate/Time, EstimatedDeliveryPeriod and DeliveryAddress of the depot, and `Despatch/DespatchAddress` (Castrano's warehouse) (preferred); (b) at least the dates; if the department's postal address is all the world knows, drop `InhouseMail`, `Department` and `MarkAttention` for the delivery role (parties' option).
- Needs decision: no
- From: broad (F4), logistics (F4), context (F2), parties (F6, Low, address part)

### tender/29#F5 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty …": the value is a system boundary and says nothing about transport equipment; the boundary is in the lifecycle description. 39 files.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent.
- Options: (a) remove it (preferred; also resolved by F16); (b) TC write-up on the missing boundary element.
- Needs decision: no
- From: context (F4, Needs decision yes)

### tender/29#F6 · Medium · Lifecycle stage "Manufacturing" for an emission from the mine to the gate
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: As 25#F9: code (manufacturing only) and text (extraction to gate) cover different stages.
- Condition: code and description cover the same stages.
- Options: (a) omit the code or split by stage (preferred; also resolved by F16).
- Needs decision: no
- From: added in the merge (context F10 noted that the catalogue's remarks come along with every copy), aligned with 25#F9 and the decisions file

### tender/29#F7 · Medium · A province in `Region`, three times
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries"; a province is `CountrySubentity`, as the Bayvarran addresses use. 219 in 104 files.
- Condition: provinces are in `CountrySubentity`; `Region` is absent or holds a region.
- Options: (a) move them (preferred).
- Needs decision: no
- From: broad (F6, part), parties (F1), context (F5)

### tender/29#F8 · Medium · Language code in `LocaleCode`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 code. 362 in 213 files.
- Condition: `LocaleCode` is absent or names a locale from a locale list.
- Options: (a) remove it (preferred); (b) `en-XB` from a locale list.
- Needs decision: no
- From: broad (F6, part), parties (F2), context (F6)

### tender/29#F9 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The delivery customer is a municipal department (ISIC 8411); a liquidation status and a "Commercial register" type do not fit a body that is not a company.
- Condition: neither on the public body.
- Options: (a) drop both (preferred); (b) reduce the legal entity to name and CompanyID.
- Needs decision: no
- From: broad (F9, part, Low), parties (F8, Low), context (F8, Low)

### tender/29#F10 · Low · No packages, handling units or vehicle for a palletised road shipment
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`
- Why: The benches are sold on pallets of four (`15-Tender.xml`: orderable unit "Pallet of 4"; the item's waste is "Stretch film and pallet straps, per bench"), so the shipment is ten pallets on a lorry. The advice gives only a gross weight and the carrier: no number or kind of packages, no handling units, no vehicle, and no route although the goods cross the border the same day (30). The receiver cannot count what arrives, and the damage report the note asks for has no unit to refer to.
- Condition: the shipment states at least the number and kind of packages or handling units (10 pallets of 4 benches), consistent with quantity and weight.
- Options: (a) `TransportHandlingUnit` ×10 (or `TotalTransportHandlingUnitQuantity` 10) and the lorry in a shipment stage (preferred); (b) the package count only.
- Needs decision: no
- From: logistics (F5), broad (F4, part)

### tender/29#F11 · Low · "No status" stated for the document and the line
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: Both signify the status "with respect to its original state" (revised, cancelled …). This is the first and only advice of the release; "no status" says what absence says (IND5/IND6, no fillers).
- Condition: status codes are present only when there is a status to report.
- Options: (a) remove both (preferred).
- Needs decision: no
- From: broad (F7), logistics (F9), context (F7)

### tender/29#F12 · Low · No serial numbers although the contract requires them on the benches
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260327`
- Why: The contract's additional condition is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cbc:AdditionalConditions` = `Benches must carry the maker's serial number.` The advice identifies the 40 benches by one lot only (`ItemInstance/SerialID` is not used); the later damage case concerns one particular bench (33, "PARK-HB-B17"), which no document ties to a serial number.
- Condition: the despatched benches are identified by serial numbers, or the advice says where the list is.
- Options: (a) item instances with SerialID, or a serial range (preferred); (b) the lot plus a reference to a packing list.
- Needs decision: no
- From: logistics (F7)

### tender/29#F13 · Low · Line document reference with only an ID
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:DocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: "A reference to a document associated with this despatch line", with only an ID, which is at once the contract and the procurement file number (24#F11). Context refuted it (the definition allows any associated document); the reader still cannot tell what is referenced.
- Condition: the reference states what it refers to (e.g. DocumentType "Framework contract"), or is absent.
- Options: (a) add the document type (preferred); (b) remove it.
- Needs decision: no
- From: logistics (F8), broad (F9, part); context refuted it (carried)

### tender/29#F14 · Low · Programme code differs from the procurement documents
- XPath: `/DespatchAdvice/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/DespatchAdvice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: As 26#F15: the programme is `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in 01–03 and 24, and here the same string serves as project identifier and as the buyer's accounting code (header and line). Broad, money and context refuted the accounting code itself in a logistics provider's document (passed on from the order so the buyer can book the receipt); the code difference remains.
- Condition: one code for the programme throughout the flow.
- Options: as 26#F15.
- Needs decision: no
- From: logistics (F10)

### tender/29#F15 · Low · Contacts that do not fit their roles
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- Why: The despatching party is a warehouse operator (ISIC 5210) and its contact is "Warehouse office", but its job title and department are those of a sales desk (the same pair as Valdara's order desk, `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`): name, title and department do not agree. `DeliveryCustomerParty` is "The delivery recipient", whose contact should receive goods; it is the procurement office that bought them, with nobody named at the place of arrival.
- Condition: the despatch contact's title and department fit a warehouse office; the delivery recipient's contact is the one that receives the goods.
- Options: (a) e.g. "Despatch clerk" / "Warehouse", and a depot goods-in contact for the delivery customer (preferred); (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F8), parties (F5), parties (F6, contact part)

### tender/29#F16 · Low · The whole catalogue record of the item repeated in a despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:Dimension[4]`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: A despatch advice says what was put on the lorry: item, variant, lot, quantity. The line repeats the catalogue entry of 25 in full (keywords, brand, load test method, seat-height range, emission with method and period, circularity profile with repairability), which a warehouse despatching pallets neither states nor uses; the catalogue's problems (F2, F5, F6, two keywords in one element) come along with the copy.
- Condition: the item carries its identification and the properties the despatch uses; the catalogue description stays in the catalogue.
- Options: (a) reduce the item to identification, name, variant, lot and physical data (preferred); (b) keep the full copy and record the design decision.
- Needs decision: no (aligned with the decisions file; context said yes)
- From: broad (F9, part), context (F10)

### tender/29#F17 · Low · Master data of the seller that the despatch does nothing with
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketName` = `Ferrano Stock Exchange`
- Why: The seller's share capital, fully-paid indicator and stock-exchange listing add nothing to the description of a despatch. Parties refuted the listing (part of a listed company's description), carried. Context also counted the seller's `ServiceProviderParty`; the merge follows broad and parties, who refuted it here: this document is the despatch Castrano performs as Valdara's provider (see Considered and refuted).
- Condition: the seller carries share capital and listing only in documents whose purpose uses them.
- Options: (a) remove them here (preferred).
- Needs decision: no
- From: context (F9, part)

### tender/29#F18 · Low · Registration date 1996-01-01 for the despatch party and the carrier
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Castrano Logistics SRU and Trasvia Haulage SRU share 1996-01-01 with about 25 unrelated companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<' world/examples | wc -l`); it reads as a filler. Giving each company its own date changes their histories.
- Condition: each company's `RegistrationDate` is its own, or the element is absent.
- Options: (a) a date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes (company histories; parties said no)
- From: parties (F3)

### tender/29#F19 · Low · Wholly owned subsidiary of a large listed company classed as small
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- Why: `EntitySizeCode` is "A code signifying the size category of the legal entity". Castrano is SMALL and owned 100 % by `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`, which the same document classes as `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`. Under the EU SME definition (own knowledge) a wholly owned subsidiary counts with its owner; the world may define size per legal entity, which the XML does not say.
- Condition: the size class of a wholly owned subsidiary follows the rule the world uses; if groups count together, Castrano is not small.
- Options: (a) state the rule; the group reading is preferred as the usual meaning; (b) size per legal entity, then nothing changes.
- Needs decision: yes
- From: parties (F4)

### tender/29#F20 · Low · Party tax exemption reason worded as a transaction
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the text begins with a kind of sale; only its second half is the party's status.
- Condition: the party-level reason states the party's status.
- Options: (a) reword, e.g. "Public body: exempt from the state sales tax" (preferred).
- Needs decision: no
- From: parties (F7)

### tender/29#F21 · Low · Same Urvanian party tagged `en-XU` here and `en-XB` in the Bayvarran-issued examples; Italian names tagged as English
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- Why: This Castrano-issued advice tags Valdara's English renderings `en-XU` and gives the legal form twice; the Bayvarran-issued examples tag the same texts `en-XB` with a single untagged legal form (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). This example is the `en-XU` side of the inconsistency across the flow. The renderings are moreover Italian names and legal forms tagged as English (the earlier flows' second Low/yes question). Neither can be settled from the XML.
- Condition: the same text carries the same `languageID` in every example, and the tag names the language of the text, or the convention is documented.
- Options: (a) `en-XU` everywhere, as here, and the convention recorded (preferred); (b) document the issuer rule.
- Needs decision: yes
- From: parties (F9); Italian-name question added by the merge, as in 24–28

### tender/29#F22 · Low · World item number that is a valid GTIN-12
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- Why: As 25#F21: valid GS1 check digit (recalculated: 7), readable as a GTIN-12 in the US/Canada range; the world's own scheme is the counter-argument.
- Condition: world item numbers cannot be read as valid GTINs, or their verification is recorded.
- Options: (a) change the world item-number format (preferred); (b) record the verification.
- Needs decision: yes
- From: added in the merge, aligned with 25#F21 and the decisions file

## Checked and consistent
- `OrderReference` `LPWD-PO-26-0212` and order line 1 resolve to 26 and its only line; delivered 40 EA = ordered 40 = invoiced 40 (`32-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `40`); `LineCountNumeric` 1.
- Sub-lines (recalculated): anchor sets 36 delivered + 4 on back order = 40, one per bench, with reason and time ("within a week"); bolts 170 − 10 oversupplied = 160 = 40 × 4, matching "four ground anchors and the bolts to fix them".
- Shipment CL-SH-26-0216, consignment CL-CS-26-0217, carrier Trasvia Haulage and gross weight 1660 kg as in 30 (shipment and weight also in 31).
- Gross weight (recalculated): 1660 / 40 = 41.5 kg per bench, the world's gross bench weight (`sea/10-PackingList.xml:/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` = `3984` for 96 benches = 41.5 kg; net `sea/10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762`, 39.19 kg per bench). See "Refuted in the merge" for the comparison with the resource consumption.
- Volume: 1.8 × 0.62 × 0.78 m = 0.87 m³ per bench, 35 m³ for 40 before stacking: one articulated lorry (about 90 m³) suffices (from logistics).
- Lot VI-LOT-260327 = manufacture date 2026-03-27, between the acceptance of the colour change (25 March) and the despatch (30 March); issue 30 March 17:37 follows the export declaration (13:40) and precedes the import declaration (31 March).
- Castrano Logistics as despatch party is Valdara's warehousing and despatch provider (same register number), signs the advice, and is 100 % owned by Valdara: the three statements agree. Trasvia Haulage: ISIC 4923, planning contact, international haulage permit XU-HAUL-2020-0877 valid to 2030-06-30 (from parties).
- DespatchAdviceTypeCode DELIVERY, CertificateTypeCode PERMIT in their lists.
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/DespatchAdvice/cbc:AccountingCostCode`: the buyer's cost code in a document of the seller's warehouse, repeated on the line — refuted: passed on from the order so the buyer can book the receipt (from broad, money, context); the programme-code difference is F14.
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[2]/cbc:OversupplyQuantity`: bolts are no order line — refuted: they belong to the bench, 4 each, so 10 over is an oversupply (from broad, logistics, context).
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate`: 40 benches made two days after the colour was agreed — refuted: coating stocked frames in another colour in two days is feasible (from broad, logistics).
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted: this document is the despatch Castrano performs for the seller (from broad, parties); context counted it in its F9, not followed.
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: ICD 0990 — refuted, not an allocated ISO 6523 ICD (own knowledge) (from broad, parties).
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` — refuted: text element, same everywhere (from parties).
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 — refuted, not assigned in E.164 (from parties).
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — refuted by parties; the merge keeps it in F17 (from parties).
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID`: certificate without issuer — refuted: the scheme says whose licence it is (from parties); the authorisation in a despatch advice — refuted: the transport crosses the border and the licence entitles the carrier to it (from context).
- `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: redundant next to the delivery customer — refuted: no "if different" condition, and the advice refers to the buyer's order (from parties).
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderQuantity`: 4 sets late while the invoice bills complete benches — refuted for this document: stated with reason and time; the billing is 32's (from logistics; money listed it under "Outside this review").
- `/DespatchAdvice/cbc:ID`: running number shared with other parties' documents (0214 response, 0215–0217 here, 0218 export) — refuted as a finding of this example: each ID is of the kind its element names (from logistics).
- `/DespatchAdvice/cac:DespatchLine/cac:DocumentReference/cbc:ID`: the contract as a line reference — refuted by context (any associated document); the merge keeps logistics' F13 for the missing type (from context).
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: DELIVERY — refuted, fits (from context).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: customs-trader numbers of the parties as copied master data — considered by the merge and refuted: the consignment crosses the Urvania–Bayvarra border the same day, and the despatch advice accompanies the goods to the importer (merge).

## Refuted in the merge
### broad/F2 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1660`; `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `40`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`.
- Part's argument: one bench "contains" 34 kg of steel and 22.5 kg of hardwood, 56.5 kg; 40 benches weigh 2260 kg net before anchors, bolts, packaging and ten pallets; 1660 kg (41.5 kg per bench) is below the net weight. Condition: gross weight ≥ 40 × bench weight + accessories, packaging and pallets, and per-bench material figures agree with it. Options: about 2600 kg gross (also in 30, 31), or lower material figures.
- Refuted because: `ResourceConsumption` is "A record of a resource consumed, such as energy, water, or materials", i.e. the input to production, not the content of the product. Casting (gates and risers returned to the melt) and sawing slats from hardwood leave material behind; a yield of about 70 % (39.19 / 56.5) is plausible (own knowledge of foundry and sawmill yields). The world's bench weighs 39.19 kg net and 41.5 kg gross (sea/10-PackingList: 3762 / 3984 kg for 96 benches), and 1660 = 40 × 41.5 exactly. Gross is therefore not below net. Merger E refuted the same claim for 30. Whether ten pallets' tare should be added to the shipment's gross weight (the definition includes packaging and transport equipment) is listed under "Outside this review".

### logistics/F6 · Low · Gross weight is light against the materials the item is said to contain
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1660`.
- Part's argument: 41.5 kg gross per bench; deducting ten pallets (about 200 kg), 36 anchor sets (about 144 kg) and 170 bolts (about 17 kg) leaves about 32 kg per bench, against 56.5 kg of material consumed, a loss of over 40 %; a cast-steel bench of 1.8 m weighs 50 kg or more. Condition and options as broad/F2.
- Refuted because: as above, consumption is not product weight; the world's bench weight (39.19 kg net, 41.5 kg gross, sea/10) is consistent with 1660 kg for 40. The part's deduction of pallets and anchors assumes the 41.5 kg excludes them, which the XML does not state; that question is the pallet-tare remark under "Outside this review", not a contradiction within this example.

## Changed in the merge
- logistics/F2 (High), broad/F5 (Medium) → F2: High, aligned with the decisions file.
- broad/F4, logistics/F4, context/F2, parties/F6 (address part) → F4: combined, Medium (a despatch advice's purpose depends on the dates, as in the earlier flows).
- context/F4 → F5: Needs decision no, aligned.
- F6 (lifecycle stage) and F22 (GTIN-like item number) added by the merge.
- broad/F6 → F7 and F8: split.
- broad/F9, parties/F8, context/F8 → F9 (public body, raised to Medium), F13 (reference), F16 (catalogue copy).
- broad/F4 (part), logistics/F5 → F10.
- broad/F8, parties/F5, parties/F6 (contact part) → F15: all contacts grouped, as in the decisions file.
- context/F10 → F16: Needs decision no.
- context/F9 → F17: the service provider removed from it (refuted by broad and parties).
- parties/F3 → F18: Needs decision changed from no to yes, aligned with the decisions file.
- parties/F9 → F21: the Italian-name question added.
- broad/F2, logistics/F6 → "Refuted in the merge", aligned with merger E's refutation for 30.

## Outside this review
- Whether ten pallets' tare (and the anchor sets) are included in 1660 kg: the shipment's gross weight is defined as "the weight of the goods plus packaging plus transport equipment", and 1660 = 40 × 41.5 leaves nothing for pallets if 41.5 is the bench's packed weight; a cross-flow plausibility question for the bench's world weight (as merger E noted for 30).
- No later despatch of the four anchor sets on back order appears in the flow (from logistics).
- Whether 40 benches on ten pallets fit one road vehicle, and the lorry's route from Ferrano to Lumeport on the map, are capacity and location questions (from broad, logistics).
- Whether Bayforth Forwarding, named as freight forwarder in 27, should appear here is 27#F9 (from parties).
