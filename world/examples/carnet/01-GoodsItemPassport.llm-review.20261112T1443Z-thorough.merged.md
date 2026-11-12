# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/01-GoodsItemPassport.xml`, Git blob `b7c20e53167125d7f3ee0260e4bdca609da4e0b0` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8533627 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### carnet/01#F1 · High · The carnet as issued already shows all four counterfoils stamped
- XPath: `/GoodsItemPassport/cbc:IssueDate` = `2026-05-25`
- XPath: `/GoodsItemPassport/cbc:Status` = `Issued`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Issued`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:Note` = `Stamped by customs.`
- Why: The Goods Item Passport is "a document providing a temporary export license, also knowned as
  an ATA Carnet". This one is the carnet as the chamber issues it: version 1, status "Issued", issuer
  endorsement "Issued", validity starting on the issue date
  (`/GoodsItemPassport/cac:ValidityPeriod/cbc:StartDate` = `2026-05-25`). On that day the goods
  have not left Urvania, so no customs office can yet have stamped the exportation, importation,
  re-exportation or re-importation counterfoil. Yet all four say "Stamped by customs.", with stamp
  and voucher references. The flow places these events later: on 2026-07-24 the island's customs
  still has no re-export record
  (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`),
  and the re-importation is evidenced only on 2026-08-28
  (`04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`).
  A document issued on 2026-05-25 states events of the following three months.
- Condition: the carnet as issued does not state that any counterfoil has been stamped, or the
  example is a later state of the carnet whose version and date follow the last stamped event.
- Options: (a, preferred) keep the four counterfoils with their customs offices and goods but drop
  the "Stamped by customs." notes and the stamp references, since the carnet at issue carries the
  counterfoils still to be stamped and 04 evidences the stamps; (b) present the example as the
  carnet after use (later VersionID, issue date after the re-importation), which changes its role in
  the flow.
- Needs decision: yes (which moment of the carnet's life the example shows)
- From: broad (F1), context (F1), logistics (F2)

### carnet/01#F2 · High · The representative's "mobile on the road" is the holder's order-desk line
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Name` = `Mobile on the road`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: RepresentativeParty is "the Party who accompanies the Goods while temporarily exported"; the
  person's contact is named as his mobile while travelling, but its number is the telephone of
  Valdara's "Order desk" in the same document, while the holder's contact lists a different number
  as cellular phone (`OtherCommunication` with ChannelCode `AL`). The document thus says, of the
  same number, that it is the desk's fixed line and the travelling person's mobile: customs calling
  the person at the border reach the order desk in Ferrano. The number is the order desk's in 75
  examples (`grep -rl --include='*.xml' -F '+999 1 041 518 4274' world/examples | wc -l`).
- Condition: the representative's contact number reaches that person while he travels and is not
  the order desk's number, or the contact's name no longer says it is a mobile.
- Options: (a, preferred) give the person a mobile number of his own; (b) rename the contact or drop
  it and rely on the holder's contact.
- Needs decision: no
- From: parties (F1), broad (F10), context (F7)

### carnet/01#F3 · High · Emission factor × base quantity does not give the emission value
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g.,
  emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor
  applies". With 0.82 per 1 EA (one bench), factor × base = 0.82, not 96 kg CO2e. No other figure
  in the item explains it: 96 / 0.82 ≈ 117, which matches neither the material consumed per bench
  (34 kg steel + 22.5 kg hardwood = 56.5 kg) nor the weight (83 kg for 2 benches). 96 kg CO2e itself
  is plausible for about 34 kg of steel and 22.5 kg of hardwood cradle to gate (own knowledge: about
  2 kg CO2e per kg of steel). The same triple occurs in 39 examples
  (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueFactorNumeric × ValueBaseMeasure = ValueMeasure in consistent units, or factor and
  base are absent.
- Options: (a, preferred) drop factor and base, since 96 kg is a product footprint and not activity
  × factor, or make the factor 96 per 1 EA; (b) a base the factor really applies to (e.g. a factor
  per kg of a stated material mass that gives 96).
- Needs decision: no
- From: broad (F3), logistics (F1), context (noted within F5)

### carnet/01#F4 · Medium · A province in Region
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province is a subdivision of the country, for which UBL has
  CountrySubentity. The world puts the Bayvarran states there (e.g. `Coastal State`), so the
  Urvanian provinces are encoded differently from the same level in Bayvarra. "Province of …" is in
  Region in 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no province is held in Region; where given, it is in CountrySubentity (and, if a list
  exists, CountrySubentityCode).
- Options: (a, preferred) move it to CountrySubentity, as for the Bayvarran states; (b) drop it where
  the address format does not need it.
- Needs decision: no
- From: broad (F6), parties (F2)

### carnet/01#F5 · Medium · A given name in OtherName ("second family name")
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:OtherName` = `Mara`
- Why: UBL defines Person/OtherName as "This person's second family name". "Mara" is a given name;
  the person's family name is `Orsenna`, and nothing gives him a second family name. The element
  carries a meaning other than its definition.
- Condition: OtherName is absent, or holds the person's second family name.
- Options: (a, preferred) drop it; (b) a real second family name if the world's naming customs have
  one.
- Needs decision: no
- From: parties (F3), broad (part of F9)

### carnet/01#F6 · Medium · Customs administrations described as companies in a commercial register
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania and the Island Customs Service (ISIC 8411, public
  administration) are state authorities. COMMERCIAL is "a register of businesses" in the world's
  list, and CompanyLiquidationStatusCode is "the party's liquidation status"; an authority is
  neither entered in a business register nor in liquidation. With an lxml count of PartyLegalEntity
  elements with that RegistrationName and COMMERCIAL over `world/examples/*/*.xml`, the same
  description occurs in 10 examples for Urvania's customs, 6 for the Island Customs Service and 7 for
  the Customs and Border Service of Bayvarra.
- Condition: neither customs party is described as registered in a commercial or companies register
  or with a liquidation status.
- Options: (a, preferred) for public bodies keep name and identifier and drop CorporateRegistrationScheme
  and CompanyLiquidationStatusCode; (b) a world register type for public bodies, if the world has one.
- Needs decision: yes (how the world identifies public bodies affects every authority in the examples)
- From: broad (F5), parties (F4)

### carnet/01#F7 · Medium · An emission system boundary in FullnessIndicationCode
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "a code signifying whether a piece of transport equipment is full,
  partially full, or empty. This indication is used as a parameter when calculating the
  environmental emission." Cradle to gate (list EmissionBoundaryCode) is the system boundary of a
  product footprint; no transport equipment is involved in the bench's manufacturing emission. The
  boundary is already said in
  `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`.
  The same use occurs in 39 examples (`grep -rl --include='*.xml' 'EmissionBoundaryCode">CRADLE' world/examples | wc -l`);
  other examples use the element for its meaning (LoadTypeCode FCL).
- Condition: FullnessIndicationCode is absent here or says how full a piece of transport equipment
  is.
- Options: (a, preferred) drop it and keep the boundary in LifecycleStageDescription; (b) record the
  lack of a boundary element as a finding for the UBL TC.
- Needs decision: no
- From: broad (F4), context (F4)

### carnet/01#F8 · Low · Elements used whose UBL 2.5 definitions are copied from other contexts
- XPath: `/GoodsItemPassport/cbc:StatusCode` = `VALID`
- XPath: `/GoodsItemPassport/cbc:Status` = `Issued`
- XPath: `/GoodsItemPassport/cbc:VersionID` = `1`
- XPath: `/GoodsItemPassport/cbc:ExportReasonCode` = `EXHIBITION`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: UBL 2.5 defines the GoodsItemPassport's StatusCode and Status as "The reason for importing
  the goods", ExportReasonCode also as "The reason for importing the goods", VersionID as "the
  current version of this request for proof", the counterfoil's GoodsItemPassportID as the carnet
  number "usually the number on the upper part of the orange hazard placard required on the means of
  transport", and SignatoryContact as "The individual representing the exporter who signs the
  Certificate of Origin application". The values follow the element names (record status, export
  reason, version, carnet number, the chamber's signing desk), which is evidently what was meant;
  for ExportReasonCode, GoodsItemPassportID and SignatoryContact the parts agree that the value is a
  legitimate reading (see "Considered and refuted"). Under the semantic-conformance rule the copied
  definitions are a defect of the model to record, not a misuse in the example; for StatusCode/Status
  the value does not fit the definition as written at all.
- Condition: each such use is recorded as a finding on the UBL 2.5 definitions for the OASIS UBL TC,
  or the element is not used.
- Options: (a, preferred) keep the values and record the copied definitions in
  `analysis/codelist-decisions.md` for the write-up; (b) drop StatusCode/Status (the endorsement
  already says "Issued").
- Needs decision: yes
- From: broad (F15), context (F8)

### carnet/01#F9 · Low · Italian text tagged as English
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: These renderings carry `languageID="en-XU"` but are Italian (the legal form half Italian,
  half English). A languageID names the language of the text. 104 examples carry an Italian-style
  street name under an `en-X*` tag
  (`grep -rlE --include='*.xml' 'languageID="en-X[UBL]">(Via|Piazza|Valico|Corso|Strada|Viale|Largo)' world/examples | wc -l`).
  It may be a deliberate convention of the world (Italian-style exonyms such as "Ferrano").
- Condition: each rendering is in the language its languageID names, or the world records that
  English keeps these names.
- Options: (a) translate ("Market Square", "Workshops Street", "Border Crossing"); (b) record the
  Italian-style names as the established English exonyms of the world; (c) tag them with the
  language they are in.
- Needs decision: yes (the world's language convention)
- From: parties (F9), broad (part of F12)

### carnet/01#F10 · Low · Party master data the carnet does nothing with
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007376017`
- XPath: `/GoodsItemPassport/cac:HolderParty/cbc:WebsiteURI` = `https://www.valdara.example`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: A carnet identifies the holder for the guarantee and for customs. Nothing in it uses the
  holder's share capital, listed shares or warehousing provider (Castrano Logistics, "Warehousing and
  despatch", plays no part in the temporary export; the goods travel with the representative and the
  TransportAdvisorParty is Bayforth Forwarding), or the VAT registration of the Urvanian customs (the
  Island Customs Service, in the same role on the other side, has none). No tax is charged and no
  party pays another under this document. The chamber's VAT registration is the weakest case: 02
  and 03 refute it there because the exporting guarantor is liable for the duties claimed from the
  guarantee; in this document the chamber carries it as IssuerParty, a role that pays nothing. The
  website is the mildest item (a party's website is ordinary identification). They look copied from
  master data (section 4.8, IND5).
- Condition: every party detail present has a role in the carnet procedure (identity, address,
  contact, legal identity the guarantee needs), or the document states its reason.
- Options: (a, preferred) drop SecurityListing, CorporateStockAmount, FullyPaidSharesIndicator,
  ServiceProviderParty and the customs' PartyTaxScheme; decide on the chamber's PartyTaxScheme
  together with the guarantor role; (b) keep one with a stated reason.
- Needs decision: no
- From: context (F6), parties (F5, F6), broad (part of F8)

### carnet/01#F11 · Low · Chambers of commerce described as companies in a commercial register
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The two chambers (ISIC 9411, membership organisations) are registered as businesses with a
  liquidation status. The world's CorporateRegistrationType list has a "Register of associations"
  (ASSOCIATION) next to COMMERCIAL ("A register of businesses."). Against this, the parties part
  argued that chambers can be private associations or companies, and the world gives both a register
  number, so COMMERCIAL is a legitimate reading. The merge could not settle it: it depends on what
  chambers are in the world.
- Condition: each chamber is described as what it is in the world (association register, public
  body, or a commercial register if the world says so).
- Options: (a, preferred) the association register; (b) as for the public bodies in F6.
- Needs decision: yes
- From: broad (F14); refuted by parties (see "Considered and refuted")

### carnet/01#F12 · Low · Two names for the issuing chamber's carnet office
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:Contact/cbc:Name` = `Certificates office`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: The issuing chamber's contact is its "Certificates office", but the carnet is signed by its
  "Carnet desk", which has no telephone or e-mail anywhere. In 03 the Selanu chamber also signs as
  "Carnet desk" while its contact is "Carnet office". Either the two names are one office, or the
  primary contact is not the office that handles carnets.
- Condition: the issuer's contact and the signing desk are one office under one name, or the
  signing desk is reachable.
- Options: (a, preferred) one name for the office that issues carnets, in the contact and the
  endorsement.
- Needs decision: no
- From: parties (F11)

### carnet/01#F13 · Low · The holder's contact is the order desk
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The holder is the temporary exporter answerable for the carnet (formalities, guarantee,
  claims such as 02). Its contact for that is the export or customs function (the representative
  is in "Export sales"), not the desk that takes customers' orders.
- Condition: the holder's contact is the person or desk responsible for the carnet or for export and
  customs formalities.
- Options: (a, preferred) an export or customs desk of Valdara; (b) drop the contact and use the
  representative.
- Needs decision: no
- From: broad (F11), parties (F7)

### carnet/01#F14 · Low · Middle name and suffix of the representative without a reason
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:MiddleName` = `Ilse`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:NameSuffix` = `Jr`
- Why: Every optional name part is filled for Ing. Davide Orsenna: "Ilse" is a female given name and
  "Jr" an English-language suffix on an Urvanian man with Italian-style names. Nothing uses them; the
  identity data a border crossing needs (passport, national ID, nationality) is already there. They
  read as fillers (IND5/IND6). (OtherName is F5.)
- Condition: each name part present is plausible for the person and belongs to his name as the world
  describes it.
- Options: (a, preferred) keep first and family name, title and passport; drop both; (b) give the
  person a naming convention in the world that explains them.
- Needs decision: no
- From: broad (part of F9), parties (F8)

### carnet/01#F15 · Low · The same addresses tagged with different English variants in the flow
- XPath: `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: Here the English renderings of the Lisavan addresses (Selanu chamber, Island Customs Service)
  are tagged `en-XU`, while 02 and 03 tag the same renderings `en-XL`, and tag the Ferrano
  chamber's Urvanian address `en-XL` too. The tag follows the country of the document's issuer, not
  the address, so the same party's address is described differently in each example.
- Condition: a party's address renderings carry the same languageID in every example of the flow.
- Options: (a, preferred) tag each rendering by the address's own country (or plain `en`); (b) keep
  the issuer-based variant and record it as a convention.
- Needs decision: no
- From: parties (F10), broad (part of F12)

### carnet/01#F16 · Low · Transit through Bayvarra without transit counterfoils
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransitCountry/cbc:IdentificationCode` = `XB`
- Why: The consignment is routed through Bayvarra, but the carnet has only exportation, importation,
  re-exportation and re-importation counterfoils. An ATA carnet used for transit through a third
  customs territory normally carries transit vouchers (own knowledge). The logistics part refuted
  this because the transit can run under another transit procedure; the merge agrees that this is
  possible, but nothing in the flow says so, so whether it is a problem depends on the world's rules
  for transit under the Trade Accord.
- Condition: either the carnet has transit counterfoils for Bayvarra, or the world's rules (another
  transit procedure, or the Trade Accord) cover the transit and the example does not contradict them.
- Options: (a) confirm the world's transit rule; (b) add transit counterfoils.
- Needs decision: yes
- From: broad (F16); refuted by logistics (see "Considered and refuted")

### carnet/01#F17 · Low · Selanu airport as office of "subsequent" entry
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name` = `Island Customs Service, Selanu airport`
- Why: UBL defines OfficeOfSubSequentiallyEntryLocation as "A location that is involved in the
  subsequent entry of goods in a consignment. This could mean a customs office or facility where
  goods are processed after their initial entry point". Context: Selanu airport is where the samples
  first enter Lisavu (the importation counterfoil is stamped there:
  `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:CustomsOfficeLocation/cbc:Name` = `Customs office, Selanu airport`),
  so it is the first office of entry of the customs territory, not a subsequent one, and the
  importation counterfoil already says where the goods enter. Broad and logistics: the goods first
  enter Bayvarra in transit (TransitCountry XB), so the island's office is a subsequent entry. Both
  readings fit the definition's wording; in customs practice (own knowledge) an office of subsequent
  entry is one within the same customs territory after the first, which favours the context reading.
  The merge could not settle it.
- Condition: the element is absent, or names an office where the goods are processed after a
  different, earlier point of entry that the example can name.
- Options: (a, preferred) drop it (the importation counterfoil's CustomsOfficeLocation already says
  where the goods enter); (b) keep it if the world's reading counts the transit country's entry as
  the initial one, and record that reading.
- Needs decision: yes
- From: context (F3); refuted by broad and logistics (see "Considered and refuted")

### carnet/01#F18 · Low · The same customs office named two ways, and no customs office identified
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name` = `Island Customs Service, Selanu airport`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:CustomsOfficeLocation/cbc:Name` = `Customs office, Selanu airport`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:CustomsOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: The office at Selanu airport is named once with the authority's name in the location name
  ("the name is the place, not the company") and once without; none of the locations carries an
  identifier, although the air flow identifies the airport by UN/LOCODE
  (`air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`).
  The Urvanian border post is named only descriptively, without place name or code.
- Condition: one place is named one way in the example, a location name names the place, and each
  customs office location carries an identifier where the world has one.
- Options: (a, preferred) one name ("Customs office, Selanu airport") and a `cbc:ID` (XLSLA or a
  customs office code); (b) at least the same name in both places.
- Needs decision: no
- From: logistics (F4), parties (F12), context (name part of F3)

### carnet/01#F19 · Low · Item master data the carnet does nothing with
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:Name` = `Load capacity`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ProductDocumentationDocumentReference/cbc:ID` = `VI-RM-B180`
- Why: A carnet's general list identifies the goods for customs: description, quantity, weight,
  value, origin, marks (own knowledge). Keywords ("assigned by the seller", but a carnet has no
  seller), warranty, load-test properties, the product carbon footprint, the circularity profile
  (resources, waste, repairability, maintenance, product documentation) serve neither guarantor nor
  customs in this flow. They look copied from the item master data (IND5).
- Condition: the carnet's item carries only data a party of the carnet procedure uses to identify or
  value the goods, or the flow states a reason for the rest.
- Options: (a, preferred) reduce the item to identification and customs data (name, description,
  seller's ID, commodity codes, origin, dimensions if used to identify); (b) keep an aggregate where
  the story gives the carnet a reason for it, and state that reason.
- Needs decision: yes (the same item data is in 39 examples; removing it here may lower coverage)
- From: broad (part of F8), context (F5)

### carnet/01#F20 · Low · Item number reads as a real GTIN-12
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The scheme `urn:ubl-examples:world:item` is fictional, but 771020000027 has a valid GTIN-12
  check digit (7, recomputed in the merge) and comes with a barcode symbology, so it reads as a real
  GTIN. As a GTIN-12 (U.P.C.) it lies in GS1 US company-prefix space; read as a GS1 prefix, the
  issuer scope 771 lies in the range of GS1 Colombia (770–771) (own knowledge). Whether it is
  assigned could not be checked. The number occurs in 39 examples and the scheme in 64
  (`grep -rl --include='*.xml'` for the number and for the schemeID, `wc -l`).
- Condition: the world's item numbers cannot be read as GTINs assigned in the real GS1 system, or the
  source verification records why this pattern is safe.
- Options: (a, preferred) check against the recorded verification of the world's item scheme; if
  none exists, choose a pattern that is not a valid GTIN; (b) keep it and record the reasoning.
- Needs decision: yes
- From: broad (F17), logistics (F6)

### carnet/01#F21 · Low · References that give only an ID
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionFactorDocumentReference/cbc:ID` = `VI-LCA-2025`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:ExportationDocumentReference/cbc:ID` = `EXP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:ImportationDocumentReference/cbc:ID` = `IMP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cac:ReexportationDocumentReference/cbc:ID` = `REEXP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:AdditionalDocumentReference/cbc:ID` = `SCC-FAIR-26-INV`
- Why: None of these documents exists in the examples and none of the references says what it is.
  "SCC-FAIR-26-INV" is presumably the Selanu chamber's invitation to the fair, the reason for the
  temporary export, but nothing says so. The "…-STAMP" IDs name a stamp rather than a "document used
  for the export/import of the goods"; they are typed by their element, but a reader cannot tell
  what document stands behind them.
- Condition: each remaining reference says what kind of document it is (DocumentType or
  DocumentTypeCode, with issuer or date where useful).
- Options: (a, preferred) add the document type (for the counterfoils, the customs document numbers);
  (b) drop references the carnet does not need (see F19, and the stamp references if F1 is fixed by
  option a).
- Needs decision: no
- From: broad (F13), context (F9), logistics (F5)

### carnet/01#F22 · Low · Final re-exportation date on the exportation counterfoil, set at issue
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `/GoodsItemPassport/cbc:Note[2]` = `Samples for the Selanu trade fair; to come back within six months.`
- Why: UBL: "Final date of re-exportation, if less than the overall validity period of te Goods Item
  Passport or ATA Carnet". Under the ATA system (own knowledge: Istanbul Convention, Annex A) this
  time limit is fixed by the customs of the country of temporary admission on the importation
  voucher. Here it sits on the exportation counterfoil EXP-1 (Urvanian border post) and is known on
  the day of issue, while the importation counterfoil IMP-1, the one 02 and 03 claim on, carries
  none. The note's six months do not give the date either: six months from issue end on 2026-11-25,
  and from any later importation later still; 2026-11-21 is within six months, so it does not
  contradict the note, but its basis is not stated. The date matters, since 02 and 03 are judged
  against it (see their reviews).
- Condition: the final re-exportation date, if present, is on the importation counterfoil and its
  basis agrees with the note, or the example says why the exporting side records it.
- Options: (a, preferred) move it to counterfoil IMP-1 and align it with the note; (b) drop it; (c)
  if it is the date the holder promised, say so in a note.
- Needs decision: no
- From: broad (F7), context (F2), logistics (F3)

### carnet/01#F23 · Low · The re-importation document is identified differently in the carnet and in the proof
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cac:ReimportationDocumentReference/cbc:ID` = `REIMP-1-STAMP`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- Why: The re-importation by Urvania's customs is referenced here as REIMP-1-STAMP and in the proof
  (04) as XU-CUS-REIMP-26-0044; neither reference has a type, so the two cannot be recognised as the
  same document or told apart as different ones.
- Condition: the same customs document has the same ID wherever the flow references it, and each
  reference says what it is.
- Options: (a, preferred) use the customs document number in both, with a DocumentType; (b) drop the
  stamp reference here (see F1, F21).
- Needs decision: no
- From: logistics (part of F5)

## Checked and consistent
- Declared customs value 99800 XUF = 2 × 49900 XUF, the bench's price in
  `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900` and
  `road/15-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `49900` (money, broad).
  The carnet carries no fee, guarantee or tax amount, and needs none (money). XUF is not an ISO 4217
  code assigned to a real currency (money).
- Physics (logistics, broad; figures from the document, densities and yields own knowledge): gross
  83 kg for 2 benches = 41.5 kg each, the same as 3984 kg for 96 benches in
  `road/05-ExportCustomsDeclaration.xml`. Materials consumed 34 kg steel + 22.5 kg hardwood per bench
  include casting and sawing losses; five slats of about 1750–1800 × 70 × 30–35 mm at 700–750 kg/m³
  weigh 13–16.5 kg; a cast frame about 20–27 kg: consistent with 41.5 kg.
- Dimensions 1800 × 620 × 780 mm, seat height 450 mm within 440–460 mm.
- HS 940179, national tariff 94017910 and CPC 38111 agree.
- Validity 2026-05-25 to 2027-05-25: one year, the maximum validity of an ATA carnet (own knowledge).
- Goods item 2 EA = 2 EA on all four counterfoils; every counterfoil's GoodsItemPassportID equals the
  document ID, which 02 and 03 reference.
- Route: exportation and re-importation at the Urvanian land border, transit XB, importation and
  re-exportation at Selanu airport; the transport advisor Bayforth Forwarding (`20411644`, XB
  register) is the same party as the forwarder in the mast flow.
- Parties: identifiers, names, tax IDs, address IDs, contacts and endpoints of the two chambers and
  the two customs agree with 02, 03 and 04 (language tags aside, F15). Ferrano chamber as issuer and
  exporting guarantor, Selanu chamber as importing guarantor, Valdara as holder ("normally the
  temporary exporter") and as representative through its sales engineer: roles fit.
- check_ids.py: ISIN `XU0001042501` check digit correct. MIC `XFER` is not in the ISO 10383 file
  in the sources; ICD `0990` is not in the ICD list in the sources (parties).
- DocumentDistribution `COLLECT` to the holder fits the holder collecting the carnet (context).
- Merge: every definition quoted above was re-read in `annotate.py`; the counts were redone over
  `*.xml` only (39, 39, 104, 75, 39, 64; customs and chambers with an lxml script).

## Considered and refuted
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:GoodsItemPassportID`: definition
  mentions "the number on the upper part of the orange hazard placard" — refuted as an example
  problem, the first part of the definition (the carnet's identifier) fits the value; the definition
  is recorded in F8 (from broad, logistics).
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name`:
  Selanu airport is the first, not a subsequent, entry — refuted because the goods first enter
  Bayvarra in transit (from broad, logistics). The merge could not settle this and kept it as F17,
  with both arguments.
- `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: definition
  "the number of shares" against an amount — refuted, the element is an Amount type and 250 million
  ferra is plausible for a listed manufacturer; whether it belongs in the carnet is F10 (from broad,
  money).
- `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name`:
  definition about a certificate of origin application — refuted as misuse, generic definition text
  reused; recorded as a model defect in F8 (from broad).
- `/GoodsItemPassport/cbc:ExportReasonCode`: defined as "the reason for importing the goods" —
  refuted as misuse, for a temporary export to a fair the reason is the same on both sides; recorded
  in F8 (from broad).
- `/GoodsItemPassport/cbc:Note[2]`: "Samples" for goods exported for exhibition — refuted, everyday
  wording for exhibits (from broad).
- `/GoodsItemPassport/cbc:Status`, `/GoodsItemPassport/cbc:ExportReason`: no languageID while the
  notes have one — refuted, no rule requires it for single-language text (from broad).
- `/GoodsItemPassport/cac:ExportingCustomsParty/cac:Contact/cbc:Note`: weekday office hours for a
  border office — refuted, the contact is the administration's office; the carnet does not depend on
  its hours (from broad).
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:ExportationDocumentReference/cbc:ID`:
  a stamp is not "a document used for the export" — refuted, the ID can be read as the customs'
  record of the export act, typed by its element (from context; the missing type remains in F21).
- `/GoodsItemPassport/cac:IssuerEndorsement/cbc:DocumentID`: the carnet's own ID as "An identifier
  for this endorsement" — refuted, the issuer's endorsement of this very carnet; a legitimate reading
  (from context).
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransportAdvisorParty/cac:PartyName/cbc:Name`:
  a forwarder without a place in a carnet — refuted, the forwarder advises on the route via Bayvarra
  (from context).
- `/GoodsItemPassport/cbc:ExportReason`: text copying the code — refuted, the text adds the fair
  (from context).
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransitCountry/cbc:IdentificationCode`:
  transit without transit counterfoils — refuted because the transit can run under another procedure
  (from logistics). The merge kept it as F16, Needs decision, because nothing in the world says so.
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note`: contradiction with 02's "found
  no re-export stamp" — refuted, the holder's counterfoil can be stamped while the customs' voucher
  is missing; what remains is the timing (F1) (from logistics; see also "Refuted in the merge").
- `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure`: a pallet would push the
  gross weight above 83 kg — refuted, the document states no pallet and the waste profile is generic
  product data (from logistics).
- `/GoodsItemPassport/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode`:
  a chamber in a commercial register — refuted because chambers can be private associations or
  companies and the world gives both chambers a register number (from parties). The merge kept it as
  F11, Needs decision, because the world's list has an association register and the question
  depends on what chambers are in the world.
- `/GoodsItemPassport/cac:RepresentativeParty/cac:PartyIdentification/cbc:ID`: representative is the
  same organisation as the holder — refuted, the holder's employee who travels with the samples is the
  party who accompanies the goods (from parties).
- `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:IdentityDocumentReference/cbc:ID`:
  passport, national ID and birth data as excessive — refuted, the person crosses borders with the
  goods under the carnet (from parties).
- `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PostalAddress`: no PostalZone — refuted, no
  Lisavan address in the flows has one; it is Lisavu's format (from parties).
- `/GoodsItemPassport/cac:HolderParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990:10427` as
  a real ISO 6523 identifier — refuted, ICD 0990 is not assigned in the sources' ICD list (from
  parties).
- `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cac:StandardPropertyIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`:
  an identification agency as issuer of a property identifier — refuted, a legitimate reading (from
  parties).
- `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:AddressTypeCode`: POSTAL with
  both a post box and a street — refuted, common and not contradictory (from parties).

## Refuted in the merge
### broad/F2 · High · Re-exportation counterfoil "stamped" contradicts the claim of the island's customs
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`
- Why (broad): counterfoil REEXP-1 at Selanu airport says it was stamped, while the rest of the flow
  rests on the opposite (no re-export stamp in 02, chased in 03, proven by the re-importation
  counterfoil in 04); had REEXP-1 been stamped, the importation would have been discharged.
- Condition (broad): no example of the flow states that REEXP-1 was stamped, unless the cause of the
  claim changes. Needs decision: no.
- Refuted because: in the ATA procedure (own knowledge) customs stamp the counterfoil, which stays in
  the carnet, and detach the voucher for their own file; when the voucher does not reach or is not
  matched in the importation office's records, that office claims, and the holder proves
  re-exportation with the stamped counterfoil or with alternative evidence. The proof (04) confirms
  this reading: it attaches the re-exportation counterfoil "stamped by the Island Customs Service"
  (`04-ProofOfReexportation.xml:/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`).
  So 01 and 04 agree that REEXP-1 was stamped; what remains is the wording of 02's note (a stamp
  not found rather than a voucher missing), which lies in 02 and is a finding there
  (carnet/02#F4 of this merge), and the timing of all stamps, which is F1 here.

## Changed in the merge
- broad/F1, context/F1, logistics/F2 → F1: combined; kept the XPaths of all three (Status,
  ApprovalStatus, IssueDate); options merged.
- parties/F1 (High), broad/F10 (Low), context/F7 (Low) → F2: combined at High, because the document
  calls the same number the desk's line and the person's mobile, a contradiction between two values
  of this example (section 6), not only a contact that does not fit the role.
- broad/F3, logistics/F1 → F3: combined; context's remark in its F5 added as source.
- broad/F9 (Low, needs decision yes) split: OtherName → F5 at Medium with parties/F3 (a given name in
  an element defined as second family name is a meaning other than the definition); MiddleName and
  NameSuffix → F14 at Low with parties/F8, Needs decision no (removing name fillers does not change who
  the person is).
- broad/F12 (Needs decision yes) split: the issuer-based region subtag → F15 with parties/F10 (Needs
  decision no, encoding only); Italian text under `en` → F9 with parties/F9 (Needs decision yes, the
  world's language convention).
- broad/F8 (holder and item together, Needs decision yes) split: party data → F10 with context/F6,
  parties/F5 and parties/F6 (Needs decision no); item data → F19 with context/F5 (Needs decision yes,
  because the same item data is in 39 examples and coverage may depend on it). F10 notes the
  counter-argument of the 02/03 parts for the chamber's VAT registration.
- broad/F15, context/F8 → F8: combined; all six elements listed; ExportReasonCode, GoodsItemPassportID
  and SignatoryContact are in F8 only as model-definition defects, as the parts' refutations say.
- broad/F7 (Low), context/F2 (Medium), logistics/F3 (Low) → F22 at Low: the value fits the definition
  ("final date of re-exportation"); its placement on the exportation counterfoil rests on ATA
  practice (own knowledge), not on the UBL definition. Logistics' "not six months" softened: 2026-11-21
  lies within six months, so it does not contradict the note; only its basis is unstated.
- context/F3 (Medium) → F17 at Low with Needs decision yes: broad and logistics refuted it, the merge
  could not settle it, so it stays with both arguments (section 3, merge). Its remark on the authority's
  name in the location name joined F18.
- logistics/F4, parties/F12 → F18: combined.
- broad/F13, context/F9, logistics/F5 → F21: combined; logistics' point that 04 identifies the
  re-importation document differently split out as F23, because it is a contradiction with another
  example.
- broad/F16 → F16 kept with logistics' refutation as counter-argument, options reordered (confirming
  the world's rule first).
- broad/F14 → F11 kept with parties' refutation as counter-argument.
- broad/F17, logistics/F6 → F20: combined; the two parts' prefix statements (GS1 US for a GTIN-12,
  GS1 Colombia for prefix 771) both kept and qualified; the issuer scope added as XPath.
- broad/F6, parties/F2 → F4; broad/F5, parties/F4 → F6 (customs counts redone); broad/F4, context/F4
  → F7; broad/F11, parties/F7 → F13: combined without change of severity.

## Outside this review
- Whether the re-exportation from Lisavu and the re-importation into Urvania fit the dates of the
  fair and of the other flows that move the same benches (timeline across documents; from broad and
  logistics).
