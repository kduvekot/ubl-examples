# LLM review: 05-Forecast.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/05-Forecast.xml`, Git blob `e5ca058f329dbb9d83da42c0dcf6bbefbfd16c1c` (committed)
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

### retail/05#F1 · High · Reference to the promotion does not resolve to the retail event of the flow
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26`
- XPath: `/Forecast/cbc:Note` = `Includes the spring garden promotion.`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:ID` = `BS-RE-26-0222`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:BuyerEventID` = `BM-SPRING-GARDEN-26`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:SellerEventID` = `LD-PROMO-26-03`
- Why: the forecast "Includes the spring garden promotion", and its only additional document reference is `BM-RE-26`, with no document type. The promotion is the retail event 06, issued the same morning by the same sender (08:17, before this forecast at 11:55), with document ID `BS-RE-26-0222`, buyer's event ID `BM-SPRING-GARDEN-26` and seller's event ID `LD-PROMO-26-03`. `BM-RE-26` is none of them and occurs in no other example (verified: `grep -rl --include='*.xml' 'BM-RE-26<'` finds only this file). 08-Order cites the event correctly as `BS-RE-26-0222`. The forecast cannot be linked to the event it includes: a broken reference.
- Condition: the forecast's reference to the promotion resolves to 06-RetailEvent (its document ID) and says what it is.
- Options: (a, preferred, all three parts) `BS-RE-26-0222` with a document type "Retail event"; (b) if `BM-RE-26` is a separate internal promotion plan, describe it and also refer to 06; (c) drop the reference and rely on the note (context).
- Needs decision: no
- From: broad, logistics, context

### retail/05#F2 · High · Emission factor and base do not give the stated emission
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as 02#F1: recomputed, 0.82 × 1 EA = 0.82 kg, not 96 kg; 96 / 0.82 = 117.1; 0.82 × 56.5 kg of materials = 46.3. 39 files carry the triple (verified).
- Condition: `ValueMeasure` = factor × activity quantity in the base's unit, or factor and base absent (or, with F11, no emission in the forecast at all).
- Options: (a, preferred) drop the emission from the forecast (F11), or at least factor and base; (b) an activity and unit that multiply out to 96 kg.
- Needs decision: no
- From: broad, logistics, context

### retail/05#F3 · Medium · A language code in LocaleCode
- XPath: `/Forecast/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Forecast/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code. 362 occurrences in 213 files (verified).
- Condition: every `LocaleCode` holds a locale from a locale list, or is absent.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad, parties, context (LocaleCode part of its F4)

### retail/05#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail, not a street name. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it; (b) record it in Bayvarra's address format.
- Needs decision: no
- From: broad, parties

### retail/05#F5 · Medium · Life-cycle stage "manufacturing" for a footprint from the mine to the factory gate
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: as 02#F7: code and description name different scopes (raw materials, transport and manufacturing against manufacturing only). No part raised it here; added for consistency with 02/04 and the earlier flows.
- Condition: code and description name the same scope (or, with F11, no emission in the forecast).
- Options: (a, preferred) drop the emission from the forecast (F11); otherwise omit the code.
- Needs decision: no
- From: added by the merge

### retail/05#F6 · Medium · A system-boundary code in the fullness indication
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: as 02#F8: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle boundary. 39 files (verified).
- Condition: no boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it (with F11, the whole emission); (b) record the missing boundary element for the TC.
- Needs decision: no
- From: context (fullness part of its F4)

### retail/05#F7 · Low · Signature without anything that signs
- XPath: `/Forecast/cac:Signature/cbc:ID` = `BM-SIG-26-0422`
- Why: only an ID and a signatory, no method or attachment; nothing in the story needs a signed forecast (IND5/IND6). 137 of 147 signatures in the world have this shape (lxml).
- Condition: a signature with a reason and its data, or none.
- Options: (a, preferred) drop it; (b) method and attachment with a reason.
- Needs decision: yes (world-wide convention, as in the air and utilities merges)
- From: context

### retail/05#F8 · Low · Party master data the forecast does nothing with
- XPath: `/Forecast/cac:SenderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Forecast/cac:SenderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Forecast/cac:SenderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Forecast/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Forecast/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Forecast/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/Forecast/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: a sales forecast between trading partners uses none of the logo, consumer web shop, social-media profile, share capital, customs trader number (domestic flow) or tax registrations; they are master data (section 4.8). `CorporateStockAmount` holds share capital where UBL defines "The number of shares in the capital stock of a corporation": TC write-up note.
- Condition: the parties carry what forecasting uses.
- Options: (a, preferred) leave them out; (b) record the share-capital definition conflict for the TC where the value stays.
- Needs decision: no
- From: parties (F3, F4, F7), context (F5, party part)

### retail/05#F9 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: as the sender of a forecast the buying office fits; job title and department are a seller's customer service and contradict the name. Same contact in 41 files (verified).
- Condition: name, job title and department agree with each other and with the role.
- Options: (a, preferred) a buyer's (or demand planner's) job title in purchasing.
- Needs decision: no
- From: broad, parties

