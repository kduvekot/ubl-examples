# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/21#F1 · High · The bench's emission value, factor and base do not agree
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: Factor × base = 0.82 × 1 EA = 0.82, not the stated 96 kg CO2e (96 / 0.82 = 117.1); `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies". Added by the merge (no part raised it), as in 19, 20, sea d and the earlier flows.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a) preferred: drop factor and base; (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: merge (no part raised it)

### sea/21#F2 · Medium · Gate number in AdditionalStreetName of the despatch party's postal address
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." A business-park gate is a vehicle access point, not a street, and has no place in the postal address of the party a receipt advice goes to. 79 occurrences in 76 files, always Lumeway's address (parties, grep over `*.xml`).
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop it, giving it only where vehicles need it; (b) the park's internal road name.
- Needs decision: no
- From: broad (F1), parties (F1)

### sea/21#F3 · Medium · A language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F2)

### sea/21#F4 · Medium · Lifecycle stage "Manufacturing" for an emission described from the mine to the factory gate
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: The code names one stage, the description covers extraction, transport and manufacturing (cradle to gate, EN 15804 A1–A3, own knowledge). Added by the merge, as in 19 and 20.
- Condition: Code and description name the same scope.
- Options: (a) preferred: a product-stage code or drop the code; (b) narrow the description.
- Needs decision: no
- From: merge (no part raised it)

### sea/21#F5 · Medium · "Cradle to gate" in an element that says whether transport equipment is full
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty …"; a footprint boundary is another concept. Added by the merge (TC write-up), as in 19 and 20.
- Condition: The element is absent from the item's footprint, or holds a fullness indication.
- Options: (a) preferred: drop it; (b) record the missing boundary element for the UBL TC.
- Needs decision: no
- From: merge (no part raised it)

### sea/21#F6 · Low · Document status "no status"
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `NoStatus`
- Why: "No status" conveys what absence conveys (rule: no fillers, nothing implied by absence); 26 `DocumentStatusCode` = `NoStatus` in the examples (context, grep over `*.xml`).
- Condition: `DocumentStatusCode` is present only where the status is worth stating.
- Options: (a) preferred: drop it; (b) keep it by a recorded project decision.
- Needs decision: no
- From: context (F4)

### sea/21#F7 · Low · The warehouse asks the seller for a credit that would go to the buyer
- XPath: `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectActionCode` = `CREDIT`
- XPath: `26-CreditNote.xml:/CreditNote/cac:OriginatorDocumentReference/cbc:ID` = `VT-CLAIM-26-0019`
- Why: `RejectActionCode` is "A code signifying the action that the delivery party wishes the despatch party to take as the result of a rejection". The delivery party is Nalevi Warehousing, which stores the goods for Velumi and has no purchase relation with Lumeway; a credit can only go to the buyer, and in the flow it follows the buyer's own claim. Counter-argument (parties, and broad on the risk question): the element is defined as the delivery party's wish, the warehouse reports for the buyer whose goods it receives, and the credit note is then issued to the buyer; the flow is consistent. The merge cannot settle whether the warehouse may ask in its own name.
- Condition: The action the warehouse asks for is one it can want from the despatch party, or the advice states it relays the buyer's request.
- Options: (a) preferred: keep CREDIT and state (e.g. in a note) that the warehouse relays Velumi's request; (b) a replacement or no action, leaving the remedy to the buyer's claim.
- Needs decision: yes
- From: context (F1); parties' refutation carried as counter-argument

### sea/21#F8 · Low · Received quantity 11 reads as a missing casting, though the twelfth arrived damaged
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `11`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- Why: Twelve castings were despatched (`20-DespatchAdvice.xml`), and the twelfth arrived in a crushed box: it was received and rejected. `ReceivedQuantity` is "The quantity received"; 11 reads as eleven arrived, while 11 + 1 = 12 works only if "received" means "accepted". Ambiguous rather than contradictory.
- Condition: The quantities state unambiguously that 12 arrived, 11 were accepted and 1 was rejected.
- Options: (a) preferred: `ReceivedQuantity` 12 with `RejectedQuantity` 1; (b) keep 11 and record the reading as the world's rule.
- Needs decision: no
- From: broad (F2)

### sea/21#F9 · Low · The rejected side frame is not identified, although every frame was despatched with a serial number
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectReason` = `One box crushed at the port; the frame inside is cracked.`
- XPath: `20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230`
- Why: The despatch advice gives each of the twelve side frames an item instance with its own serial (VI-SF-01230 to VI-SF-01241). The receipt rejects one as cracked without saying which, so the credit and any claim against carrier, port or insurer cannot be tied to a unit; the receipt line's item has room for it (`ItemInstance`).
- Condition: The rejected unit is identified by the identifier it was despatched with.
- Options: (a) preferred: the rejected frame's item instance (serial) on line 2; (b) its serial in the reject reason.
- Needs decision: no
- From: context (F2), logistics (F2)

