# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/10#F1 · High · Declaration issued after the transportation status reports it accepted and the goods released
- XPath: `/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- Why: The import declaration is issued on 2026-03-24 at 09:54. The carrier's status report of the same morning, issued at 09:10, states that the border crossing was completed at 08:55, "Customs released the goods at the border" and "Import declaration accepted by Bayvarra's customs" (`09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`). A declaration cannot be accepted, and goods released on it, almost an hour before it is lodged. The waybill also expects the import to be declared "by the distributor at the border".
- Condition: the declaration is issued before the release and acceptance reported in `09-TransportationStatus.xml` (before 07:30–08:55 on 2026-03-24).
- Options: (a) preferred: an earlier issue time (pre-lodged before arrival at the border); (b) move the border crossing and the status report after 09:54.
- Needs decision: no

### road/10#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

### road/10#F3 · Low · Certificate of origin referenced by an ID that two documents carry
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: The reference has only an ID, no document type and no version or date. Both `06-CertificateOfOrigin.xml` (application submitted, endorsement "Pending") and `07-CertificateOfOrigin.xml` (approved and legalised) carry this ID with VersionID 1. For a claim of preferential origin the importer must point to the approved certificate; as it stands the reference resolves to both, one of which is not a valid certificate.
- Condition: the reference identifies the approved certificate unambiguously (by type plus a distinguishing version, date or ID) and says it is a certificate of origin.
- Options: (a) preferred: add DocumentTypeCode and the issue date 2026-03-22 (or the version, once 06 and 07 differ in VersionID); (b) give the application in 06 its own ID.
- Needs decision: no

## Checked and consistent
- Shipment CL-SH-26-0154, gross weight 4106.4 kg and goods items (96 benches 3984 kg, 12 castings 122.4 kg) agree with `05-ExportCustomsDeclaration.xml` and the waybill.
- DespatchLineReference lines 1 and 2 of CL-DA-26-0153 resolve to the bench and side-frame lines of `04-DespatchAdvice.xml`.
- PreviousCustomsDeclaration VI-CD-26-0156 is the export declaration of the same goods (`05-ExportCustomsDeclaration.xml`).
- Importer, consignee and notifier Lumeway match the waybill's consignee; consignor Valdara matches the waybill.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: an import declaration giving the Urvanian exit office rather than a Bayvarran office of entry — refuted because the UBL 2.5 ImportCustomsDeclaration has no office-of-entry location (checked in UBL-Entities-2.5.gc: the only location of this kind is Customs Exit Office), and "the customs exit office of the goods being declared" is the exit office on the export side.
