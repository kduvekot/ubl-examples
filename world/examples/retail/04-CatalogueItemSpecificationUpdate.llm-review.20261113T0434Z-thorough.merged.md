# LLM review: 04-CatalogueItemSpecificationUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/04-CatalogueItemSpecificationUpdate.xml`, Git blob `bc08c5d7cc1e9ec6f62cb02c0b6ddfcd217352bc` (committed)
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

### retail/04#F1 · High · Reference to the catalogue: wrong issue time, a revision after this document, and the superseded version
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:VersionID` = `1.0`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueTime` = `09:01:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionDate` = `2026-04-20`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:VersionID` = `1.1`
- Why: in a CatalogueReference `IssueTime` is "The time at which the catalogue was issued", `RevisionDate`/`RevisionTime` "The date/time on which the information in the catalogue was last revised" and `VersionID` "An identifier for the current version of the catalogue". Verified: the catalogue was issued at 17:28 (09:00 is 02's revision time); the last revision given, 2026-05-21 14:00, is five hours after this document was issued (2026-05-21 09:01) and matches neither 02 (2026-04-20 09:00) nor 03 (2026-05-20 14:00); and after 03 the current version is 1.1, not 1.0. The reference thus describes no catalogue version consistently. The same values recur in 03 and 20 (03#F2).
- Condition: the reference gives 02's issue time 17:28, a last revision and a version that belong to one catalogue version as it stood when this document was issued (after 03: 1.1), and nothing later than this document's issue.
- Options: (a, preferred) issue time 17:28:00, revision of version 1.1 (2026-05-20, with a time before 03's issue once 03#F1 is fixed), VersionID 1.1; (b) reduce the reference to ID, UUID and issue date.
- Needs decision: no
- From: broad, logistics, context

### retail/04#F2 · High · Emission factor and base do not give the stated emission
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: as 02#F1: the factor is "used to calculate the value measurement (e.g., emissions per unit of activity)"; recomputed, 0.82 × 1 EA = 0.82 kg, not 96 kg; 0.82 × 56.5 kg of materials = 46.3; 96 / 0.82 = 117.1. 39 files carry the triple (verified).
- Condition: `ValueMeasure` = factor × activity quantity in the base's unit, or factor and base absent.
- Options: (a, preferred) drop factor and base (an LCA product total); (b) an activity and unit that multiply out to 96 kg.
- Needs decision: no
- From: broad, logistics, context

### retail/04#F3 · Medium · A language code in LocaleCode
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats the language code. 362 occurrences in 213 files (verified).
- Condition: every `LocaleCode` holds a locale from a locale list, or is absent.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale listID (context's preference).
- Needs decision: no
- From: broad, parties, context

### retail/04#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is a vehicle access detail. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it; (b) record it in Bayvarra's address format.
- Needs decision: no
- From: broad, parties

### retail/04#F5 · Medium · Update about new slat wood that does not state the new wood in its structured data
- XPath: `/CatalogueItemSpecificationUpdate/cbc:Name` = `New slat wood for the Serra 180`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description` = `Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried hardwood, for bolting to the ground.`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ResourceOriginDescription` = `Slats from Upland State, Bayvarra`
- Why: the document is "used to update information (e.g., technical descriptions and properties) about Items in an existing Catalogue", and its whole purpose is the new slat wood. Only the free-text description says "another kiln-dried hardwood", without naming it; the "Slat wood" property, the hardwood consumption (22.5 kg from Upland State, measured over 2025), the emission and every identifier are those of 02 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`, verified). A receiver comparing structured data sees no change; a different hardwood (density about 550 to over 900 kg/m³, own knowledge) would also change the 22.5 kg of slats. Medium: information the document's purpose depends on is missing.
- Condition: the structured property that describes the slats names the new wood, and the figures that depend on it (hardwood mass, origin, footprint) are updated or stated to be unchanged for a reason.
- Options: (a, preferred) name the new wood in the "Slat wood" property and the description, and update or confirm the dependent figures; (b) if only the source of the same wood changes, say that instead of "another hardwood".
- Needs decision: yes (which wood replaces the old one is part of the story)
- From: broad (Medium), logistics (Low), context (Medium)

