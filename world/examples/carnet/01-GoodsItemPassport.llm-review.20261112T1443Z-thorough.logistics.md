# LLM review: 01-GoodsItemPassport.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### carnet/01#F1 · High · Emission value is not factor × base
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". With a base of 1 EA (one bench), factor × base = 0.82 × 1 = 0.82, but the stated value is 96 kg CO2e. No other figure in the item turns 0.82 into 96: 96 / 0.82 = 117, which matches neither the material consumed per bench (34 kg steel + 22.5 kg hardwood = 56.5 kg) nor the goods item weight (83 kg for 2 benches). The same item data occurs with the same three values in 39 examples (every `EnvironmentalEmission` with a `ValueFactorNumeric` over `world/examples/*/*.xml`, counted with an lxml script over `*.xml` only), all failing the same check.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure` (in consistent units), or no factor/base is given.
- Options: (a) preferred: make the factor the emission per bench (96 per 1 EA) or express it per kg of a stated base (e.g. a factor per kg of material with that mass as base), so the product holds; (b) drop factor and base if the 96 kg is a measured total with no single factor behind it.
- Needs decision: no

### carnet/01#F2 · High · The carnet as issued already shows all four counterfoils stamped
- XPath: `/GoodsItemPassport/cbc:IssueDate` = `2026-05-25`
- XPath: `/GoodsItemPassport/cbc:IssueTime` = `15:04:00`
- XPath: `/GoodsItemPassport/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Issued`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:Note` = `Stamped by customs.`
- Why: The document is the carnet as issued by the chamber (status "Issued", validity starting on the issue date). At that moment the goods have not yet left Urvania, so none of the counterfoils can have been stamped; yet all four (exportation at the Urvanian border, importation and re-exportation at Selanu airport, re-importation at the Urvanian border) say "Stamped by customs.", with their stamp and voucher references. The flow itself places these events later: on 2026-07-24 the island's customs still had no re-export record (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`) and the re-importation is only proven on 2026-08-28 (`04-ProofOfReexportation.xml:/ProofOfReexportation/cbc:IssueDate` = `2026-08-28`). The document thus states, at issue time, events that happen up to three months after it.
- Condition: either the carnet as issued carries counterfoils without customs stamps (no "Stamped by customs." and no stamp references), or the example represents a later state of the carnet whose issue date/version follows the last stamped event.
- Options: (a) preferred: keep the example as the carnet at issue and leave the counterfoils unstamped (the stamps are evidenced by 04), because the flow starts with issuance; (b) show the carnet as returned after use (later version with its own date), which changes the role of the example in the flow.
- Needs decision: yes

### carnet/01#F3 · Low · Final re-exportation date on the exportation counterfoil, and not six months
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `/GoodsItemPassport/cbc:Note[2]` = `Samples for the Selanu trade fair; to come back within six months.`
- Why: Under the ATA Convention (my own knowledge) the time limit for re-exportation is fixed by the customs of the country of temporary admission when they stamp the importation voucher; the exporting customs do not set it. Here it sits on the exportation counterfoil (EXP-1, Urvanian border post). The date is also not "six months" from either reference point stated: six months from issue (2026-05-25) is 2026-11-25. The date matters for the flow because the request and reminder (02, 03) are judged against it.
- Condition: the final re-exportation date is on the importation counterfoil, and it agrees with the time limit stated in the note (or the note states the basis of the date).
- Options: (a) preferred: move the date to `GoodsItemPassportCounterfoil[2]` (IMP-1) and align it with the note; (b) keep it on EXP-1 and explain in the note why the exporting side records it.
- Needs decision: no

