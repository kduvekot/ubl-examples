# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/02#F1 · High · A new catalogue that supersedes a previous version
- XPath: `/Catalogue/cbc:ActionCode` = `NEW`
- XPath: `/Catalogue/cbc:PreviousVersionID` = `0.9`
- XPath: `/Catalogue/cbc:VersionID` = `1.0`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`
- Why: ActionCode `NEW` (list meaning "New catalogue") and the lines' ActionCode `ADD` say this is
  the first catalogue between the parties. PreviousVersionID is defined as "An identifier for the
  previous version of the Catalogue that is superseded by this version", and ReplacedRelatedItem as
  "An item in an existing catalogue that is being replaced by the item in this catalogue line"; both
  say an earlier catalogue exists and is superseded. The request this catalogue answers,
  01-CatalogueRequest.xml, asks for an update of a catalogue (`01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`),
  which no example carries. The document thus says both "new" and "replaces version 0.9".
- Condition: the catalogue is either new (no PreviousVersionID, no item "in an existing catalogue"
  being replaced) or an update/replacement of an identified earlier catalogue, and 01 asks for the
  same thing.
- Options: (a) preferred: a new catalogue, version 1.0 without PreviousVersionID, and the replaced
  item expressed only through ReplacementRelatedItem or a note, because 03 and 04 are the updates of
  this catalogue; (b) a replacement of an earlier catalogue, with 01 referring to it.
- Needs decision: yes

### retail/02#F2 · High · Emission factor times base does not give the emission
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g.,
  emissions per unit of activity)" and ValueBaseMeasure "The base quantity to which the value factor
  applies (e.g., per km, per kg, per unit produced)". With a base of 1 each (one bench) the factor
  gives 0.82 × 1 = 0.82 kg CO2e, not the stated 96 kg. Nor does it fit the materials of the
  circularity profile (34 kg steel + 22.5 kg hardwood = 56.5 kg; 56.5 × 0.82 = 46.3 kg). The three
  values cannot all be right.
- Condition: ValueFactorNumeric × the activity quantity (in the unit of ValueBaseMeasure) equals
  ValueMeasure, or the factor is absent.
- Options: (a) preferred: drop the factor and base, since the value is a measured product footprint
  (EmissionFactorSource names measured energy use); (b) give a factor per kg of material with a base in
  kg that multiplies out to 96 kg.
- Needs decision: no

### retail/02#F3 · Medium · A catalogue item marked as ordered from a catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: CatalogueIndicator is "An indicator that this item was ordered from a catalogue (true) or not
  (false)". It describes an ordered item (in an order, despatch advice or invoice). In the catalogue
  itself nothing has been ordered, so the indicator states nothing true about this document.
- Condition: no CatalogueIndicator in the catalogue's items.
- Options: drop it here; it belongs, if anywhere, in 08-Order.xml's lines.
- Needs decision: no

### retail/02#F4 · Medium · A system-boundary code in the fullness indication
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty. This indication is used as a parameter when calculating the environmental
  emission." The value comes from an emission boundary list ("Cradle to gate"), which is about the
  life-cycle scope of a product footprint, not about how full a vehicle is. A bench's
  manufacturing footprint has no transport equipment whose fullness matters. The same list is used in
  this element in 39 examples (counted with `grep -l` for
  `FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"` over `*.xml`).
- Condition: FullnessIndicationCode carries a fullness code for a piece of transport equipment, or is
  absent; the cradle-to-gate scope is expressed elsewhere.
- Options: (a) preferred: drop the element and keep the scope in LifecycleStageCode/Description
  (see F5); (b) if UBL has no element for the boundary, record it as a finding for the TC.
- Needs decision: no

### retail/02#F5 · Medium · A language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value is the
  ISO 639 language code (listID `ISO 639`) and repeats Language/ID. The pattern occurs in 213
  examples (`grep -l 'LocaleCode listID="ISO 639"'` over `*.xml`).
- Condition: LocaleCode holds a locale code or is absent.
- Options: a locale such as `en-XB` with a locale listID (preferred), or drop it.
- Needs decision: no

### retail/02#F6 · Low · Life-cycle stage "manufacturing" for a cradle-to-gate footprint
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: LifecycleStageCode is "A code indicating the lifecycle stage to which this emission applies".
  The description and Description ("Mining, steel making, casting, …") cover raw-material
  extraction as well as manufacturing, i.e. several stages. The code names one of them.
- Condition: the code and the description name the same scope.
- Options: a code for the cradle-to-gate scope (raw materials and manufacturing), if the list has
  one; or a description limited to manufacturing.
- Needs decision: no

### retail/02#F7 · Low · An active spare part that is replaced and replacing at once
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cbc:LifeCycleStatusCode` = `ACTIVE`
- Why: the line sells `VI-C180`. ReplacementRelatedItem says `VI-C180-2026` "may be a replacement for
  the item in this catalogue line", ReplacedRelatedItem says this item replaces `VI-C180-2024`. A
  2026 successor of a part offered as active and orderable in a new 2026 catalogue needs a reason
  (phase-out, interchangeability) that nothing in the document gives, and the replaced item is said
  to be in an existing catalogue that does not exist (F1).
- Condition: the replacement relations describe a situation the line explains (e.g. a life-cycle
  status or note for a successor), or are absent.
- Options: keep only the relation that has a story (e.g. the 2026 casting as successor, with a note
  or a phase-out status); drop the other.
- Needs decision: no

### retail/02#F8 · Low · Complementary item the seller does not sell, under the buyer's number
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:ID` = `BM-551004`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:Description` = `Garden bench set Marrow`
- Why: `BM-551004` is Brightmarket's own-line garden set, made for it by another supplier
  (`furniture/10-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `BM-551004`,
  brand Brackenmere). Lumeway's catalogue suggests the buyer's own product of a competitor as a
  complement, identified by the buyer's article number without saying whose number it is. A seller
  has no reason to list it in its catalogue.
