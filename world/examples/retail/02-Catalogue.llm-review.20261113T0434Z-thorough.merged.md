# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### retail/02#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". Recomputed: with a base of 1 EA the factor gives 0.82 × 1 = 0.82 kg CO2e per bench, not 96. No other quantity of the item gives 96 either: the stated materials are 34 kg steel + 22.5 kg hardwood = 56.5 kg (`/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`, `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`), and 0.82 × 56.5 = 46.3; 96 / 0.82 = 117.1, which would fit a grid factor per kWh applied to about 117 kWh, not a base in EA. The 96 kg itself is plausible (steel about 2 kg CO2e/kg gives about 68 kg, plus hardwood, casting, galvanising; own knowledge). The same triple occurs in 39 files, 10 of them in retail (verified: `grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<'`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure`, or factor and base are absent.
- Options: (a, preferred, all parts) drop factor and base: the 96 kg is a product total from an LCA (`VI-LCA-2025`, measured energy use), not a calculation from one activity; (b) state the activity the factor applies to with its unit and amount (e.g. kWh), so that factor × activity = 96 kg; (c) a factor per kg of material with a base in kg that multiplies out to 96 kg.
- Needs decision: no
- From: broad, logistics, context

### retail/02#F2 · Medium · A "new" catalogue that supersedes a previous version and replaces an item of an existing catalogue
- XPath: `/Catalogue/cbc:ActionCode` = `NEW`
- XPath: `/Catalogue/cbc:VersionID` = `1.0`
- XPath: `/Catalogue/cbc:PreviousVersionID` = `0.9`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`
- XPath: `01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- Why: `ActionCode` `NEW` ("New catalogue" in the world's list, beside `REPLACE` and `UPDATE`) and every line's `ADD` say this is the first catalogue between the parties. `PreviousVersionID` is "An identifier for the previous version of the Catalogue that is superseded by this version", and `ReplacedRelatedItem` "An item in an existing catalogue that is being replaced by the item in this catalogue line"; both say an earlier catalogue exists and is superseded. The request 01 asks for an update of `LD-CAT-SPRING-26`, an ID this catalogue does not carry and no example has. The three statements do not describe the same story. Not High (context's severity): a version 1.0 can supersede an internal draft 0.9 that was never sent, and "an existing catalogue" can be one Lumeway issued to other customers, so the values can be reconciled by reading; but as written they point in two directions, and the request and the answer do not match (01#F1).
- Condition: `ActionCode`, `PreviousVersionID`, `ReplacedRelatedItem` and 01's `RequestedCatalogueReference` agree: either a new catalogue without a superseded previous version and without an item "in an existing catalogue", or an update/replacement of a named earlier catalogue to which 01 refers.
- Options: (a, preferred, all three parts) a new catalogue: drop `PreviousVersionID`, express the casting revision only through `ReplacementRelatedItem` or a note, and drop the reference in 01, since 03 and 04 are the updates of this catalogue; (b) `ActionCode` `REPLACE` (or `UPDATE`) with the earlier catalogue identified in 01.
- Needs decision: yes
- From: broad (Low), logistics (Medium), context (High)

### retail/02#F3 · Medium · A language code in LocaleCode
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code that `Language/cbc:ID` already holds, not a locale. 362 occurrences in 213 files (verified, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad, parties, context

### retail/02#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate of the distribution centre is a vehicle access detail, not a street name, and has no place in a postal address. 79 occurrences in 76 files (verified).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading or delivery location); (b) record it in Bayvarra's address format, and the finding is dismissed.
- Needs decision: no
- From: broad, parties

### retail/02#F5 · Medium · Catalogue items marked as "ordered from a catalogue"
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:CatalogueIndicator` = `true`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:CatalogueIndicator` = `true`
- Why: `Item/CatalogueIndicator` is "An indicator that this item was ordered from a catalogue (true) or not (false)" (verified with annotate.py). It describes an ordered item (in an order, despatch advice or invoice line). In the catalogue nothing has been ordered yet, so the value states nothing true about this document; reading it as "this is a catalogue item" is not what the definition says.
- Condition: no `CatalogueIndicator` in the catalogue's items.
- Options: (a, preferred) drop it here; it belongs, if anywhere, in the order lines of 08.
- Needs decision: no
- From: context

### retail/02#F6 · Medium · Province in Region in the GTIN issuer's address
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL's `Region` is "The recognized geographic or economic region or group of countries in which this address is situated"; a province is an administrative subdivision of the country, which UBL puts in `CountrySubentity`, and the address has no `CountrySubentity`. Section 6 names "a province in Region" as Medium. 219 occurrences in 104 files (verified, `grep -rho` / `grep -rl --include='*.xml' '<cbc:Region>Province of Ferrano<'`).
- Condition: the province is in `CountrySubentity` (with `CountrySubentityCode` where the world has one), and `Region` is absent or holds a region in UBL's sense.
- Options: (a, preferred) move it to `CountrySubentity` in the address data, so all places change together; (b) drop it if Urvania's address format has no province (or drop the whole address, see F18).
- Needs decision: no
- From: broad, parties

### retail/02#F7 · Medium · Life-cycle stage "manufacturing" for a footprint from the mine to the factory gate
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies". The description and `Description` ("Mining, steel making, casting, …") cover raw-material extraction, transport and manufacturing, i.e. several stages (A1–A3 in EN 15804 terms, own knowledge); the code names one of them, so code and text equivalent disagree.
- Condition: the code and the description name the same scope.
- Options: (a, preferred) omit the code and keep the description, or use a code for the whole cradle-to-gate scope if the list gets one; (b) two emission entries, one per stage; (c) limit the description to manufacturing.
- Needs decision: no
- From: context (Low)

### retail/02#F8 · Medium · A system-boundary code in the fullness indication
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value comes from the world's emission boundary list ("Cradle to gate"), the life-cycle scope of a product footprint; a bench's manufacturing footprint has no transport equipment whose fullness matters. The list is used in this element in 39 files (verified, `grep -rl --include='*.xml' 'EmissionBoundaryCode'`).
- Condition: `FullnessIndicationCode` carries a fullness code for a piece of transport equipment, or is absent; the cradle-to-gate scope is expressed elsewhere.
- Options: (a, preferred) drop the element and keep the scope in the stage description (F7); (b) record the missing system-boundary element as a finding for the OASIS UBL TC.
- Needs decision: no
- From: context

### retail/02#F9 · Low · Signature without anything that signs
- XPath: `/Catalogue/cac:Signature/cbc:ID` = `LD-SIG-26-0420`
- Why: Signature ("A signature applied to this document") holds only an ID and the signatory party: no method, no attachment, no validation date; it records nothing a receiver could verify, and the catalogue's story gives no reason for a signature (IND5/IND6). 137 of 147 Signature aggregates in the world have this shape (lxml).
- Condition: either a signature with a reason and its data, or none.
- Options: (a, preferred) drop it; (b) add method and attachment with a reason in the story.
- Needs decision: yes (a world-wide convention; aligned with the air and utilities merges)
- From: context

### retail/02#F10 · Low · Party master data the catalogue does nothing with
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Catalogue/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Catalogue/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Catalogue/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: a catalogue between trading partners does nothing with Lumeway's customs trader number (the flow is domestic and has no customs document), the share capital of either party, or Brightmarket's logo, consumer online shop and social-media profile; they are master data, identical in every example of the flow (section 4.8). Context also counted the parties' tax registrations among the unused data; they are less clear here, because the catalogue states a tax category per line (exempt for resale), which depends on the parties' registrations, so they are not cited. `CorporateStockAmount` is moreover defined as "The number of shares in the capital stock of a corporation" while it holds an amount (share capital): a definition/data type conflict for the TC write-up (parties).
- Condition: the parties carry only what the catalogue uses.
- Options: (a, preferred) leave these values out of the catalogue; (b) keep share capital only where company law needs it, and record the definition conflict for the TC.
- Needs decision: no
- From: parties (F5, F6, F7), context (F11, party part)

### retail/02#F11 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: as the receiver of a catalogue the buying office fits; job title and department are those of a seller's customer service and contradict the name. The same contact is used for Brightmarket in 41 files (19 in retail; verified).
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title in a purchasing department, role-specific contacts elsewhere.
- Needs decision: no
- From: broad, parties

### retail/02#F12 · Low · Header contract parties repeated on every catalogue line
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ContractorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: at line level these are the customer and seller responsible for the contract the line is associated with; both lines are under the header's one contract `LD-BM-SUPPLY-2026` with the header's parties. Repeating them adds nothing (no-filler rule).
- Condition: line-level parties are present only where they differ from the header.
- Options: (a, preferred) drop them; (b) keep them only where a line really has another supplier or contract.
- Needs decision: no
- From: broad, context

### retail/02#F13 · Low · Item comparison that repeats the unit price
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:PriceAmount` = `520`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:Quantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:BaseQuantity` = `1`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cbc:MinimumOrderQuantity` = `4`
- Why: `ItemComparison` is "A combination of price and quantity used to provide price comparisons based on different sizes of order". The only comparison is 520 for one bench, exactly the line's price per one bench, for a quantity below the minimum order of four; it compares no order sizes. Broad refuted it (the orderable unit is a pallet, so a per-each price is what comparison is for), but the price itself is already per each (`BaseQuantity` 1), so the comparison repeats it.
- Condition: the line has no `ItemComparison`, or its comparisons show prices for orderable sizes that differ from or explain the line's price.
- Options: (a, preferred) remove it; (b) use it for a real comparison, e.g. per pallet with and without the discount of F15 once F15 has its own quantity band.
- Needs decision: no
- From: money, context (broad refuted)

### retail/02#F14 · Low · Complementary item under the buyer's own number, which the seller does not sell
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:ID` = `BM-551004`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:Description` = `Garden bench set Marrow`
- Why: `ComplementaryRelatedItem` is "An item that may complement the item in this catalogue line". `BM-551004` is Brightmarket's own-line garden set, made for it by another supplier (`furniture/08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `BM-551004`; also in furniture/10 and as Brightmarket's seller's item ID in retail/22, verified). Lumeway's catalogue suggests a competitor-made product of the buyer, identified by the buyer's number without saying whose it is. Cross-selling advice to the retailer is a possible reading (broad), so whether it belongs is a story question.
- Condition: a complementary item in the catalogue is one Lumeway can supply, or the reference makes clear that it is the buyer's item and why it is suggested.
- Options: (a, preferred) drop it, or name a complementary item from Lumeway's range; (b) keep it and make the cross-selling intent explicit.
- Needs decision: yes
- From: broad (yes), context (no)

### retail/02#F15 · Low · "Full container" discount whose condition cannot be met and is not stated
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Full container`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `4`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MaximumQuantity` = `192`
- Why: the allowance sits in the item location quantity whose minimum is 4 and maximum 192, so by its place the 3 % applies to every order from one pallet upwards, while its reason makes it conditional on a full container, which nothing quantifies. The flow has no container: delivery is by full truck load (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`), and the order of 24 benches, inside the band, neither claims nor gets the 3 % (`08-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Promotion support`). Arithmetic recomputed: 520.00 × 0.03 = 15.60, as stated.
- Condition: the discount's condition is one the catalogue states and the flow can visibly meet or not (its own quantity band and a reason matching road delivery), or the allowance is absent; order and invoice agree with whether the 24 benches qualify.
- Options: (a, preferred) its own `RequiredItemLocationQuantity` with a minimum for a full truck load and a matching reason; (b) remove it.
- Needs decision: no
- From: broad, money

### retail/02#F16 · Low · Valdara's GTINs are in Lumeway's GS1 company prefix
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: Lumeway's GLN and the GTINs of Valdara's bench and side frame share the company prefix 9520610; across the world that prefix is Lumeway's (its GLNs 9520610900008 and 9520610900015 and its GRAIs 095206100000122… all use it; verified with grep), and other companies follow the same pattern (Brackenmere's GLN and GTINs under 9523710). The items are Valdara's (brand Valdara, manufacturer Valdara Industries, made in Urvania, GTIN issued by Codana in Urvania). Under the GS1 allocation rules the brand owner allocates the GTIN from its own prefix (own knowledge). Check digits are correct.
- Condition: Valdara's GTINs and Lumeway's GLNs/GRAIs are under different company prefixes, or the story states that Lumeway allocated the GTINs.
- Options: (a, preferred) a company prefix of Valdara's own for its GTINs; (b) state that the distributor allocated them.
- Needs decision: yes
- From: parties

### retail/02#F17 · Low · Codana: a small private limited company with a public-service contact
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cbc:IndustryClassificationCode` = `8299`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `SRU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- Why: Codana, the agency that issues GTINs and property identifiers, is a small SRU (private limited company) classified 8299, yet its contact is "Member services", a "Public service officer" in "Public services". A members' service points to a membership organisation (as GS1 member organisations are, ISIC 9411; own knowledge), a public-service officer to a public body; neither fits a private company, and name and department disagree.
- Condition: Codana's legal form, industry classification and contact describe the same kind of organisation.
- Options: (a, preferred) decide what Codana is (membership association, public agency or company) and align legal form, classification and contact; parties prefer a not-for-profit membership association; (b) if F18 reduces the issuer to ID and name, the question remains for the examples that describe Codana in full.
- Needs decision: yes
- From: parties, broad (contact part of its F9)

### retail/02#F18 · Low · Full master data of the GTIN issuer on line 1
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:ID` = `4160200261972596`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Codana Identification Agency SRU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `member@codana.example`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`
- Why: the issuer of the GTIN on line 1 carries Codana's full address, tax registration, legal entity, contact and electronic address; on line 2 the same issuer has ID and name only. Lumeway and Brightmarket do nothing with Codana's tax registration or contact; the data looks copied from master data (section 4.8), and the same issuer is described two ways in one document.
- Condition: the issuer carries what identifies it, the same way on both lines.
- Options: (a, preferred) reduce it to identifier and name, as on line 2.
- Needs decision: no
- From: broad (F9), parties (F10), context (F11, issuer part)

### retail/02#F19 · Low · Romance street name tagged as Bayvarran English
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`
- Why: the second rendering of Codana's street is tagged `languageID` `en-XB` but is an Italian-form name, not English. Parties refuted it: the world consistently renders Urvanian street names in Bayvarran English with Romance exonyms (verified: "Via delle Officine" 31 times, "Via del Magazzino" 6 times, "Via dei Codici" twice under `en-XB`), as English keeps foreign street names. Broad noted it as a possible world convention. Whether a tag `en-XB` is right for such an exonym is a convention the world has not documented; the earlier flows' merges (road, rail, cotton) kept the same question as Low/yes.
- Condition: every rendering is in the language its `languageID` names, or the exonym convention is documented.
- Options: (a, preferred) document the convention (an exonym used in Bayvarran English keeps `en-XB`); (b) a tag for the Romance form, or drop the second rendering (or the whole address, F18).
- Needs decision: yes
- From: broad (inside its F9; parties refuted), added as a finding by the merge for consistency with the earlier flows

### retail/02#F20 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the date `1996-01-01` is shared by 25 unrelated parties of the world in three countries (parties, lxml), among them Bayforth Forwarding, Harbourline Factoring, Codana, Brackenmere and Castrano, while the others have dates of their own (Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January is a filler, not a fact of the world.
- Condition: the registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) the party's real registration date from its history; (b) leave it out (also follows from F18).
- Needs decision: yes
- From: parties

### retail/02#F21 · Low · World item numbers that are valid GTIN-12
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: the world's item numbers (`schemeID` `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (recomputed for both: valid); read as GTIN-12 (GTIN-13 `0771020000027`) they lie in GS1 prefix 077, assigned to GS1 US (own knowledge), so they can be mistaken for real GTINs (rule "fictional values must not be mistaken for real ones"). `771020000027` occurs in 39 files (verified). No part raised it here; the earlier flows' merges (rail, road, plastics) kept it as Low/yes.
- Condition: the world item numbers cannot be read as valid GTINs, or their non-assignment is recorded from a GS1 source.
- Options: (a, preferred) a world item-number format that is not a valid GTIN; (b) record the verification.
- Needs decision: yes
- From: added by the merge (aligned with earlier flows)

### retail/02#F22 · Low · Urvanian customs tariff codes in a Bayvarran domestic catalogue
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the catalogue is from a Bayvarran distributor to a Bayvarran retailer for Bayvarra only; the national tariff codes are Urvania's (`listID` `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`), the export country's, which neither party uses in this trade. Context refuted it: the goods are of Urvanian origin and imported, and the world has no Bayvarran tariff list (verified: all 61 tariff codes over `*.xml` use the XU list). That explains why no Bayvarran code is given, but not why a domestic catalogue needs the Urvanian one.
- Condition: national tariff codes in the catalogue are those of a country whose customs the parties deal with, or they are absent.
- Options: (a, preferred) drop them (the HS code is enough); (b) a Bayvarran tariff code if Brightmarket needs one.
- Needs decision: no
- From: broad (context refuted)

### retail/02#F23 · Low · Dependent price tied to Coastal State while both prices apply in all of Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:DependentPriceReference/cac:LocationAddress/cbc:CountrySubentity` = `Coastal State`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: `LocationAddress` is "The reference location for this dependent price reference". Both the side frame's price and the bench price it depends on apply to all of Bayvarra and the catalogue has no state-specific price; naming Coastal State (where the buyer's store is) suggests that the 12.31 % relation holds only there. The percentage itself is right: 64 / 520 = 0.12308 = 12.31 %, and 12.31 % × 520 = 64.01, rounded to the stated 64 (recomputed).
- Condition: the reference location is the territory where both prices apply, or is absent.
- Options: (a, preferred) drop `LocationAddress` or set it to the country; (b) introduce state-specific prices (story change).
- Needs decision: no
- From: money, context

### retail/02#F24 · Low · Spare bench side frame classified as a general cast article, not as a part of seats
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[1]/cbc:CommodityCode` = `732599`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- XPath: `01-CatalogueRequest.xml:/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:Description` = `Outdoor furniture and its spare parts.`
- Why: the item is a "Spare side frame for the Serra bench", a part made for one seat. Under the HS and its interpretative rules, identifiable parts of seats of heading 9401 that are not parts of general use fall under 9401.99, not 7325.99 "Other cast articles of iron or steel" (own knowledge). The request 01 asks for heading 9401 with its spare parts, and the bench itself is under `940179`. Context checked 732599 as fitting a cast frame; tariff classification is a judgement the world should settle.
- Condition: the side frame's HS and national codes are those of parts of seats (940199 and its subdivision), or the example states why the frame is classified as a cast article.
- Options: (a, preferred) HS `940199` with the matching national line (if national codes stay, F22); (b) keep 7325 and accept the difference to 01 explicitly.
- Needs decision: yes
- From: logistics

## Checked and consistent
- Validity period, contract `LD-BM-SUPPLY-2026`, territory XB and the two items agree with 01; `LineCountNumeric` `2` matches the lines; header, line and price validity all end 2026-07-19.
- Line 1 ordering data: pallet of 4 (`ContentUnitQuantity`, increment, minimum 4, maximum 192 = 48 pallets), `DeliveryUnit` batch 4, `Package` `PX` quantity 4.
- Prices: 520 per bench (base 1 EA) and 64 per side frame, price list LD-PL-2026; the order and invoice use 520 (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `520`); the inventory report values 3 benches at 1560.00 = 3 × 520 (money).
- Tax: category E, 0 %, exemption RESALE under STT on both lines, as in the order and invoice.
- `ApplicableDeliveryPeriod` starts 2026-04-27, after issue plus the 3-day lead time; the order's delivery on 2026-04-30 qualifies.
- Bench physics (logistics, broad): 5 slats of 4.5 kg = 22.5 kg, 6.4 dm³ each at about 700 kg/m³ (e.g. 1800 × 90 × 40 mm); load 450 kg over three seats; seat height 450 mm within 440–460, below the back height 780 mm; four benches of 1800 × 620 × 780 mm on one pallet plausible; 0.4 kg packaging waste per bench.
- GTINs `9520610000012`, `9520610000029` and the GLNs pass the check digit; prefix 952 is GS1's demonstration range.
- HS `940179` and CPC `38111` fit the bench; warranty (five years, maker Valdara as warranty party) agrees with both warranty texts.
- Roles: Lumeway provides, Brightmarket receives; line parties (warranty party, manufacturer, information content provider) are the parties the lines describe; Brightmarket and Lumeway are described identically in every example of the flow (parties).
- Header and line references `LD-GTC-2026`, `LD-PL-2026`, `VI-DS-B180`, `VI-LCA-2025`, `VI-RM-B180` are used with the same meaning in other examples (logistics).

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:ItemComparison/cbc:PriceAmount` = `520`: a comparison that repeats the price — refuted by broad (the orderable unit is a pallet, so a per-each comparison is what ItemComparison is for); not followed by the merge, kept as F13 (from broad).
- `/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`: contradicts an active, newly added item — refuted because UBL defines it as an item that "may be a replacement", which a newer casting revision can be while the current one is still sold (from broad; see also "Refuted in the merge").
- `/Catalogue/cbc:RevisionTime` = `09:00:00`: inconsistent with the issue at 17:28 — refuted: a revision before the issue on the same day, after the request at 08:42, is plausible (from broad, context; recomputed: 08:42 < 09:00 < 17:28).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:TradingRestrictions` = `Not sold to consumers.`: contradicts Brightmarket selling benches to consumers (21-PurchaseReceipt) — refuted because it restricts Lumeway's own sales, not the retailer's resale (from broad, context).
- `/Catalogue/cbc:Note` = `Prices for trade customers, before sales tax.`: contradicts the exempt category — refuted because it says the prices exclude sales tax, which is true whatever the category (from money).
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`: wrong list for a discount — refuted, 95 "Discount" in UN/EDIFACT 5189 (from money).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`: not English though tagged `en-XB` — refuted by parties (world convention of Romance exonyms in Bayvarran English); not followed by the merge, kept as the Low/yes F19 (from parties).
- `/Catalogue/cac:CatalogueLine[1]/cac:WarrantyParty/cac:PartyName/cbc:Name` = `Valdara Industries`: does the warranty party fit — it does, the warranty is "from the maker" (from parties).
- `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: misuse of BlockName — refuted, a business park fits the definition (from parties).
- `/Catalogue/cac:SourceCatalogueReference/cbc:ID` = `VI-CAT-2026`: broken reference — refuted, Valdara's own catalogue to its distributor, outside the flow (from logistics).
- `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`: unresolved — refuted as a reference, an item of an earlier catalogue need not be an example (from logistics; its "existing catalogue" is part of F2).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteMeasure` = `0.4`: 1.6 kg per pallet of four — plausible (from logistics).
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode`: Urvanian tariff code — refuted by context (Urvanian origin, no Bayvarran tariff list); not followed, kept as F22 with the argument (from context).
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredRelatedItem/cbc:ID`: the spare frame "requires" the bench — refuted, a spare part is only of use with its bench (from context).
- `/Catalogue/cac:CatalogueLine[1]/cac:KeywordItemProperty/cbc:Value`: repeats Item/Keyword — refuted, the line-level keyword property is its meaning (from context).

## Refuted in the merge
### context/F7 · Low · An active spare part that is replaced and replacing at once
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacementRelatedItem/cbc:ID` = `VI-C180-2026`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:ReplacedRelatedItem/cbc:ID` = `VI-C180-2024`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cbc:LifeCycleStatusCode` = `ACTIVE`
- The part's finding: the line sells `VI-C180`; ReplacementRelatedItem says `VI-C180-2026` "may be a replacement for the item in this catalogue line", ReplacedRelatedItem says this item replaces `VI-C180-2024`. A 2026 successor of a part offered as active and orderable needs a reason (phase-out, interchangeability) that nothing gives, and the replaced item is said to be in an existing catalogue that does not exist. Condition: the replacement relations describe a situation the line explains, or are absent. Options: keep only the relation that has a story, drop the other. Needs decision: no.
- Refuted because: the "existing catalogue" half is the same problem as F2 and is kept there. The other half rests on the definition, which says the related item "may be a replacement": a newer casting revision that can be used in place of the current one is exactly that, and it does not require the current part to be phased out (broad's refutation). A chain 2024 → current → 2026 of a casting is an ordinary revision history; nothing in the document contradicts it.

## Changed in the merge
- broad/F1, logistics/F1, context/F2 → F1: combined; logistics' material-mass calculation added.
- broad/F5 (Low/yes), logistics/F2 (Medium/yes), context/F1 (High/yes) → F2: Medium. Not High because the values can be reconciled by reading (internal draft 0.9; an existing catalogue to other customers); not Low because the request and the answer describe different stories. ReplacedRelatedItem and the request's reference grouped in.
- broad/F2, parties/F1, context/F5 → F3: combined; context's preference (en-XB) kept as option (b), drop preferred as in all earlier flows.
- broad/F4, parties/F2 → F4; broad/F3, parties/F3 → F6: combined.
- context/F6 (Low) → F7: raised to Medium, aligned with the rail, road and air merges (the code and its text equivalent disagree: section 4.4).
- context/F12 → F9: "Needs decision" no → yes, aligned with the air and utilities merges.
- parties/F5, F6 (Low/yes), F7 and the party part of context/F11 → F10: one finding; parties/F6's yes set to no (see 01#F6); context's tax registrations not cited (the catalogue's tax categories depend on them).
- broad/F10, parties/F8 → F11; broad/F11, context/F10 → F12: combined.
- money/F3, context/F9 → F13: combined; broad's refutation answered in the Why.
- broad/F6 (yes), context/F8 (no) → F14: yes kept (whether Lumeway suggests the buyer's own set is a story question).
- broad/F7, money/F1 → F15: combined.
- parties/F9 and the contact part of broad/F9 → F17; broad/F9 (rest), parties/F10 and the issuer part of context/F11 → F18.
- F19 (exonym tagging) and F21 (GTIN-like item numbers) added by the merge, aligned with the earlier flows; F19 from broad's remark and parties' refutation.
- money/F2, context/F13 → F23: combined.
- context/F7 → Refuted in the merge (its catalogue half folded into F2).

## Outside this review
- `tender/15-Tender.xml` gives `VI-C180-2026` as a replacement item for the whole Serra 180 bench, while here it replaces the side frame casting (from broad): belongs to that example's review.
- 03-CataloguePricingUpdate changes the side frame's price to 58 without updating the dependent price percentage (from money): a finding of 03 (03#F11).
