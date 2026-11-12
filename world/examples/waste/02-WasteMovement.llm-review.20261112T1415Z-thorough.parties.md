# LLM review: 02-WasteMovement.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/02-WasteMovement.xml`, Git blob `32c42c37c829fb72899a0b9b0b8748b5caf542d9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

### waste/02#F1 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`, as the world does for Bayvarra's states (`CountrySubentity` = Coastal State / Upland State, 799 occurrences over `*.xml`). The same value occurs 219 times in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of Ferrano'`, summed).
- Condition: no address in this example carries a province in `Region`; a province, where given, is in `CountrySubentity`.
- Options: (preferred) move the province to `CountrySubentity` for all Urvanian addresses, as for Bayvarra; or drop it where the postal zone suffices.
- Needs decision: no

### waste/02#F2 · Medium · Movement document sent to the customs administration for a movement inside Urvania
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteMovement/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `01-WasteNotification.xml:/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: The waste movement document reports the transport of waste notified in `01-WasteNotification.xml` to the competent authority. Producer/notifier (Valdara) and recovery facility (Rinova, the sender) are both in Ferrano, Urvania, and neither document shows a border crossing, so there is no export or import for a customs administration to permit or control (`CustomsParty` in the notification: "The competent authority granting a permit to export or import the waste"). The receiver is therefore not the authority that consented to a domestic movement. Same problem as waste/01#F2; it is a finding here because this document addresses the movement report to that party.
- Condition: the receiver of the movement document is the authority that consented to the notified movement, and that authority fits the movement (an export/import authority only for a transboundary movement), in agreement with `01-WasteNotification.xml`.
- Options: (a) a competent Urvanian waste/environment authority as receiver, the same party as in the notification (preferred for a domestic story); (b) make the movement transboundary; (c) keep customs if the world's story makes it the competent authority for waste, and state that in the world.
- Needs decision: yes

### waste/02#F3 · Medium · Rinova is named as disposal facility for a recovery movement
- XPath: `/WasteMovement/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteMovement/cbc:WasteMovementTypeCode` = `RECOVERY`
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material". The movement is of type Recovery, and Rinova's permit covers recovery operation R3 only; no disposal operation is reported. Naming Rinova as disposal facility as well as recovery facility contradicts the type code and the permit (same as waste/01#F3, repeated in this document).
- Condition: `DisposalFacilityParty` is present only for a disposal operation that is part of this movement; otherwise only `RecoveryFacilityParty` identifies Rinova.
- Options: (preferred) remove `DisposalFacilityParty`; or name a separate disposal party with its own authorization if residues are disposed of.
- Needs decision: no

### waste/02#F4 · Low · Recovery facility and carrier both registered on 1 January 1996
- XPath: `/WasteMovement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The same New Year's Day date is given to 25 different legal entities across the world (script over `world/examples/*/*.xml` collecting `PartyLegalEntity/RegistrationDate` per `RegistrationName`; 181 files), while others have individual dates (Valdara `1962-04-12`). It looks like a default rather than a real registration date (rule "no fillers").
- Condition: each `RegistrationDate` is the party's own registration date in the world, or is absent.
- Options: (preferred) individual plausible dates; or remove the element. If the world has all registers re-founded on 1996-01-01, record that and dismiss.
- Needs decision: yes

### waste/02#F5 · Low · Party data that the movement document does not use
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteMovement/cac:NotifierParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteMovement/cac:NotifierParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A waste movement document reports a transport of notified waste. The authority's VAT number, the notifier's share capital and stock-exchange listing, and the notifier's warehousing-and-despatch provider (Castrano Logistics, who is neither carrier nor any other party of the movement; the carrier is Trasvia Haulage) have no function here. The same Valdara blocks occur in 75 examples (`grep -rl --include='*.xml' -F 'VI-SP-2026-01'`), i.e. master data copied into every document (section 4.8).
- Condition: every party detail present has a use in the movement document.
- Options: (preferred) leave these elements out; or, if Castrano acts in the movement, give it a role the document uses, consistent with the carrier.
- Needs decision: no

### waste/02#F6 · Low · Customs administration described as a company in the commercial register
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/WasteMovement/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The receiver is a public administration (ISIC 8411). A government authority is not entered in the commercial register and has no liquidation status. All four public bodies of the world are described this way, in 23 examples (`grep -rlE --include='*.xml'` on their `RegistrationName`).
- Condition: the authority's legal entity, if present, has no commercial-register scheme and no liquidation status, or a scheme that fits public bodies.
- Options: (preferred) keep only the registration name; or drop `PartyLegalEntity` for the authority.
- Needs decision: no

### waste/02#F7 · Low · Contacts that do not fit the authority and the notifier
- XPath: `/WasteMovement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteMovement/cac:NotifierParty/cac:Contact/cbc:Department` = `Sales`
- Why: The movement report is handled by the authority's office for waste-movement consents, not a border office (there is no border crossing, F2). The notifier's contact is Valdara's sales order desk, the same contact Valdara carries in all its 75 examples whatever its role; questions about the notified waste go to whoever answers for it (environment/HSE, plant), not to sales.
- Condition: the authority's contact handles waste movements; the notifier's contact answers for the notified waste.
- Options: (preferred) role-specific contacts; or omit the contacts.
- Needs decision: no

### waste/02#F8 · Low · Carrier's authorization is a general international haulage licence, not a waste-carrier authorization
- XPath: `/WasteMovement/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: For a waste movement the relevant authorization of the carrier is its permission to carry waste (Basel movement document, own knowledge). The general international haulage licence is the one copied into all 15 Trasvia examples (`grep -rl --include='*.xml' -F 'International road haulage'`), and the movement is domestic (F2).
- Condition: the carrier's authorization here permits it to carry this waste, or is absent.
- Options: (preferred) a waste-carrier registration for Trasvia in the world, shown here; or omit it.
- Needs decision: yes

## Checked and consistent
- Every party shared with `01-WasteNotification.xml` and `03-Invoice.xml` (Valdara XU-R-104274, Rinova XU-R-104548, Customs XU-R-105507, Trasvia XU-R-104822) is described identically: address and address ID, tax scheme, legal entity, contact, language, electronic address, authorizations (c14n comparison).
- Notifier, waste producer and distribution recipient (`/WasteMovement/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`) are the same party, which fits the distribution note that the producer keeps a copy with the notification.
- Sender and signatory are Rinova, the recovery facility that received the waste; plausible for the issuer of the movement report on receipt.
- Rinova's permit `XU-ENV-2024-0311` is valid until 2029-12-31, after the issue date 2026-04-02; R3 fits plastic recovery.
- Bilingual renderings (`qau`, `en-XU`) carry the same content.

## Considered and refuted
- `/WasteMovement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`: suspected a contact unfit for the facility reporting the movement — refuted because Rinova's customer service is the desk that deals with its customers' waste deliveries; acceptable for the facility.
- `/WasteMovement/cac:NotifierParty/cbc:IndustryClassificationCode` = `3100`: suspected mismatch with polyethylene production waste — refuted, a furniture maker produces such waste.
- `/WasteMovement/cac:DisposalFacilityParty/cac:PartyIdentification/cbc:ID` = `XU-R-104548`: checked whether the facility roles point to different parties than in the notification — they are the same as in `01-WasteNotification.xml` (the role problem itself is F3).
- `/WasteMovement/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`: suspected a customs-trader ID with no use — kept out of F5 because, as long as the document goes to the customs administration (F2), the trader ID is the identifier that authority knows; it falls with F2.
