# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### cotton/03#F1 · Low · DocumentStatusCode "NoStatus" states nothing
- XPath: `/DeliveryNote/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Delivery Note with respect to its original state, e.g., original, revised, or cancelled". "No status on document" gives no status; the element is present without carrying information (IND5). Broad refuted it: it states explicitly that the note is neither a replacement nor a cancellation (IND6). The merge follows context and the earlier flows' merges (wood, plastics, rail, air, road, packaging: Low/no, drop): a first delivery note has nothing to be distinguished from, and the code's name says it carries no status.
- Condition: the delivery note carries no `DocumentStatusCode`, or one that states a status the story has.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: context (F5); broad (considered and refuted, argument carried)

### cotton/03#F2 · Low · The buyer's cost centre "Seed cotton purchases" in the farm's delivery note
- XPath: `/DeliveryNote/cbc:AccountingCostCode` = `200`
- XPath: `/DeliveryNote/cbc:AccountingCost` = `Seed cotton purchases`
- XPath: `/DeliveryNote/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- Why: `AccountingCost` is "The accounting cost centre, applied to the Delivery Note as a whole". The note is issued (ID prefix LCF) and signed by the farm; "Seed cotton purchases" with code 200 is the ginnery's cost centre (the same values head its self-billed invoices 01 and 04). The farm purchases no seed cotton, and nothing says the code is the buyer's, quoted for routing.
- Condition: the cost centre in the delivery note fits the issuer, or the document makes clear it is the buyer's routing code.
- Options: (a, preferred) leave the cost centre out; (b) keep it if the season agreement asks the farm to quote the gin's cost centre, and say so.
- Needs decision: no
- From: broad (F3), context (F4)

### cotton/03#F3 · Low · Project reference to a chamber of commerce quality project
- XPath: `/DeliveryNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: `ProjectReference` is "A reference to a project with which this Delivery Note is associated". The prefix SCC is the Selanu Chamber of Commerce's (its certificates and signatures carry it), which is not a party to this delivery. A farm's delivery of seed cotton under a season call-off is not a project, and nothing in the note says what the project is or does with this delivery. The same reference is in 04 and 05.
- Condition: the delivery note carries a project reference only if the story has a project this delivery belongs to, and then says what it is.
- Options: (a, preferred) leave it out; (b) give the project a role in the story (e.g. a quality programme the delivery is sampled for) and describe it.
- Needs decision: yes (whether such a project exists in the world)
- From: broad (F4, project part), context (F2)

### cotton/03#F4 · Low · Weighbridge ticket referenced by ID only
- XPath: `/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `AdditionalDocumentReference` with only an ID does not say what the document is. The note ("weighed at the gin") and the prefix suggest the gin's weighbridge ticket, but no `DocumentTypeCode` or `DocumentDescription` says so; no example of the flow has this ID, and 04 and 05 cite it as a `ReceiptDocumentReference` (a Receipt Advice), so readers of the flow get two kinds for one document.
- Condition: the reference states what kind of document `SCG-WB-26-0311` is, consistently with how 04 and 05 cite it.
- Options: (a, preferred) add a document type ("Weighbridge ticket") to the reference; (b) drop it if the note is enough.
- Needs decision: no
- From: broad (F4, weighbridge part), logistics (F2), context (F3)

### cotton/03#F5 · Low · Address lines repeat the structured address and mix languages
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the four lines repeat `StreetName`, `Description`, `District` and `CityName`; lines 1 and 4 combine the Lisavan and English forms in one text without `languageID`, although `Line` "may be repeated only to provide the same content in multiple natural languages". Same as 01#F6 (where parties' counter-argument, a Lisavan print format, is recorded).
- Condition: the farm's postal address states each part once, and language-specific renderings carry `languageID`.
- Options: (a, preferred) drop the address lines; (b) keep only lines with information not in the structured parts.
- Needs decision: no
- From: broad (F6)

