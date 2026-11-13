# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

@@HEADER@@

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

### sea/19#F1 · High · The bench's emission value, factor and base do not agree
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". Factor × base = 0.82 × 1 EA = 0.82, not the stated 96 kg CO2e; conversely 96 / 0.82 = 117.1 units of base. The three values contradict each other. No part of this run raised it; the merge adds it because the same item block was found in the earlier flows (road, rail, retail merges: High, drop factor and base), and the coordinator listed it as a recurring problem.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure` (in consistent units), or factor and base are absent.
- Options: (a) preferred: drop `ValueFactorNumeric` and `ValueBaseMeasure` (the 96 kg per bench is a direct result, base 1 EA adds nothing); (b) a factor and base whose product is 96 kg (e.g. per kg of steel), with the activity named.
- Needs decision: no
- From: merge (no part raised it)

### sea/19#F2 · Medium · A language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 language code of `Language/cbc:ID` and name no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F3)

### sea/19#F3 · Medium · Gate number in AdditionalStreetName of the consignor's postal address
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." A business-park gate is a vehicle access point, not a street, and a postal address holds nothing that only matters for vehicles. 79 occurrences in 76 files, always Lumeway Distribution's address (parties, grep over `*.xml`).
- Condition: The consignor's postal address holds no gate.
- Options: (a) preferred: drop it from the postal address, giving it only where vehicles need it (pickup/delivery location); (b) the park's internal road name, if it has one.
- Needs decision: no
- From: broad (F3), parties (F2)

### sea/19#F4 · Medium · The customs authority is described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41448`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CustomsParty` is "the Authority who is legally responsible for processing the Declaration"; the Island Customs Service is a state administration (its own ISIC 8411). Its legal entity gives it a `CompanyID` in the "Island companies register" of type "Commercial register" and a liquidation status; a customs administration is not a registered company and cannot be liquidated. The world's registration type list has no code for public bodies (26 such public-body aggregates in the examples, parties, lxml over `*.xml`).
- Condition: The customs authority's legal entity claims no commercial-register registration and carries no liquidation status.
- Options: (a) preferred: keep `RegistrationName` (and the party identification), drop `CompanyID`, `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode`; (b) a register of public bodies with its own type code.
- Needs decision: no
- From: parties (F1), broad (F8, part, Low)

### sea/19#F5 · Medium · Shipment gross weight leaves out the container
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` = `3984`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:GrossWeightMeasure` = `122.4`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", while `GoodsItem/GrossWeightMeasure` is the weight "including packing and packaging but excluding the carrier's equipment". Merge recalculation: 3984 + 122.4 = 4106.4 kg, the goods items only; with the container's tare of 3750 kg (manifest) the shipment weighs 4106.4 + 3750 = 7856.4 kg, the container's gross weight on the bill of lading. Customs practice declares gross mass without the container; under the semantic-conformance rule that does not change the element's meaning. The same 4106.4 is the `Shipment/GrossWeightMeasure` of 8 examples of the flow (09, 10, 11, 12, 14, 15, 19, 20; logistics, XPath query over `sea/*.xml`).
- Condition: `Shipment/GrossWeightMeasure` includes the transport equipment (7856.4 kg), or the goods-only weight is given only in elements whose definition excludes the equipment.
- Options: (a) preferred: leave the goods' weights on the goods items (they already sum to 4106.4 kg) and give the shipment 7856.4 kg; (b) drop `Shipment/GrossWeightMeasure` here.
- Needs decision: no
- From: broad (F1), logistics (F2)

### sea/19#F6 · Medium · Customs value of the goods is the FOB price, although freight is declared and the bill of lading gives a CIF customs value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `307.200`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:Amount` = `1162.121`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`
- XPath: `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `53778.00`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". Merge recalculation: 49920.00 XBL × 0.4 = 19968.000 XLC and 768.00 × 0.4 = 307.200 XLC, total 20275.200 XLC = 50688.00 XBL × 0.4, the FOB value (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`). The goods were sold CIF Selanu and invoiced at 53778.00 XBL = FOB 50688.00 + freight 2950.00 + insurance 140.00, and the bill of lading gives 53778.00 as the value for customs purposes. On a CIF valuation basis (WTO Valuation Agreement Art. 8.2, as most countries apply it; own knowledge) the customs value would be 53778.00 × 0.4 = 21511.200 XLC. The declaration lists a freight share, but not inside the value, and gives no reason why Lisavu values FOB. Broad refuted "value without freight under CIF" because customs can build the CIF value from the separate freight element; that reading is possible, but the definition says "total declared value", and the bill of lading's customs value disagrees either way. Which basis Lisavu uses is a question of its customs law, hence a decision.
- Condition: The declared customs values follow one stated valuation basis of Lisavu, consistent with the freight and insurance figures in the same declaration and with the customs value in the bill of lading.
- Options: (a) preferred: CIF basis, each goods item's value including its share of freight and insurance (total 21511.200 XLC); (b) keep FOB as Lisavu's rule, say so, and align the bill of lading's customs value.
- Needs decision: yes
- From: money (F1); broad's refutation carried as counter-argument

