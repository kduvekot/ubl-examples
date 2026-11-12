# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: parties

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### carnet/01#F1 · High · The representative's "mobile on the road" is the holder's order-desk line
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Name` = `Mobile on the road`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: The person who "accompanies the Goods while temporarily exported" (RepresentativeParty) is given a contact named as his mobile while travelling, but its number is the fixed number of Valdara's "Order desk" (the same number is the order desk's telephone in 74 other examples, 75 with this one, counted with `grep -rl --include='*.xml' -F '+999 1 041 518 4274' world/examples`). The holder's contact in the same document lists a different number as cellular phone (`OtherCommunication` with `ChannelCode` `AL`). The label and the number contradict each other: whoever calls the representative at the border reaches the order desk in Ferrano.
- Condition: the representative's contact number is a number that reaches Mr Orsenna while he travels (a mobile number), or the contact is not labelled as a mobile.
- Options: (a, preferred) give the person contact his own mobile number (the order desk's cellular number is a desk phone, not his); (b) drop the person contact and rely on the holder's contact.
- Needs decision: no

### carnet/01#F2 · Medium · A province in Region
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "the recognized geographic or economic region or group of countries in which this address is located"; a province is a subdivision of the country, for which UBL has `CountrySubentity` ("the political or administrative division of a country in which this address is located"). The Bayvarran addresses of the world use `CountrySubentity` for their states (e.g. `Coastal State`), so the Urvanian provinces are encoded differently from the equivalent level in Bayvarra. "Province of Ferrano" occurs in `Region` in 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no Urvanian province is held in `Region`; where the province is given, it is in `CountrySubentity` (and, if a code list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the province to `CountrySubentity`, as for the Bayvarran states; (b) drop it where the address format does not need it.
- Needs decision: no

### carnet/01#F3 · Medium · A given name in OtherName ("second family name")
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:OtherName` = `Mara`
- Why: UBL defines `Person/OtherName` as "This person's second family name". "Mara" is a given name, not a family name, and the person's family name is `Orsenna`; nothing in the example says he has a second family name.
- Condition: `OtherName` is absent, or holds a second family name.
- Options: (a, preferred) drop `OtherName`; (b) give a real second family name if the naming customs of Urvania have one.
- Needs decision: no

### carnet/01#F4 · Medium · Customs administrations described as companies in a commercial register
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania and the Island Customs Service are state authorities (ISIC 8411, public administration). A state authority is not a company entered in a commercial or companies register, and `CompanyLiquidationStatusCode` ("the party's liquidation status") does not apply to it. The same description of customs and maritime authorities occurs in 24 examples (counted with an lxml script over `world/examples/*/*.xml`: PartyLegalEntity with RegistrationName "Customs Administration of Urvania" 10, "Customs and Border Service of Bayvarra" 7, "Island Customs Service" 6, "Maritime Administration of Lisavu" 1, all COMMERCIAL and ACTIVE).
- Condition: neither customs party is described as registered in a commercial or companies register, and neither carries a liquidation status.
- Options: (a, preferred) drop `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` for public authorities, keeping the registration name and the identifier the state gives them; (b) if the world has a register of public bodies, describe that register with its own type code.
- Needs decision: yes (how the world identifies public bodies affects every authority in the examples)

### carnet/01#F5 · Low · Customs VAT registration copied into the carnet
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The ExportingCustomsParty is "the Party who is competent of Customs in the exporting country"; nothing in a carnet involves the customs administration's own VAT registration. It looks copied from master data. The Island Customs Service, in the same role on the other side, has none.
- Condition: the customs party carries no `PartyTaxScheme`, or the document gives a reason for it.
- Options: (a, preferred) drop it.
- Needs decision: no