### retail/04#F6 · Medium · Life-cycle stage "manufacturing" for a footprint from the mine to the factory gate
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: as 02#F7: the description covers raw-material extraction, transport and manufacturing; the code names manufacturing only, so code and text equivalent disagree.
- Condition: code and description name the same scope.
- Options: (a, preferred) omit the code (or a code for the whole cradle-to-gate scope if the list gets one); (b) two emission entries; (c) a description limited to manufacturing.
- Needs decision: no
- From: context (Low)

### retail/04#F7 · Medium · A system-boundary code in the fullness indication
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: as 02#F8: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle boundary. 39 files (verified).
- Condition: a fullness code for transport equipment, or no element.
- Options: (a, preferred) drop it and keep the scope in the description; (b) record the missing boundary element for the TC.
- Needs decision: no
- From: context

### retail/04#F8 · Low · The revision date and time are those of the pricing update, and the validity starts the day before the issue
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueDate` = `2026-05-21`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:RevisionDate` = `2026-05-20`
- Why: this document makes version 1.2, but gives the same revision date and time as the pricing update 03, which made version 1.1. Two revisions of the same catalogue at the same moment mean either one revision (one version too many) or a copied time. The `ValidityPeriod` ("during which the information in the Catalogue Revision is effective") starts on 2026-05-20, the day before the new wood was announced, without a reason. Not Medium (context): taken alone, a revision made on 20 May at 14:00 and sent the next morning at 09:01 is plausible, and broad accepted a validity from the revision date; the impossible time is 03's (issued 13:10 with a 14:00 revision, 03#F1), so the clash may be resolved there.
- Condition: version 1.2 has its own revision date and time, after that of 1.1 and not later than this document's issue; the validity starts no earlier than the issue date unless a note gives the reason.
- Options: (a, preferred) revision on 2026-05-21 before 09:01 and validity from 2026-05-21; (b) keep 2026-05-20 14:00 for this revision, give 03 an earlier one, and add a note why the new wood applies from 20 May.
- Needs decision: no
- From: broad (Low), logistics (Low), context (Medium)

### retail/04#F9 · Low · Signature without anything that signs
- XPath: `/CatalogueItemSpecificationUpdate/cac:Signature/cbc:ID` = `LD-SIG-26-1.2`
- Why: only an ID and a signatory, no method or attachment; nothing a receiver could check, and no story reason for a signature (IND5/IND6). 137 of 147 signatures in the world have this shape (lxml). The ID is built from the document's version 1.2 (broad noted this as consistent).
- Condition: either a signature with a reason and its data, or none.
- Options: (a, preferred) drop it; (b) method and attachment with a reason, ID from Lumeway's own numbering.
- Needs decision: yes (world-wide convention, as in the air and utilities merges)
- From: context (signature part of its F8)

### retail/04#F10 · Low · Party master data the item update does nothing with
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- Why: a domestic item specification update uses no customs trader number, share capital, logo, consumer web shop, social-media profile or tax registration (it states no price or tax, money checked); master data (section 4.8). `CorporateStockAmount` holds share capital where UBL defines "The number of shares in the capital stock of a corporation": TC write-up note.
- Condition: the parties carry only what the update uses.
- Options: (a, preferred) leave them out; (b) keep share capital only where company law needs it and record the conflict for the TC.
- Needs decision: no
- From: parties (F4, F5, F6), context (F8, master-data part)

### retail/04#F11 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: name and e-mail fit a buyer; job title and department are a seller's customer service. Same contact in 41 files (verified).
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title in purchasing.
- Needs decision: no
- From: broad, parties

