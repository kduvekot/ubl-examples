# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/02-Catalogue.xml`, Git blob `9ab014c2e27df7270bfea2ec3db014a3637bf54d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/02#F1 · High · Sales territory Bayvarra, but the price is taxed as an export outside Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- Why: `ApplicableTerritoryAddress` is "The applicable sales territory" of the price, tax and quantity conditions in the same `RequiredItemLocationQuantity`. Both lines restrict them to Bayvarra, yet the tax category is `G` ("Free export item, tax not charged") with the exemption "Export outside Bayvarra". A sale inside Bayvarra is not an export, and a sale to the catalogue's receiver Velumi Trading in Lisavu (`/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`) is outside the stated territory. Territory and tax treatment contradict each other.
- Condition: in each line, the territory of the item location quantity and its tax category agree (export exemption only for a territory outside Bayvarra, e.g. Lisavu).
- Options: (a) preferred: territory `XL` (the receiver's country, where the export price applies); (b) keep `XB` and give the Bayvarran sales tax category instead, with a second item location quantity for export.
- Needs decision: no

### sea/02#F2 · High · Emission value is not factor × base
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". 0.82 × 1 EA = 0.82, not 96 kg. No other quantity of the item gives 96 either: the stated material is 34 kg steel + 22.5 kg hardwood = 56.5 kg (`/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure`, `…[2]`), and 0.82 × 56.5 = 46.3. The same 96 / 0.82 / 1 EA occurs in 39 examples (`grep -l "<cbc:ValueFactorNumeric>0.82" world/examples/*/*.xml`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure` (in consistent units), or the factor and base are absent.
- Options: (a) preferred: factor 96 kg CO2e per 1 EA (the emission per bench); (b) a factor per kg of material with the material mass as base, if the LCA works that way; (c) drop factor and base.
- Needs decision: no

### sea/02#F3 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." It belongs to transport emissions. A product's cradle-to-gate LCA boundary is something else, and the code comes from a list of emission boundaries (`EmissionBoundaryCode`), not of load factors. The same code in this element occurs in 39 examples (`grep -l 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"' world/examples/*/*.xml`).
- Condition: `FullnessIndicationCode` is absent from product emissions, or holds a fullness code of transport equipment.
- Options: (a) preferred: drop it; the boundary is already stated in `LifecycleStageDescription`; (b) state the boundary in `EmissionCalculationMethod`'s text or in the method code if the world's list has one.
- Needs decision: no

### sea/02#F4 · Medium · The bench's spare side frame classified as a general cast article, not as a part of a seat
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:ItemClassificationCode` = `42999`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the item is a "Spare side frame for the Serra bench", made for that seat only. In the HS, Section XV Note 1 excludes articles of Chapter 94, and parts of seats go to heading 9401 (subheading 9401.99, parts other than of wood); CPC has the matching class for parts of seats (own knowledge of HS 2022 and CPC 2.1). 7325.99 ("Other cast articles of iron or steel") is for castings that are not parts of a particular article. The same 732599 occurs in 22 examples (`grep -l 732599 world/examples/*/*.xml`).
- Condition: HS, national tariff and CPC codes of the side frame classify it as a part of a seat of heading 9401, or the item is described as a casting of general use.
- Options: (a) preferred: HS 940199 with the matching national tariff and CPC codes (code lists of the world may need the entries); (b) none better seen.
- Needs decision: no

### sea/02#F5 · Medium · CatalogueIndicator in a catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: `CatalogueIndicator` is "An indicator that this item was ordered from a catalogue (true) or not (false)". It describes an item as ordered (in an order, despatch or invoice line). In the catalogue itself nothing has been ordered; the value says nothing the document type does not already say.
- Condition: catalogue items carry no `CatalogueIndicator`.
- Options: (a) preferred: drop it here, keep it in the order and follow-up documents; (b) none better seen.
- Needs decision: no

### sea/02#F6 · Medium · Province in Region
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a "political or administrative division of a country", i.e. `CountrySubentity`, which the Bayvarran addresses of the same document use (`/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). `Region` = "Province of Ferrano" occurs in 104 examples (`grep -c "<cbc:Region>Province of Ferrano" world/examples/*/*.xml`, files with a count above 0).
- Condition: the province of an Urvanian address is in `CountrySubentity` (with `CountrySubentityCode` where the world has one), not in `Region`.
- Options: (a) preferred: move it to `CountrySubentity`; (b) none better seen.
- Needs decision: no

### sea/02#F7 · Medium · Language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is the language again (`Language/ID` = `en`), not a locale. The document itself writes the Bayvarran locale as `en-XB` in `languageID` attributes. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/02#F8 · Medium · A gate in AdditionalStreetName
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate of a business park is not a street name and has no place in a postal address. Same value in 25 of 29 sea examples (`grep -c "Gate 3" world/examples/sea/*.xml`).
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address; give the gate in a delivery or pickup location where a document needs it.
- Needs decision: no

### sea/02#F9 · Low · Full master data of the identification agency inside an item identification
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105644`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- Why: the issuer of the GTIN is given with its tax registration, legal entity, contact and electronic address, while the same issuer in line 2 is identified by ID and name only (`/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`). The catalogue does nothing with the agency's tax scheme or legal form; it looks copied from master data.
- Condition: the issuer party of an item identification carries only what identifies the issuer, unless the catalogue has a use for more.
- Options: (a) preferred: identification and name, as in line 2; (b) none better seen.
- Needs decision: no

### sea/02#F10 · Low · Public-service contact of a private company
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- Why: Codana is a private limited company (`/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `SRU`) whose contact is named "Member services"; job title and department of a public body do not fit it or the name.
- Condition: job title and department agree with the contact's name and the kind of party.
- Options: (a) preferred: e.g. "Member services officer" / "Member services"; (b) drop the contact with F9.
- Needs decision: no

### sea/02#F11 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver of a catalogue is reached through purchasing, which the name and e-mail say; job title and department are those of a seller's customer service. Same values in every sea example with this contact.
- Condition: name, job title and department of Velumi's contact describe the same function.
- Options: (a) preferred: purchasing job title and department.
- Needs decision: no

### sea/02#F12 · Low · Dependent price percentage does not give the stated price
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`
- Why: `Percent` is "The percentage by which the price of the different item is multiplied to calculate the price of the item". 520 × 12.31 % = 64.01 XBL, not 64; the percentage looks back-calculated from the price (64 / 520 = 12.3077 %) rather than being the rule the price follows.
- Condition: price of line 1 × `Percent` / 100 = price of line 2 (to the currency's precision), or no dependent price reference.
- Options: (a) preferred: drop the dependent price reference, since the side frame has its own price; (b) a percentage that yields the price exactly.
- Needs decision: no

### sea/02#F13 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the English renderings of Velumi Trading's address in Lisavu are tagged `en-XB` (English as used in Bayvarra), while the same address of the same party is tagged `en-XL` in the documents Velumi sends itself (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`). Across the sea flow the tag follows the sender's country rather than the address: `en-XB` in 16 examples, `en-XL` in 8 (`grep -c 'languageID="en-XB">Reef Street'` and `'languageID="en-XL">Reef Street'` over `world/examples/sea/*.xml`). The same rendering of the same address should carry the same language tag; for a Lisavu address `en-XL` is the natural one.
- Condition: Velumi's address renderings carry the same `languageID` in every example of the flow.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere; (b) a world-wide rule that the tag is the sender's locale, stated where the world documents its conventions.
- Needs decision: no

## Checked and consistent
- GTINs `9520610000012`, `9520610000029` and GLN `9520610900008` have correct check digits (`check_ids.py`).
- Line 1 allowance: 520.00 × 0.03 = 15.60 XBL = `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:Amount`.
- Alternative currency prices use the same rate in both lines: 520 → 208 XLC and 64 → 25.6 XLC (0.4).
- Price validity, catalogue validity and delivery period fit each other (2026-05-04 / 2026-05-11 to 2026-10-31); lead time 3 days fits the delivery period start.
- Minimum quantity 4, batch quantity 4, pallet of 4 and the transaction condition "per pallet of four benches" agree; 192 maximum = 48 pallets.
- Physics: 34 kg steel + 22.5 kg hardwood = 56.5 kg per bench for 1800 × 620 × 780 mm with cast steel side frames: plausible (own estimate); 0.4 kg film and straps per bench plausible.
- HS 940179 for a park bench with a metal frame fits HS 2022 (own knowledge).

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`: the stage seemed narrower than the cradle-to-gate description — refuted because cradle-to-gate is the product (production) stage including raw materials, which "Manufacturing" can name.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`: generic "Discount" for a full-container discount — refuted because 95 is a valid general code and the reason text states the condition.
