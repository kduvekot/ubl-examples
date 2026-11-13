# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/02#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a base of 1 each, the factor says 0.82 kg CO2e per bench, while `ValueMeasure` says 96 kg CO2e per bench. The figures cannot both hold. 96 / 0.82 ≈ 117, which suggests 0.82 is an emission factor per kWh (a typical grid factor, own knowledge) applied to about 117 kWh, but then the base unit is not "each". The value 96 itself is plausible: 34 kg steel at about 2 kg CO2e/kg plus 22.5 kg kiln-dried hardwood at about 0.4 kg CO2e/kg gives about 77 kg before casting and galvanising energy (own knowledge, quantities from `ResourceConsumption`). The same triple occurs for this bench in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'` over `world/examples`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base: the value per bench is what the catalogue needs; (b) state the activity the factor applies to, with its unit (e.g. kWh) and the activity amount, so that factor × activity = 96 kg.
- Needs decision: no

### retail/02#F2 · Medium · Language codes in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language code that `Language/cbc:ID` already holds, not a locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale code such as `en-XB` with a list that defines it.
- Needs decision: no

### retail/02#F3 · Medium · Province in Region in the GTIN issuer's address
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL's `Region` is "The recognized geographic or economic region or group of countries in which this address is situated"; a province is a political or administrative division of the country, which UBL puts in `CountrySubentity`. The same value occurs in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of Ferrano'`, files with a non-zero count).
- Condition: the province is in `CountrySubentity` (with `CountrySubentityCode` if Urvania has one), and `Region` is absent or holds a region in UBL's sense.
- Options: (a, preferred) move it to `CountrySubentity`; (b) drop it if Urvania's address format has no province.
- Needs decision: no

### retail/02#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml'`, non-zero files).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format makes the gate part of the postal address, record that in the format; the finding is then dismissed.
- Needs decision: no

### retail/02#F5 · Low · A new catalogue that supersedes a previous version and replaces an item of an existing catalogue
- XPath: `/Catalogue/cbc:ActionCode` = `NEW`
- XPath: `/Catalogue/cbc:PreviousVersionID` = `0.9`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`
- Why: `PreviousVersionID` is "An identifier for the previous version of the Catalogue that is superseded by this version", and `ReplacedRelatedItem` "An item in an existing catalogue that is being replaced by the item in this catalogue line". Both presuppose an earlier catalogue exchanged with Brightmarket, while the action code says this is a new catalogue and every line is `ADD`. No earlier catalogue exists in the flow; 01-CatalogueRequest refers to one (`01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`) that is not this one and does not exist (see the review of 01).
- Condition: either the catalogue is new and carries no previous version and no replaced item of an existing catalogue, or it is an update of a named earlier catalogue and its action codes say so.
- Options: (a, preferred) drop `PreviousVersionID` and `ReplacedRelatedItem` (a first catalogue under the 2026 supply agreement); (b) make it a replacement of an earlier catalogue and let 01 reference that one.
- Needs decision: yes

### retail/02#F6 · Low · Complementary item identified by the buyer's own item number
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:ID` = `BM-551004`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:Description` = `Garden bench set Marrow`
- Why: `BM-551004` is Brightmarket's own item number for its own-line Marrow set made by another supplier (`furniture/08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `BM-551004`; in `22-Order.xml` it is Brightmarket's seller's item ID). Lumeway does not sell it, and a related item in Lumeway's catalogue that is only identifiable in the receiver's own numbering, without saying so, is unusual. It may be legitimate as cross-selling advice, but nothing says whose number it is.
- Condition: a complementary item in the catalogue is one Lumeway offers, or the reference makes clear that it is the buyer's item.
- Options: (a, preferred) drop it, or refer to a complementary item from Lumeway's range (e.g. the anchor set, which is already an accessory); (b) keep it if the world wants Lumeway to suggest Brightmarket's own set, and make that explicit in the description.
- Needs decision: yes

### retail/02#F7 · Low · Discount for a "full container" in a flow without containers
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`
- Why: the discount's condition is a full container, but the flow delivers by full truck load without any container (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`; no transport equipment in 11–15), and the catalogue states no quantity that makes a container full. The arithmetic holds (3 % of 520.00 = 15.60).
- Condition: the allowance's reason describes a condition that can be met in the flow, with the quantity it needs, or the allowance is absent.
- Options: (a, preferred) a reason that fits road delivery (e.g. full truck load, or a quantity threshold such as a number of pallets); (b) drop the allowance.
- Needs decision: no