### sea/19#F7 · Medium · Urvania's national tariff used in an import declaration lodged in Lisavu
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XL`
- Why: `CommodityCode` is "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". In an import declaration the national subdivision that matters is the importing country's tariff, which determines the duty; this declaration applies in Lisavu and is lodged with the Island Customs Service. Both goods items carry, as 8-digit code, an entry of `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, Urvania's national tariff (Urvania is the country of origin, neither exporting nor importing country). The code is valid in its list but not the one the importing customs applies. The XU list is the only national tariff list in the examples (61 uses, `grep -rho --include='*.xml' 'listID="urn:ubl-examples:world:X[A-Z]:codelist:CustomsTariffCode"'`; context, logistics, broad). Earlier flows judged the XU code Low where it was copied into non-customs documents; here it is the classification the declaration rests on, hence Medium.
- Condition: The national commodity code in this import declaration is from the tariff the Island Customs Service applies (a Lisavan or common Trade Accord tariff), or only the HS code is declared.
- Options: (a) preferred: a Lisavan (or common Accord) tariff list with the corresponding codes; (b) if the Accord has one common tariff, give that list an Accord-level listID; (c) keep only the 6-digit HS code of `CommodityClassification[1]`.
- Needs decision: yes (whether Lisavu has its own tariff)
- From: context (F1), logistics (F1), broad (F5, Low)

### sea/19#F8 · Medium · Lifecycle stage "Manufacturing" for an emission described from the mine to the factory gate
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; the code says Manufacturing, while the description (the same element's text equivalent) covers raw material extraction, transport and manufacturing, i.e. cradle to gate (EN 15804 modules A1–A3, own knowledge). Code and text disagree. Added by the merge, aligned with the earlier flows' merges (Medium/no).
- Condition: The lifecycle stage code and its description name the same scope.
- Options: (a) preferred: a code for the product stage (raw material to factory gate) if the world list has one, or drop the code and keep the description; (b) narrow the description to manufacturing only (changes the value 96 kg).
- Needs decision: no
- From: merge (no part raised it)

### sea/19#F9 · Medium · "Cradle to gate" in an element that says whether transport equipment is full
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." A system boundary of a product footprint is not a fullness indication; the code comes from the world's EmissionBoundaryCode list, a list meant for another concept. Added by the merge, aligned with the earlier flows (Medium/no; candidate for the TC write-up, since UBL has no element for the boundary).
- Condition: `FullnessIndicationCode` is absent from an item's product footprint, or holds a fullness indication.
- Options: (a) preferred: drop it (the description already states the boundary); (b) record the missing boundary element as a finding for the OASIS UBL TC.
- Needs decision: no
- From: merge (no part raised it)

### sea/19#F10 · Medium · The commercial invoice the customs value rests on is not referenced
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InvoiceLine/cbc:ID` = `1`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InvoiceLine/cbc:InvoicedQuantity` = `96`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- XPath: `22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147`
- XPath: `22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `49920.00`
- Why: Goods item 1 carries "invoice line 1", but the declaration nowhere says which invoice; its only document reference is the bill of lading. The seller's invoice `LD-INV-26-0147` (issued 2026-05-14, before this declaration) is the basis of the customs value (19968.000 XLC = 49920.00 XBL × 0.4) and is what customs checks it against. Goods item 2 (12 side frames) has no invoice line. The invoice-line reference cannot be resolved, which the declaration's purpose depends on (broad Medium; logistics Low).
- Condition: The declaration references `LD-INV-26-0147` (as commercial invoice), and each goods item points to its invoice line.
- Options: (a) preferred: an `AdditionalDocumentReference` to `LD-INV-26-0147` with a type, and invoice line 2 on goods item 2; (b) at least the invoice reference.
- Needs decision: no
- From: broad (F2), logistics (F4)

### sea/19#F11 · Low · A validity period for an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:StartDate` = `2026-05-19`
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `30`
- Why: `ValidityPeriod` is "A period, assigned by the issuer, during which the information in the declaration is valid". A declaration for release for free circulation (`SubTypeCode` FREECIRC) is accepted and the goods released; it does not lapse after 30 days, and nothing in the flow uses the period (no fillers).
- Condition: A validity period is present only where the procedure gives the declaration a validity (e.g. a pre-lodged declaration).
- Options: (a) preferred: drop it; (b) make it a pre-lodged declaration with a reason (changes the story).
- Needs decision: no
- From: context (F3)

### sea/19#F12 · Low · The declaration does not say how the goods arrived; the bill of lading reference has ID only
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: The declaration names an exit office ("customs exit office of the goods being declared") belonging to Bayvarra's export, but neither the office of entry or lodging in Selanu, nor the container (`TWLU4120872`), the vessel (Tidewell Harbour, voyage TH-26-19E), the mode at the border or the arrival date. Only the bill of lading number, without type, links the declaration to the transport. An import declaration is normally matched against the carrier's manifest (`15-Manifest.xml`) by these data. The exit office itself was refuted as a finding by broad and context (see "Considered and refuted").
- Condition: The declaration identifies the transport by which the goods entered Lisavu (at least container or vessel/voyage, and place of entry), and the bill of lading reference says what it is.
- Options: (a) preferred: a main-carriage `ShipmentStage` with mode, vessel and journey (which would also give the empty stage of F14 a content), the container on a `TransportHandlingUnit`, and the Selanu office as location; (b) at least `DocumentTypeCode` on the reference and the Selanu office.
- Needs decision: no
- From: logistics (F3)

### sea/19#F13 · Low · Contacts that do not fit an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:Contact/cbc:Name` = `Export desk`
- Why: The importer's contact is named Purchasing but is a customer service officer in Sales: name, title and department disagree, and none is the import function customs would ask (the broker's contact `Declarations` fits its role). The forwarder appears with its export desk in an import declaration. Both are master-data contacts used in every role of the flow.
- Condition: The importer's contact agrees in name, title and department and is responsible for imports; the forwarder's contact handles the import side, or is absent.
- Options: (a) preferred: role-specific contacts; (b) drop the contacts where the broker is customs' contact.
- Needs decision: no
- From: parties (F5), broad (F8, part)

