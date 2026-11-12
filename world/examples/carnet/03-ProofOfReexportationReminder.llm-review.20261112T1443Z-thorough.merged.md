# LLM review: 03-ProofOfReexportationReminder.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/03-ProofOfReexportationReminder.xml`, Git blob `a4b75fb8a0fa66ce587c269390e36886f30cf151` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8533627 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### carnet/03#F1 · High · Duties and tax of 1,300 coral are more than three times the value of the goods
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Note` = `Duties and import consumption tax of 1,300 coral fall due if no proof arrives within 30 days.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99800`
- XPath: `road/15-Invoice.xml:/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `packaging/09-PurchaseReceipt.xml:/PurchaseReceipt/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- Why: PaymentTerms/Amount is "The monetary amount covered by these payment terms", here the import
  duties and import consumption tax the island would claim on the carnet goods. Both are a percentage
  of the customs value, which the carnet declares as 99,800 ferra for the two benches. At the rates the
  examples use (1 XUF = 0.01 XBL in road/15 from XUF to XBL; 1 XBL = 0.4 XLC in packaging/09 from XBL
  to XLC; recomputed in the merge), the goods are worth 99,800 × 0.01 × 0.4 = 399.20 coral, and 1,300
  coral is 326 % of that. No combination of a duty and a consumption tax gets near it: the highest
  tax rate in the examples is 20 % (money part; the merge's `grep -rhoE --include='*.xml'
  '<cbc:Percent>[0-9.]+'` over world/examples finds 20 % at most apart from a single 70 %, which no
  duty plus tax of 326 % approaches), and duty on seats is a few percent (own knowledge).
  Nothing in the document (rate, penalty) explains the amount; it looks computed in another currency
  or on another base.
- Condition: the amount in PaymentTerms/Amount and in the note can be derived from the carnet's
  customs value converted to coral at the island's duty and tax rates, or the note says what else it
  includes (e.g. a penalty).
- Options: (a, preferred) recompute the claim from 399.20 XLC with Lisavu's duty and consumption tax
  rates and use the same figure in Amount and Note; (b) if a penalty is meant, say so in the note and
  keep it plausible.
- Needs decision: yes (the island's duty and tax treatment of the benches)
- From: money (F1), broad (F1)

### carnet/03#F2 · Medium · Duties claimed before the carnet's re-exportation time limit has expired
- XPath: `/ProofOfReexportationReminder/cbc:IssueDate` = `2026-08-23`
- XPath: `/ProofOfReexportationReminder/cbc:Note[2]` = `Without proof, the import duties will be claimed from the guarantee.`
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-09-22`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:ValidityPeriod/cbc:EndDate` = `2027-05-25`
- Why: The reminder threatens to claim the duties from the guarantee and sets them due on
  2026-09-22. Under temporary admission with an ATA carnet (own knowledge) duties become payable
  only when the goods have not been re-exported by the date set for re-exportation; the carnet the
  reminder refers to (`GoodsItemPassportID` FCC-DOC-26-0724) sets 2026-11-21 (its note: "to come back
  within six months"). On 2026-09-22 the goods could still lawfully be on the island. In addition,
  the claim procedure of the ATA and Istanbul Conventions gives the guaranteeing association six
  months from the claim to furnish proof, not 30 days (own knowledge, article not checked by the
  money part or the merge). Same root as carnet/02#F1.
- Condition: PaymentDueDate is not earlier than the carnet's re-exportation deadline plus the period
  the guarantor has to furnish proof, or the document states why the duties fall due earlier.
- Options: (a, preferred) shorten the carnet's final re-exportation date (on the importation
  counterfoil) so that it has passed before 2026-07-24 (see carnet/02#F1), and give the guarantor the
  conventional period; (b) move the reminder and its due date after 2026-11-21; (c) explain in the
  note why the island claims earlier.
- Needs decision: yes (timeline of the flow's story)
- From: logistics (F1), money (F2)

### carnet/03#F3 · Medium · A province in Region
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "the recognized geographic or economic region or group of countries in which this
  address is located"; a province is a subdivision of the country (CountrySubentity), where the world
  puts the Bayvarran states. "Province of …" is in Region in 104 examples
  (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: the province is not in Region; if given, it is in CountrySubentity.
- Options: (a, preferred) move it to CountrySubentity; (b) drop it.
- Needs decision: no
- From: broad (F3), parties (F1)

### carnet/03#F4 · Medium · The Island Customs Service described as a company in the companies register
- XPath: `/ProofOfReexportationReminder/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationReminder/cac:ImportingCustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ProofOfReexportationReminder/cac:ImportingCustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: A customs authority (ISIC 8411) is not in "a register of businesses" and has no liquidation
  status. The same description occurs for the Island Customs Service in 6 examples, Urvania's customs
  in 10, Bayvarra's in 7 (lxml count over `world/examples/*/*.xml`).