- Condition: related items in the catalogue are items the seller can supply, or the relation has a
  stated reason.
- Options: drop the complementary item (preferred), or replace it with one of Lumeway's own items.
- Needs decision: no

### retail/02#F9 · Low · Item comparison for a quantity that cannot be ordered
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:Quantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:PriceAmount` = `520`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cbc:MinimumOrderQuantity` = `4`
- Why: ItemComparison is "A combination of price and quantity used to provide price comparisons based
  on different sizes of order". The only comparison is the unit price for one bench, which repeats
  the line's price and is below the minimum order quantity (pallets of four). It compares nothing.
- Condition: an item comparison, if present, gives the price for an orderable size different from
  the base price, or is absent.
- Options: drop it (preferred), or give the price per pallet of four or per larger quantity.
- Needs decision: no

### retail/02#F10 · Low · Line-level contract parties repeat the header
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: at line level these are "The customer responsible for the contract with which this catalogue
  line is associated" and the seller responsible for it. Both are the header's parties of the one
  contract `LD-BM-SUPPLY-2026`; no line is under another contract. Repeating them says nothing new.
- Condition: line-level contract parties are present only where they differ from the header.
- Options: drop them from the lines.
- Needs decision: no

### retail/02#F11 · Low · Master data the catalogue does nothing with
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cbc:IndustryClassificationCode` = `8299`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Codana Identification Agency SRU`
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Catalogue/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the issuer of the GTIN on line 1 carries a full party with address, tax scheme and legal
  entity, while the same issuer on line 2 carries only ID and name
  (`/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`);
  a customs trader number of the provider in a domestic catalogue and the receiver's social media
  profile play no part in a catalogue. The parties also carry share capital and tax registrations
  that the catalogue does not use.
- Condition: party data in the catalogue is what a catalogue uses, and the same issuer is described
  the same way on both lines.
- Options: reduce the GTIN issuer on line 1 to ID and name; drop customs, social-media, share-capital
  and tax detail from the parties.
- Needs decision: no

### retail/02#F12 · Low · Signature without anything that signs
- XPath: `/Catalogue/cac:Signature/cbc:ID` = `LD-SIG-26-0420`
- Why: Signature has only an ID and the signatory party: no method, no attachment, no validation
  date. It records nothing a receiver could verify, and the catalogue's story gives no reason for a
  signature. A filler (IND5/IND6).
- Condition: either a signature with a reason and its data, or none.
- Options: drop it (preferred).
- Needs decision: no

### retail/02#F13 · Low · Dependent price tied to one state while the reference price applies to the whole country
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cac:LocationAddress/cbc:CountrySubentity` = `Coastal State`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: LocationAddress is "The reference location for this dependent price reference". The bench
  price of line 1 is one price for all of Bayvarra, and line 2's own territory is Bayvarra; naming
  Coastal State as the reference location suggests a state-specific bench price that the catalogue
  does not have.
- Condition: the reference location is the territory where the referenced price applies, or is
  absent.
- Options: drop LocationAddress (preferred), or make it Bayvarra.
- Needs decision: no

## Checked and consistent
- ProviderParty (Lumeway) and ReceiverParty (Brightmarket) fit the definitions; SellerSupplierParty
  and ContractorCustomerParty agree with 01-CatalogueRequest.xml.
- Validity periods: header, line and price validity all 2026-04-20 to 2026-07-19; the delivery
  period for the price starts 2026-04-27, after the issue date.
- Line 1 ordering data agree with each other: pallet of 4, ContentUnitQuantity 4, increment 4,
  minimum 4, maximum 192 (48 pallets), DeliveryUnit BatchQuantity 4, Package quantity 4 with code PX.
- DependentPriceReference: 64 / 520 = 12.31 %.
- WarrantyInformation, WarrantyParty (the maker, Valdara) and WarrantyValidityPeriod (5 years) agree.
- HS 940179 and CPC 38111 fit a bench with a metal frame; HS 732599 fits a cast side frame.
- TradingTerms reference `LD-GTC-2026` is the document referenced at header level.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`: an
  Urvanian national tariff code in a catalogue for Bayvarra — refuted because the item is of Urvanian
  origin and imported; the world has no Bayvarran tariff list (all 61 tariff codes over `*.xml` use
  the XU list), so the code identifies the goods as they were imported.
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredRelatedItem/cbc:ID`: the spare frame "requires" the
  bench — refuted because a spare part is only of use with the bench it fits, which is what a
  required related item expresses.
- `/Catalogue/cac:CatalogueLine[1]/cac:KeywordItemProperty/cbc:Value`: repeats Item/Keyword —
  refuted because KeywordItemProperty is the line-level keyword property and holding a keyword is its
  meaning.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:TradingRestrictions`: "Not
  sold to consumers" while Brightmarket sells the benches to consumers (21-PurchaseReceipt.xml) —
  refuted because the restriction is on Lumeway's own sales; the retailer's resale is not affected.
- `/Catalogue/cbc:RevisionTime`: revision at 09:00 the same day the request came in at 08:42 —
  refuted because the revision precedes the issue at 17:28 and follows the request.
