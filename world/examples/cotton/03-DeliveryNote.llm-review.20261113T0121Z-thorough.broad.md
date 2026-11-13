# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/03#F1 · Low · Gross weight of the shipment fits neither loose cotton nor loaded trailers
- XPath: `/DeliveryNote/cac:Shipment/cbc:GrossWeightMeasure` = `20400`
- XPath: `/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000`
- XPath: `/DeliveryNote/cbc:Note[2]` = `Three trailer loads, weighed at the gin.`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport equipment". The seed cotton is delivered loose (no packaging), so gross minus net (2 400 kg) would be the transport equipment. Three farm trailers that each carry 6 t of loose seed cotton (about 60 m³ at a loose bulk density of roughly 100 kg/m³, own knowledge) weigh some 2–4 t each empty, i.e. 6–12 t together, plus the tractors. 2 400 kg is neither zero (no equipment) nor the trailers' weight. If the difference is trash and moisture deducted at the gin, it is not gross weight in the UBL sense.
- Condition: the gross weight is either the goods plus equipment as defined, with a plausible equipment weight, or it is absent; a deduction for trash or moisture, if there is one, is stated as such.
- Options: (preferred) drop the shipment gross weight, because the delivered quantity is the weighed net; or state gross as goods plus the trailers' tare from the weighbridge; or, if 2 400 kg is a quality deduction, say so in the line and make 04 bill the right quantity.
- Needs decision: yes

### cotton/03#F2 · Low · The textile mill as originator and beneficiary of the farm's seed-cotton delivery
- XPath: `/DeliveryNote/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: the delivery note is the farm's record of seed cotton delivered to the ginnery under the ginnery's season agreement. The mill is not a party to that purchase: it orders lint from the ginnery later (08, issued 2026-02-24) and its forecast (02) covers lint from 16 February. The farm has no reason to know or name the ginnery's customer, and the seed cotton is not "ultimately intended" for the mill (it becomes lint and seed, of which only part is sold to the mill).
- Condition: the delivery note names only parties that take part in, or are known to the farm for, this delivery.
- Options: (preferred) drop both roles; or, if the story is that the mill finances or pre-buys the season's crop, state that link in the document and in the season agreement, and keep the roles.
- Needs decision: yes

### cotton/03#F3 · Low · The buyer's cost centre in the supplier's delivery note
- XPath: `/DeliveryNote/cbc:AccountingCostCode` = `200`
- XPath: `/DeliveryNote/cbc:AccountingCost` = `Seed cotton purchases`
- Why: the delivery note is issued and signed by the farm (`/DeliveryNote/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`). "Seed cotton purchases" is the ginnery's cost centre (it is the ginnery's in 01 and 04); a farm does not book its sale to a purchases cost centre, and nothing says the code was given by the buyer for routing.
- Condition: an accounting cost on the delivery note belongs to the party whose accounting it serves, and that is clear from the document.
- Options: (preferred) drop the cost centre from the delivery note; or keep it only if the season agreement asks the farm to quote the ginnery's cost centre, and say so.
- Needs decision: no

### cotton/03#F4 · Low · References with an identifier only
- XPath: `/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `/DeliveryNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: the additional reference is presumably the ginnery's weighbridge ticket (the note says the loads were weighed at the gin), but it carries no type code or description, so the receiver has to guess what it is. The project reference points to a chamber of commerce quality project; nothing in the delivery note uses it or says what the delivery has to do with it.
- Condition: every reference states what it refers to where that is not obvious, and every reference has a purpose in this delivery note.
- Options: (preferred) give the weighbridge ticket a document type (code or description) and drop the project reference unless the season agreement ties deliveries to the project; or explain the project link in the note.
- Needs decision: no

### cotton/03#F5 · Low · The ginnery's contact for receiving goods is its sales desk
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the delivery customer is "The Party to whom the goods or services were delivered"; its contact should be the gin yard or intake that received and weighed the trailers, not the lint sales desk.
- Condition: the delivery customer's contact is a receiving / intake function.
- Options: (preferred) a gin-yard or weighbridge contact; or no contact.
- Needs decision: no

### cotton/03#F6 · Low · Address lines repeat the structured address and mix languages
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the four address lines repeat `StreetName`, `Description`, `District` and `CityName`; lines 1 and 4 combine the Lisavan and English forms in one text without `languageID`, although `Line` may be repeated "only to provide the same content in multiple natural languages".
- Condition: the farm's postal address states each part once, and language-specific renderings carry `languageID`.
- Options: (preferred) drop the address lines; or keep only lines with information not in the structured parts.
- Needs decision: no

### cotton/03#F7 · Low · Expiry date on a commercial-register entry
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: the farm's entry in the island companies register is given an expiry date; `RegistrationExpirationDate` is meant for registrations that expire, "e.g., registration for an import/export license". A company-register entry normally does not.
- Condition: the expiry date belongs to a registration that expires and is the one described.
- Options: (preferred) drop it; or make the world's register rules say that sole proprietorships register yearly.
- Needs decision: yes

## Checked and consistent
- The self-billed invoice 04 bills the same 18000 kg and refers to this delivery note (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`) with the same delivery date (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`), the same order reference and the same item.
- Issue time 14:29 on the delivery date, after the loads were weighed: plausible.
- Lint yield: 18000 kg of seed cotton at a typical turnout of 33–38 % (own knowledge) gives about 5 900–6 800 kg of lint; the mill's order of 6129 kg (08) fits.
- Farm and ginnery are described the same way as in 01 and 04.

## Considered and refuted
- `/DeliveryNote/cac:OrderReference/cbc:ID`: refers to no example — refuted: a call-off number under the season agreement, not a document of the flow; 04 uses the same reference.
- `/DeliveryNote/cbc:DocumentStatusCode`: `NoStatus` as filler — refuted: states explicitly that the note is neither a replacement nor a cancellation (IND6).
- `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department`: the farm's office in "Sales" — refuted: the farm office is the farm's selling point; acceptable for a micro farm.
