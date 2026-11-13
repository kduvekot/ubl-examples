# LLM review: 08-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/08-Order.xml`, Git blob `4b9ab738473f9a4b2d8102ca056f226654c8875b` (committed)
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

### retail/08#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each, the factor gives 0.82 × 1 = 0.82 kg CO2e per bench, while the value is 96 kg per bench. 96 / 0.82 = 117.1, which matches no quantity in the document (the bench's material consumption is 34 + 22.5 = 56.5 kg; 0.82 × 56.5 = 46.3). The values are those of 02-Catalogue. The same factor occurs in 39 XML files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`, recounted in the merge).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base: the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg; (c) drop the emission from the order altogether (see F13).
- Needs decision: no
- From: broad, context, logistics

### retail/08#F2 · High · Taxable amount ignores the order's own document-level allowance
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12480.00`
- XPath: `/Order/cac:AllowanceCharge/cbc:Amount` = `624.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11856.00`
- XPath: `18-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `11856.00`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied to calculate the tax amount". The order deducts a document-level promotion support of 624.00 (recomputed: 0.05 × 12480.00 = 624.00), so the net amount is 12480.00 − 624.00 = 11856.00, which is also the payable amount (tax 0.00 at 0 %). The tax subtotal uses the gross line total instead, and the invoice for the same order and the same allowance uses 11856.00, so order and invoice disagree on the tax base. The tax amount is unaffected only because the rate is 0 %. The allowance carries no tax category of its own.
- Condition: the order's taxable amount equals the line extension amount minus the document-level allowance (11856.00), as in the invoice.
- Options: (a, preferred) taxable amount 11856.00, and a tax category (E, RESALE) on the allowance as in the invoice, so the allocation is explicit; (b) move the promotion support to the line, so that the line extension amount carries it.
- Needs decision: no
- From: broad, money

### retail/08#F3 · Medium · Language codes in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code that `Language/cbc:ID` already holds and names no locale; ISO 639 is a list of languages, not of locales. Recounted in the merge: 362 `Language/LocaleCode` elements with this value in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; the parties part's 364 also counted one `PreferredLanguageLocaleCode` and one `TenderLanguageLocaleCode`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (nothing in the order depends on a locale); (b) a locale such as English as used in Bayvarra from a locale list (e.g. BCP 47), if a regional variant matters. Fix it in the party master data, so it applies everywhere.
- Needs decision: no
- From: broad, context, parties

### retail/08#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is an entrance of the distribution centre at Distribution Drive 43, not a street; it matters only to vehicles, and a postal address holds nothing that only matters for vehicles. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`; `-rl` for the files).
- Condition: no `AdditionalStreetName` of Lumeway holds the gate; where a transport document needs the gate, it is given in that document's pickup or despatch location.
- Options: (a, preferred) drop it from the postal address (party master data) and give the gate where a vehicle needs it; (b) if Bayvarra's address format makes the gate part of the postal address, record that in the format definition, and the finding is dismissed.
- Needs decision: no
- From: broad, parties

