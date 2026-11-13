# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/12-WeightStatement.xml`, Git blob `63cbeb9c6ff2202636e981ef15d7262f47f2a1a5` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/12#F1 · Medium · Verified gross mass without weighing method or date, outside the dedicated aggregate
- XPath: `/WeightStatement/cbc:WeightStatementTypeCode` = `VGM`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: the document is a verified gross mass statement. UBL 2.5 has a dedicated aggregate, `TransportEquipment/VerifiedGrossMass` ("The verified gross mass of this piece of transport equipment"), whose `GrossMassMeasure` is "The total verified gross mass of a packed container which includes the cargo weight, block and bracing materials and container tare", with a mandatory `WeighingMethodCode` ("A code signifying the weighing method used (e.g. according the SOLAS Convention)", cardinality 1) and optional weighing date and time (checked in UBL-Entities-2.5.gc). Here the mass is in `TransportEquipment/GrossWeightMeasure`, and neither method nor date and time of weighing are given. Under SOLAS VI/2 a VGM states the method by which it was obtained (own knowledge); the carrier receiving it needs to know which, so the document's purpose depends on it. The dedicated aggregate is used once in the world (`grep -l '<cac:VerifiedGrossMass>' world/examples/*/*.xml`: sea/14-BillOfLading.xml).
- Condition: the verified gross mass is stated with its weighing method and the weighing date (and time), preferably in `VerifiedGrossMass`, and the weighing party there agrees with the document's `WeighingParty`.
- Options: (a, preferred) add `VerifiedGrossMass` (method, date, time, gross mass, weighing party, documentary evidence) to the container, keeping `TareWeightMeasure`; drop the equipment gross weight or keep it equal; (b) state method and date in the document's existing elements if the world keeps the simpler encoding.
- Needs decision: no
- From: logistics (F1), broad (F2, Low)

### cotton/12#F2 · Medium · The shipper named as the party signing the VGM on its own behalf
- XPath: `/WeightStatement/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/WeightStatement/cac:ShipperParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/WeightStatement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- Why: `ResponsibleParty` is "The Party who signs the Verified Gross Mass (VGM) on behalf of the Shipper." The definition presupposes someone other than the shipper (SOLAS VI/2 lets a person duly authorised by the shipper sign; own knowledge). Here it is the shipper itself, so the role says nothing the `ShipperParty` and the signature do not already say: the same pattern as a payer equal to the debtor, which section 6 names as Medium. SOLAS also asks for the name of the person signing, which is not given.
- Condition: `ResponsibleParty` is absent, or names a party or person other than the shipper that signs the VGM for it.
- Options: (a, preferred) drop `ResponsibleParty`, since the ginnery signs its own VGM; (b) a person (e.g. the ginnery's shipping clerk) or another party that signs for it (the forwarder, the port's weighing station).
- Needs decision: no
- From: parties (F1), broad (F3, Low)

### cotton/12#F3 · Medium · Language code in `LocaleCode`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F1), parties (F2)

### cotton/12#F4 · Low · A weighing station is named, but the mass is the arithmetic sum of cargo and tare
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TareWeightMeasure` = `3750`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- Why: `WeighingParty` is "The Party who executes the weight measure (e.g. weighing station)". Recalculated: 6190.29 kg (goods with packaging, 10, 11, 13) + 3750 kg tare = 9940.29 kg exactly. A value to 10 g that equals the declared cargo weight plus the tare is a SOLAS method-2 figure, calculated by the shipper from the weighed contents; a port weighing station points to method 1 (weighing the packed container), and a weighbridge reading would not reproduce the sum to the gram (own knowledge). The weighing party and the figure do not fit one method.
- Condition: the weighing party and the stated mass correspond to one method: a weighed value for the packed container if the port weighed it, or the shipper as the party that weighed the cargo if the mass is the sum with the tare.
- Options: (a, preferred: broad, context) keep the port as weighing party (method 1) with a weighed figure at the weighbridge's resolution (e.g. 9940 kg) and the weighing time; (b, logistics' preference) method 2 with the ginnery as weighing party, which fits the 0.01 kg precision and the bale weights.
- Needs decision: no
- From: logistics (F2), context (F1), broad (F2)