### carnet/01#F4 · Low · Customs offices named two ways and without identifiers
- XPath: `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name` = `Island Customs Service, Selanu airport`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:CustomsOfficeLocation/cbc:Name` = `Customs office, Selanu airport`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:CustomsOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: The same office at Selanu airport is named in two different ways, one of them with the company name in the location name ("the name is the place, not the company"), and none of the locations carries an identifier, although the air flow identifies Selanu airport by UN/LOCODE (`air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`). The Urvanian border post is named only descriptively ("land border, Urvanian side") with no place name or code.
- Condition: one place is named one way in the example; each customs office location carries an identifier (UN/LOCODE or a customs office code) where the world has one.
- Options: (a) preferred: add `cbc:ID` (XLSLA or an office code) and use one name; (b) at least use the same name in both places.
- Needs decision: no

### carnet/01#F5 · Low · References with only an ID that does not say what it is
- XPath: `/GoodsItemPassport/cac:AdditionalDocumentReference/cbc:ID` = `SCC-FAIR-26-INV`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cac:ExportationDocumentReference/cbc:ID` = `EXP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:ImportationDocumentReference/cbc:ID` = `IMP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cac:ReexportationDocumentReference/cbc:ID` = `REEXP-1-STAMP`
- XPath: `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cac:ReimportationDocumentReference/cbc:ID` = `REIMP-1-STAMP`
- Why: None of these references has a DocumentType or description; "SCC-FAIR-26-INV" (presumably the fair's invitation) is not obvious, and the "...-STAMP" IDs refer to a stamp, which is not a document "used for the export/import of the goods". The re-importation document is identified differently in 04 (`04-ProofOfReexportation.xml:/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`), so the two cannot be linked.
- Condition: each reference says what kind of document it is (DocumentType or DocumentTypeCode), and the same customs document has the same ID wherever it is referenced in the flow.
- Options: (a) preferred: give the references the customs document numbers used in 02/04 and a DocumentType; (b) drop the stamp references if no document stands behind them (the counterfoil and voucher already identify the event).
- Needs decision: no

### carnet/01#F6 · Low · Item number looks like a real GTIN-12
- XPath: `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- Why: The 12-digit number has a valid GTIN-12 (UPC-A) check digit (7) and is given with a barcode symbology, so it reads as a real GTIN; GS1 prefix 770–771 is, to my knowledge, allocated to GS1 Colombia, and 12-digit UPC-A numbers starting with 7 lie in GS1 US company-prefix space. The schemeID is the world's own, but the rule "fictional values must not be mistaken for real ones" asks for a check against GS1. The same number occurs in 39 examples, and other numbers of the same pattern (771…, 772…) in further examples (grep over `*.xml`).
- Condition: the item number cannot be read as a GTIN assigned in the real GS1 system, or the sources record why the prefix is safe.
- Options: (a) preferred: confirm against the recorded verification of the world's item scheme; if none exists, choose a pattern that is not a valid GTIN; (b) keep it and record the reasoning in the sources.
- Needs decision: yes

## Checked and consistent
- Quantities: goods item 2 EA = counterfoil goods items 2 EA on all four counterfoils.
- Physics, bench weight (figures from the document, densities from my own knowledge): gross 83 kg for 2 benches = 41.5 kg per bench including packing. Materials consumed per bench 34 kg steel + 22.5 kg hardwood = 56.5 kg; with casting yield ~80 % and sawing yield ~60 % the finished bench is ~27 kg steel + ~13.5 kg wood ≈ 40.5 kg, plus 0.4 kg film and straps ≈ 41 kg: consistent. Five slats of ~1750 × 70 × 30 mm at ~700 kg/m³ weigh 5 × 2.6 ≈ 13 kg: consistent with the wood share.
- Dimensions: 1800 × 620 × 780 mm, seat height 450 mm within its stated range 440–460 mm; load 450 kg over three seats is a plausible static test.
- Validity: 2026-05-25 to 2027-05-25 is one year, the maximum validity of an ATA carnet (own knowledge); the counterfoils' re-exportation date lies within it.
- Route: exportation at the Urvanian land border, transit country XB, importation at Selanu airport, re-exportation at Selanu airport and re-importation at the Urvanian border: a coherent round trip; the transport advisor is the Bayvarran forwarder used for air freight to the island.
- Counterfoil carnet IDs all equal the document ID `FCC-DOC-26-0724`, which 02 and 03 reference.
- Commodity codes: national `94017910` is a subdivision of HS `940179`; check_ids found no ID with a check digit to verify.

## Considered and refuted
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:OfficeOfSubSequentiallyEntryLocation/cbc:Name`: suspected misuse, since Selanu airport is the first entry into Lisavu — refuted because the consignment first enters Bayvarra (transit country XB), so the island office is a subsequent entry office.
- `/GoodsItemPassport/cac:Shipment/cac:Consignment/cac:TransitCountry/cbc:IdentificationCode`: transit through Bayvarra without transit counterfoils — refuted because the transit can run under another transit procedure; the carnet need not carry transit vouchers.
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note`: contradiction with 02's "found no re-export stamp" — not kept as a separate finding: in an ATA claim the holder's counterfoil can be stamped while the customs' voucher is missing; the problem that remains is the timing (F2).
- `/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure`: suspected that a pallet (the waste profile mentions pallet straps) would push the gross weight above 83 kg — refuted because this document states no pallet, and the waste profile is generic product data.
- `/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:GoodsItemPassportID`: the UBL definition mentions "the number on the upper part of the orange hazard placard" — a defect of the definition text, not of the value.

## Outside this review
- Whether the samples were at the Selanu fair and back within the dates the other documents imply (timeline across documents).