### sea/21#F10 · Low · The receipt is not linked to the shipment, container or pallet received; the bill of lading reference has ID only
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box crushed at the port; the frame inside is cracked.`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`
- Why: The advice has no Shipment (consignment `LD-CS-26-0133`, container `TWLU4120872`) and no handling units, although the goods arrived as 25 SSCC-labelled pallets; the crushed box is on the one pallet of boxes (SSCC above), which the receipt does not name. The damage is the basis of the credit requested here and of the later claim documents (`26-CreditNote.xml`, `28-DebitNote.xml`). The bill of lading is referenced by number only, without saying what it is.
- Condition: The receipt identifies the consignment or container received and the pallet carrying the damaged box; the bill of lading reference states its type.
- Options: (a) preferred: a Shipment with consignment and container, and the SSCC of pallet 25 on line 2; (b) at least the container ID and the document type.
- Needs decision: no
- From: logistics (F1), broad (F5)

### sea/21#F11 · Low · Contacts whose name, job title and department disagree
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The receipt is issued by the warehouse's goods-in ("Counted and checked at goods-in"), and its contact is named Goods inwards, but is a customer service officer in Sales; the buyer's Purchasing contact is also in Sales. Name, title and department contradict each other.
- Condition: Each contact's name, title and department describe the same function (goods receipt, purchasing).
- Options: (a) preferred: matching titles and departments; (b) drop title and department.
- Needs decision: no
- From: broad (F3), parties (F3)

### sea/21#F12 · Low · Tax registration and share capital of the despatch party in a receipt advice
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The warehouse reports quantities received and rejected; it carries no amounts or taxes and does nothing with Lumeway's sales-tax registration or share capital (copied master data, section 4.8). The other parties carry no tax scheme.
- Condition: The despatch party carries only the party data a receipt advice uses.
- Options: (a) preferred: drop `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator`; (b) keep them with a reason.
- Needs decision: no
- From: parties (F4), money (F1)

### sea/21#F13 · Low · Catalogue and product-passport data copied into the receipt advice
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- Why: A receipt advice reports what was received and in what condition. The bench's item repeats the whole catalogue description (keywords, warranty, sales conditions, load test, emissions with the errors of F1, F4, F5, circularity); neither the warehouse nor the seller uses it as information about the receipt. The second line does without it.
- Condition: The receipt lines identify the items received (identifiers, name, instance where relevant) and carry no catalogue or sales data.
- Options: (a) preferred: reduce the bench's item to its identifiers and name.
- Needs decision: no
- From: broad (F4), context (F3)

### sea/21#F14 · Low · GTINs in the distributor's GS1 company prefix, not the manufacturer's
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: Valdara's bench and side frame carry GTINs in `9520610`, the prefix of Lumeway's GLN `9520610900008`; under GS1 rules the brand owner allocates the GTIN (own knowledge). Added by the merge, as in 19, 20, sea d and retail.
- Condition: The GTINs are in the brand owner's prefix, or the world states that Lumeway is the brand owner.
- Options: (a) preferred: GTINs in Valdara's prefix; (b) record Lumeway as brand owner.
- Needs decision: yes
- From: merge (no part raised it)

### sea/21#F15 · Low · World item numbers with valid GS1 check digits
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: Both carry a valid GTIN-12 check digit (merge recalculated: 7 and 4) in prefix 077 (GS1 US range; own knowledge), so they can be mistaken for real GTINs. Added by the merge, as in 19 and 20.
- Condition: The world item numbers cannot be read as valid GTINs, or the convention is recorded.
- Options: (a) preferred: a non-GTIN format; (b) record the convention.
- Needs decision: yes
- From: merge (no part raised it)

