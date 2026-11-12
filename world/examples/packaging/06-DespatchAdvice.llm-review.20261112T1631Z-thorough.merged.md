# LLM review: 06-DespatchAdvice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/06-DespatchAdvice.xml`, Git blob `87ee027fe7a7634e3733f7816740466502baaf2c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1d81251 2026-11-12 Reviews of the packaging flow, run 20261112T1631Z-thorough: parts written so far
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

### packaging/06#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language already in `Language/ID` and names no locale. The same
  value occurs 362 times in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`,
  re-counted in the merge); no other LocaleCode value occurs anywhere.
- Condition: in all three parties, `LocaleCode` is absent or holds a locale (language and region)
  from a locale list named in `listID`.
- Options: (a) remove it (preferred by broad and context, and here: it needs no new code list);
  (b) a real locale such as `en-XB` from a locale list (preferred by parties).
- Needs decision: no
- From: broad F2, context F2, parties F1

### packaging/06#F2 · Medium · The despatch advice says neither when the goods leave nor when they arrive
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0528`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and
  services"; the receiver uses it to plan goods-in. This one says what is sent (600 shirts, 168 kg),
  by whom and to whom, but not when: the shipment has no `Delivery` (no `Despatch` with an actual
  despatch date or time, no estimated, requested or promised delivery period), no line carries a
  date, and there is no transport event. The order `05-Order.xml` has no requested date either, so
  nothing in the flow gives it. Only the issue date 2026-05-12 suggests it, which would be implying
  by absence (IND6). Logistics adds that 10 of the world's 11 despatch advices carry no despatch or
  delivery date (only `road/04-DespatchAdvice.xml` has `cbc:ActualDespatchDate`). Verified in the
  merge: the XML has no `cac:Delivery` and no date other than `IssueDate` and the registration dates.
- Condition: the despatch advice states when the goods were (or will be) despatched and when they
  are expected at Brightmarket, in the dedicated elements of `Shipment/Delivery`; anything stated as
  actual lies at or before the issue time 2026-05-12 11:35.
- Options: (a) preferred: `Shipment/cac:Delivery` with `cac:Despatch/cbc:ActualDespatchDate` (and
  time) and `cac:EstimatedDeliveryPeriod`, because both are what the receiver acts on; (b) at least
  the despatch date or the estimated delivery period.
- Needs decision: no
- From: broad F1, context F1, logistics F1

### packaging/06#F3 · Low · The note refers to a consignment note the document does not identify
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The note directs the store to record damage on "the consignment note", but the despatch
  advice references none (no `AdditionalDocumentReference`, no carrier's consignment reference in
  `Consignment`), and no consignment note, waybill or CMR exists in the flow; the consignment
  `LTM-CS-26-0528` is referred to by no other example (grep over `*.xml`). The free text relies on a
  document that cannot be linked. Low, because a road consignment note travelling with the goods is
  normal practice. The context part refuted this candidate for that reason; the merge keeps it,
  because the store needs the note's number to record damage against it and two parts found it.
