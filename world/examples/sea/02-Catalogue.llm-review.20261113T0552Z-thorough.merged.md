# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/02-Catalogue.xml`, Git blob `9ab014c2e27df7270bfea2ec3db014a3637bf54d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/02#F1 · High · Sales territory Bayvarra, but the same price is exempt as an export outside Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- Why: `ApplicableTerritoryAddress` is "The applicable sales territory" of the item location quantity, and `ApplicableTaxCategory` "A tax category applicable to this item location quantity". In both lines the same block says the price applies to sales in Bayvarra and that the Upland State sales tax is not charged because of an export outside Bayvarra (category G, 0 %). A sale inside the territory Bayvarra is not an export. The receiver, Velumi Trading, is on Lisavu (`/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`), and the flow treats the sale as an export (`05-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`; `22-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`), so it is the territory that does not fit. The merge tried the reading "territory = where the seller sells from" and rejected it: the definition says sales territory, and the delivery is CIF Port of Selanu (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`).
- Condition: in each `RequiredItemLocationQuantity`, territory and tax category agree: a territory outside Bayvarra with the export exemption, or Bayvarra with the domestic tax.
- Options: (a) preferred: territory `XL` (Lisavu), keeping the export exemption the rest of the flow uses; (b) two item location quantities, Bayvarra with state sales tax and Lisavu with the exemption, if the catalogue serves both.
- Needs decision: no (logistics said yes; the fix keeps the flow's tax treatment, so the story does not change)
- From: broad (F1), money (F1), context (F1), logistics (F2, Low)

### sea/02#F2 · High · Emission value is not factor × base
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". Recalculated: 0.82 × 1 EA = 0.82, not 96 kg CO2e. No other quantity of the item closes the gap: 96 / 0.82 = 117.1; the material input 34 kg steel + 22.5 kg hardwood = 56.5 kg gives 0.82 × 56.5 = 46.3; the packing list's net weight is about 38 kg per bench (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762` for 96 benches and 12 frames). The value 96 kg itself is plausible for about 34 kg of galvanised cast steel plus sawing and transport (logistics, own knowledge). The same triple occurs in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure` in the stated units, or factor and base are absent.
- Options: (a) preferred: drop factor and base and keep 96 kg per bench as the value (a product footprint from the LCA `VI-LCA-2025`, not one factor), as in all earlier flows; (b) a factor on a real activity base (e.g. per kg of steel, base in KGM) whose product is 96; (c) factor 96 per 1 EA (broad's preference).
- Needs decision: no
- From: broad (F2), logistics (F1), context (F2)

### sea/02#F3 · Medium · A language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `/Catalogue/cac:ProviderParty/cac:Language/cbc:ID` = `en` and names no locale. 362 such elements in 213 examples of the world (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or a locale (language with region) from a locale list.
- Options: (a) preferred: drop it, as in all earlier flows; (b) `en-XB` from a list of language tags (broad's and context's preference).
- Needs decision: no
- From: broad (F7), parties (F1), context (F6)

### sea/02#F4 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate of a business park is not a street name and has no use in a postal address. 79 occurrences in 76 examples of the world, 25 in this flow (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate; where a truck needs it, a delivery, pickup or despatch location carries it.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F8), parties (F2), context (F12, Low)

### sea/02#F5 · Medium · Price list status "Active" where the element names original, copy, revision or cancellation
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- Why: `PriceList/StatusCode` is "A code signifying whether this price list is an original, copy, revision, or cancellation". "Active" comes from the world's `RecordStatusCode` list and is a life-cycle state (in force), which the price's `ValidityPeriod` already gives (2026-05-04 to 2026-10-31); it is none of the states the definition names. A code from a list meant for another kind of status is a value with another meaning (section 6, Medium).
- Condition: `StatusCode` holds one of the kinds the definition names, from a list that has them, or is absent.
- Options: (a) preferred: a value meaning "original" (first issue of `LD-PL-2026`); (b) drop it.
- Needs decision: no
- From: money (F3, Low), context (F5)

### sea/02#F6 · Medium · "Full container" discount attached to the whole quantity range from 4 benches
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `4`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- Why: the allowance is "An allowance or charge associated with this item location quantity", and the block applies from `MinimumQuantity` 4 to `MaximumQuantity` 192 ("the minimum/maximum quantity that can be ordered to qualify for a specific price"). As encoded, every order of 4 to 192 benches qualifies for 3 %; the condition "Full container" cannot be read or checked, and a pallet of four is not a full container. The flow shows it: Velumi orders 96 benches (within 4–192) that travel in one 40-foot container, and the order, order response and invoice all price the bench at 520 without the allowance (`05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`, `22-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `520`). Recalculated: 0.03 × 520.00 = 15.60 per bench, 96 × 15.60 = 1,497.60 XBL that would be missing downstream if the encoded range applied. Logistics' figures make "not full" the likely reading (41.5 m³ gross for 96 benches against about 67.7 m³ inside a 40-foot box). Not High, because the reason text can be read as the condition, so the order does not contradict an unambiguous statement.
- Condition: the quantity (or other condition) at which the "Full container" allowance applies can be read from the catalogue, and order, order response and invoice are consistent with it.
- Options: (a) preferred: a separate `RequiredItemLocationQuantity` for full-container orders with its own `MinimumQuantity` and the allowance only there, the range 4–192 without it; (b) one range, with the full-container quantity stated in the allowance, checked against the 96 benches.
- Needs decision: no
- From: money (F2); context's "Considered and refuted" (conditional discount legitimate, expression a money question) and logistics' `MaximumQuantity` refutation carried as context

### sea/02#F7 · Medium · CatalogueIndicator "ordered from a catalogue" in the catalogue itself
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: `CatalogueIndicator` is "An indicator that this item was ordered from a catalogue (true) or not (false)". In a catalogue nothing has been ordered; the indicator belongs to an ordered item. In this flow it occurs only here (`grep -c CatalogueIndicator world/examples/sea/*.xml`), not in 05-Order, which does order from this catalogue. The merge tried the reading "orderable from a catalogue" and rejected it: the definition is in the past tense of an order.
- Condition: no `CatalogueIndicator` in the catalogue lines.
- Options: (a) preferred: drop it here; if wanted, put it on the ordered item in 05-Order.
- Needs decision: no
- From: broad (F5), context (F4)

### sea/02#F8 · Medium · A province in Region (Codana Identification Agency)
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country …, such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran address of the same document uses (`/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano<'`).
- Condition: the province of an Urvanian address is in `CountrySubentity` (with `CountrySubentityCode` where the world has one), not in `Region`.
- Options: (a) preferred: move it to `CountrySubentity` in every Urvanian address.
- Needs decision: no
- From: broad (F6), parties (F3), context (F7)

### sea/02#F9 · Medium · LifecycleStageCode MANUFACTURING for a footprint from the ore at the mine
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". The description and `Description` ("Mining, steel making, casting, galvanising, sawing and the transport between them") cover raw-material extraction, transport and manufacturing, i.e. the whole product stage, while the code names manufacturing only; code and text equivalents disagree (section 4.4). The broad part refuted this (cradle-to-gate is the production stage, which "Manufacturing" can name); every earlier flow's merge kept it as Medium (road, rail, air, retail, sea b/c), because in life-cycle practice (EN 15804 A1–A3, own knowledge) raw-material supply is a stage of its own.
- Condition: the lifecycle stage code covers what the description says (raw material supply to factory gate), or the description is limited to manufacturing.
- Options: (a) preferred: a code for the product stage / cradle-to-gate from the world's lifecycle list (adding it if needed); (b) keep `MANUFACTURING` and let the description say that it includes upstream supply.
- Needs decision: no
- From: broad (Considered and refuted); made a finding in the merge, aligned with earlier flows

### sea/02#F10 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." Cradle-to-gate is the system boundary of a product footprint, from the world's `EmissionBoundaryCode` list; a bench in a catalogue has no transport equipment. The boundary is already in `LifecycleStageDescription`. 39 `FullnessIndicationCode` elements in the world carry `CRADLETOGATE` (context, `grep -rho --include='*.xml'`).
- Condition: `FullnessIndicationCode` is absent from product emissions, or holds a fullness code of transport equipment.
- Options: (a) preferred: drop it; (b) note the definition's narrowness in the TC write-up if a boundary code was intended.
- Needs decision: no
- From: broad (F3), context (F3)

### sea/02#F11 · Medium · The bench's spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:ItemClassificationCode` = `42999`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the item is a "Spare side frame for the Serra bench" (`/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Description`), made for that seat only. In the HS, Section XV Note 1 excludes articles of Chapter 94, and identifiable parts of seats go to heading 9401 (subheading 9401.99, parts other than of wood); 7325.99 is for other cast articles that are not parts of a particular article (own knowledge of HS 2022). The context part listed 732599 as fitting; the merge follows broad (a cast part made for one seat model is not a casting of general use) and aligns with sea merger b. The same 732599 occurs in 22 examples (`grep -l 732599 world/examples/*/*.xml`).
- Condition: HS, national tariff and CPC codes classify the side frame as a part of a seat of heading 9401, or the item is described as a casting of general use.
- Options: (a) preferred: HS 940199 with the matching national tariff and CPC codes (the world's lists may need the entries); (b) none better seen.
- Needs decision: no
- From: broad (F4); context (Checked and consistent) disagreed

### sea/02#F12 · Low · Velumi Trading described differently from the documents it issues (en-XB tags, legal form only in English)
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: the English renderings of Velumi's address in Lisavu are tagged `en-XB` and its legal form is given once, in English; in the order Velumi issues the same party has `en-XL` and its legal form in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`, `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The flow splits along the issuer (16 sea examples `en-XB">Reef Street`, 8 `en-XL">Reef Street`, `grep -c`). The same address of the same party should be described the same way; whether the tag follows the issuer is a world convention not documented anywhere the review may read.
- Condition: Velumi's postal address, registration address and legal form carry the same renderings and `languageID` values in every example of the flow, following one documented rule.
- Options: (a) preferred: `en-XL` and the legal form in both languages everywhere, as in 05-Order.xml; (b) a documented rule that the tag is the issuer's variety, with the Lisavan legal form still given.
- Needs decision: yes
- From: broad (F13, Low/no), parties (F4)

### sea/02#F13 · Low · Receiver's legal entity and address copied into a catalogue that does not use them
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `LTD`
- Why: the catalogue offers items to Velumi; nothing in it depends on Velumi's legal form, size, registration or registered address. Master data copied into a document that does not use it (section 4.8).
- Condition: `ReceiverParty` carries identification, name, contact and electronic address only, or the catalogue has a reason for the rest.
- Options: (a) preferred: reduce `ReceiverParty`.
- Needs decision: no
- From: context (F11)

### sea/02#F14 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Velumi Trading (island register) and Codana Identification Agency (Urvanian commercial register) share the New Year's Day date with companies in all three registers: 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while parties with a history have their own (Lumeway `1988-10-03`). It reads as a default value (no fillers).
- Condition: every `RegistrationDate` is the party's date in the world, or absent.
- Options: (a) preferred: an own date per company; (b) drop it where the world has none.
- Needs decision: yes
- From: parties (F6)

### sea/02#F15 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver of a catalogue is reached through purchasing, which name and e-mail say; job title and department are a seller's customer service and repeat Lumeway's own (`/Catalogue/cac:ProviderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`).
- Condition: name, job title and department of Velumi's contact describe its purchasing function.
- Options: (a) preferred: a purchasing job title and department; (b) drop title and department.
- Needs decision: no
- From: broad (F11), parties (F5), context (F10)

### sea/02#F16 · Low · GTINs of the maker's Valdara items in Lumeway's GS1 company prefix
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:BrandName` = `Valdara`
- Why: both GTINs start with `9520610`, the company prefix of Lumeway's own GLN (`/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`), while the items carry the maker's brand `Valdara` and Valdara Industries is their manufacturer and information content provider. A GTIN is allocated by the brand owner from its own company prefix (GS1 General Specifications, own knowledge), so the numbers say the distributor owns the brand. No sea part raised it; added in the merge, aligned with retail a/b/c and sea b/d.
- Condition: the GTINs come from the company prefix of the brand owner, or the brand owner is Lumeway.
- Options: (a) preferred: GTINs under a Valdara company prefix (Valdara's own GS1 number in the 952 range); (b) a story in which Lumeway owns the brand.
- Needs decision: yes (who owns the brand)
- From: merge (no part)

### sea/02#F17 · Low · Full master data of the GTIN issuer in one catalogue line
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Codana Identification Agency SRU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `member@codana.example`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`
- Why: `IssuerParty` is "The Party who issues this Item Identification"; the catalogue needs at most its identity to qualify the GTIN. In line 1 Codana comes with VAT number, legal entity, contact, postal address and endpoint; in line 2 (and as issuer of the property identifier `UR-SF-0450`) the same party is given by ID and name only. The catalogue does nothing with the rest, and the two lines describe the same party differently (section 4.8).
- Condition: Codana is described the same way in both lines, with no tax, legal-entity or contact data the catalogue does not use.
- Options: (a) preferred: ID and name only, as in line 2; (b) only what lets the receiver reach the agency, the same in both lines.
- Needs decision: no
- From: broad (F9), parties (F7), context (F8)

### sea/02#F18 · Low · Romance exonym "Via dei Codici" tagged as Bayvarran English
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- Why: the rendering next to the Urvanian name is tagged as English as used in Bayvarra, but "Via dei Codici" is not English. The parties part refuted it (Urvanian exonyms are Italianate throughout the world, and the tag follows the same issuer convention as F12). That is a world convention not documented where the review can read it; earlier merges (road, rail, cotton, retail a) kept it as Low/yes.
- Condition: each rendering is in the language its `languageID` names, or the convention (English exonyms of Urvanian names are Italianate) is documented.
- Options: (a) preferred: document the convention with the en-XB/en-XL rule of F12; (b) an English rendering ("Codes Street") or a tag that fits the rendering.
- Needs decision: yes
- From: parties (Considered and refuted); made a finding in the merge, aligned with retail a

### sea/02#F19 · Low · Codana's contact: a private agency's member services described as public services
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `SRU`
- Why: Codana is a private limited company (SRU) and its contact is named "Member services", but job title and department are those the world gives to public authorities (the same pair for the Trade Accord Council and the customs services, parties). Name, title and department disagree. Retail a set "Codana's nature" to needs decision yes; here the preferred fix (dropping the contact with F17) needs no decision on what Codana is.
- Condition: name, job title and department agree with each other and with the kind of party, or the contact is absent.
- Options: (a) preferred: drop the contact (with F17); (b) a member-services title and department.
- Needs decision: no
- From: broad (F10), parties (F8)

### sea/02#F20 · Low · World item numbers that are valid GTIN-12s
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: the world's item numbers (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 check digit (recalculated: the first eleven digits of 771020000027 give check digit 7, those of 771020000034 give 4) and start with 7, a range of GS1 US company prefixes (own knowledge). They could be mistaken for real GTIN-12s, against the rule "fictional values must not be mistaken for real ones". No sea part raised it; added in the merge, aligned with rail, road, plastics, retail and sea b/d. Whether these numbers are assigned could not be checked (no GEPIR access).
- Condition: world item numbers cannot be read as valid GTINs (different length or invalid check digit), or are verified as unassigned.
- Options: (a) preferred: change the world's item-number format; (b) record a verification.
- Needs decision: yes (world-wide scheme)
- From: merge (no part)

### sea/02#F21 · Low · Spare part priced as a percentage of the bench, and the percentage does not give the price
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`
- Why: `Percent` is "The percentage by which the price of the different item is multiplied to calculate the price of the item". Recalculated: 520 × 12.31 % = 64.012 → 64.01 XBL at the currency's two decimals (the catalogue writes amounts with two decimals, e.g. `15.60`), not 64.00; 64 / 520 = 12.3077 %, so the percentage is back-calculated from the price rather than the rule it follows. The money part refuted this (rounding; a two-decimal percent cannot be more exact), but `Percent` may carry more decimals, and the spare has its own price, so the dependency has no reason in the catalogue.
- Condition: either the spare's price is stated without a dependency, or 520 × `Percent` / 100 = the price at the currency's precision.
- Options: (a) preferred: drop `DependentPriceReference`; (b) a percentage that yields the price exactly (12.3077) or a round rule from which the price is derived.
- Needs decision: no
- From: broad (F12), context (F9); money (Considered and refuted, counter-argument above)

## Checked and consistent
- GTINs `9520610000012`, `9520610000029` and GLN `9520610900008` pass their check digits (`check_ids.py`); prefix 952 is GS1's demonstration range.
- Line 1 allowance recalculated: 0.03 × 520.00 = 15.60 = `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:Amount` = `15.60`.
- Alternative currency prices recalculated: 520 × 0.4 = 208 (`/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `208`), 64 × 0.4 = 25.6 (`/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `25.6`); 0.4 is the flow's rate (`22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`).
- Prices 520 and 64 XBL and the tax category (G, 0 %, EXP, STT) are those of the order, order response and invoice.
- Catalogue and price validity 2026-05-04 to 2026-10-31; delivery period from 2026-05-11; lead time 3 days; the order of 2026-05-07 and the shipment of 2026-05-14 lie within them.
- Minimum quantity 4, batch quantity 4, package `PAL-4` of 4 and "per pallet of four benches" agree; 96 benches is a multiple of 4 within 4–192; the bill of lading's bench pallets carry 4 each (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity` = `4`).
- Physics: 34 kg steel + 22.5 kg hardwood consumed per bench against about 38 kg net per bench in the packing list: plausible with casting and sawing yields of about 0.7 and 0.6 (logistics, own knowledge); 0.4 kg film and straps per bench plausible.
- HS 940179 (seats with metal frames, other) for the bench fits HS 2022 (own knowledge). Dimensions are the same in the order, packing list and export declaration.
- Manufacturer and information content provider of both items are Valdara Industries (`XU-R-104274`), as everywhere in the flow; Codana is described as in `retail/02-Catalogue.xml`.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`: generic "Discount" / wrong list — refuted because the entry is an allowance (`ChargeIndicator` false) and 95 is the UN/EDIFACT 5189 allowance code, the reason text naming the condition (from broad, money).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:AlternativeCurrencyPrice/cbc:PriceAmount` = `208`: a fixed alternative price over six months ignores rate changes — refuted because it is a stated price in its own right ("the price expressed in an alternative currency") and the rate is constant across the flow (from money).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192` as "one full container" (192 benches would need about 83 m³ against about 67.7 m³ inside a 40-foot box) — refuted because nothing ties the maximum to one container (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180` and the other item document references resolve to no example — refuted: each sits in an element that names what it is (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty`: a GTIN is allocated by the brand owner, so the issuer could be Valdara — refuted for the issuer element: the world's convention is "GS1 / ISO via Codana", Codana acting as numbering organisation; "The Party who issues this Item Identification" fits it (from parties). (The prefix question is F16.)
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription`: packaging waste per bench with a 2025 measurement period — refuted: the period is when the waste per bench was measured (from context).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cac:StandardPropertyIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`: the identification agency as issuer of a property identifier — refuted: an agency running item identification can also run a property dictionary (from context).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason`: a "full container" discount in a catalogue — refuted by context within its lens (conditional discounts are legitimate catalogue content); the money question is F6.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode`: refuted by broad — not followed, see F9.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]`: refuted by parties — not followed, see F18.
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent`: refuted by money — not followed, see F21.

## Changed in the merge
- broad/F1, money/F1, context/F1, logistics/F2 → F1: logistics' Low/yes raised to High/no with the three other parts (the fix keeps the flow's tax treatment).
- broad/F2, logistics/F1, context/F2 → F2: preferred option set to dropping factor and base (logistics, context, earlier flows); broad's "factor 96 per EA" kept as option (c).
- broad/F7, parties/F1, context/F6 → F3: preferred option set to drop (broad and context preferred a locale), aligned with all earlier flows.
- context/F12 → F4: Low raised to Medium, aligned with broad, parties and earlier flows.
- money/F3 → F5: Low raised to Medium with context (a code from a list for another kind of status).
- broad's refutation of MANUFACTURING → F9 (Medium/no), aligned with earlier flows.
- broad/F13 (no) + parties/F4 (yes) → F12: grouped, needs decision yes.
- broad/F9, parties/F7, context/F8 → F17: grouped.
- parties' refutation of "Via dei Codici" → F18 (Low/yes), aligned with retail a.
- broad/F10, parties/F8 → F19: grouped; preferred option set to dropping the contact (parties), which makes the decision on Codana's nature unnecessary.
- F16 (GTIN prefix) and F20 (GTIN-like world item numbers) added by the merge, aligned with retail and sea b/d.
- money's refutation of the dependent percentage not followed → F21.

## Outside this review
- The catalogue (issued 2026-05-04 09:17) precedes the business card it would normally follow (01-BusinessCard.xml, issued the same day 16:39): a timeline question across documents (from context).