### retail/05#F10 · Low · Frozen document indicator: by its definition, false says the forecast cannot be changed
- XPath: `/Forecast/cac:ForecastLine/cbc:FrozenDocumentIndicator` = `false`
- XPath: `/Forecast/cac:ForecastLine/cbc:Note` = `Week-by-week figures follow in the store's portal.`
- XPath: `/Forecast/cbc:VersionID` = `1`
- Why: UBL defines `FrozenDocumentIndicator` as "An indicator that the status of the forecast is modifiable (true) or not (false)" (verified with annotate.py; the only occurrence in the world). Read by the definition, `false` says the line is not modifiable, i.e. frozen, the opposite of what the element's name suggests. The forecast is version 1, not based on consensus and announces weekly figures to follow, which suggests it is open to change; the value seems to follow the name. Context had Medium (the element carries the opposite meaning); but a forecast frozen for the period, with weekly detail given elsewhere, is a possible reading, and the document says nothing that contradicts it, so the intent cannot be settled from the XML. The name/definition conflict is a candidate for the TC write-up.
- Condition: the indicator, read by its UBL definition, says what the story intends, or is absent.
- Options: (a, preferred) `true` if the forecast may still change, and record the name/definition conflict for the OASIS UBL TC; (b) drop the indicator.
- Needs decision: yes
- From: broad (Low), context (Medium)

### retail/05#F11 · Low · The forecast carries the item's full catalogue description
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Dimension[4]/cbc:MinimumMeasure` = `440`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: a Forecast is "A document used to forecast sales or orders"; it needs the item's identification and the quantity. The line repeats the catalogue description in full: the distributor's wording "from the distributor's stock", Urvania's tariff code (not used between two Bayvarran parties), the seller's own sales conditions, the load test, dimensions with tolerances, the footprint and the circularity profile. The supplier published all of it; the forecast does nothing with it.
- Condition: the forecast's item carries what identifies it and what the forecast depends on.
- Options: (a, preferred) reduce the item to name and identifiers (seller's ID `LD-10442`, GTIN); (b) keep an attribute only if the forecast depends on it (e.g. the colour variant).
- Needs decision: no
- From: broad (F5), context (F5, item part)

### retail/05#F12 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/Forecast/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: as 02#F16: the brand owner Valdara's GTIN is under Lumeway's company prefix 9520610 (own knowledge of the GS1 allocation rules).
- Condition: Valdara's GTINs and Lumeway's keys under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a Valdara prefix; (b) state that the distributor allocated it.
- Needs decision: yes
- From: parties

### retail/05#F13 · Low · World item number that is a valid GTIN-12
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: as 02#F21 (valid check digit, recomputed; GS1 US prefix 077 when read as a GTIN).
- Condition: world item numbers cannot be read as valid GTINs, or their non-assignment is recorded.
- Options: (a, preferred) a non-GTIN format; (b) record the verification.
- Needs decision: yes
- From: added by the merge (aligned with earlier flows)

## Checked and consistent
- Forecast period 2026-05-04 to 2026-06-15 contains the promotion period of 06 (`06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11`, to 2026-05-24); the line period equals the header's; `ForecastTypeCode` `TOTAL` and the note agree.
- Quantities: 40 benches in six weeks (ten pallets) against a stock of 3 (07), an order of 24 (08) and a 12-bench display (06); 3 + 24 = 27 covers the display and the first weeks, the rest can come from later orders (logistics).
- Issue time 11:55 is after 06 (08:17), so the forecast can include the confirmed promotion.
- Sender/buyer Brightmarket and receiver/seller Lumeway fit a buyer's sales forecast; both described as in every retail example.
- Item identifiers (`LD-10442`, GTIN `9520610000012`, `VI-B180`) agree with 02 line 1; GTIN and GLN check digits correct.

## Considered and refuted
- `/Forecast/cbc:BasedOnConsensusIndicator` = `false`: contradicts the agreed promotion — refuted, the promotion was agreed, not the forecast figures (from broad, context).
- `/Forecast/cbc:IssueTime` = `11:55:00`: against 06's issue at 08:17 — consistent (from broad).
- `/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `40`: not a multiple of the pallet of four — refuted, 40 is ten pallets, and a sales forecast counts consumer units anyway (from logistics).
- `/Forecast/cac:ForecastLine/cac:ForecastPeriod/cbc:StartDate`: line period repeats the header — refuted, it is the period of the line's quantity (from context).
- `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse — refuted (from parties).

## Changed in the merge
- broad/F2, logistics/F1, context/F1 → F1; broad/F1, logistics/F2, context/F2 → F2: combined.
- context/F4 split into F3 (LocaleCode, with broad/F3, parties/F1) and F6 (fullness indication).
- F5 (MANUFACTURING) and F13 (GTIN-like item number) added by the merge for consistency with 02/04 and the earlier flows.
- context/F6 → F7: "Needs decision" no → yes, aligned with the air and utilities merges.
- parties/F3, F4 (Low/yes → no, see 01#F6), F7 and the party part of context/F5 → F8.
- broad/F7, parties/F5 → F9.
- broad/F6 (Low/yes), context/F3 (Medium/yes) → F10: Low, because a frozen forecast is a possible reading and nothing in the document contradicts it.
- broad/F5 and the item part of context/F5 → F11.
- broad/F4, parties/F2 → F4.