### sea/19#F14 · Low · The customs broker repeated in an otherwise empty shipment stage
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: Tevaro is the importer's agent, holder of the power of attorney, notifier, customs agent of a shipment stage and signatory. The shipment stage contains nothing but the customs agent (no mode, means, place or time), so it is not "A stage in the transport movement of this shipment" but a container for a role already stated. The parties part refuted the double agent (agent and power-of-attorney holder say different things) and the notifier (the broker is the party customs deals with); the merge accepts those and keeps the finding for the empty stage.
- Condition: A shipment stage is present only to describe a stage of the transport.
- Options: (a) preferred: drop the empty stage (or give it its transport content, F12 option a); (b) keep the notifier only if it means something different here.
- Needs decision: no
- From: context (F4); parties' refutations carried

### sea/19#F15 · Low · Power of attorney notarised by a chamber of commerce, witnessed by the warehouse company, mandate reference without meaning
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:NotaryParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:WitnessParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:MandateDocumentReference/cbc:ID` = `MAND-2026-014`
- Why: `NotaryParty` is "The Party who notarises this Power of Attorney"; a chamber of commerce certifies signatures and origin but is not a notary (own knowledge). `WitnessParty` is "A Witness to this Power of Attorney"; a witness attests a signing and is normally a natural person, while Nalevi Warehousing is the company that receives the goods (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`) and has an interest of its own in the clearance; nothing explains why it witnessed a power of attorney of 2026-01-05. The mandate reference `MAND-2026-014` occurs in no other example and has no type, so it is unclear what mandate it is.
- Condition: The notary is a notary (or absent); the witness is a person with no interest in the clearance (or absent); the mandate reference says what it is or is left out.
- Options: (a) preferred: drop `NotaryParty` and `WitnessParty` (a customs power of attorney is usually a signed form with neither) and give the mandate a type or drop it; (b) a notary's office in Selanu and a natural person as witness.
- Needs decision: yes (changes who takes a role; broad said no)
- From: broad (F6), context (F5), parties (F4)