### cotton/03#F6 · Low · Expiry date on a commercial-register entry
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)". The farm's entry in the island companies register normally does not expire. In 01 parties read it as a seasonal farm registration (`XL-FARM-REG-0412` in 04); that is possible but would not be the company registration described here. Cannot settle without the world's register rules (same as 01#F7).
- Condition: the expiry date belongs to a registration that expires and is the one described.
- Options: (a, preferred) drop it; (b) make the world's register rules say that sole proprietorships register yearly.
- Needs decision: yes
- From: broad (F7)

### cotton/03#F7 · Low · Contacts do not fit the role or the party
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the delivery customer is "The Party to whom the goods or services were delivered"; its contact should be the gin yard or weighbridge that received and weighed the three trailer loads, not the lint sales desk. The farm is a one-person micro sole proprietorship; a "Customer service officer" in "Sales" describes a sales organisation it does not have. Broad refuted the farm's part (the farm office is the farm's selling point, acceptable for a micro farm); parties found it. The department may be read loosely, the job title hardly; kept, Low.
- Condition: the delivery customer's contact is a receiving/intake function (or absent), and the farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) a gin-yard or weighbridge contact for the ginnery; no job title/department (or "Owner") for the farm; (b) drop the contacts.
- Needs decision: no
- From: broad (F5), parties (F2, F3); broad (considered and refuted for the farm, argument carried)

### cotton/03#F8 · Low · The ginnery's customs-trader number in a domestic delivery note
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: section 4.8. A domestic delivery of seed cotton from a Lisavan farm to a Lisavan gin involves no customs; the note does nothing with the number, which reads as copied from master data (IND5).
- Condition: every identifier of the parties is one the document has a use for.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: parties (F5)

### cotton/03#F9 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Shared by the ginnery, the mill, Bayforth Forwarding and both ports; 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`). Reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the date on which that party was registered in the world's story, or absent.
- Options: (a, preferred) a date from the company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F4)

