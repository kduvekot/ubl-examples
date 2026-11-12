# LLM review: 06-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/06-CertificateOfOrigin.xml`, Git blob `faaaba8b3816ead4cce39fdf9204e831ab65f4f7` (committed)
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

### road/06#F1 · High · Emission factor × base does not give the emission value
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

### road/06#F2 · Medium · The buyer's order number used as the job number of the application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- Why: OriginalJobID is "the latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." It is an identifier of the application job in the issuer's or applicant's system. The value is the buyer's purchase order (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), a document of another party and another kind; the order is already referenced as the supporting document (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`). The application has its own reference (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `VI-AP-26-0158`).
- Condition: OriginalJobID holds a job number of the CoO application (assigned by the applicant or the chamber), not an order number.
- Options: (a) preferred: a job number of the application, the same in 06 and 07 since they are the same job (e.g. the application reference or a chamber job number); (b) if no separate job number exists, the application reference VI-AP-26-0158.
- Needs decision: no

### road/06#F3 · Low · Previous job of a first application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: PreviousJobID is "an identifier for the previous job used in case the application requires query or change". This is a first application (VersionID 1, no amendment or replacement in the flow), and VI-CO-25-0412 is a 2025 number that no example in the flow issues; nothing explains which earlier job it is or why this application refers to it.
- Condition: PreviousJobID is present only if the application continues or changes an earlier job, and that job is identifiable (or the reason is stated).
- Options: (a) preferred: remove PreviousJobID; (b) if the 2025 certificate for the same benches is meant to support this one, say so (e.g. as a supporting document reference with a type).
- Needs decision: no

### road/06#F4 · Low · Same document ID and version for the application and for the approved certificate
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cbc:VersionID` = `1`
- Why: `06-CertificateOfOrigin.xml` (application submitted, endorsement pending, issued 2026-03-20) and `07-CertificateOfOrigin.xml` (approved and legalised, issued 2026-03-22) carry the same ID and the same VersionID 1, with different content. The import declaration refers to the certificate by ID only (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`), which therefore resolves to both. ID is assigned by the sender; the sender of 06 is the applicant (Valdara signs it), yet it already carries the chamber's certificate number.
- Condition: the two documents can be told apart by their identifiers (different ID, or the same ID with different VersionID), and a reference to the approved certificate resolves to 07 only.
- Options: (a) preferred: keep FCC-CO-26-0157 for the certificate and give 07 VersionID 2 (or give the application 06 its own ID, e.g. the application reference); (b) let the import declaration also quote the version or issue date.
- Needs decision: no

## Checked and consistent
- Shipment ID CL-SH-26-0154, goods item quantities (96, 12), gross weights (3984, 122.4 kg) and declared values agree with `05-ExportCustomsDeclaration.xml` and `10-ImportCustomsDeclaration.xml`.
- Exporter, importer and issuing country (XU) agree with the export and import declarations.
- Origin XU for both goods items agrees with the item OriginCountry in the order and the despatch advice.

## Considered and refuted
- `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cbc:ID`: the shipment ID assigned by the 3PL appears in the certificate (issued 2026-03-20/22) before the despatch advice that first reports it (`04-DespatchAdvice.xml`, 2026-03-23) — refuted because a shipment number is commonly reserved when the shipment is planned; the despatch advice is not where it is created.
