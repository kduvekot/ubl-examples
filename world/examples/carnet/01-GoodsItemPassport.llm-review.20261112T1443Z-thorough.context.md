# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### carnet/01#F1 · High · Carnet issued before the journey already carries all four counterfoils as stamped
- XPath: `/GoodsItemPassport/cbc:IssueDate` = `2026-05-25`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:Note` = `Stamped by customs.`
- Why: The document is the carnet as issued by the chamber (`/GoodsItemPassport/cbc:Status` = `Issued`, `/GoodsItemPassport/cbc:VersionID` = `1`, issuer endorsement and signature of the chamber). On the day of issue the goods have not left Urvania, so no customs office can yet have stamped the exportation, importation, re-exportation or re-importation counterfoil. The flow confirms that these events come later: the re-importation is only evidenced on 2026-08-28 (`04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ReexportationEvidence/cbc:Description` = `Re-importation counterfoil of the carnet, stamped by Urvania's customs: the samples left the island and came home.`), and two months after issue the importing country still asks for proof (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`). A document issued on 2026-05-25 states facts of the following months.
- Condition: The carnet as issued does not state that any counterfoil has been stamped; the counterfoils it carries are the blank sets to be presented (or only those that exist at issue), and stamping is recorded only in documents dated after the customs act.
- Options: (a, preferred) keep the four counterfoils with their customs offices and goods but drop the "Stamped by customs." notes, since the carnet at issue carries the counterfoils still to be stamped; (b) present this document as a later version of the carnet (higher VersionID, issue date after the re-importation) that records the stamps — that changes the story of the flow.
- Needs decision: yes

