# LLM review: 04-CatalogueItemSpecificationUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/04-CatalogueItemSpecificationUpdate.xml`, Git blob `bc08c5d7cc1e9ec6f62cb02c0b6ddfcd217352bc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/04#F1 · High · Reference to the catalogue: wrong issue time, a revision after this document, and the superseded version
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueTime` = `09:01:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:RelatedCatalogueReference/cbc:VersionID` = `1.0`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:VersionID` = `1.1`
- Why: in CatalogueReference, IssueTime is "The time at which the catalogue was issued"; the catalogue
  was issued at 17:28, and 09:00 is its revision time. RevisionDate/Time is "The date/time on which
  the information in the catalogue was last revised": 2026-05-21 14:00 is five hours after this
  document was issued (09:01 the same day). VersionID is "An identifier for the current version of
  the catalogue": after 03-CataloguePricingUpdate.xml the current version is 1.1, not 1.0.
- Condition: the reference gives the catalogue's issue time 17:28, a last revision not later than
  this document's issue (the 1.1 revision of 03), and the current version 1.1.
- Options: correct the three values; or reduce the reference to ID, UUID and issue date, which is all
  the receiver needs to find the catalogue.
- Needs decision: no

### retail/04#F2 · High · Emission factor times base does not give the emission
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g.,
  emissions per unit of activity)", per ValueBaseMeasure. 0.82 per one bench gives 0.82 kg CO2e, not
  96 kg (the same values as in 02-Catalogue.xml).
- Condition: factor × activity quantity = ValueMeasure, or no factor.
- Options: drop factor and base (preferred, the value is a measured footprint), or a factor and base
  that multiply out to 96 kg.
- Needs decision: no

### retail/04#F3 · Medium · The update of the slat wood is in free text only; the structured data still describe the old wood
- XPath: `/CatalogueItemSpecificationUpdate/cbc:Name` = `New slat wood for the Serra 180`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description` = `Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried hardwood, for bolting to the ground.`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:AdditionalItemProperty[2]/cbc:Value` = `Kiln-dried hardwood`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ResourceOriginDescription` = `Slats from Upland State, Bayvarra`
- Why: the document is "used to update information (e.g., technical descriptions and properties)
  about Items in an existing Catalogue", and its whole purpose is the new slat wood. Only the
  description says "another kiln-dried hardwood", without naming it. The property "Slat wood", the
  hardwood consumption (22.5 kg, origin Upland State, measured in 2025) and the emission figures are
  exactly those of 02-Catalogue.xml, i.e. of the old wood; a receiver comparing the structured data
  sees no change at all.
- Condition: the structured properties that describe the slats name the new wood, and the figures
  that depend on it (hardwood consumption, origin, footprint) are either updated or stated to be
  unchanged for a reason.
- Options: (a) preferred: name the new wood in the "Slat wood" property (and the description), and
  adjust or drop the material and emission figures that were measured for the old wood; (b) if only
  the supplier of the same wood changes, say that instead of "another hardwood".
- Needs decision: yes

### retail/04#F4 · Medium · The revision date is that of the previous update, and the validity starts before the issue
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`
- XPath: `/CatalogueItemSpecificationUpdate/cbc:IssueDate` = `2026-05-21`
- Why: RevisionDate/Time are "The date/time, assigned by the seller, on which the Catalogue was
  revised". This document makes revision 1.2, but gives the date and time of the 1.1 revision of
  03-CataloguePricingUpdate.xml (2026-05-20 14:00). Its ValidityPeriod, "during which the
  information in the Catalogue Revision is effective", starts on 2026-05-20, the day before the new
  wood was announced; benches sold that day would retroactively have another slat wood.
- Condition: the revision date/time are those of this revision (not after the issue), and the
  validity starts no earlier than the issue date, unless the story gives a reason for a retroactive
  start.
- Options: revision on 2026-05-21 before 09:01 and validity from 2026-05-21 (preferred).
- Needs decision: no

### retail/04#F5 · Medium · A system-boundary code in the fullness indication
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty". "Cradle to gate" is a life-cycle boundary, not a fullness; a product
  footprint has no transport equipment whose fullness is a parameter. Same use in 39 examples
  (`grep -l` over `*.xml`).
- Condition: a fullness code for transport equipment, or no element.
- Options: drop it (preferred) and keep the scope in the life-cycle description.
- Needs decision: no

### retail/04#F6 · Medium · A language code in LocaleCode
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value is the
  ISO 639 language code. Same pattern in 213 examples (`grep -l` over `*.xml`).
- Condition: a locale code, or no LocaleCode.
- Options: `en-XB` with a locale listID (preferred), or drop it.
- Needs decision: no

### retail/04#F7 · Low · Life-cycle stage "manufacturing" for a cradle-to-gate footprint
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: the description includes raw-material extraction; the code names manufacturing only.
- Condition: code and description name the same scope.
- Options: a code covering raw materials and manufacturing, or a narrower description.
- Needs decision: no

### retail/04#F8 · Low · Trading terms "Unchanged.", repeated contract parties, signature and master data without use
- XPath: `/CatalogueItemSpecificationUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/CatalogueItemSpecificationUpdate/cac:Signature/cbc:ID` = `LD-SIG-26-1.2`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueItemSpecificationUpdate/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: "Unchanged." describes no trading term; the line-level contract parties repeat the header's
  parties of the one contract; the signature has only an ID and a signatory and signs nothing; a
  domestic item update uses no customs trader number, social-media profile, share capital or tax
  registration. All without a use in this document (IND5/IND6).
- Condition: each of these is absent or has a use here.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- The update line ID `1` is the bench's catalogue line in 02-Catalogue.xml, and the item
  identifiers (seller's `LD-10442`, manufacturer's `VI-B180`, GTIN `9520610000012`) match it.
- RelatedCatalogueReference ID, UUID, IssueDate match 02-Catalogue.xml; this document's VersionID
  `1.2` follows 03's `1.1`.
- Dimensions, load property, warranty text, classifications and document references are those of
  02-Catalogue.xml.

## Considered and refuted
- `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`:
  Urvanian tariff code in a Bayvarran catalogue — refuted for the reasons given in 02's review (the
  goods are imported from Urvania; the world has no other tariff list).
- `/CatalogueItemSpecificationUpdate/cac:CatalogueItemSpecificationUpdateLine/cac:Item/cbc:Description`:
  the description is fuller than the catalogue's ("The manufacturer's Serra bench, from the
  distributor's stock.") — refuted because a fuller technical description is what an item
  specification update is for.