- Condition: no business-register scheme and no liquidation status on the customs party.
- Options: (a, preferred) drop both for public bodies; (b) a world register type for public bodies.
- Needs decision: yes (how the world registers public bodies)
- From: broad (F2), parties (F2)

### carnet/03#F5 · Low · The same addresses tagged with a different English variant than in 01 and 04
- XPath: `/ProofOfReexportationReminder/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:IssuerParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:ImportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: All English renderings here are tagged `en-XL`, including the Ferrano chamber's Urvanian
  address, while 01 and 04 tag the same renderings `en-XU`, including the Selanu chamber's. The tag
  follows the issuer of the document, so the same party's address is described differently from
  example to example.
- Condition: each party's address renderings carry the same languageID in every example of the flow.
- Options: (a, preferred) tag by the address's own country (or plain `en`); (b) keep the issuer-based
  variant and record it as a convention.
- Needs decision: no
- From: parties (F4), broad (part of F5)

### carnet/03#F6 · Low · Chambers of commerce in a commercial register
- XPath: `/ProofOfReexportationReminder/cac:ImportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Chambers (ISIC 9411) are associations or public-law bodies; the world's list has a "Register
  of associations". Against it (parties part of 01): chambers can be private associations or
  companies, and the world gives both a register number. The merge could not settle it.
- Condition: each chamber is described as what it is in the world.
- Options: (a, preferred) the association register; (b) as for public bodies (F4).
- Needs decision: yes
- From: broad (F6)

### carnet/03#F7 · Low · Italian street name tagged as Lisavan English
- XPath: `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: The rendering carries `languageID="en-XL"` but is Italian. 104 examples carry Italian-style
  street names under an `en-X*` tag (grep as in carnet/01#F9); it may be a convention of the world.
- Condition: the rendering is in the language its languageID names, or the world records the
  convention.
- Options: (a) an English rendering ("Market Square"); (b) record the Italian-style names as the
  world's English exonyms; (c) tag the text with the language it is in.
- Needs decision: yes (the world's language convention)
- From: parties (F3), broad (part of F5)

### carnet/03#F8 · Low · The issuer's endorsement carries the request's ID and the request's status
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:DocumentID` = `SCC-DOC-26-0726`
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Open`
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode` = `GUARANTOR`
- Why: ApprovalStatus is "The status of this endorsement"; "Open" is the status of the pending
  request (the proof has not arrived), not of an endorsement, which is given or not. DocumentID is
  "An identifier for this endorsement" but carries the request's ID (02); the logistics part refuted
  this point because the parent is defined as "An Issuers endorsment of this Request for Proof of
  Reexportation", so the request's ID is a legitimate reading; the merge keeps it as a secondary point
  since the element identifies the endorsement, not the endorsed document. The endorser is the Selanu
  chamber, which also issues and signs the reminder, so the endorsement adds no third party's
  approval; the request is already referenced in
  `/ProofOfReexportationReminder/cac:ProofOfReexportationRequestDocumentReference/cbc:ID` = `SCC-DOC-26-0726`.
- Condition: an IssuerEndorsement, if present, states the status of the endorsement itself and
  states an endorsement the reminder needs; the open state of the request is not put in it.
- Options: (a, preferred) drop the IssuerEndorsement, the signature already authenticates the
  reminder; (b) give it an endorsement status (e.g. "Endorsed") and leave the request's state to the
  note.
- Needs decision: no
- From: broad (F4), context (F1)

### carnet/03#F9 · Low · Signatory contact defined for a certificate-of-origin application
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: UBL 2.5 defines EndorserParty/SignatoryContact as "The individual representing the exporter
  who signs the Certificate of Origin application before submitting it to the issuer party". Here it
  is the guaranteeing chamber's desk signing a reminder. The value is what the element name suggests;
  the definition is copied from the certificate-of-origin context, a model defect as in carnet/01#F8.
- Condition: the use is recorded as a finding on the UBL 2.5 definition, or the element is not used
  (which also follows from F8 option a).
- Options: (a, preferred) keep it and record the definition for the OASIS UBL TC write-up; (b) drop it.
- Needs decision: yes
- From: context (F2)

### carnet/03#F10 · Low · The Selanu chamber signs as "Carnet desk", its contact is "Carnet office"
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- XPath: `/ProofOfReexportationReminder/cac:ImportingGuarantorParty/cac:Contact/cbc:Name` = `Carnet office`
- Why: The endorsing office and the party's contact appear to be the same office under two names;
  the signing "desk" has no means of contact. "Carnet desk" is also the name under which the Ferrano
  chamber signs in 01, so the two chambers' offices are not told apart by name.
