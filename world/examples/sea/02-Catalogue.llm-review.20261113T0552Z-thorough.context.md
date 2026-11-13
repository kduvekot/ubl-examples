# LLM review: 02-Catalogue.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/02#F1 · High · Sales territory Bayvarra, but the tax category is an export outside Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- Why: ApplicableTerritoryAddress is "the applicable sales territory" of the item location quantity,
  and the same ItemLocationQuantity applies tax category G (free export item) with the exemption
  "Export outside Bayvarra". A price whose sales territory is Bayvarra cannot at the same time be a
  zero-rated export outside Bayvarra. The receiver, Velumi Trading, is on Lisavu
  (`/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`), so
  the price block that is offered to it is the one for sales into Lisavu.
- Condition: in each line, the applicable territory and the applicable tax category describe the
  same situation (export territory with the export exemption, or Bayvarra with the domestic tax).
- Options: (a) preferred: territory Lisavu (or the islands) for the export price, since the
  receiver is there; (b) two ItemLocationQuantity blocks, Bayvarra with state sales tax and Lisavu
  with the export exemption.
- Needs decision: no

### sea/02#F2 · High · Emission value does not follow from its factor and base
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g.,
  emissions per unit of activity)", ValueBaseMeasure "the base quantity to which the value factor
  applies". With a base of 1 each, the factor gives 0.82 × 1 = 0.82, while the value is 96 kg CO2e
  per bench. Neither 0.82 kg per bench nor a factor of 0.82 for a base of one bench yields 96; the
  base of the factor (it might be per kg of steel or per kWh) is not the one stated.
- Condition: ValueFactorNumeric × ValueBaseMeasure, in the stated units, gives ValueMeasure, or the
  factor and base are absent.
- Options: (a) preferred: drop factor and base, since the 96 kg is a product footprint computed
  from the life-cycle study (`VI-LCA-2025`) rather than one factor; (b) state the actual activity
  base (e.g. kg of material) with its quantity so that the product holds.
- Needs decision: no

### sea/02#F3 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: In EmissionCalculationMethod, FullnessIndicationCode is "a code signifying whether a piece of
  transport equipment is full, partially full, or empty". Cradle-to-gate is the system boundary of
  a product footprint, from the world's EmissionBoundaryCode list; it says nothing about the
  fullness of transport equipment, and a bench in a catalogue has none. The boundary is already
  stated in `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription`
  = `From the ore at the mine to the bench leaving the factory gate.` Over `world/examples/*/*.xml`,
  39 FullnessIndicationCode elements carry `CRADLETOGATE` from the boundary list (5 others carry FCL
  from a load-type list).
- Condition: FullnessIndicationCode is absent from item emissions, or holds a fullness code where an
  emission of a transport is calculated.
- Options: (a) preferred: drop it; the boundary is in LifecycleStageCode/Description; (b) record the
  misfit of the definition as a finding for UBL if the TC intended a boundary code here.
- Needs decision: no

### sea/02#F4 · Medium · CatalogueIndicator "ordered from a catalogue" in the catalogue itself
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: CatalogueIndicator is "an indicator that this item was ordered from a catalogue (true) or not
  (false)". In a Catalogue no item has been ordered; the indicator belongs to an order or an
  ordered line. In this flow it occurs only here (grep over sea `*.xml`), not in the Order that
  orders from this catalogue.
- Condition: no CatalogueIndicator in the catalogue lines.
- Options: (a) preferred: drop it here, and if wanted put it on the ordered item in 05-Order, which
  does order from this catalogue.
- Needs decision: no