### carnet/01#F6 · Low · Holder's company master data the carnet does nothing with
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/GoodsItemPassport/cac:HolderParty/cbc:WebsiteURI` = `https://www.valdara.example`
- Why: A carnet identifies the holder for the guarantee and for customs. The holder's stock listing, share capital, a logistics service provider "Warehousing and despatch" that plays no part in the temporary export (the goods travel with the representative; the TransportAdvisorParty is Bayforth Forwarding), and the website have no function in this document. They look copied from the party's master data.
- Condition: every holder detail present has a role in the carnet (identification, guarantee, contact), or the document says why it is there.
- Options: (a, preferred) drop the security listing, stock amount, shares indicator and service provider; keep what identifies the holder; (b) if the share capital matters for the guarantee, say so in the document.
- Needs decision: no

### carnet/01#F7 · Low · Holder contact is the order desk
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The holder's primary contact in a carnet is whoever answers for the carnet (customs formalities, the guarantee, claims such as the later proof-of-reexportation request). A sales order desk is the contact for customers placing orders.
- Condition: the holder's contact is a person or desk responsible for the carnet or for export/customs formalities.
- Options: (a, preferred) an export or customs desk of Valdara; (b) drop the contact and use the representative.
- Needs decision: no

### carnet/01#F8 · Low · Middle name and suffix without a reason
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:MiddleName` = `Ilse`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cbc:NameSuffix` = `Jr`
- Why: "Davide Ilse … Orsenna Jr": "Ilse" is a female given name, and "Jr" an English-language suffix, on an Urvanian man whose names otherwise follow Italian-style naming. Neither has a role in identifying him beyond the passport and national ID that are already given; they read as fillers (IND5/IND6).
- Condition: every name part present is plausible for the person and needed to identify him.
- Options: (a, preferred) drop both; (b) replace them with plausible values if the story wants them.
- Needs decision: no

### carnet/01#F9 · Low · Italian text tagged as English
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The second rendering of each value carries `languageID="en-XU"` (English as used in Urvania), but the text is Italian. A `languageID` must name the language of the text. 104 examples carry an Italian-style street name under an `en-X*` tag (`grep -rlE --include='*.xml' 'languageID="en-X[UBL]">(Via|Piazza|Valico|Corso|Strada|Viale|Largo)' world/examples | wc -l`). This may be a deliberate convention of the world (Italian-style exonyms such as "Ferrano"), which is why it needs a decision.
- Condition: each rendering is in the language its `languageID` names: English text under `en-*`, or the Italian-style form under a tag that names it.
- Options: (a) translate the street names and legal form into English ("Market Square", "Workshops Street"); (b) if the world treats these names as the established exonyms used in English, record that convention and keep them; (c) tag them with the language they are in.
- Needs decision: yes

### carnet/01#F10 · Low · The same addresses tagged with different English variants in the flow
- XPath: `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/GoodsItemPassport/cac:ImportingCustomsParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: Here the Lisavan addresses of the Selanu Chamber of Commerce and the Island Customs Service carry their English renderings as `en-XU`, while 02 and 03 tag the same renderings `en-XL`, and tag the Ferrano chamber's Urvanian address `en-XL`. The tag follows the country of the document's issuer, not the address. The same party's address is thereby described differently in each example (the checklist asks for the same address to be described the same way everywhere).
- Condition: a party's address renderings carry the same `languageID` in every example of the flow.
- Options: (a, preferred) tag the English rendering of an address by the address's own country (or by plain `en`); (b) keep the issuer-based variant and record it as a convention.
- Needs decision: no

### carnet/01#F11 · Low · Two names for the chamber's carnet office
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:Contact/cbc:Name` = `Certificates office`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: The issuing chamber's primary contact is its "Certificates office", but the carnet is signed by its "Carnet desk", which has no telephone or e-mail anywhere. In 03 the Selanu chamber also signs as "Carnet desk" while its contact is "Carnet office". Either the two names are one office or the primary contact is not the office that handles carnets.
- Condition: the issuer's contact and the signing desk are either the same office under one name, or the signing desk is reachable.
- Options: (a, preferred) use one name for the office that issues carnets, in the contact and the endorsement.
- Needs decision: no