### sea/19#F16 · Low · Bayvarran tax registrations and share capital of consignor and forwarder in a Lisavan import declaration
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: The Island Customs Service needs the consignor's and forwarder's name, address and identification; their Bayvarran state sales-tax registrations and the consignor's share capital play no part in levying Lisavu duties (the importer, who is liable, carries no tax scheme). Copied master data (section 4.8).
- Condition: Consignor and forwarder carry only the party data the declaration uses.
- Options: (a) preferred: drop their `PartyTaxScheme` and the consignor's `CorporateStockAmount`/`FullyPaidSharesIndicator`; (b) keep them with a stated customs purpose.
- Needs decision: no
- From: parties (F6), money (F3)

### sea/19#F17 · Low · Catalogue and product-passport data copied into the customs declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: The bench's item carries the complete catalogue description: keywords, warranty, the seller's sales conditions, load test, colour options, emissions (see F1, F8, F9 for their own errors), circularity profile and product documentation. An import declaration needs what identifies, classifies, values and checks the goods; customs and the broker do nothing with these elements. Goods item 2 (the side frame) is declared without them, which shows the declaration does not need them. The same blocks appear in `20-DespatchAdvice.xml`, `21-ReceiptAdvice.xml` and `22-Invoice.xml`.
- Condition: The declared items carry only what customs uses (and data a stated customs rule asks for).
- Options: (a) preferred: reduce the bench's item to identification, classification, origin and classification-relevant properties; (b) if a product passport is part of Lisavan import rules in the world, keep the circularity (and emission) data with that rule and drop the sales data.
- Needs decision: no
- From: broad (F7), context (F2)

### sea/19#F18 · Low · The bench's GTIN is in the distributor's GS1 company prefix, not the manufacturer's
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- Why: The GTIN of Valdara Industries' bench (manufacturer's item `VI-B180`) begins with `9520610`, the company prefix of Lumeway Distribution's GLN `9520610900008`. Under GS1 allocation rules the brand owner allocates the GTIN; a distributor allocates one only for its own label (own knowledge). Nothing says the bench is a Lumeway private-label product. Both check digits are valid (`check_ids.py`). Added by the merge, aligned with the retail merges (Low/yes); whose brand the bench is, is story.
- Condition: The GTIN is in the company prefix of the brand owner the world names, or the world states that Lumeway is the brand owner.
- Options: (a) preferred: a GTIN in Valdara's own prefix; (b) record Lumeway as brand owner.
- Needs decision: yes
- From: merge (no part raised it)

### sea/19#F19 · Low · The world item number has a valid GS1 check digit
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: The world's item number is 12 digits with a valid GTIN-12 check digit (merge recalculated: weights 3/1 from the right over 77102000002 give 43, check digit 7). Read as a GTIN-12 (= GTIN-13 `0771020000027`, prefix 077, GS1 US range; own knowledge), it can be mistaken for a real GTIN, against the rule that fictional values must not be mistaken for real ones. Added by the merge, aligned with the retail and road merges (Low/yes).
- Condition: The world item number cannot be read as a valid GTIN (another length or format), or the world records why it may.
- Options: (a) preferred: a format that is not a valid GTIN (e.g. a letter prefix); (b) record the convention.
- Needs decision: yes
- From: merge (no part raised it)

### sea/19#F20 · Low · Freight share given for the benches only, and the whole insurance policy attached to the benches
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:Amount` = `1162.121`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Ocean freight, share of the benches`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `307.200`
- Why: The freight 2950.00 XBL (2700 + 250, `14-BillOfLading.xml`) = 1180.000 XLC is apportioned by value: 1180.000 × 19968.000 / 20275.200 = 1162.121 XLC for the benches (merge recalculated); the side frames' share, 1180.000 − 1162.121 = 17.879 XLC, is declared nowhere, so the declared freight does not add up. The insurance policy, whose insured value 59155.80 XBL is 110 % of the CIF value of both goods items (1.1 × 53778.00, as on the bill of lading), is attached to goods item 1 only ("insurance policies that apply to this goods item") and in XBL while the declaration's values are in XLC; read per goods item, the benches appear insured for more than the whole consignment and the frames not at all.
- Condition: Freight and insurance are given per goods item for every goods item, adding up to the totals, or once for the shipment.
- Options: (a) preferred: give goods item 2 its freight share (17.879 XLC) and an insurance reference, or move both to the shipment; (b) leave them out if Lisavu's valuation does not use them (F6).
- Needs decision: no
- From: broad (F4), logistics (F5), money (F2)

