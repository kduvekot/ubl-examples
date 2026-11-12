# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/01-GoodsItemPassport.xml`, Git blob `b7c20e53167125d7f3ee0260e4bdca609da4e0b0` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### carnet/01#F1 · High · Every counterfoil already "stamped by customs" when the carnet is issued
- XPath: `/GoodsItemPassport/cbc:IssueDate` = `2026-05-25`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:Note` = `Stamped by customs.`
- Why: The Goods Item Passport is "a document providing a temporary export license, also knowned as
  an ATA Carnet", issued by the chamber on 2026-05-25 with a validity starting the same day
  (`/GoodsItemPassport/cac:ValidityPeriod/cbc:StartDate` = `2026-05-25`). At issue, no customs office
  has seen the goods: exportation, importation, re-exportation and re-importation all lie in the
  future (the flow's own later documents are dated July and August 2026). Yet all four
  counterfoils state that they were stamped by customs, including the re-importation in Urvania that
  `04-ProofOfReexportation.xml` only reports in August. The issued document thus states events that
  have not happened.
- Condition: no counterfoil of the carnet as issued on 2026-05-25 states a customs stamp or other
  customs action that can only happen after the issue.
- Options: (a, preferred) drop the "stamped" notes, so the counterfoils describe the blank vouchers
  as issued; (b) if the example is meant to show the carnet at the end of its life, say so (a later
  version, `VersionID` and status) and give the stamps in a way that matches 02–04 (see F2).
- Needs decision: yes (which moment of the carnet's life the example shows)

### carnet/01#F2 · High · Re-exportation counterfoil "stamped" contradicts the claim of the island's customs
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`
- Why: Counterfoil REEXP-1 (re-exportation at "Customs office, Selanu airport") says it was stamped.
  The whole rest of the flow rests on the opposite: the island's customs found no re-export stamp
  (02), the guarantor chases the proof (03), and the proof is given by the re-importation counterfoil
  instead (04). If REEXP-1 had been stamped, the importation would have been discharged and there
  would be no claim.
- Condition: no example of the flow states that the re-exportation counterfoil REEXP-1 was stamped,
  unless the flow's story is changed so that the claim has another cause.
- Options: (a, preferred) REEXP-1 carries no stamp (no note, or a note saying it was not
  discharged); together with F1 this is simplest if the counterfoils are shown blank at issue;
  (b) change the cause of the claim in 02–04.
- Needs decision: no