- Condition: the endorsement's signatory contact and the chamber's contact use one name for the same
  office, or the signatory is reachable.
- Options: (a, preferred) "Carnet office" in the endorsement (or drop the endorsement, F8).
- Needs decision: no
- From: parties (F5)

### carnet/03#F11 · Low · Customs reference with only an ID
- XPath: `/ProofOfReexportationReminder/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: As in 02 (carnet/02#F8), the reference has no DocumentType or issuer and no example has this
  ID as document ID, so it is not clear what it is (presumably the island customs' claim).
- Condition: the reference says what kind of document it is and who issued it, or is removed.
- Options: (a, preferred) add DocumentType and the issuing party; (b) drop it, since the reminder
  refers to the request, which carries it.
- Needs decision: no
- From: broad (F7), context (F3), logistics (F2)

## Checked and consistent
- `/ProofOfReexportationReminder/cac:ProofOfReexportationRequestDocumentReference/cbc:ID` =
  `SCC-DOC-26-0726` resolves to `02-ProofOfReexportationRequest.xml`; same parties, same carnet
  FCC-DOC-26-0724, same counterfoil (`/ProofOfReexportationReminder/cac:GoodsItemPassportCounterfoil/cbc:ID` = `IMP-1`).
  The counterfoil needs no own GoodsItemPassportID; the document-level one covers it (logistics).
- Dates: reminder 30 days after the request (2026-07-24 → 2026-08-23); due date 2026-09-22 =
  2026-08-23 + 30 days, as the note says (recomputed in the merge).
- The note's 1,300 coral equals the Amount; XLC is the importing country's currency, the right one
  for the island's duties; three decimals as in most XLC amounts in the examples (money).
- PaymentTerms is used as its definition says ("used for generating a subsequent invoice in case no
  proof of re-exportation can be provided"); the proof (04, 2026-08-28) arrives before the due date,
  so the flow rightly has no follow-up invoice (money, context).
- ProcedureCode `2000` "Temporary admission, no previous procedure" fits the carnet's procedure.
- Parties: roles fit their definitions here (ImportingGuarantorParty issues "on behalf of their
  Customs Authority"); identifiers, names, tax IDs, address IDs, contacts and endpoints agree with 01
  (language tags aside, F5).
- Merge: definitions re-read with `annotate.py`; exchange-rate direction checked in
  road/15 and packaging/09.

## Considered and refuted
- `/ProofOfReexportationReminder/cbc:ProcedureCode`: unrelated to a reminder — refuted, the reminder
  is sent under the temporary-admission procedure (from broad, logistics).
- `/ProofOfReexportationReminder/cac:PaymentTerms`: out of place in a reminder — refuted, UBL defines
  it for exactly this use (from broad).
- `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount`: payment data in a non-commercial
  document — refuted for the same reason; the amount itself is F1 (from context).
- `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode`: wrong role —
  refuted, `GUARANTOR` "Guaranteeing association" is the Selanu chamber's role (from context).
- `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:DocumentID`: the request's ID rather than
  the reminder's — refuted because the parent is defined as an endorsement "of this Request for Proof
  of Reexportation" (from logistics). The merge kept the point as a secondary part of F8 (see there).
- `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:PartyTaxScheme/cbc:CompanyID`:
  master data copied — refuted, the exporting guarantor is liable for the duties claimed from the
  guarantee (from parties).
- `/ProofOfReexportationReminder/cac:ExportingGuarantorParty/cac:Contact/cbc:Name`: "Certificates
  office" rather than a carnet office — refuted as a finding here, the chamber's single contact in
  every example; the naming question is carnet/01#F12 (from parties).

## Changed in the merge
- money/F1 (High), broad/F1 (Medium, needs decision yes) → F1 at High: the amount cannot be derived
  from the customs value of the referenced carnet (arithmetic against a referenced document,
  section 6); Needs decision yes kept from broad, since fixing it requires the island's duty and tax
  treatment of the goods.
- logistics/F1, money/F2 → F2: combined; money's point on the six-month proof period added with its
  qualification (own knowledge, article not checked).
- broad/F4, context/F1 → F8: combined; logistics' refutation of the DocumentID point added as
  counter-argument; options reordered (dropping the endorsement first, as broad preferred).
- broad/F5 (Needs decision yes) split: the issuer-based region subtag → F5 with parties/F4 (Needs
  decision no); Italian under `en` → F7 with parties/F3 (Needs decision yes).
- broad/F6 → F6 kept; counter-argument from the parties part of 01 added.
- broad's "Outside this review" note (the timing of the claim, raised in 02) → F2, since logistics and
  money made it a finding of this example.
- broad/F2, parties/F2 → F4 (counts redone); broad/F3, parties/F1 → F3; broad/F7, context/F3,
  logistics/F2 → F11: combined without change of severity.

