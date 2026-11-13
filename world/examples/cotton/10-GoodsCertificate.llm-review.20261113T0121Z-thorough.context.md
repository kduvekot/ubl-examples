# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/10-GoodsCertificate.xml`, Git blob `a573492644f6156f64f31e963d3578b9c5d69634` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/10#F1 · High · "10 bales sampled out of 80" for a shipment of 27 bales
- XPath: `/GoodsCertificate/cac:Attestation/cbc:Note` = `10 bales sampled out of 80.`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: The certificate is issued for shipment SCG-SH-26-0200, one goods item of 6,129 kg of lint in
  bales of about 227 kg: 6,129 / 227 = 27 bales, the quantity of the order 08. The attestation says
  the inspector sampled 10 of 80 bales. 80 bales of 227 kg would be 18,160 kg. Either the sample
  was drawn from a larger stock than the shipment the certificate covers, which a phytosanitary
  certificate for this consignment cannot attest, or the count is wrong.
- Condition: the number of bales the attestation sampled from is the number of bales of the
  certified shipment, or the certificate explains that the lot inspected is larger and includes the
  shipment.
- Options: (a, preferred) "10 bales sampled out of 27"; (b) keep 80 and state that the inspected lot
  in the warehouse included the 27 bales of the shipment.
- Needs decision: no

### cotton/10#F2 · High · A previous version of a certificate that is at version 1
- XPath: `/GoodsCertificate/cac:PreviousDocumentReference/cbc:ID` = `SCC-PH-25-0198`
- XPath: `/GoodsCertificate/cbc:VersionID` = `1`
- Why: PreviousDocumentReference is "A reference to the previous version of the goods certificate";
  VersionID "Identifies the current version of this goods certificate". Version 1 has no previous
  version. SCC-PH-25-0198 reads as a phytosanitary certificate of 2025, i.e. another certificate
  (perhaps of last season's shipment), not an earlier version of this one.
- Condition: PreviousDocumentReference is present only if the certificate is a later version, and
  then points to that earlier version of the same certificate.
- Options: (a, preferred) leave PreviousDocumentReference out; (b) if last season's certificate is
  relevant, cite it as an AdditionalDocumentReference with a description.
- Needs decision: no

### cotton/10#F3 · Medium · The classing certificate given as the original version of the phytosanitary certificate
- XPath: `/GoodsCertificate/cac:OriginalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- Why: OriginalDocumentReference is "A reference to the original version of the goods certificate".
  XL-CLS-2026-0042 is a cotton classing certificate (CertificateTypeCode COTTONCLASS, in the item of
  this same document), a different certificate of a different kind, not an earlier version of this
  phytosanitary certificate, which is itself at version 1.
- Condition: OriginalDocumentReference is present only for a later version, pointing to version 1
  of the same certificate.
- Options: (a, preferred) leave OriginalDocumentReference out; the classing certificate is already
  in the item's Certificate.
- Needs decision: no

### cotton/10#F4 · Medium · A phytosanitary certificate issued by a chamber of commerce and sanctioned by customs
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:LegalAuthorityParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `/GoodsCertificate/cbc:Description` = `The ginned cotton is free of the pests named by Bayvarra's plant health rules.`
- Why: Under the International Plant Protection Convention, phytosanitary certificates are issued by
  the exporting country's national plant protection organisation, by its officers or authorised
  inspectors (own knowledge of the IPPC and ISPM 12). A chamber of commerce issues certificates of
  origin and, as in this flow, classing certificates; customs does not sanction plant health
  certificates. LegalAuthorityParty is "The legal Authority, when different from the issuer, who
  sanctions this Goods Certificate". In this certificate the plant-health authority of Lisavu is
  missing and both roles are filled by bodies that do not have that function.
- Condition: the issuer, or the legal authority sanctioning the certificate, is Lisavu's plant
  protection authority (or a body the story makes responsible for plant health).
- Options: (a, preferred) make the legal authority the island's plant health service (adding the
  party to the world if it does not exist), with the chamber as issuer only if the story delegates
  inspection to it; (b) change the certificate type to one a chamber issues.
- Needs decision: yes (who is responsible for plant health in Lisavu is part of the world)

### cotton/10#F5 · Low · Customs value and classing certificate in a plant health certificate, and a criterion type taken from the processing type list
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `6055.452`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cac:GoodsProcessing/cac:CriterionItem/cbc:TypeCode` = `PROCESSING`
- Why: A phytosanitary certificate attests freedom from pests; the declared customs value and the
  lint's commercial grade (the classing certificate) play no part in it. CriterionItem/TypeCode is
  "A code describing the type of criteria", but the value comes from the GoodsProcessingTypeCode
  list, a list of kinds of processing, and only says "Processing", which describes nothing the
  criterion "Seed removed; lint only" does not already say. These read as copied item data and a code
  from another element's list.
- Condition: the certificate carries the data its attestation uses, and every code is from a list
  meant for its element.
- Options: (a, preferred) leave the customs value, the classing certificate and the criterion type
  code out; (b) use a criterion type list if criteria of several types are needed.
- Needs decision: no

## Checked and consistent
- Shipment SCG-SH-26-0200 is the shipment of 09, 11, 12, 13 and 15; gross 6,190.29 kg and net
  6,129 kg agree with them.
- The ginning period 2026-02-07 to 2026-02-22 starts after the farm's delivery to the gin (03,
  2026-02-05) and ends before the inspection; the certificate is valid from issue to 2026-03-14 for
  Bayvarra, which covers the sailing in 13 and the import declaration 15 (2026-03-06).
- Exporter and applicant (ginnery), importer and consignee (mill), and the note "Inspected at the
  ginnery's warehouse" with the ginnery as warehouse party agree with each other.
- Attestation lines and sub-line (boll weevil, pink bollworm) agree with the attestation's
  description.

## Considered and refuted
- `/GoodsCertificate/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`: the buyer's order in
  a plant health certificate suspected as unused — refuted because plant health certificates are
  often tied to the commercial transaction for the importing authority, and the order resolves to 08.
- `/GoodsCertificate/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: a
  forwarder in a certificate — refuted because the forwarder handles the certificate for the
  shipment it books, which the flow shows.