### carnet/01#F3 · High · Emission factor × base quantity does not give the emission value
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines ValueFactorNumeric as "a numeric factor used to calculate the value measurement
  (e.g., emissions per unit of activity)" and ValueBaseMeasure as "the base quantity to which the
  value factor applies". With a factor of 0.82 per 1 each, the value would be 0.82 kg, not 96 kg
  CO2e per bench. No other quantity in the item explains 0.82 (96/0.82 ≈ 117, which matches neither
  the bench's weight of 41.5 kg nor its 56.5 kg of steel and wood). 96 kg CO2e itself is plausible
  for about 34 kg of steel and 22.5 kg of hardwood cradle to gate (own knowledge: about 2 kg CO2e
  per kg of steel). The same triple 96 / 0.82 / 1 EA occurs in 39 examples (grep -rl
  '<cbc:ValueFactorNumeric>0.82<' --include='*.xml' world/examples).
- Condition: ValueFactorNumeric × ValueBaseMeasure = ValueMeasure, with the factor's unit implied by
  the base (e.g. 96 kg per 1 EA), or the factor and base are absent.
- Options: (a, preferred) factor 96 per 1 EA, or drop factor and base, since the value is a product
  footprint and not activity × factor; (b) a base the factor really applies to (e.g. 0.82 kg CO2e
  per kg of a stated material mass that gives 96).
- Needs decision: no

### carnet/01#F4 · Medium · An emission system boundary in FullnessIndicationCode
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL defines FullnessIndicationCode as "a code signifying whether a piece of transport
  equipment is full, partially full, or empty. This indication is used as a parameter when
  calculating the environmental emission." The value comes from the world's EmissionBoundaryCode
  list (cradle to gate, EN 15804 A1–A3), a system boundary of a product footprint; no transport
  equipment is involved in a bench's manufacturing footprint. Other examples use the element for
  its meaning (LoadTypeCode FCL). The boundary is already stated in prose in
  `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription`
  = `From the ore at the mine to the bench leaving the factory gate.`. The same code in this
  element occurs in 39 examples (grep -rl 'EmissionBoundaryCode">CRADLE' --include='*.xml').
- Condition: FullnessIndicationCode is absent here, or carries a transport-equipment fullness code.
- Options: (a, preferred) drop it; the boundary is expressed by LifecycleStageCode/Description;
  (b) if the boundary must be coded, find the element whose definition covers it, or record the
  gap as a finding for the UBL TC.
- Needs decision: no

### carnet/01#F5 · Medium · Customs administrations described as companies in a commercial register
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania and the Island Customs Service (ISIC 8411, general
  public administration) are state authorities. UBL's CorporateRegistrationScheme is "the corporate
  registration scheme used to register the party" and CompanyLiquidationStatusCode "the party's
  liquidation status"; an authority is not registered as a business ("a register of businesses",
  the world's list) and cannot be in liquidation. The same description of these two parties occurs
  in 12 (Urvania) and 9 (Lisavu) examples (grep -rl for the party name, then for
  'CorporateRegistrationTypeCode…>COMMERCIAL', over *.xml).
- Condition: neither customs party is described as registered in a commercial register or with a
  liquidation status.
- Options: (a, preferred) give public bodies only what applies to them (name, identifier, perhaps
  the legal basis in CompanyLegalForm), without a corporate registration scheme or liquidation
  status; (b) a world register type for public bodies, if the world has one.
- Needs decision: yes (how the world registers public bodies)

### carnet/01#F6 · Medium · A province in Region
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province, a country's administrative subdivision, belongs in
  CountrySubentity ("the territorial subdivision of a country"). 104 examples carry
  `<cbc:Region>Province…` (grep -rl --include='*.xml').
- Condition: the province is in CountrySubentity (and, if wanted, its code in
  CountrySubentityCode), not in Region.
- Options: (a, preferred) move it to CountrySubentity; (b) drop it if the address format of
  Urvania does not use it.
- Needs decision: no

### carnet/01#F7 · Low · Final re-exportation date on the exportation counterfoil, set at issue
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- Why: UBL: "Final date of re-exportation, if less than the overall validity period". Under the ATA
  system (own knowledge: Istanbul Convention, Annex A) the time limit for re-exportation is fixed by
  the customs of the country of temporary admission, on the importation voucher, when the goods are
  imported. Here it sits on the exportation counterfoil and is known on the day of issue. The note
  "to come back within six months" does not explain the date either: six months after any
  importation on or after the issue date ends on 2026-11-25 or later.
- Condition: the final re-exportation date, if present, is on the importation counterfoil IMP-1 (the
  one the importing customs fills in), or the example explains why the exporting side fixes it.
- Options: (a, preferred) move it to counterfoil IMP-1; (b) drop it.
- Needs decision: no

### carnet/01#F8 · Low · Master data copied into a carnet that does nothing with it
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ProductDocumentationDocumentReference/cbc:ID` = `VI-RM-B180`
- Why: A carnet's general list identifies the goods for customs (description, quantity, weight,
  value, origin, marks) and its holder and guarantors. The holder's listed shares and share
  capital, its warehousing provider (Castrano Logistics, who plays no part in the temporary
  export), the item's search keywords, warranty, product carbon footprint, circularity profile,
  repairability and maintenance data, and the property groups of the catalogue serve no purpose
  of this document (rule "no fillers", IND5). They look copied from the party's and the item's
  master data.
- Condition: every element of holder and item in the carnet serves identifying the goods or the
  parties for the temporary export.
- Options: (a, preferred) keep only the customs identification of the goods and the parties;
  (b) keep an element where the story gives the carnet a reason for it, and state that reason.
- Needs decision: yes (affects coverage)

### carnet/01#F9 · Low · Name parts of the accompanying representative look like fillers
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:MiddleName` = `Ilse`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:OtherName` = `Mara`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:NameSuffix` = `Jr`
- Why: The representative "who accompanies the Goods" is Ing. Davide Orsenna. Every optional name
  part UBL offers is filled: a middle name, a "second family name" (OtherName) and the suffix "Jr".
  Nothing in the example uses them, and together they read as coverage rather than as a person
  (two given-name-like names on a person whose other renderings use none). The identity data a
  border crossing may need (passport, nationality) is already there.
- Condition: each name part present belongs to the person's name as the world describes it.
- Options: (a, preferred) keep first and family name, title and passport; drop the rest unless the
  world gives this person those names; (b) keep them and give the person a naming convention in
  the world that explains them.
- Needs decision: yes

### carnet/01#F10 · Low · "Mobile on the road" gives the office landline
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Name` = `Mobile on the road`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: The representative's contact is named as a mobile for use while travelling with the goods,
  but its number is the holder's order-desk telephone; the holder's cellular number is a different
  one.
- Condition: the representative's travelling contact number is a mobile number of that person (or
  the contact's name no longer says it is a mobile).
- Options: (a, preferred) a mobile number of the person; (b) rename the contact.
- Needs decision: no

### carnet/01#F11 · Low · The holder's contact is the order desk
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The holder is the temporary exporter answerable for the carnet; its contact for the carnet
  is the export or customs function (the representative is in "Export sales"), not the desk that
  takes customers' orders.
- Condition: the holder's contact is the function that handles the carnet (export, customs or
  shipping).
- Options: (a, preferred) the export or customs desk; (b) drop the contact, the representative
  already gives one.
- Needs decision: no

### carnet/01#F12 · Low · English renderings of addresses tagged with the issuer's region, not the address's
- XPath: `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The English street and city names of the Lisavan parties are tagged `en-XU` here, while
  02 and 03 tag the very same address `en-XL` (and tag the Urvanian addresses `en-XL`). The region
  subtag follows the issuing country of the document, so the same address is described differently
  in each example. Separately, the Urvanian "English" renderings are Italian ("Piazza del Mercato",
  "Via delle Officine", "Valico di Confine"); 103 examples carry such Via/Piazza/Valico names under
  an `en-X?` tag (grep -rlE 'languageID="en-X.">(Via|Piazza|Valico) ' --include='*.xml').
- Condition: the same address is tagged the same way in every example, and each rendering is in the
  language its languageID names.
- Options: (a, preferred) tag each rendering by the address's own country (en-XL for Lisavu), and
  either translate the Italian names or tag them as the language they are in; (b) if the world
  decided that Urvanian English keeps Italian street names, record that decision.
- Needs decision: yes (the world's language convention)

### carnet/01#F13 · Low · References that give only an ID
- XPath: `/GoodsItemPassport/cac:AdditionalDocumentReference/cbc:ID` = `SCC-FAIR-26-INV`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionFactorDocumentReference/cbc:ID` = `VI-LCA-2025`
- Why: None of these documents exists in the examples, and the reference does not say what it is
  (the additional reference is presumably the fair's invitation from the Selanu chamber, which
  would be the reason for the temporary export). A reader cannot tell what they refer to.
- Condition: each remaining reference says what kind of document it is (DocumentType or
  DocumentTypeCode, with issuer or date where useful).
- Options: (a, preferred) add the document type; (b) drop references the carnet does not need
  (see F8).
- Needs decision: no

### carnet/01#F14 · Low · Chambers of commerce described as companies in a commercial register
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The two chambers (ISIC 9411, membership organisations) are registered as businesses with a
  liquidation status. Chambers are associations or public-law bodies; the world's
  CorporateRegistrationTypeCode list has an ASSOCIATION register, yet COMMERCIAL is the only value
  used in all examples (633 occurrences).
- Condition: each chamber is described according to what it is in the world (association register,
  public body, or a commercial register only if the world says so).
- Options: (a, preferred) the association register; (b) as for the public bodies in F5.
- Needs decision: yes

### carnet/01#F15 · Low · Wrong definitions of StatusCode, Status and VersionID in the model
- XPath: `/GoodsItemPassport/cbc:StatusCode` = `VALID`
- XPath: `/GoodsItemPassport/cbc:Status` = `Issued`
- XPath: `/GoodsItemPassport/cbc:VersionID` = `1`
- Why: UBL 2.5 defines StatusCode in GoodsItemPassport as "The reason for importing the goods,
  expressed as a code", Status as "The reason for importing the goods, expressed as text", and
  VersionID as "the current version of this request for proof". The example uses them for the
  carnet's record status and version, which is the evident intent of the element names but not
  their definitions. Under the semantic-conformance rule this is either a use against the
  definition or a defect of the model to report.
- Condition: either the example no longer uses these elements against their definitions, or the
  definitions are recorded as a model defect in the findings for the OASIS UBL TC.
- Options: (a, preferred) record as model defect and keep the values; (b) drop StatusCode/Status.
- Needs decision: yes

### carnet/01#F16 · Low · Transit through Bayvarra without transit counterfoils
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransitCountry/cbc:IdentificationCode` = `XB`
- Why: The consignment is routed through Bayvarra, but the carnet has only exportation, importation,
  re-exportation and re-importation counterfoils. An ATA carnet used for transit through a third
  customs territory carries transit vouchers (own knowledge), unless the Trade Accord makes XU–XB a
  single customs territory or waives them.
- Condition: either the carnet has transit counterfoils for Bayvarra, or the world's rules exempt
  transit through Bayvarra and the example does not contradict them.
- Options: (a) add transit counterfoils; (b) confirm the exemption from the world's rules.
- Needs decision: yes

### carnet/01#F17 · Low · Item number with a real GTIN-12 check digit and barcode symbology
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- Why: The world scheme `urn:ubl-examples:world:item` is fictional, but 771020000027 is a valid
  12-digit GTIN (check digit 7 computed with the GS1 algorithm), and a 12-digit GTIN starting with
  7 lies in the U.P.C. company-prefix range administered by GS1 US (own knowledge). Read as a real
  GTIN it could belong to a real company. I could not check whether it is assigned. 64 examples use
  the scheme (grep -rl 'schemeID="urn:ubl-examples:world:item"' --include='*.xml').
- Condition: the world's item numbers cannot be read as real GTINs, or the source verification
  records why this range is safe.
- Options: (a) check against the sources recorded for GS1 and note the result; (b) change the
  number format so that it is not GTIN-shaped.
- Needs decision: yes

## Checked and consistent
- Declared customs value 99800 XUF = 2 × 49900 XUF, the bench's price in
  `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900`.
- Gross weight 83 kg for 2 benches = 41.5 kg each, the same as 3984 kg for 96 benches in
  `road/05-ExportCustomsDeclaration.xml`. Against the materials: 5 hardwood slats of about
  1800 × 70 × 35 mm at about 750 kg/m³ ≈ 16.5 kg, a cast steel frame ≈ 20 kg, plus anchors and film
  (own estimates); resource consumption of 34 kg steel and 22.5 kg wood per bench includes the
  casting and sawing losses. Plausible.
- HS 940179 under section XX (NatureCode XX), national tariff 94017910 and CPC 38111 agree.
- Seat height 450 mm within 440–460 mm; dimensions plausible for a 3-seat bench.
- ISIN XU0001042501 check digit correct (check_ids.py); market code XFER is not in the real ISO
  10383 MIC list (world/codelists/sources/iso10383).
- Validity 2026-05-25 to 2027-05-25: one year, the usual carnet validity.
- The carnet number in every counterfoil's GoodsItemPassportID equals the document ID, and 02, 03
  and 04 refer to the same number or to its counterfoils.
- Parties: holder, issuer/exporting guarantor (Ferrano Chamber of Commerce), importing guarantor
  (Selanu Chamber of Commerce) and customs are described with the same identifiers, contacts and
  addresses in 02–04 (language tags aside, F12).

## Considered and refuted
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:GoodsItemPassportID`: UBL's definition
  mentions "the number on the upper part of the orange hazard placard", a copy error in the model —
  refuted as an example problem because the first part of the definition (the carnet's identifier)
  fits the value; the definition text is worth reporting with F15.
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name`:
  suspected that Selanu airport is the first, not a subsequent, entry — refuted because the goods
  first enter Bayvarra in transit and then Lisavu, so the island's office is the subsequent entry.
- `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: UBL defines it
  as "the number of shares", while it is an amount — refuted for the example: an amount of share
  capital matches the element's type; the definition is a model wording issue (the element is
  still covered by F8).
- `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name`: the
  definition speaks of the exporter signing a certificate of origin application — refuted: generic
  definition text reused across documents; a functional contact of the issuing chamber fits the
  endorsement.
- `/GoodsItemPassport/cbc:ExportReasonCode`: defined as "the reason for importing the goods" —
  refuted: for a temporary export to a fair the reason is the same on both sides.
- `/GoodsItemPassport/cbc:Note[2]`: "Samples" for goods exported under the exhibition reason —
  refuted: everyday wording for exhibits; the coded reason is exhibition.
- `/GoodsItemPassport/cbc:Status`, `/GoodsItemPassport/cbc:ExportReason`: no languageID while the
  notes have one — refuted: no rule requires it for single-language text.
- `/GoodsItemPassport/cac:ExportingCustomsParty/cac:Contact/cbc:Note`: weekday office hours for a
  "Border office" — refuted: the contact is the administration's office, not the border post's
  counter; the carnet does not depend on its hours.

## Outside this review
- Whether the re-exportation from Lisavu and the re-importation into Urvania fit the dates of the
  fair and of the other flows that move the same benches (timeline question across documents).