### retail/02#F8 · Low · Urvanian customs tariff codes in a Bayvarran domestic catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the catalogue is from a Bayvarran distributor to a Bayvarran retailer, for Bayvarra only. The national tariff codes given are Urvania's (`listID` `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`), the export country's, which neither party uses in this trade; Lumeway imported the goods under Bayvarra's tariff, if any. Copied from the manufacturer's data, they serve no purpose here.
- Condition: national tariff codes in the catalogue are those of a country whose customs the parties deal with, or they are absent.
- Options: (a, preferred) drop them (the HS code is enough for a domestic catalogue); (b) give Bayvarra's tariff code if Brightmarket needs it.
- Needs decision: no

### retail/02#F9 · Low · Master data of the GTIN issuer copied into the catalogue, with a contact that does not fit
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`
- Why: the issuer of the GTIN is identified by its register ID and name; its full address, tax scheme, legal entity, contact and electronic address are not used by a catalogue between Lumeway and Brightmarket (line 2 gives the same issuer with ID and name only). The contact presents a private limited company (`SRU`) as a public service. The English rendering of the street (`languageID` `en-XB`) is an Italian-form name, not an English one; this may be a world convention for Urvanian exonyms.
- Condition: the issuer party carries only what identifies it, as in line 2; if details stay, the contact fits a company and each rendering is in the language its `languageID` names.
- Options: (a, preferred) reduce the issuer to ID and name; (b) keep the details, adjust the contact, and confirm the exonym convention.
- Needs decision: no

### retail/02#F10 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: as the receiver of a catalogue the buying office fits; job title and department are those of a seller's customer service and contradict the name. The same contact is used for Brightmarket in all 19 retail examples that describe it in detail.
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title and purchasing department.
- Needs decision: no

### retail/02#F11 · Low · Header parties repeated on every catalogue line
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ContractorCustomerParty`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:SellerSupplierParty`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ContractorCustomerParty`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:SellerSupplierParty`
- Why: the line-level parties are the same as the header's `ContractorCustomerParty` and `SellerSupplierParty`. On a line they only make sense where a line has a different contract party or supplier; repeating the header adds no information (no-filler rule).
- Condition: line-level parties are present only where they differ from the header.
- Options: (a, preferred) drop them; (b) keep them only if a line really has another supplier (e.g. the manufacturer for spare parts).
- Needs decision: no

## Checked and consistent
- Validity period, contract `LD-BM-SUPPLY-2026`, territory XB and the two items agree with 01-CatalogueRequest; `LineCountNumeric` `2` matches the lines.
- Line 1: pallet of 4 (`ContentUnitQuantity`, increment, minimum 4, maximum 192 = 48 pallets), `DeliveryUnit` batch 4, `Package` `PX` quantity 4: consistent. Price 520 per each; discount 3 % × 520.00 = 15.60.
- Line 2: dependent price 12.31 % × 520 = 64.01, rounded to the stated 64.
- Bench physics: 34 kg steel + 22.5 kg hardwood ≈ 56.5 kg; five slats of 4.5 kg each fit a hardwood slat of 1.8 m × about 0.12 m × 0.03 m at about 700 kg/m³ (own knowledge). Dimensions 1800 × 620 × 780 mm with seat height 450 mm (440–460) are consistent.
- GTINs `9520610000012` and `9520610000029` and the GLNs pass the check digit; prefix 952 is GS1's demonstration range.
- HS `940179` (seats with metal frames) and `732599` (cast articles) and CPC `38111` and `42999` fit the items.
- Tax category `E` with exemption reason "sale for resale" fits a sale to a retailer for resale; the same treatment is used on both lines.
- Warranty: five years in `WarrantyValidityPeriod` agrees with both warranty texts, and the warranty party is the manufacturer.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:PriceAmount` = `520`: suspected a comparison that repeats the price — refuted because the orderable unit is a pallet of four, and a comparison price per each is what `ItemComparison` is for.
- `/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`: suspected to contradict an active, newly added item — refuted because UBL defines it as an item that "may be a replacement", which a newer casting revision can be without the current one being withdrawn.
- `/Catalogue/cbc:RevisionTime` = `09:00:00`: suspected inconsistent with issue at 17:28 — refuted: revision before issue on the same day is plausible.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:TradingRestrictions` = `Not sold to consumers.`: suspected to contradict Brightmarket selling the bench to a consumer (21-PurchaseReceipt) — refuted because the restriction is Lumeway's own trade (it sells only to trade customers), not a restriction on resale.

## Outside this review
- `tender/15-Tender.xml` gives `VI-C180-2026` as a replacement item for the whole Serra 180 bench, while here it is the replacement of the side frame casting: belongs to the review of that example.