### sea/21#F16 · Low · Signature with an ID and a signatory only
- XPath: `/ReceiptAdvice/cac:Signature/cbc:ID` = `NW-SIG-26-RA`
- Why: `Signature` carries only an `ID` and a `SignatoryParty`: no signature method, no date or time, no attached or referenced digital signature, so it says nothing more than the party names already say. In addition, the ID is built from the document type, which reads as an identifier made up for the example rather than the signer's own numbering. Added by the merge (no part raised it), aligned with the earlier flows' merges (air, utilities, retail, sea b: Low/yes, most signatures in the examples have this form).
- Condition: The signature carries what makes it a signature (method, time, or the referenced signature), or is absent; its ID is the signer's own number.
- Options: (a) preferred: drop the `Signature` where no signature is applied; (b) add `SignatureMethod`, a signing date/time and the digital signature reference.
- Needs decision: yes (a world-wide convention)
- From: merge (no part raised it)

## Checked and consistent
- References: order `VT-PO-26-0127`, despatch advice `LD-DA-26-0145` (header and both lines, line IDs 1 and 2) and bill of lading `TOL-BL-26-0139` exist and agree in parties (broad, context, logistics).
- Quantities: 96 of 96 benches; side frames 11 + 1 rejected = 12 despatched; header `PARTIAL`, `DAMAGED`, `CREDIT` agree with line 2 (all parts).
- The rejected frame is what the credit note credits: one frame at 64 XBL (`26-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `1`, `26-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `64.00`, at `22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `64`), delivery date `26-CreditNote.xml:/CreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-21` (money).
- Dates: received and issued 2026-05-21 (17:22), after the discharge (05-18) and the import declaration (05-19) (broad, context, logistics).
- Parties: issuer and signatory Nalevi (`IC41722`) is the despatch advice's delivery recipient and the order's delivery party; Nalevi and Velumi carry `en-XL` and Lisavan renderings; ISIC 5210 / 4649 fit; GTINs and GLN pass `check_ids.py` (parties, broad).

## Considered and refuted
- `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`: credit requested from the seller although the risk passed at loading in Lumeport (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRisk` = `Risk passes when the goods are on board the vessel in Lumeport.`) — refuted: the buyer may ask, and `26-CreditNote.xml` grants it as goodwill under CIF and claims from the insurer (from broad).
- `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`: the warehouse, not the buyer, asking for a credit — refuted by parties (the element is the delivery party's wish; it reports for the buyer); not fully followed by the merge, kept as F7 Low/yes with this argument (from parties).
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedDate` = `2026-05-21`: the B/L's on-carriage receipt event is 05-19 — refuted: that event is planned on the B/L, and the customs inspection explains a later receipt (from broad).
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box crushed at the port; the frame inside is cracked.`: a box crushed in a sealed container — refuted: the container was opened for the customs inspection at Selanu (`28-DebitNote.xml`) (from broad).
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:QuantityDiscrepancyCode`: redundant with 11 + 1 = 12 — refuted: the discrepancy is between despatched and accepted, damage is its type (from context).
- `/ReceiptAdvice/cbc:ReceiptAdviceTypeCode` = `Actual`: needing a passed inspection — refuted: the code covers arrival accepted "or not" (from context).
- `/ReceiptAdvice/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`: the buyer's customs trader number — refuted: imported for that trader, received after clearance (from parties).

## Changed in the merge
- Added by the merge: F16 (signature with ID and signatory only, Low/yes), aligned with the earlier flows.
- Added by the merge: F1 (emission triple, High), F4 (MANUFACTURING), F5 (CRADLETOGATE), F14 (GTIN prefix), F15 (world item numbers), aligned with 19, 20, sea d and the earlier flows.
- context/F4 Needs decision yes → no (F6), aligned with all flows.
- context/F1 Needs decision no → yes (F7): parties refuted it with a definition-based argument; the merge cannot settle it; preferred option changed to the relay note, which satisfies both readings.
- Combined: broad/F1 + parties/F1 → F2; context/F2 + logistics/F2 → F9; logistics/F1 + broad/F5 → F10; broad/F3 + parties/F3 → F11; parties/F4 + money/F1 → F12; broad/F4 + context/F3 → F13.

## Outside this review
- `14-BillOfLading.xml` plans the on-carriage receipt for 2026-05-19; the goods are received on 2026-05-21 (timeline across documents) (from logistics).