### cotton/03#F10 · Low · The textile mill as originator and beneficiary of the farm's seed-cotton delivery
- XPath: `/DeliveryNote/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- Why: `OriginatorCustomerParty` is "A customer party as originator"; `BeneficiaryParty` is "A Party for whom the associated transaction is ultimately intended or who derives benefit from it." The transaction is the ginnery's purchase of seed cotton from the farm, called off under the ginnery's season agreement (`SCG-SEASON-2026/03`, assigned by the buyer). The mill orders lint from the ginnery later and separately (08, issued 2026-02-24); the ginnery gins the seed cotton and sells lint on its own account, keeping seed and waste. Nothing in this note ties the seed cotton to a mill order, and the farm has no evident reason to know the ginnery's customer; 01 names no originator or beneficiary. On the other side, 04 and 05 cite the mill's `LTM-SEASON-2026` as `OriginatorDocumentReference`, which suggests the story intends the mill's season agreement to drive the ginnery's purchases. Context rated it Medium (the mill did not originate the order); because the reading in which the mill pre-buys the crop is possible and is story, the merge keeps Low with a decision, as broad and parties did.
- Condition: the mill appears as originator or beneficiary of the farm-to-ginnery documents only if the story makes it the party that requested, or for whom, the seed cotton is bought, and then consistently in every document of that purchase (01, 03, 04, 05).
- Options: (a, preferred) drop both roles from the farm-to-ginnery documents; (b) if the mill finances or pre-buys the farm's crop, say so in the story and the season agreement, reference the mill's agreement here, and name it the same way in 01, 03, 04 and 05.
- Needs decision: yes
- From: broad (F2), parties (F1), context (F1)

### cotton/03#F11 · Low · Shipment gross weight fits neither "goods plus equipment" nor a loose delivery
- XPath: `/DeliveryNote/cac:Shipment/cbc:GrossWeightMeasure` = `20400`
- XPath: `/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000`
- XPath: `/DeliveryNote/cbc:Note[2]` = `Three trailer loads, weighed at the gin.`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment." The seed cotton is "delivered loose by trailer", so no packaging. Recalculated: 20 400 − 18 000 = 2 400 kg for three loads, 800 kg per trailer. A trailer carrying 6 000 kg (18 000 / 3) of loose seed cotton needs, at a loose bulk density of roughly 80–150 kg/m³ (own knowledge), 40–75 m³ of body and weighs several tonnes empty, not 800 kg. If the trailers are counted, the gross weight is far too low; if not, gross equals the goods (18 000 kg) and the 2 400 kg are unexplained. They may be the weighed seed cotton before a trash or moisture deduction, but then the difference is a deduction, not packaging or equipment, and nothing says so. Context refuted it (gross includes the trailers, as the definition says); the calculation shows 800 kg per trailer is not their tare, so the refutation does not hold.
- Condition: the gross weight is goods plus packaging plus transport equipment and is plausible for three trailer loads, or it is absent, or the difference to the delivered quantity is stated as what it is (e.g. a weighbridge deduction).
- Options: (a, preferred) drop the shipment gross weight (the delivered quantity is the weighed net); (b) gross = goods + the three trailers' tare from the weighbridge; (c) if 18 000 kg is net after a deduction, state the weighed and deducted weights (and bill the right quantity in 04).
- Needs decision: yes (what the 2 400 kg are is part of the story of the delivery)
- From: broad (F1), logistics (F1); context (considered and refuted, not followed)

## Checked and consistent
- 04 bills the same 18 000 kg and refers to this note (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`) with the same delivery date (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`), order reference and item; `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `18000`.
- Issue time 14:29 on the delivery date, after three loads were weighed: plausible.
- Lint turnout (recomputed): 6 129 kg of lint ordered in 08 / 18 000 kg seed cotton = 34.05 %, within the usual 33–40 % (own knowledge).
- Farm and ginnery are identified and described as in 01, 04, 05 and 06; the signatory is the farm, which issues the note. The farm's `PhysicalLocation` (the fields) has a reason here: it is where the loads come from (parties, context).
- Item `LCF-SC`, HS 520100 and CPC 01921 agree with 01, 04 and 05.
- Money: no amounts in the document (the money part found nothing).

## Considered and refuted
- `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`: refers to no example / contract-based ID as order reference — refuted: a call-off under the season agreement, assigned by the buyer (prefix SCG) as the definition requires; 04 uses the same reference. (from broad, logistics, context)
- `/DeliveryNote/cbc:DocumentStatusCode` = `NoStatus`: broad refuted (IND6); the merge followed context: F1. (from broad)
- `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: broad refuted for a micro farm; folded into F7 with parties' finding. (from broad)
- `/DeliveryNote/cac:DespatchSupplierParty`: a farm rarely "executed the delivery" itself — refuted: the loads came by trailer, no carrier is named, a farm hauling its own crop is normal, and 04 pays a haulage allowance. (from parties)
- `/DeliveryNote/cac:Shipment/cbc:GrossWeightMeasure` = `20400`: context refuted (gross includes the trailers); not followed by the merge, see F11. (from context)

## Changed in the merge
- context/F5 → F1: kept Low/no; broad's refutation recorded as not followed (aligned with earlier flows).
- broad/F3 + context/F4 → F2: combined.
- broad/F4 split: project part + context/F2 → F3 (Low/yes, as context); weighbridge part + logistics/F2 + context/F3 → F4 (Low/no).
- broad/F5 + parties/F2 + parties/F3 → F7: grouped (contacts of both parties); broad's refutation for the farm carried.
- broad/F2 + parties/F1 (Low) + context/F1 (Medium) → F10: Low/yes; 04/05's `OriginatorDocumentReference` added as evidence for the other reading.
- broad/F1 + logistics/F1 → F11: combined, arithmetic redone; context's refutation answered.