### retail/04#F12 · Low · Trading terms that say only "Unchanged."
- XPath: `/CatalogueItemSpecificationUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- Why: as 03#F9: "Unchanged." describes no term; an update of the slat wood has nothing to do with trading terms (money, context); broad refuted it (the explicit statement avoids implying by absence, IND6). Only 03 and 04 carry the value (verified).
- Condition: no `TradingTerms`, or terms that apply; the reading of IND5/IND6 for updates documented.
- Options: (a, preferred) remove `TradingTerms`; (b) repeat the actual terms with LD-GTC-2026; (c) keep the explicit statement.
- Needs decision: yes
- From: money, context (broad refuted)

### retail/04#F13 · Low · Header contract parties repeated on the line
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the line's contract parties are those of the header's one contract; they add nothing.
- Condition: line-level contract parties only where they differ from the header.
- Options: (a, preferred) drop them.
- Needs decision: no
- From: broad, context

### retail/04#F14 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: as 02#F16: the GTIN of Valdara's bench is under Lumeway's company prefix 9520610; the brand owner allocates GTINs from its own prefix (own knowledge of the GS1 rules).
- Condition: Valdara's GTINs and Lumeway's keys are under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a Valdara prefix; (b) state that the distributor allocated it.
- Needs decision: yes
- From: parties

### retail/04#F15 · Low · World item number that is a valid GTIN-12
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: as 02#F21: valid GS1 check digit (recomputed), GS1 US prefix 077 when read as a GTIN; can be mistaken for a real GTIN.
- Condition: world item numbers cannot be read as valid GTINs, or their non-assignment is recorded.
- Options: (a, preferred) a non-GTIN format for the world item scheme; (b) record the verification.
- Needs decision: yes
- From: added by the merge (aligned with earlier flows)

### retail/04#F16 · Low · Urvanian customs tariff code in a Bayvarran domestic catalogue update
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: as 02#F22: Urvania's national tariff, which neither Bayvarran party uses in this trade. Context's refutation (goods imported from Urvania; the world has only the XU tariff list, all 61 tariff codes) carried: it explains the absence of a Bayvarran code, not the presence of the Urvanian one.
- Condition: national tariff codes are those of a customs territory the parties deal with, or absent.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (context refuted)

## Checked and consistent
- Update line `1` is the bench's catalogue line in 02 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10442`); seller's ID, GTIN `9520610000012` (check digit correct) and manufacturer's ID `VI-B180` agree with 02.
- Dimensions (1800 × 620 × 780 mm, seat height 450 within 440–460), load capacity, warranty, HS `940179`, transaction conditions and document references agree with 02.
- `RelatedCatalogueReference` ID, UUID and issue date match 02; `VersionID` 1.2 follows 03's 1.1; validity end 2026-07-19 as the catalogue; `LineCountNumeric` 1.
- No price, allowance or tax data, as fits an item specification update; the price stays 520 (money).
- Parties described as in every retail example; GLN check digits correct.

## Considered and refuted
- `/CatalogueItemSpecificationUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`: retroactive start — refuted by broad (validity from the revision date is plausible); partly not followed, part of the Low F8 (from broad).
- `/CatalogueItemSpecificationUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`: filler — refuted by broad; kept as the Low/yes F12 with both readings (from broad).
- `/CatalogueItemSpecificationUpdate/cbc:VersionID` = `1.2`: skips a version — refuted, 03 made 1.1 (from logistics).
- `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`: Urvanian tariff code — refuted by context; not followed, F16 (from context).
- `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description`: fuller than the catalogue's — refuted, a fuller technical description is what the update is for (from context).
- `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse — refuted (from parties).

## Changed in the merge
- broad/F2, logistics/F1, context/F1 → F1; broad/F1, logistics/F2, context/F2 → F2: combined.
- broad/F3 (Medium), logistics/F3 (Low), context/F3 (Medium) → F5: Medium (the purpose of the update depends on the missing information).
- context/F7 (Low) → F6: raised to Medium, as 02#F7 and the earlier flows' merges.
- broad/F6 (Low), logistics/F4 (Low), context/F4 (Medium) → F8: Low (see Why).
- context/F8 split into F9 (signature; "Needs decision" no → yes), F10 (master data, with parties/F4, F5 (Low/yes → no), F6), F12 (with money/F1; no → yes) and F13 (with broad/F9).
- F15 added by the merge for consistency with 02 and the earlier flows.
- broad/F4, parties/F1, context/F6 → F3; broad/F5, parties/F2 → F4; broad/F8, parties/F7 → F11: combined.