## Checked and consistent
- Values: 49920.00 × 0.4 = 19968.000 and 768.00 × 0.4 = 307.200 XLC at 0.4 XLC per XBL (forwarding instructions, bill of lading, invoice); the same values in XBL in `11-ExportCustomsDeclaration.xml`; 19968.000 + 307.200 = 20275.200 XLC = 50688.00 XBL (FOB) (broad, money, logistics; merge recalculated).
- Weights: 3984 + 122.4 = 4106.4 kg, equal to the packing list and the bill of lading; 3984 / 96 = 41.5 kg per bench including its share of 24 pallets; 122.4 / 12 = 10.2 kg per casting; 7856.4 − 3750 = 4106.4 (broad, logistics).
- References: previous declaration `BF-CD-26-0136` is the customs declaration inside `11-ExportCustomsDeclaration.xml`; `TOL-BL-26-0139` resolves; shipment `LD-SH-26-0132`, consignor, consignee (Velumi), forwarder and customs party agree with 14 and 15 (broad, logistics, parties).
- Quantities 96 benches and 12 side frames agree with order, despatch advice and invoice (broad, context).
- GTINs `9520610000012`, `9520610000029` and GLN `9520610900008` pass `check_ids.py`; HS 940179 / 732599 fit benches with metal frames and cast steel parts (broad).
- Issued 2026-05-19 09:07, after the discharge 2026-05-18 11:20 (`17-TransportationStatus.xml`); free circulation under a purchase agrees with the sale (broad, context, logistics).
- Parties: Tevaro (`IC41585`) is agent, power-of-attorney holder, notifier, stage customs agent and signatory, and the document prefix `TCB` is Tevaro's; importer/consignee Velumi (`IC41859`, `XL-TR-041859`) and consignor Lumeway (`20410274`) match 14 and 15; the customs party `IC41448` matches the manifest, its contact (import office) fits; Lisavu addresses carry `en-XL` and Lisavan renderings; manufacturer Valdara (`XU-R-104274`) consistent; ISIC codes fit (parties).
- The note "Duties paid by the importer's account at customs" agrees with the power of attorney's scope (context, money).

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.`: contradiction with the bill of lading's disbursement terms (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DisbursementPaymentTerms/cbc:Note` = `Island customs fees advanced by the broker and recharged to the consignee.`) — refuted: duties and the broker's advanced fees are different amounts (from broad, money).
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`: an exit office in an import declaration — refuted: it is the only customs office element the UBL 2.5 ImportCustomsDeclaration has, and the export exit office is a true and usable reference (from broad, context; see F12 for what is missing).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`: value without freight under CIF — refuted by broad (freight given separately, customs builds the CIF value); not followed by the merge, carried as counter-argument in F6 (from broad).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Ocean freight, share of the benches`: freight in an import declaration as unused data — refuted: freight to the place of entry is part of a CIF-based customs value (from context).
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `BF-CD-26-0136`: a reference that does not resolve — refuted: it is the ID of the CustomsDeclaration inside `11-ExportCustomsDeclaration.xml` (from logistics).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`: the agent given twice — refuted: agent and power-of-attorney holder are different statements and agree (from parties; see F14).
- `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`: the broker as master-level contact — refuted: the broker is the party customs deals with (from parties).
- `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`: not customs-specific — refuted: ISIC 8411 covers duty collection (from parties).
- Missing duty and tax amounts — refuted: the UBL 2.5 ImportCustomsDeclaration has no duty or tax aggregates; customs makes the assessment (from money).

## Changed in the merge
- Added by the merge: F1 (emission triple, High), F8 (MANUFACTURING, Medium), F9 (CRADLETOGATE, Medium), F18 (GTIN prefix, Low/yes), F19 (world item number, Low/yes), aligned with the earlier flows' merges; no part raised them in this example.
- broad/F8 split: the customs authority's company attributes join parties/F1 in F4 (Medium, as all earlier flows); the importer contact joins parties/F5 in F13.
- broad/F5 (Low) → F7 (Medium), as context/F1 and logistics/F1: the code is the classification the declaration rests on, from the wrong country's list.
- logistics/F4 (Low) → F10 (Medium, as broad/F2): the invoice-line reference cannot be resolved and the customs value rests on it.
- broad/F6 Needs decision no → yes (F15), as context/F5 and parties/F4.
- context/F4 → F14: narrowed to the empty shipment stage, parties' refutations accepted.
- broad/F4, logistics/F5, money/F2 → F20: combined.
- broad/F1, logistics/F2 → F5: combined. broad/F7, context/F2 → F17: combined. parties/F6, money/F3 → F16: combined.

## Outside this review
- `15-Manifest.xml` and other examples of the flow (09–12, 14, 20) give the same 4106.4 kg as `Shipment/GrossWeightMeasure`; each belongs to its own review (from broad, logistics).