### retail/08#F5 · Medium · DataSendingCapability describes the e-document channel, not purchase-card data
- XPath: `/Order/cac:SellerSupplierParty/cbc:DataSendingCapability` = `UBL 2.5 over the trade accord network`
- XPath: `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: `SupplierParty/DataSendingCapability` is "Text describing the supplier's ability to send invoice data via a purchase card provider (e.g., VISA, MasterCard, American Express)". Nothing in the flow is paid by purchase card: the order and the invoice use credit transfer (`18-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`). The value describes the network over which the supplier exchanges UBL documents, which the parties' `ElectronicAddress` already gives. The element occurs in this example only (`grep -rl --include='*.xml' DataSendingCapability world/examples`, recounted).
- Condition: `DataSendingCapability` is absent, or describes the supplier's ability to send invoice data through a purchase-card provider in a flow where a purchase card is used.
- Options: (a, preferred) remove it; (b) give the element a real case in a flow with a purchase card.
- Needs decision: no
- From: money, context, parties

### retail/08#F6 · Medium · A life-cycle boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty". `CRADLETOGATE` (list `EmissionBoundaryCode`) is the system boundary of a product footprint, which has nothing to do with the fullness of transport equipment. 39 XML files carry it (`grep -rl --include='*.xml' CRADLETOGATE world/examples | wc -l`). UBL 2.5 has no element for the system boundary; that gap is a candidate for the write-up to the UBL TC.
- Condition: `FullnessIndicationCode` holds no system-boundary code.
- Options: (a, preferred) drop it; the boundary stays in the life-cycle description; record the missing element for the TC write-up.
- Needs decision: no
- From: context (combined there with LocaleCode; split in the merge)

### retail/08#F7 · Medium · Life-cycle stage code says manufacturing (A3), the description says ore to factory gate (A1–A3)
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: the world's `LifecycleStageCode` list defines `MANUFACTURING` as "Making the product (EN 15804 module A3)" and `SOURCING` as "Raw material supply and its transport (EN 15804 modules A1 and A2)". The description, and the emission description ("Mining, steel making, casting, galvanising, sawing and the transport between them"), cover A1 to A3. The code and the text next to it describe different stages.
- Condition: the stage code and the stage description cover the same stage(s).
- Options: (a, preferred) omit the code and keep the description; (b) two emission entries (SOURCING and MANUFACTURING) with their shares of the 96 kg.
- Needs decision: no
- From: added by the merge (no part raised it), aligned with retail merges a and c and with road and rail

### retail/08#F8 · Low · Substitute proposed in a colour the referenced catalogue does not offer
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Park bench Serra 180, moss green`
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRN`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the buyer proposes the bench in moss green as a substitute, as the seller's item `LD-10442` with extension `GRN`. The catalogue the order refers to offers the bench only in Ferro grey (`ExtendedID` `GRY`, colour property with the single value Ferro grey); no XML file of the world has the extension `GRN` (`grep -rl --include='*.xml' '<cbc:ExtendedID>GRN'`: this file only). The context part refuted this: a buyer may propose an alternative the catalogue does not carry, and the seller can decline it. Against that, the buyer quotes the seller's own item number with a variant extension the seller never assigned. The merge cannot settle whether this is a problem.
- Condition: a proposed substitute is an item or variant the seller offers, or the story says the buyer asks for a variant outside the catalogue.
- Options: (a, preferred) add the green variant to the catalogue (another list value of the colour property, with its own identifiers), so the substitution is possible; (b) drop the substitute line item; (c) keep it and leave out the seller's extended ID, describing the wish in the name.
- Needs decision: yes
- From: broad (context: considered and refuted)

### retail/08#F9 · Low · Substitute line item has the same line ID as the ordered item
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cbc:ID` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: `LineItem/ID` is "An identifier for this line item, assigned by the buyer". The proposed substitute (moss green) is a different line item from the ordered grey bench, but has the same ID, so a response cannot tell them apart by ID. Not High: both sit in the same order line and in different elements, so nothing that refers to them is broken today.
- Condition: the substitute has an ID of its own.
- Options: (a, preferred) e.g. `1.1` for the substitute.
- Needs decision: no
- From: context

### retail/08#F10 · Low · No requested delivery date in an order placed for a promotion
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11`
- Why: the order refers to the spring promotion (06-RetailEvent, starting 2026-05-11), but its `Delivery` gives only a location and a party, no requested delivery period. The distributor must infer the date from the catalogue's 3-day lead time and the event; the transport request 11 and the despatch advice 12 then fix a date the order never asked for.
- Condition: the order states when the goods are wanted, consistent with the promotion start and the catalogue's delivery period, or the story says the date is agreed elsewhere.
- Options: (a, preferred) `Delivery/RequestedDeliveryPeriod` ending well before 2026-05-11 (e.g. 2026-04-29 to 2026-05-04); (b) a note referring to the catalogue's lead time.
- Needs decision: no
- From: broad, context, logistics

### retail/08#F11 · Low · Delivery-terms location given as text naming the company, although the place has a GLN
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: for DDP the named place is where the seller's obligations end. It is the same goods-in as the delivery location, which has GLN `9522610900019`, but here it is only a free-text description that starts with the company name.
- Condition: the DDP named place identifies the same goods-in as the delivery location (by its GLN, or a description of the place).
- Options: (a, preferred) `DeliveryTerms/DeliveryLocation/ID` `9522610900019`; (b) drop the delivery terms' location if the delivery location is meant.
- Needs decision: no
- From: logistics

### retail/08#F12 · Low · "Third-party" account ID that carries the buyer's own prefix
- XPath: `/Order/cac:BuyerCustomerParty/cbc:AdditionalAccountID` = `BM-LUM-01`
- Why: in `CustomerParty`, `AdditionalAccountID` is "An identifier for the customer's account, assigned by a third party". `BM-LUM-01` follows Brightmarket's own numbering (`BM-6120` as its `CustomerAssignedAccountID`, `BM-LOGO-2024`, `BM-SIG-…`) and names Lumeway; no third party that keeps an account for Brightmarket appears in the order.
- Condition: an `AdditionalAccountID` of the buyer is assigned by a third party evident in the story, or it is absent.
- Options: (a, preferred) drop it; (b) make it a third party's ID (e.g. of the factor in 18-Invoice) with a reason.
- Needs decision: no
- From: context, parties

### retail/08#F13 · Low · The order carries the item's full catalogue description
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:EnvironmentalEmissionTypeCode` = `CO2E`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- Why: the order identifies the bench by the buyer's, seller's, manufacturer's and standard identifiers and by the catalogue line, then repeats the catalogue's full description: dimensions with tolerances, load test, footprint, circularity profile, Urvania's customs tariff code (not used between two Bayvarran parties) and the distributor's own wording ("from the distributor's stock") in a document written by the buyer. The order does nothing with any of it.
- Condition: the ordered item carries its identifiers and what the order depends on (name, colour variant, catalogue reference).
- Options: (a, preferred) reduce the item to name, identifiers, the ordered variant and the catalogue reference.
- Needs decision: no
- From: broad, context (context had it together with the party master data; split in the merge, as in road and rail)

