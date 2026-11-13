# LLM review: 13-Waybill.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/13-Waybill.xml`, Git blob `0e28ae8a70150ecfdb1e12ab9527a6f9336f5e5e` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 51ac641 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/13#F1 · Medium · A consignment note without the goods, the place of taking over and the place of delivery
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `996`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- Why: a Waybill is "A transport document describing a shipment", and this one is presented as a CMR
  consignment note. Its shipment has only an ID, a gross weight and a consignment with the consignee:
  no goods description, no number of packages or handling units, no marks, no place and date of taking
  over, no place of delivery. These are the particulars a consignment note exists to record (CMR art.
  6(1), from own knowledge) and what the consignee checks on delivery ("Deliver against signature of
  the consignee"). 12-DespatchAdvice.xml has them (six pallets, marks "BRIGHTMARKET LUMEPORT / 001 of
  006" …, Marrowdale to the Lumeport store).
- Condition: the waybill states what is carried (description, number and type of handling units,
  marks), where it is taken over and when, and where it is to be delivered.
- Options: add the six pallets with marks and a goods description, the pickup (Marrowdale, 2026-04-29)
  and the delivery location (the store's goods-in) (preferred).
- Needs decision: no

### retail/13#F2 · Medium · The consignment ID given as the shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or
  Forwarding Instruction associated with this shipment". `LD-CS-26-0228` is the consignment's own ID
  (same document, Consignment/ID). The forwarding instruction of this shipment is Lumeway's transport
  request `LD-TR-26-0227`.
- Condition: ShippingOrderID is the identifier of the forwarding instruction, or absent.
- Options: `LD-TR-26-0227` (preferred), or drop the element.
- Needs decision: no

### retail/13#F3 · Medium · "Three originals: consignor, consignee, carrier", but the consignor gets an electronic copy
- XPath: `/Waybill/cbc:Note` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed".
  It sends the consignee's original with the goods and an electronic copy to the consignor, Lumeway.
  The note says the consignor receives an original. The two statements about the consignor's copy
  contradict each other.
- Condition: the note and the distribution list agree on what the consignor receives.
- Options: (a) preferred: distribute an original to the consignor (and mention the carrier's
  original or leave it implicit as the issuer's); (b) change the note.
- Needs decision: no

### retail/13#F4 · Medium · A language code in LocaleCode
- XPath: `/Waybill/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/13#F5 · Low · A CMR consignment note for a domestic carriage
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- Why: the CMR convention governs international carriage by road, where taking over and delivery are
  in two different countries (CMR art. 1, from own knowledge). This carriage runs from Marrowdale to
  Lumeport, both in Bayvarra. A real international convention is invoked for a carriage it does not
  cover, unless Bayvarra applies the CMR to domestic carriage by its own law, which the documents do
  not say.
- Condition: the document type matches the carriage (a national consignment note), or the world
  records that Bayvarra applies the CMR domestically.
- Options: (a) a national road consignment note type (preferred); (b) record the domestic application
  of the CMR in the world's story.
- Needs decision: yes

### retail/13#F6 · Low · Issue location named after the consignor
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeway Distribution`
- Why: IssueLocation is "The location where this waybill was issued". The value is a company, not a
  place; the place is the Marrowdale distribution centre, where Bayforth's driver takes the goods over.
- Condition: the issue location names a place.
- Options: "Marrowdale" or "Lumeway distribution centre, Marrowdale" with its address or GLN.
- Needs decision: no

### retail/13#F7 · Low · Signature and master data without use
- XPath: `/Waybill/cac:Signature/cbc:ID` = `BF-SIG-BF-WB-26-0231`
- XPath: `/Waybill/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the signature has only an ID and the carrier as signatory; a consignment note is signed by
  consignor and carrier, and this record carries neither a method nor an attachment. A domestic
  carriage uses no customs trader number, share capital or social-media profile (IND5/IND6).
- Condition: a signature with what makes it one (and the consignor's where the note says it is
  signed), or none; parties without unused master data.
- Options: drop the master data; complete or drop the signature.
- Needs decision: no

## Checked and consistent
- SenderParty and CarrierParty Bayforth (the carrier issues the waybill), ReceiverParty and
  ConsignorParty Lumeway, consignee Brightmarket, as in 11 and 12.
- Shipment ID `LD-SH-26-0230`, consignment ID and gross weight 996 kg agree with 12-DespatchAdvice.xml.
- The waybill is issued on the day of pickup (2026-04-29), within the service start of 11.
- 16-Invoice.xml refers to this waybill by its ID `BF-WB-26-0231`.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator`: `false` in a domestic carriage — refuted because the indicator
  states that no value was declared for carriage, which is a real statement on a consignment note.
- `/Waybill/cbc:Description`: describes the transport rather than the contents — refuted because
  "Text describing the contents of the Waybill" refers to the document's content, which is this
  carriage.