### carnet/01#F2 · Medium · Final date of re-exportation on the exportation counterfoil
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- Why: UBL defines the element as "Final date of re-exportation, if less than the overall validity period of te Goods Item Passport or ATA Carnet". Under the ATA system (Istanbul Convention, Annex A; own knowledge) this time limit is fixed by the customs of the country of temporary admission when they stamp the importation counterfoil and voucher; it is not something the customs of the exporting country set on the exportation counterfoil. Counterfoil[1] is `EXP-1`, presented at `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:CustomsOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`; the importation counterfoil `IMP-1` (Counterfoil[2], Selanu airport), which is the one the importing country later claims on (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID` = `IMP-1`), carries no date.
- Condition: The final date of re-exportation is on the importation counterfoil (the one the importing customs stamp), not on the exportation counterfoil.
- Options: (a, preferred) move the date to Counterfoil[2] (`IMP-1`); (b) if it is meant as the date the holder promised, state it in a note instead, since the element means the customs time limit.
- Needs decision: no

### carnet/01#F3 · Medium · Office of subsequent entry names the first office of entry
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name` = `Island Customs Service, Selanu airport`
- Why: UBL defines OfficeOfSubSequentiallyEntryLocation as "A location that is involved in the subsequent entry of goods in a consignment … where goods are processed after their initial entry point". Selanu airport is where the samples first enter Lisavu (the importation counterfoil is stamped there: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:CustomsOfficeLocation/cbc:Name` = `Customs office, Selanu airport`); the consignment names no initial entry point before it, and Bayvarra is only a transit country. The value is the first office of entry, not a subsequent one. In addition the Location name is the customs administration plus the place, not just the place.
- Condition: OfficeOfSubSequentiallyEntryLocation is either absent or names an office where the goods are processed after a different, earlier point of entry; a Location name names the place.
- Options: (a, preferred) remove it; the importation counterfoil's CustomsOfficeLocation already says where the goods enter; (b) use it only if the story has a second office (e.g. clearance at the fair after entry at the airport) and then name that place.
- Needs decision: no

### carnet/01#F4 · Medium · FullnessIndicationCode carries a system boundary
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL defines FullnessIndicationCode as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." Cradle to gate is the boundary of a product life-cycle assessment, a concept the definition does not cover, and the emission here is a manufacturing emission with no transport equipment involved. The same value with the list EmissionBoundaryCode occurs in 39 examples (`grep -rl --include='*.xml' 'EmissionBoundaryCode' world/examples | wc -l`); the 5 other uses carry LoadTypeCode `FCL`, which fits the definition.
- Condition: FullnessIndicationCode, where present, says how full a piece of transport equipment is; the cradle-to-gate boundary, if kept, is in an element whose definition covers it (e.g. the lifecycle stage description already present) or in text.
- Options: (a, preferred) drop FullnessIndicationCode here (there is no transport equipment) and keep the boundary in `LifecycleStageDescription`, which already says it; (b) record the lack of a boundary element as a finding for the UBL TC.
- Needs decision: no

### carnet/01#F5 · Low · Item master data the carnet does nothing with
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:Name` = `Load capacity`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile`
- Why: A carnet's general list identifies the goods for customs: description, quantity, weight, value, origin, marks (own knowledge of the ATA carnet). Keywords ("assigned by the seller party", but a carnet has no seller), warranty, load-test results, emissions, circularity profile, repairability and product documentation look copied from the item master data; neither guarantor nor customs do anything with them in this flow. Inside the copied emission the arithmetic does not hold either: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82` per base quantity 1 each gives 0.82, not 96 kg (outside this lens; noted for the logistics and merge parts).
- Condition: The carnet's item carries only data a party of the carnet procedure uses to identify or value the goods; anything else has a stated reason in the flow.
- Options: (a, preferred) reduce the item to identification and customs data (name, description, seller's ID, HS codes, origin, dimensions if used to identify); (b) keep a given aggregate only with a reason in the story (e.g. the fair asks for the sustainability data — then the carnet is still the wrong document).
- Needs decision: no

### carnet/01#F6 · Low · Party master data the carnet does nothing with
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/GoodsItemPassport/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007376017`
- XPath: `/GoodsItemPassport/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: Nothing in a temporary-admission carnet uses the holder's stock listing, share capital or warehousing service provider, or the VAT registration of the chamber and of the customs administration: no tax is charged and no party pays another under this document. They look copied from party master data (section 4.8).
- Condition: Every party aggregate in the carnet carries only data the carnet procedure uses (identity, address, contact, legal identity where the guarantee needs it), or the reason for the rest is visible in the flow.
- Options: (a, preferred) remove SecurityListing, CorporateStockAmount/FullyPaidSharesIndicator, ServiceProviderParty and the PartyTaxScheme of issuer and customs; (b) keep one with a stated reason.
- Needs decision: no

### carnet/01#F7 · Low · "Mobile on the road" contact carries the order desk's landline
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Name` = `Mobile on the road`
- XPath: `/GoodsItemPassport/cac:RepresentativeParty/cac:Person/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- XPath: `/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`
- Why: The representative's contact is named as his mobile phone while travelling with the goods, but its number is the holder's order desk telephone; the holder's mobile number is a different one (`/GoodsItemPassport/cac:HolderParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`). The name and the value contradict each other, and customs reaching the person accompanying the goods would call the office.
- Condition: The representative person's contact number is a number that reaches that person while accompanying the goods, distinct from the order desk's number, or the contact name does not claim it is a mobile.
- Options: (a, preferred) give the person a mobile number of his own; (b) rename the contact.
- Needs decision: no

### carnet/01#F8 · Low · Elements used whose UBL definitions are copied from other contexts
- XPath: `/GoodsItemPassport/cbc:StatusCode` = `VALID`
- XPath: `/GoodsItemPassport/cbc:ExportReasonCode` = `EXHIBITION`
- XPath: `/GoodsItemPassport/cbc:VersionID` = `1`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: In UBL 2.5 the GoodsItemPassport's StatusCode and Status are defined as "The reason for importing the goods", ExportReasonCode as "The reason for importing the goods", VersionID as "the current version of this request for proof", the counterfoil's GoodsItemPassportID as the carnet number "usually the number on the upper part of the orange hazard placard required on the means of transport", and SignatoryContact as "The individual representing the exporter who signs the Certificate of Origin application". The values follow the element names (a record status, an export reason, the carnet number, the chamber's signing desk), which is what was evidently meant, but under the semantic-conformance rule they do not fit the definitions as written. This is a defect of the model, not of the example.
- Condition: Each such use is either justified and recorded as a finding on the UBL 2.5 definitions, or the element is not used.
- Options: (a, preferred) keep the values and record the copied definitions in `analysis/codelist-decisions.md` for the write-up to the OASIS UBL TC; (b) drop StatusCode/Status (the issuer endorsement already says `Issued`).
- Needs decision: yes

### carnet/01#F9 · Low · Additional document reference without saying what it is
- XPath: `/GoodsItemPassport/cac:AdditionalDocumentReference/cbc:ID` = `SCC-FAIR-26-INV`
- Why: The reference carries only an ID; no DocumentType or DocumentTypeCode says what the document is (from the ID, perhaps an invitation to the fair by the Selanu chamber). The carnet's other references are typed by their element; this one is not, and no other example of the flow has this ID.
- Condition: The reference says what kind of document it is (DocumentTypeCode or DocumentType), or it is removed.
- Options: (a, preferred) add the document type; (b) remove it if the carnet does not need it.
- Needs decision: no

## Checked and consistent
- ValidityPeriod 2026-05-25 to 2027-05-25: one year, the maximum validity of an ATA carnet; FinalReexportationDate 2026-11-21 lies within it and matches the note "to come back within six months" (2026-05-25 + 6 months = 2026-11-25).
- IssuerParty and ExportingGuarantorParty are the same chamber, as in the ATA chain where the issuing association guarantees in its own country; ImportingGuarantorParty is the Selanu chamber, the same as in 02, 03 and 04.
- RepresentativeParty is the holder with the person accompanying the goods, which fits "The Party who accompanies the Goods while temporarily exported".
- The counterfoils' customs offices follow the route: exportation and re-importation at the Urvanian land border, importation and re-exportation at Selanu airport, transit country Bayvarra.
- DocumentDistribution `COLLECT` to the holder fits: the holder collects the carnet from the chamber.
- check_ids.py: ISIN `XU0001042501` check digit correct.

## Considered and refuted
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:ExportationDocumentReference/cbc:ID`: suspected that a stamp is not "a document used for the export" — refuted because the ID can be read as the customs' record of the export act, which is a document of the export; the reference is typed by its element.
- `/GoodsItemPassport/cac:IssuerEndorsement/cbc:DocumentID`: suspected that the carnet's own ID is not "An identifier for this endorsement" — refuted because the issuer's endorsement is the endorsement of this very carnet, and UBL names the element Document Identifier; the reading is legitimate.
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransportAdvisorParty/cac:PartyName/cbc:Name`: suspected that a forwarder has no place in a carnet — refuted because the forwarder advises on the route via Bayvarra, which the carnet's transit country reflects, and "provides transport advice" fits.
- `/GoodsItemPassport/cbc:ExportReason`: suspected text copying the code — refuted because the text adds the fair, which the code does not say.