### retail/08#F14 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: an order between two trading partners uses neither Brightmarket's logo, consumer web shop and social-media profile, nor the share capital of the parties, nor Lumeway's customs trader number: every movement of the flow is inside Bayvarra and no example of the flow is a customs document. The values are Lumeway's and Brightmarket's master data, identical in every example of the flow. On `CorporateStockAmount` the parties part also notes that UBL defines it as "The number of shares in the capital stock of a corporation" while its data type is an amount; the world uses it for the share capital. That conflict is a candidate for the TC write-up; it does not change what this order should carry (parties part: Needs decision yes; set to no in the merge, as in furniture, road and rail, because dropping unused data changes no story).
- Condition: the parties in the order carry only data the order uses.
- Options: (a, preferred) leave logo, web shop, social media, share capital and customs trader number out of this document (keep logo, shop and social media for the consumer documents 21 and 22, the customs number for import and export flows); record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context, parties

### retail/08#F15 · Low · Brightmarket's party contact: buying office, customer service officer and sales at once
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: the party contact is named "Buying office" (buying@brightmarket.example), but its job title and department are those of a seller's customer service; the three contradict each other. As the buyer, the buying office fits the role. The order's role contacts (`BuyerContact`, `DeliveryContact`, `AccountingContact`) fit their roles; only the party contact is wrong. The same contact is used in every role Brightmarket has (41 XML files contain `<cbc:Name>Buying office</cbc:Name>`, parties part's count).
- Condition: name, job title and department of the party contact agree with each other and with Brightmarket's role in the order.
- Options: (a, preferred) a buyer's job title in purchasing for the master contact, and role-specific contacts where Brightmarket's role is not purchasing.
- Needs decision: no
- From: broad, parties

### retail/08#F16 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: Lumeway's GLN and the bench's GTIN share the company prefix 9520610, which is Lumeway's across the world (its GLNs and the SSCCs of `12-DespatchAdvice.xml` start with it). The item is Valdara's: brand Valdara, manufacturer Valdara Industries (Urvania), origin Urvania. Under GS1's allocation rules (own knowledge of the parties part) the brand owner allocates the GTIN from its own prefix; a distributor does so only when the brand owner has none. Check digits are correct (`check_ids.py`, recomputed in the merge).
- Condition: Valdara's GTINs and Lumeway's GLNs/SSCCs/GRAIs are under different company prefixes, or the story states that Lumeway allocated the GTINs.
- Options: (a, preferred) give Valdara its own company prefix; (b) state in the story that the distributor allocated the GTINs.
- Needs decision: yes
- From: parties

### retail/08#F17 · Low · Signature with an ID and a signatory only
- XPath: `/Order/cac:Signature/cbc:ID` = `BM-SIG-26-0424`
- Why: the signature has no method, no attachment and no date: it records no signature. This is a world-wide convention (137 of 147 `Signature` aggregates hold only ID and signatory, lxml count of the air merge), so changing it is a decision.
- Condition: a signature carries what makes it one, or is absent.
- Options: (a, preferred) drop it; (b) add the signature method or attachment.
- Needs decision: yes
- From: context (Needs decision no there; set to yes, aligned with retail merges a and c, air and utilities)

### retail/08#F18 · Low · World item number that is a valid GTIN-12
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: the world's item number (`schemeID` `urn:ubl-examples:world:item`) is twelve digits with a valid GS1 mod-10 check digit (recomputed in the merge: 7), so it reads as a GTIN-12 in GS1's US/Canada range. Fictional values must not be mistaken for real ones; whether the number is assigned in GS1's register was not checked.
- Condition: the world item number cannot be mistaken for a real GTIN, or its absence from GS1's register is recorded.
- Options: (a, preferred) a world item-number format that is not a valid GTIN; (b) record a check against GS1's register in the sources.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail merges a and c, rail, road and plastics

## Checked and consistent
- Arithmetic, redone in the merge: 24 × 520 = 12480.00 = line and document `LineExtensionAmount`; 0.05 × 12480.00 = 624.00 = allowance; 12480.00 − 624.00 = 11856.00 = `PayableAmount`; tax 0.00 at 0 %.
- 24 benches = six pallets of four, within the catalogue's 4–192 band and its increment of 4; price 520 per each = the catalogue's trade price (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`).
- Catalogue reference and the item's catalogue document reference `LD-CAT-26-0218` resolve to 02-Catalogue; the retail event `BS-RE-26-0222` resolves to 06-RetailEvent.
- Payment terms (30 days net), delivery terms DDP and tax category E with RESALE under STT agree with 02-Catalogue and 18-Invoice; accounting code 6120 "Garden department" is the one the invoice carries.
- Role contacts fit their roles: the buyer's buyer, goods-in and accounts payable contacts; the seller's key account manager, dispatch office and accounts receivable.
- `TransactionConditions` `LD-TC-01` with `ACCEPTED`: the buyer accepts the seller's conditions named in the catalogue.
- GLNs `9520610900008`, `9522610900002`, `9522610900019`, GTIN `9520610000012` and item number `771020000027` pass the GS1 check digit (recomputed in the merge).
- Brightmarket and Lumeway are described identically in every example of the flow (parties part, leaf by leaf); register IDs agree with `CompanyID` and the endpoint IDs; each party is registered for STT in the state of its address.

## Considered and refuted
- `/Order/cac:ValidityPeriod/cbc:EndDate` = `2026-04-26`: suspected too short, or before the delivery on the 30th — refuted because the validity period is the period in which the order may be accepted, and 10-DocumentStatus reports acceptance on 2026-04-26 (from broad, context).
- `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`: suspected incomplete without an account — refuted because in an order the buyer only announces how it will pay; the payee's account follows in the invoice (from broad).
- `/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Promotion support`: suspected that the 5 % has no basis — refuted because an order may carry an allowance agreed for the promotion it refers to, and the seller's invoice confirms the same 5 % (from money).
- `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.03`: the catalogue's "Full container" discount not applied — refuted because six pallets on a truck are not a full container; the unclear condition belongs to the catalogue's review (from money).
- `/Order/cac:BuyerCustomerParty/cbc:CustomerAssignedAccountID` = `BM-6120`: suspected the cost centre used as account ID — refuted because the definition lets the customer identify its account by its own number, and `AccountingCostCode` 6120 agrees (from parties).
- `/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Telephone` = `+999 2 38 2511 0411`: goods-in, buyer and buying office share one number — refuted: a store's switchboard number is plausible (from parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`: checked whether the delivery party fits — it does: the buyer receives the goods at its own goods-in (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits it, and `PlotIdentification` "Plot 14" is the land parcel (from parties).
- The context part's refutation of the green substitute (a buyer may propose an alternative the catalogue does not carry) was not followed; see F8, where both arguments stand.

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1: combined; option (c) from context added.
- broad/F2, money/F1 → F2: combined; the invoice comparison from money added.
- broad/F3, parties/F1, context/F3 (LocaleCode half) → F3: combined; count corrected to 362 in 213 files (parties' 364 included two other elements).
- context/F3 → split into F3 (LocaleCode) and F6 (CRADLETOGATE): two elements, two problems.
- broad/F4, parties/F3 → F4: combined.
- money/F2, context/F2, parties/F2 → F5: combined.
- F7 (MANUFACTURING) and F18 (world item number): added by the merge, aligned with the other retail merges and the earlier flows.
- broad/F5 → F8: kept Low/yes; context's refutation added as the counter-argument.
- broad/F7, context/F5 (item half) → F13; context/F5 (party half), parties/F5, F6, F9 → F14: item data and party data split into two findings (as road, rail); parties/F6 (CorporateStockAmount) Needs decision yes → no, folded into F14 with its TC note, aligned with retail a/c and earlier flows.
- broad/F6, context/F6, logistics/F2 → F10: combined.
- context/F4, parties/F4 → F12: combined.
- broad/F8, parties/F7 → F15: combined.
- context/F8 → F17: Needs decision no → yes (world-wide convention, aligned with retail a/c, air, utilities).