### sea/02#F5 · Medium · PriceList status "Active" where the element asks for original, copy, revision or cancellation
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:StatusCode` = `ACTIVE`
- Why: PriceList StatusCode is "a code signifying whether this price list is an original, copy,
  revision, or cancellation". "Active" (RecordStatusCode list) is a life-cycle state, not one of
  these; the price validity is already given by the Price ValidityPeriod next to it.
- Condition: StatusCode holds one of the kinds the definition names (e.g. original), from a list
  that has them, or is absent.
- Options: (a) preferred: a document status list value meaning original, since this is the first
  price list LD-PL-2026; (b) drop StatusCode.
- Needs decision: no

### sea/02#F6 · Medium · A language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; the value is
  the ISO 639 language code of `/Catalogue/cac:ProviderParty/cac:Language/cbc:ID` = `en` and names
  no locale. (362 such elements over `world/examples/*/*.xml`.)
- Condition: LocaleCode is absent or holds a locale.
- Options: (a) preferred: a locale for Bayvarran English; (b) drop it.
- Needs decision: no

### sea/02#F7 · Medium · A province in Region of the GTIN issuer's address
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province is "the political or administrative division of a country", which
  is CountrySubentity.
- Condition: the province is in CountrySubentity (and, if wanted, CountrySubentityCode); Region is
  absent or holds a region in the definition's sense.
- Options: (a) preferred: move it to CountrySubentity.
- Needs decision: no

### sea/02#F8 · Low · Full master data of the GTIN issuer in a catalogue line
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- Why: IssuerParty is "the Party who issues this Item Identification"; a catalogue needs at most its
  identity to qualify the GTIN. The tax registration, legal form, size, registration scheme,
  contact and endpoint of Codana do nothing in the catalogue; line 2 identifies the same issuer
  with ID and name only
  (`/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`
  = `Codana Identification Agency`).
- Condition: the GTIN issuer is described by identification and name only, as in line 2.
- Options: (a) preferred: reduce line 1's IssuerParty to line 2's form.
- Needs decision: no

### sea/02#F9 · Low · Spare part priced as a percentage of the bench, with a rounded result
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cbc:Percent` = `12.31`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `64`
- Why: DependentPriceReference is "the price of the item as a percentage of the price of some other
  item". A spare side frame is priced on its own (64 XBL, with its own price list entry); 12.31 % is
  64 / 520 back-calculated, and 520 × 12.31 % = 64.01, not 64. The dependency has no business
  reason in the catalogue (it does not say the spare's price moves with the bench's).
- Condition: either the spare's price is stated without a dependency, or the percentage is the rule
  the price follows and 520 × percent = the price.
- Options: (a) preferred: drop DependentPriceReference; (b) state a round rule (e.g. 12.5 %) and
  derive the price from it.
- Needs decision: no

### sea/02#F10 · Low · Receiver's contact: purchasing name with a seller's title and department
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi receives the catalogue as buyer; title and department are those of Lumeway's own
  contact (`/Catalogue/cac:ProviderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`).
- Condition: Velumi's contact has a purchasing title and department, or none.
- Options: (a) preferred: purchasing title and department.
- Needs decision: no

### sea/02#F11 · Low · Receiver's legal entity and address in a catalogue that does not use them
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: The catalogue offers items to Velumi; nothing in it depends on Velumi's legal form, size,
  registration or registered address. Looks copied from master data.
- Condition: ReceiverParty carries identification, name, contact and electronic address only, or
  the catalogue has a reason for the rest.
- Options: (a) preferred: reduce ReceiverParty.
- Needs decision: no

### sea/02#F12 · Low · A gate in AdditionalStreetName of the provider's postal address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is a vehicle
  entrance, not a street, and has no use in a postal address.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it, or give it in a delivery or despatch location where it matters.
- Needs decision: no

## Checked and consistent
- GTINs `9520610000012` and `9520610000029` and the GLN pass their check digits (`check_ids.py`).
- Discount line 1: 520.00 × 0.03 = 15.60, matches the Amount.
- Alternative currency prices: 520 XBL ↔ 208 XLC and 64 XBL ↔ 25.6 XLC both at 0.4, consistent.
- Price ValidityPeriod equals the catalogue ValidityPeriod (2026-05-04 to 2026-10-31); the delivery
  period lies within it; MinimumQuantity 4, DeliveryUnit BatchQuantity 4 and Package Quantity 4
  agree with "per pallet of four benches" in the transaction conditions.
- HS 940179 / CPC 38111 / national 94017910 for the bench and HS 732599 / CPC 42999 for the spare
  casting fit the items.
- ManufacturerParty and InformationContentProviderParty (Valdara Industries) fit the definition
  "the Party who specifies this Item".

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription`:
  packaging waste "per bench" with a measurement period of 2025 — refuted: the period is when the
  waste per bench was measured, which the definition of MeasurementPeriod allows.
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cac:StandardPropertyIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`:
  the identification agency as issuer of a property identifier — refuted: an agency that runs item
  identification can also run a property dictionary; nothing contradicts it.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason`:
  a "full container" discount in a catalogue line — refuted for this lens: a conditional discount
  is legitimate catalogue content; whether the condition is expressed enough is a money question.

## Outside this review
- The catalogue (issued 2026-05-04 09:17) precedes the business card it would normally follow
  (01-BusinessCard, issued the same day 16:39); a timeline question across documents.