### carnet/01#F12 · Low · The same customs office named two ways, with the authority's name in a location
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name` = `Island Customs Service, Selanu airport`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:CustomsOfficeLocation/cbc:Name` = `Customs office, Selanu airport`
- Why: Both name the customs office at Selanu airport, once with the authority's name in the place name, once without. A location's name is the place; the office is not identified by any ID, so a reader cannot tell that both are the same office.
- Condition: the office at Selanu airport has one name (and, where the world has one, an identifier) wherever it occurs.
- Options: (a, preferred) one place name, e.g. "Customs office, Selanu airport", with an office identifier if the world has a list of customs offices.
- Needs decision: no

## Checked and consistent
- Party identifiers of the four parties against 02, 03 and 04: Ferrano Chamber `XU-R-105370`, Selanu Chamber `IC42133`, Customs Administration of Urvania `XU-R-105507`, Island Customs Service `IC41448`; names, registration names, tax IDs, postal address IDs, contacts (telephone, e-mail) and endpoints are the same in all four examples (apart from the language tags of F10).
- Roles: Ferrano Chamber is IssuerParty and ExportingGuarantorParty (the issuing association guarantees in the exporting country, as UBL says "normally a chamber of commerce"); Selanu Chamber is the ImportingGuarantorParty; Valdara Industries is HolderParty ("normally the temporary exporter") and RepresentativeParty through its sales engineer who accompanies the samples.
- The holder's identifiers: register `XU-R-104274` is the PartyIdentification and the PartyLegalEntity CompanyID; customs trader ID and endpoint derive from the same number. ISIN `XU0001042501` check digit correct (check_ids.py). MIC `XFER` is not in the ISO 10383 file (`world/codelists/sources/iso10383/ISO10383_MIC.csv`); ICD `0990` is not in the ICD list in `world/codelists/sources/peppol/ICD.xml`.
- TransportAdvisorParty Bayforth Forwarding `20411644` (XB register) is the same party as the freight forwarder in the mast flow.

## Considered and refuted
- `/GoodsItemPassport/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode`: a chamber of commerce in a commercial register — refuted because chambers of commerce can be private associations or companies (ISIC 9411, membership organisations), and the world gives both chambers a register number; unlike the customs authorities (F4) this is a legitimate reading.
- `/GoodsItemPassport/cac:RepresentativeParty/cac:PartyIdentification/cbc:ID`: the representative is the same organisation as the holder — refuted because UBL defines RepresentativeParty as the party who accompanies the goods; the employee of the holder who travels with the samples is exactly that, and the Person aggregate names him.
- `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:IdentityDocumentReference/cbc:ID`: passport, national ID, birth data of the representative as excessive personal data — refuted because the person crosses borders with the goods under the carnet, and identifying him is the purpose of the RepresentativeParty.
- `/GoodsItemPassport/cac:ImportingGuarantorParty/cac:PostalAddress`: no PostalZone in the Lisavan addresses — refuted because none of the Lisavan addresses in the flows reviewed (Selanu Chamber, Island Customs Service, Selanu Telecom, Kelaro Air Cargo) has one; it is the address format of Lisavu.
- `/GoodsItemPassport/cac:HolderParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990:10427` as a real ISO 6523 identifier — refuted because ICD 0990 is not assigned in the ICD list in the sources.
- `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cac:StandardPropertyIdentification/cac:IssuerParty/cac:PartyName/cbc:Name`: Codana Identification Agency as issuer of a property identifier — refuted because an identification agency assigning identifiers to properties (as dictionaries such as IEC CDD do) is a legitimate reading of "the party that issued the standard property identification".
- `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PostalAddress/cbc:AddressTypeCode`: POSTAL with both a post box and a street address — refuted because a postal address with a post box and the building's street address is common and not contradictory.

## Outside this review
- Outside the parties lens (for the logistics and context parts): 02's note "The island's customs found no re-export stamp." against this example's counterfoil `REEXP-1` with the note "Stamped by customs."; the carnet as issued on 2026-05-25 already carrying stamped importation, re-exportation and re-importation counterfoils; and whether Selanu airport, where the goods first entered Lisavu (`IMP-1`), is an office of "subsequent" entry.