- Condition: either the consignment note is identified in the document (a document reference or
  the carrier's consignment reference), or the note does not rely on it.
- Options: (a) preferred: an `AdditionalDocumentReference` to Bayforth Forwarding's consignment
  note; (b) reword the note (e.g. "report any damage to the driver" or on this despatch advice).
- Needs decision: no
- From: broad F4, logistics F2 (refuted by context, see "Considered and refuted")

### packaging/06#F4 · Low · Master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The delivery recipient's logo reference, online shop, photo-sharing profile and share
  capital, and the despatch party's customs trader ID, have no role in advising a delivery within
  Lumeport (both addresses in Coastal State, Bayvarra; no export, so no customs). They are the
  parties' master data copied into the document (section 4.8, IND5); the logo reference is in 41
  examples (grep over `*.xml`).
- Condition: every party detail in the despatch advice has a role in it, or the example states one.
- Options: (a) preferred: leave them out here; (b) state why they are needed.
- Needs decision: no
- From: broad F5, context F5, parties F5

### packaging/06#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 companies in the
  registers of all three countries share exactly this date (271 occurrences in 181 examples,
  `grep -rc --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, re-counted in the merge), which
  reads as a default (IND5). Brightmarket, by contrast, has its own date `1979-02-14`.
- Condition: each company's RegistrationDate is its own date in the story, or absent.
- Options: (a) preferred: individual dates from the company histories; (b) remove; (c) confirm as
  a story fact.
- Needs decision: yes (dates are part of the companies' histories)
- From: broad F7, parties F4

### packaging/06#F6 · Low · Despatch and delivery contacts are the parties' buying contacts
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party". In `DespatchSupplierParty` ("The
  despatch party") it is whom the recipient contacts about the despatched goods; the mill's
  purchasing mailbox, filed under Sales as a customer service officer, is neither despatch nor
  shipping. In `DeliveryCustomerParty` ("The delivery recipient") the contact receives the goods,
  which the note asks the recipient to check on arrival, and the order names goods-in as the
  delivery location (`05-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`);
  Brightmarket's buying office in Sales is not its goods receiving. In both, name and department
  also contradict each other. Brightmarket has a goods-in contact in another flow
  (`retail/08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`).
  Each is the party's single contact used in every role (parties: 52 and 41 such contacts, lxml count
  over `*.xml`; context: 89 examples with a `Purchasing` or `Buying office` contact in Sales).
- Condition: the despatch party's contact handles despatch or shipping, and the delivery
  recipient's contact receives goods; name, job title and department agree in each.
- Options: (a) preferred: a dispatch/warehouse contact for the mill and a goods-in contact for
  Brightmarket (the latter could reuse the one from the retail flow); (b) omit the contacts if the
  advice needs none.
- Needs decision: no
- From: broad F3 (part), context F4, parties F2

### packaging/06#F7 · Low · The carrier's contact is its export desk, for a delivery within Lumeport
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- Why: The carrier's contact should be the one who handles this transport. The goods go from the
  mill (`/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` = `Lumeport`)
  to the store (`/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` = `Lumeport`),
  DDP; Bayforth Forwarding's export desk, its contact in the sea, air and cotton flows, is not the
  desk for a local delivery. `Export desk` occurs in 25 examples
  (`grep -rl --include='*.xml' '<cbc:Name>Export desk</cbc:Name>'`, re-counted in the merge), so it
  looks like the party's standard contact copied into this role.
- Condition: the carrier's contact in this despatch advice is one that handles domestic deliveries,
  or the contact is left out.
- Options: (a) preferred: a domestic transport, delivery or operations desk of Bayforth; (b) drop
  the carrier's contact.
- Needs decision: no
- From: broad F3 (part), context F3, logistics F4, parties F3 (contact part; the rest of parties F3
  is under "Refuted in the merge")

### packaging/06#F8 · Low · Nothing says how many packages to check on arrival
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `168`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`
- Why: The store is asked to check the goods on arrival, which at goods-in means counting packages
  against the advice. The despatch advice gives the shirt count and the gross weight but no number
  of cartons or handling units (`Shipment/cbc:TotalTransportHandlingUnitQuantity`,
  `Consignment/cbc:TotalPackagesQuantity`, or `TransportHandlingUnit`/`Package`), so a missing
  carton cannot be noticed at the door. Completeness remark.
- Condition: the number of packages (and, if palletised, handling units) of the shipment is stated.
- Options: (a) preferred: `Consignment/cbc:TotalPackagesQuantity` (e.g. 20 cartons of 30 shirts,
  which fits the weight check below); (b) a `TransportHandlingUnit` with its packages, if the cartons
  travel on a pallet.
- Needs decision: no
- From: logistics F3

### packaging/06#F9 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: `StandardItemIdentification` is "Identifying information for this item, assigned according
  to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value
  is twelve digits with a valid GS1 mod-10 check digit (recomputed in the merge: 0), i.e. a
  well-formed GTIN-12 (UPC-A); read as GTIN-13 its prefix 077 lies in the range GS1 US allocates
  (060–139, own knowledge). A reader or scanner will take it for a real UPC, and whether it is
  assigned cannot be excluded; the agreed rule is that fictional values must not be mistaken for
  real ones. The scheme carries 8 distinct twelve-digit values, all with valid check digits, in 64
  examples (logistics, grep over `*.xml`).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1
  allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN (letters, another length, or a
  failing mod-10 digit), which removes the confusion at the source; (b) GTINs in GS1's
  demonstration prefix 952, like the world's GTINs; (c) keep them and record why they are not
  mistaken for real UPCs.
- Needs decision: yes (world-wide identifier convention)
- From: broad F6, logistics F5

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml`; buyer,
  seller, delivery customer (`20410411`) and despatch supplier (`20412603`) agree with the order
  (parties: blocks identical, compared line by line); the line refers to order line `1`, and 600 EA
  delivered equals the 600 ordered, so type code `DELIVERY` (not partial) fits. Issued 2026-05-12
  11:35, after the order (2026-05-07) and before the invoice `07-Invoice.xml` (14:49 the same day).
- Carrier under DDP: the seller engages the carrier, consistent with
  `05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`.
- Physics: 168 kg gross for 600 shirts is 0.28 kg per shirt. A men's woven cotton shirt about
  0.22 kg (own knowledge), a garment bag about 17 g (60 cm × 1 m × 2 layers × 15 µm × 920 kg/m³,
  dimensions partly assumed), 20 cartons of 30 shirts at about 1 kg: 132 + 10 + 20 ≈ 162 kg, within
  4 % of 168 kg (logistics; arithmetic redone in the merge). No transport equipment is stated.
- The shirts "in a garment bag" link to the bags the mill bought from Rivermouth Packaging
  (`03-Order.xml`, 20 000 bags; 600 used here).
- Shipment ID `LTM-SH-26-0527` and consignment ID `LTM-CS-26-0528` occur in no other example, so they
  are not mistaken for document numbers.
- `check_ids.py` (rerun in the merge): GLN `9522610900002` passes (prefix 952, GS1 demonstration
  range).
- Bayforth Forwarding: register ID, endpoint, Coastal State tax ID `CO-1234932`, legal entity and
  Lumeport address are internally consistent.

## Considered and refuted
- `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus` and `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
  as fillers — refuted because they state that advice and line are originals, neither revised nor
  cancelled, which the definition covers (from broad, context, logistics).
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `5229`:
  a forwarder as the party "who provides the transport of goods between named points" — refuted
  because a forwarder can contract as carrier, and Bayforth Forwarding carries goods itself in the
  world (`retail/16-Invoice.xml:/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`;
  `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`)
  (from broad, context, logistics; see also "Refuted in the merge").
- `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `The store's spring order of shirts.` in May — refuted
  because an order placed on 7 May for spring/summer stock fits (from broad, context).
- `/DespatchAdvice/cbc:Note`: the consignment note it mentions exists in no example — refuted by
  context because a carrier's consignment note travels with the goods and need not be a document of
  this flow (from context). The merge disagrees in part and keeps it as F3 (Low): the note need not
  be in the flow, but the advice should identify it if the store is to report against it.
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName` = `Dockside Way`:
  a dock in a street name — refuted because "Way" makes it a street name, not a dock or gate (from
  parties).

## Refuted in the merge
### parties/F3 · Low · The carrier is a forwarder whose contact is its export desk, for a delivery within Lumeport (forwarder part)
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `5229`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- Why (as in the part): Consignment/CarrierParty is "The Party who provides the transport of goods
  between named points". Bayforth Forwarding is classified as "Other transportation support
  activities" (ISIC 5229, forwarding, not haulage), and its contact is its export desk. The goods go
  from Mill Street 21 to Brightmarket's goods-in at Market Street 50, both in Lumeport, DDP; there is
  no export and nothing that needs a forwarder. A forwarder can act as contracting carrier, but then
  its contact would be its domestic or road desk. The same contact appears in 25 examples.
- Condition (as in the part): the carrier of this town delivery is a party that carries goods (or a
  forwarder acting as carrier, said so), with a contact that handles this kind of transport.
  Options: (a) a local haulier or the mill's own transport; (b) keep Bayforth with a domestic
  contact. Needs decision: yes.
- Refuted because: the contact part is kept as F7. The forwarder part does not hold: a forwarder
  that contracts the carriage in its own name is the carrier towards the shipper, which is what
  `CarrierParty` names, and the world has Bayforth Forwarding performing carriage itself in other
  flows (`retail/16-Invoice.xml`, `sea/14-BillOfLading.xml`, cited above). Nothing requires the
  document to say "acting as carrier"; its being in `CarrierParty` says it. Three other parts
  refuted the same candidate.

## Changed in the merge
- broad F3 split → F6 (despatch and delivery contacts) and F7 (carrier's export desk) because the
  carrier's contact has a reason of its own (export desk for a domestic delivery), found separately by
  context F3 and logistics F4.
- parties F3 → F7 (contact part, Low, Needs decision changed from yes to no) and "Refuted in the
  merge" (forwarder part) because only the contact part survives; changing a contact does not change
  the story.
- parties F5 and broad F5 / context F5 → F4: grouped, with the customs trader ID (parties) and the
  share capital (named in broad's text only) as XPath lines of their own.
- logistics F2 / broad F4 → F3: kept although context refuted the candidate; reason in F3.
- F1 (LocaleCode): both options kept; preference stated as removal (broad, context) against
  parties' `en-XB`; severity Medium as in all parts, consistent with skill §6 and with
  `packaging-merge-decisions-b.md`.
- Findings renumbered by severity and position.
