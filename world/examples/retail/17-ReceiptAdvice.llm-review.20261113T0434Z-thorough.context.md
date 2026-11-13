# LLM review: 17-ReceiptAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/17-ReceiptAdvice.xml`, Git blob `47b28c9a1fccb7811613ffb860e40b9269d5dddc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/17#F1 · High · Emission factor times base does not give the emission
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F5).
- Options: drop the emission from the receipt advice (preferred), or correct the factor.
- Needs decision: no

### retail/17#F2 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples). LocaleCode is "A
  code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is a language
  code (213 examples; both counted with `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/17#F3 · Low · "Late" for a delivery that arrived within its slot, while the day's delay goes unmentioned
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaintCode` = `LATE`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaint` = `Arrived 40 minutes into the slot; unloading delayed the next truck.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- Why: TimingComplaintCode is "A complaint about the timing of delivery". Arriving 40 minutes "into
  the slot" is arriving within the slot, which is not late; no document of the flow defines a slot
  (08-Order.xml has no requested delivery time). The delivery the carrier announced for 2026-04-29 at
  14:00 arrived the next morning at 10:40, which the complaint does not mention. Code and text do not
  describe the same lateness.
- Condition: the complaint text states a lateness against a time the flow defines, and the code
  matches it.
- Options: (a) preferred: complain about the arrival a day after the announced time, or about arrival
  after the end of an agreed slot that the order states; (b) drop the complaint.
- Needs decision: no

### retail/17#F4 · Low · Two photo references that do not match each other or the receipt date
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BM-GI-PHOTO-26-0510`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:DocumentReference/cbc:ID` = `BS-PHOTO-26-0118`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:DamageDocumentationAttachment/cac:ExternalReference/cbc:URI` = `https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg`
- Why: the damage on pallet 3 is documented by a photo attachment. The document also carries two
  untyped references to photos with different prefixes (`BM-` and `BS-`) and numbers (`0510`,
  `0118`), neither of which resolves; in this flow the four digits after `26-` usually follow the
  issue date (e.g. `BM-SIG-26-0424` on the order of 2026-04-24), so `0510` reads as 10 May, after the
  receipt of 30 April. The receiver cannot tell whether these are the same photo, another photo or
  something else.
- Condition: each reference says what it is, and the photo of the damage is identified one way.
- Options: keep the attachment and drop the two references (preferred), or give one typed reference
  with the attachment.
- Needs decision: no

### retail/17#F5 · Low · Status "No status", a signature that signs nothing, and master data without use
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/ReceiptAdvice/cac:Signature/cbc:ID` = `BM-SIG-26-RA`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: an original receipt advice has no status to report; the signature has only an ID and a
  signatory; the item repeats the full catalogue entry (sales conditions, footprint, circularity,
  customs codes) and the parties carry share capital, a customs trader number and social media, none
  of which a receipt uses (IND5/IND6).
- Condition: everything present has a use in the receipt.
- Options: drop them; reduce the item to identifiers and name.
- Needs decision: no

## Checked and consistent
- OrderReference `BS-PO-26-0224`, DespatchDocumentReference `LD-DA-26-0229` and the line references
  (order line 1, despatch line 1 of `LD-DA-26-0229`) resolve to 08 and 12.
- Quantities: 23 received + 1 rejected = 24 despatched; on the damaged pallet 3 + 1 = 4.
- The damaged handling unit `095206102170000038` is pallet "003 of 006" in 12-DespatchAdvice.xml,
  matching the photo `pallet-3.jpg`.
- DeliveryAcceptanceCode "Partly refused", reject reason "Damaged", reject action "Credit requested"
  and the type code "Actual" agree with each other and with the note; 19-CreditNote.xml follows.
- Received 2026-04-30 10:40, issued 15:21 the same day.

## Considered and refuted
- `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks`: "One carton torn" while
  12-DespatchAdvice.xml describes no cartons — refuted as a question of 12's package description, not
  of this receipt (see 12's review on the packages).