### cotton/12#F5 · Low · The ginnery's sales contact for the VGM
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: here the ginnery is the shipper declaring the verified gross mass of a packed container to the carrier; questions about it go to whoever stuffed and declared the container (shipping or despatch), not to lint sales.
- Condition: the ginnery's contact in this role handles shipping or despatch, or the contact is left out.
- Options: (a, preferred) a shipping / despatch contact; (b) drop the contact (the electronic address is given).
- Needs decision: no
- From: broad (F4), parties (F3)

### cotton/12#F6 · Low · Party master data the weight statement does not use
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WeightStatement/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: a weight statement is "A document used to report weight or verified mass measurements in the transport chain". The carrier's Coastal State sales-tax registration and its share capital of 40000000 XBL, fully paid, and the ginnery's customs-trader number play no part in reporting a mass: nothing is billed, taxed, guaranteed or declared to customs (section 4.8, master data copied in). The carrier's two blocks also appear in 13 and 14.
- Condition: every identifier, registration and capital figure in the parties is one the document has a use for.
- Options: (a, preferred) drop the receiver's `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator` and the sender's customs-trader ID.
- Needs decision: no
- From: money (F1), parties (F5)

### cotton/12#F7 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/WeightStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." The ginnery and the port share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date. (The carrier here has its own date, 1974-03-01.)
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F4)

## Checked and consistent
- Gross minus tare: 9940.29 − 3750 = 6190.29 kg, the gross weight of the goods in 09, 10, 11, 13 and 15.
- Tare 3750 kg fits a 40-foot dry container (about 3700–3900 kg, own knowledge), as invoiced in 17 ("one 40-foot container"). Container fill: 27 bales of about 0.55 m³ each (a universal-density bale of about 1.4 × 0.53 × 0.74 m, own knowledge) are about 15 m³ of about 67 m³, and 9940.29 kg is far below a 40-foot box's maximum gross of about 30 t; the load fits (whether a 40-foot box is the right booking: Outside).
- `check_ids.py`: container TWLU4123110 has a valid ISO 6346 check digit; owner code TWLU is recorded as unassigned in the BIC register source (logistics).
- Shipment SCG-SH-26-0200 is the one in 09, 10, 11, 13 and 15; the receiver Tidewell Ocean Lines is the carrier of 13; the gin is shipper (consignor in 09, 13) and signatory.
- Issued 2026-03-01 15:19, before the bill of lading (2026-03-02 09:37), as a VGM must be. `XLSEL` uses the user-assigned code XL and cannot clash with a real UN/LOCODE.
- Tidewell's full description is identical in 12, 13, 14 and 17; the ginnery's identical to 01 and 11 (parties, block by block).

## Considered and refuted
- `/WeightStatement/cac:Shipment`: the container is not named in the bill of lading 13, so the VGM cannot be tied to it — not a finding of this example (a problem of 13; see Outside) (from broad).
- `/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Port of Selanu Ltd`: a port operator described as a small limited company — refuted, a port operated by a company is common and a weighing station needs no public status (from parties).
- `/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`: a location of the weighing party in a VGM — refuted because where the container was weighed is relevant to the weighing station's identity (from context).

## Changed in the merge
- broad/F2 (Low) split: method and date part merged into logistics/F1 → F1 (Medium, because a VGM's validity depends on the method); the weighing-party-vs-sum part merged with logistics/F2 and context/F1 → F4 (Low).
- broad/F3 (Low) + parties/F1 (Medium) → F2: Medium, as parties: the role repeats the shipper, the pattern section 6 names as Medium for payer = debtor; broad's person option kept as (b).
- money/F1 + parties/F5 → F6: grouped as copied master data.
- F4 options: the parts preferred different methods; the merge marks method 1 (two of three parts) as preferred and keeps logistics' method 2 as option (b).

## Outside this review
- The bill of lading 13 names no container, so the link between this VGM and the carriage rests on the shipment ID only (a problem of 13; from broad).
- Capacity: 27 bales (6129 kg, roughly 13–16 m³) fill about a fifth of a 40-foot container (about 67 m³, payload about 26 t); a 20-foot container would hold them. Whether the gin would book a 40-foot box for this lot is a capacity question across 12 and 17 (from logistics).
- Whether the owner code TWLU is assigned in the real BIC register: logistics found it recorded as unassigned in the repository's BIC source; broad could not check it offline.
