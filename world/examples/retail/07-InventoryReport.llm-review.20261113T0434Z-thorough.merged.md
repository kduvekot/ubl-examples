# LLM review: 07-InventoryReport.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/07-InventoryReport.xml`, Git blob `e1019ee6a13e2a7196d8ba163e99b452ac02b47f` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/07#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as 02#F1: recomputed, 0.82 × 1 EA = 0.82 kg, not 96 kg; 96 / 0.82 = 117.1; 0.82 × 56.5 kg of materials = 46.3. 39 files carry the triple (verified).
- Condition: `ValueMeasure` = factor × activity quantity in the base's unit, or factor and base absent (or, with F11, no emission in the report).
- Options: (a, preferred) drop the emission from the report (F11), or at least factor and base; (b) an activity and unit that multiply out to 96 kg.
- Needs decision: no
- From: broad, logistics, context

### retail/07#F2 · Medium · "Counted on Sunday evening", but the stock is reported as current on a Thursday
- XPath: `/InventoryReport/cbc:Note` = `Counted on Sunday evening.`
- XPath: `/InventoryReport/cbc:IssueDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryPeriod/cbc:EndDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:Quantity` = `3`
- Why: recomputed: 2026-04-23 is a Thursday (and the period start 2026-04-16 too); the last Sunday before it is 2026-04-19. `InventoryReportLine/Quantity` is "The quantity of the item reported that is currently in stock" and `InventoryPeriod` "The period covered by this report", ending on the issue day. A count from Sunday evening is four shopping days old at the end of the period; either the count date or the period and the "current" quantity are wrong. The order 08 of the next morning is based on this stock. Medium (logistics, context) rather than Low (broad): the value the report exists for does not mean what its element says, or the note is wrong.
- Condition: the day of the count in the note agrees with the inventory period and the issue date (the count lies at the end of the period the report covers).
- Options: (a, preferred) a note that matches the dates (e.g. counted on Thursday afternoon, the report being issued at 17:43), which keeps 08 unchanged; (b) end the period on Sunday 2026-04-19 and issue the report on Monday 2026-04-20 (context's preference).
- Needs decision: no
- From: broad (Low), logistics (Medium), context (Medium)

### retail/07#F3 · Medium · A language code in LocaleCode
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats the language code. 362 occurrences in 213 files (verified).
- Condition: every `LocaleCode` holds a locale from a locale list, or is absent.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list (context).
- Needs decision: no
- From: broad, parties, context (LocaleCode part of its F3)

### retail/07#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it; (b) record it in Bayvarra's address format.
- Needs decision: no
- From: broad, parties

### retail/07#F5 · Medium · Life-cycle stage "manufacturing" for a footprint from the mine to the factory gate
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: as 02#F7: code and description name different scopes. No part raised it here; added for consistency with 02/04 and the earlier flows.
- Condition: code and description name the same scope (or, with F11, no emission in the report).
- Options: (a, preferred) drop the emission from the report (F11); otherwise omit the code.
- Needs decision: no
- From: added by the merge

### retail/07#F6 · Medium · A system-boundary code in the fullness indication
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: as 02#F8: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle boundary. 39 files (verified).
- Condition: no boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it (with F11, the whole emission); (b) record the missing boundary element for the TC.
- Needs decision: no
- From: context (fullness part of its F3)

### retail/07#F7 · Low · Signature without anything that signs
- XPath: `/InventoryReport/cac:Signature/cbc:ID` = `BM-SIG-26-0423`
- Why: only an ID and a signatory; no method, no attachment, no reason in the story (IND5/IND6). 137 of 147 signatures in the world have this shape (lxml).
- Condition: a signature with a reason and its data, or none.
- Options: (a, preferred) drop it; (b) method and attachment with a reason.
- Needs decision: yes (world-wide convention, as in the air and utilities merges)
- From: context

### retail/07#F8 · Low · Party master data the inventory report does nothing with
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: a stock report to the supplier uses no logo, consumer web shop, social-media profile, share capital, customs trader number (domestic flow) or tax registration (the inventory value is a stock value, not a taxable amount); master data (section 4.8). `CorporateStockAmount` holds share capital where UBL defines "The number of shares in the capital stock of a corporation": TC write-up note.
- Condition: the parties carry what the report uses.
- Options: (a, preferred) leave them out; (b) record the share-capital conflict for the TC where the value stays.
- Needs decision: no
- From: parties (F3, F4, F7), context (F5, party part)

### retail/07#F9 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: name, job title and department contradict each other; for a stock report a store or stock-control contact would fit better than the buying office (broad). Same contact in 41 files (verified).
- Condition: name, job title and department agree with each other and with the role.
- Options: (a, preferred) a stock-control or buying contact with matching job title and department.
- Needs decision: no
- From: broad, parties

### retail/07#F10 · Low · Availability date for goods that are in stock
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityStatusCode` = `AVAILABLE`
- Why: `AvailabilityDate` is "The date from which the goods will be available. If not present, the goods are available now." The three benches are in stock; a date equal to the issue date says what absence would say (context). Broad refuted it: the agreed rule "nothing implied by absence" favours stating it explicitly. Here UBL's own definition gives the absence a meaning, so both readings of IND6 are possible; settle once.
- Condition: `AvailabilityDate` only for goods that become available later, or the explicit date is documented as the reading of IND6.
- Options: (a, preferred) drop it (context); (b) keep it as an explicit statement (broad).
- Needs decision: yes
- From: context (broad refuted)

### retail/07#F11 · Low · The report carries the item's full catalogue description
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- Why: an inventory report tells the supplier how many of an item are in stock; the item needs to be identified. The line carries the full catalogue entry: the distributor's wording "from the distributor's stock", Urvania's tariff code, the seller's sales conditions, footprint, circularity, load test, dimensions and warranty; the report uses none of it.
- Condition: the item carries what identifies it and what the report depends on.
- Options: (a, preferred) name and identifiers only (seller's ID `LD-10442`, GTIN).
- Needs decision: no
- From: broad (F5), context (F5, item part)

### retail/07#F12 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: as 02#F16 (brand owner Valdara's GTIN under Lumeway's company prefix 9520610; own knowledge of the GS1 rules).
- Condition: Valdara's GTINs and Lumeway's keys under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a Valdara prefix; (b) state that the distributor allocated it.
- Needs decision: yes
- From: parties

### retail/07#F13 · Low · World item number that is a valid GTIN-12
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: as 02#F21 (valid check digit, recomputed; GS1 US prefix 077 when read as a GTIN).
- Condition: world item numbers cannot be read as valid GTINs, or their non-assignment is recorded.
- Options: (a, preferred) a non-GTIN format; (b) record the verification.
- Needs decision: yes
- From: added by the merge (aligned with earlier flows)

### retail/07#F14 · Low · Inventory location without the store it is in
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:InventoryLocation/cbc:Name` = `Garden department, ground floor`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Garden department, Lumeport store`
- Why: `InventoryLocation` is "The location of the reported quantity of goods". The name gives a department and floor but no store, address or GLN, while Brightmarket, a chain ("Brightmarket Stores"), identifies this very place by GLN in 22. The supplier replenishing on this report cannot tell which store's stock it is.
- Condition: the inventory location identifies the store (name, and GLN or address) as well as the department.
- Options: (a, preferred) GLN `9522610900026` as the location's ID and the store in the name; (b) the store's address.
- Needs decision: no
- From: parties, logistics, context

## Checked and consistent
- Inventory value 1560.00 = 3 × 520.00, the trade price of 02 line 1 (stock valued at purchase price; recomputed).
- "Below the minimum of 6 before the promotion": 3 < 6; the order 08 of 2026-04-24 replenishes with 24; the note fits the promotion of 06.
- `DocumentReference` `BS-FC-26-0221` resolves to 05, issued the day before.
- Inventory period 2026-04-16 to 2026-04-23 is one week and ends on the issue date; `AvailabilityStatusCode` `AVAILABLE` fits stock on the shelf.
- Roles: Brightmarket is retailer ("The retailer, who sends this message") and inventory reporting party, Lumeway the supplier; both described as in every retail example; GLN and GTIN check digits correct.
- Item identifiers agree with 02 line 1.

## Considered and refuted
- `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityDate` = `2026-04-23`: filler — refuted by broad (IND6 favours stating it); not followed alone, kept as the Low/yes F10 with both readings (from broad).
- `/InventoryReport/cac:DocumentReference/cbc:ID`: a reference with only an ID — refuted, it resolves to the flow's forecast, an obvious companion of a stock report (from context).
- `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse — refuted (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined.
- broad/F4 (Low), logistics/F2 (Medium), context/F2 (Medium) → F2: Medium.
- context/F3 split into F3 (LocaleCode, with broad/F2, parties/F1) and F6 (fullness indication).
- F5 (MANUFACTURING) and F13 (GTIN-like item number) added by the merge, for consistency with 02/04 and the earlier flows.
- context/F7 → F7: "Needs decision" no → yes, aligned with the air and utilities merges.
- parties/F3, F4 (Low/yes → no, see 01#F6), F7 and the party part of context/F5 → F8.
- context/F4 (no) → F10: "Needs decision" yes, because broad's IND6 refutation is a possible reading.
- broad/F5 and the item part of context/F5 → F11.
- parties/F8, logistics/F3, context/F6 → F14.
- broad/F3, parties/F2 → F4; broad/F6, parties/F5 → F9.
