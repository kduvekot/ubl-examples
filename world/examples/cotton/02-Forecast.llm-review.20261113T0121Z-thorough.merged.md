# LLM review: 02-Forecast.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/02-Forecast.xml`, Git blob `564d177fc853a93d7bb7f285f6471573cea2ed35` (committed)
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

### cotton/02#F1 · High · A forecast of future lint carries a classing certificate signed 18 days after the forecast
- XPath: `/Forecast/cbc:IssueDate` = `2026-02-02`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:StartDate` = `2026-02-07`
- Why: `Signature/ValidationDate` is "The date upon which this signature was verified"; a document issued on 2026-02-02 cannot report a verification on 2026-02-20. `Item/Certificate` is "A certificate associated with this item": a classing certificate records the measured grade, staple and micronaire of one classed lot. The forecast is for 24 000 kg of lint to be supplied from 2026-02-16 to 2026-06-02; when it was issued the seed cotton of the flow had not been delivered to the gin (03, 2026-02-05) nor ginned (10, from 2026-02-07), so no lot could have been classed. The same certificate with the same validation date is in 07 and 08 and is referenced from 05 and 10 (context).
- Condition: no element of the forecast states a fact (certificate, signature verification) dated after its issue date, and any quality requirement in the forecast describes what is wanted, not the result of classing a particular lot.
- Options: (a, preferred) drop the `Certificate` from the forecast item and keep the agreed grade and staple as `AdditionalItemProperty` (already there); (b) if a reference lot of an earlier crop is meant, give it a certificate ID and validation date before 2026-02-02 and say it describes a reference lot.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### cotton/02#F2 · Medium · The mill's forecast refers to the ginnery's season agreement with the farm
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `SCG-SEASON-2026`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID` = `SCG-SEASON-2026`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- Why: the forecast goes from Lumeport Textile Mill (buyer) to Selanu Cotton Ginnery (seller). Everywhere else in the flow (verified over `cotton/*.xml`: 01, 03, 04, 05) `SCG-SEASON-2026` is the contract of the self-billed invoices between the ginnery and the farm, and the farm's call-off `SCG-SEASON-2026/03`; the mill's own season document is `LTM-SEASON-2026` (04 and 05 cite it as the originator's document). A forecast between mill and ginnery has no evident reason to refer to the ginnery's purchase agreement with its farmer, a contract the mill is not a party to, and the reference has no type or description that would explain it. Broad considered it and left it out (the mill may know the reference; an ID-only reference to an external agreement is readable); that is possible, but nothing in the flow links the mill to that agreement, so the reference cannot be linked to the relationship the forecast is about.
- Condition: every document reference in the forecast points to a document that concerns the mill–ginnery relationship, and says what it is where the ID alone does not.
- Options: (a, preferred) refer to the mill–ginnery agreement (`LTM-SEASON-2026`, or whatever the story names it) with a `DocumentTypeCode` or `DocumentDescription`; (b) leave the reference out.
- Needs decision: yes (which agreement governs the mill–ginnery relationship is part of the story)
- From: context (F2); broad (considered and refuted, argument carried)

### cotton/02#F3 · Medium · Language code in `LocaleCode`
- XPath: `/Forecast/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with `listID` `ISO 639` is a language code that repeats `Language/ID`; it names no locale (a language in a region). Recounted: 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, and `grep -rl` for files).
- Condition: every `Language/LocaleCode` holds a locale from a list that defines locales, named in its `listID`, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `ID` already says English and nothing in the document uses a locale; (b) a locale such as `en-XB` from a list that defines locales (BCP 47). Same as every earlier flow's merge.
- Needs decision: no
- From: broad (F2), parties (F1)

### cotton/02#F4 · Low · Customs-trader numbers and a tax registration in a forecast
- XPath: `/Forecast/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/Forecast/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: section 4.8. A Forecast carries a quantity (24 000 kg of lint) and no price, amount or tax, and is not a customs document. The mill's Coastal State sales-tax registration and both parties' customs-trader numbers have no use in it and read as copied from master data (IND5). Money found the same tax block in the non-billing documents 07, 09, 10, 12, 13 and 14 of the flow.
- Condition: the forecast carries a party's tax registration or customs-trader number only if it does something with it, otherwise none.
- Options: (a, preferred) drop `PartyTaxScheme` and the customs-trader numbers from the forecast's parties; (b) keep one only where the forecast is given a purpose for it.
- Needs decision: no
- From: broad (F8), money (F1), parties (F5)

### cotton/02#F5 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Forecast/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Forecast/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." The mill and the ginnery, in two registers (`XB:FBR`, `XL:ICR`), share the date with Bayforth Forwarding and both ports; 271 occurrences in 181 files (recounted with `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`). That reads as a default (IND5), unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop it where the world has none; (c) record a register-wide 1996 date in the story.
- Needs decision: yes
- From: parties (F4)

### cotton/02#F6 · Low · The mill's contact: name, job title and department contradict each other
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Forecast/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the mill sends the forecast of its own purchases as buyer; the name "Purchasing" fits, the department "Sales" and the title "Customer service officer" describe selling. The three do not describe the same contact. Parties counted the combination (a contact named Purchasing in department Sales) in 52 files.
- Condition: the buyer's contact has a name, job title and department that agree with each other and fit the buyer role.
- Options: (a, preferred) a purchasing department and a buyer's job title; (b) drop `JobTitle` and `Department` and keep the functional name.
- Needs decision: no
- From: broad (F3), parties (F2)

### cotton/02#F7 · Low · The ginnery's English address tagged as Bayvarran English, and its legal form in one untagged rendering
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/Forecast/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Forecast/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Forecast/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:Name[2]` = `Cotton lint, compressed bale`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: here the English names of the ginnery's Lisavan address carry `languageID` `en-XB`; in the ginnery's own documents (01 and others) the same names carry `en-XL`, and its legal form is given in Lisavan and English, while here only the English form appears, without `languageID`. The item's English name and description are tagged `en-XB` here and `en-XL` in 10, 11 and 16 (broad). So the same party and item are described two ways in the flow, apparently following the sender (parties lists the Bayvarran-sent 02, 07, 08, 09, 13, 15 and 18). Both parts that raised it said "no"; the merge sets "yes" to align with every earlier flow's merge, which kept the same question Low/yes because a tag that follows the issuer's English is also a defensible reading and no convention is recorded.
- Condition: the same rendering of the same address, legal form and item text carries the same renderings and `languageID`s in every example, or the rule by which the tag follows the issuer is recorded.
- Options: (a, preferred) the renderings and tags of 01 (`en-XL`, Lisavan + English legal form) everywhere, because `languageID` describes the text, not its reader; (b) record that tags follow the issuer and apply it to every text of the party.
- Needs decision: yes
- From: broad (F4), parties (F3)

### cotton/02#F8 · Low · `PackSizeNumeric` 227 for a bale "of about 227 kg"
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count. Logistics and context read 227 as the weight of a bale in kilograms (the description says "bales of about 227 kg"): a bale holds no 227 items, and a numeric without a unit cannot carry a weight, so the element would carry a meaning other than its definition (Medium). The other reading (merger B of this flow): the forecast quantity is in KGM, so the item is the kilogram of lint, and a bale holding about 227 such units is "the number of items in a pack". That reading fits the definition, but the value is then only nominal ("about"), and `PackQuantity` 1 EA ("the number of subunits making up this item") would say the kilogram is one unit. The merge cannot settle which reading the example intends, so the finding is Low with a decision. Recounted: `<cbc:PackSizeNumeric>227<` in 7 files, all in this flow (02, 07, 08, 10, 11, 15, 16).
- Condition: `PackSizeNumeric`, where present, is a count of items (in the item's own unit) in a pack, and the reading is consistent with `PackQuantity` and with how the item is quantified; the nominal bale weight, if it is meant as a weight, is in an element with a weight unit.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an `AdditionalItemProperty` with `ValueQuantity` in KGM (or the description only), because a nominal "about" weight is not a count; (b) keep them with the per-kilogram reading documented (item = 1 kg, pack = bale of 227 kg).
- Needs decision: yes
- From: broad (F7, Low), logistics (F2, Medium), context (F3, Medium)

### cotton/02#F9 · Low · Origin area "North coast" in `Region` here, in `District` in the farm's address
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `District` is "The district or geographical division of a country or region in which this address is located". The farm's address places the north coast of Lisavu in `District`; here the same area is a `Region`. Logistics refuted it within its lens: a recognised growing region of origin is what `Region` covers. That reading is possible, but then the farm's address puts the same area in another element; the inconsistency remains, so the finding stays Low.
- Condition: the north coast of Lisavu is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in `OriginAddress`, as in the farm's address (a division of one country); (b) `Region` in both, if the north coast is a recognised economic region of the island.
- Needs decision: no
- From: broad (F6), context (F4); logistics (considered and refuted, argument carried)

### cotton/02#F10 · Low · Classing results in the applicant's remarks
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for this certificate". The text is the classer's result, signed by the chamber's classer (`Signature/Note`), not a remark of the applicant. Independent of F1 (if the certificate stays anywhere in the flow, the same applies).
- Condition: the classing result is not carried as an applicant's remark, or the remark is really the applicant's.
- Options: (a, preferred) keep the results in item properties (grade and staple are there) and drop the remark; (b) move them to an element of the certificate that holds its content, if the model offers one.
- Needs decision: no
- From: broad (F5)

## Checked and consistent
- 07 revises this forecast: `07-ForecastRevision.xml:/ForecastRevision/cac:OriginalDocumentReference/cbc:ID` = `LTM-FC-26-0192`, with the same source issue date and time (2026-02-02, 09:00:00).
- Staple 28.6 MMT = 1-1/8 inch (1.125 × 25.4 = 28.575 mm), as in the remark (recomputed).
- 24 000 KGM / 227 kg = 105.7 bales, plausible for a forecast "of about"; the first order 08 is 6129 kg = 27 × 227 kg (recomputed).
- `ForecastPeriod` 2026-02-16 to 2026-06-02 starts after the issue date; roles (sender/buyer the mill, receiver/seller the ginnery) fit a buyer's order forecast (`ORDER`, `TOTAL`).
- Item `SCG-LINT`, HS 520100 and CPC 01921 as in 07, 08, 10, 11, 15, 16; HS 5201 fits lint not carded or combed.
- The mill (`20412603`) and the ginnery (`IC42681`) carry the same identifiers, register and legal data as elsewhere in the flow; the certificate issuer and signatory are the Selanu Chamber of Commerce `IC42133`, as wherever the certificate occurs.
- No price, amount, tax category or payment information is present (money).

## Considered and refuted
- `/Forecast/cbc:BasedOnConsensusIndicator` = `true`: consensus in a forecast sent as version 1 by one side — refuted: a collaborative forecast can be agreed before it is sent under the season arrangement. (from broad, context)
- `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `SCG-SEASON-2026`: broad left it out as readable; the merge followed context and made it F2. (from broad)
- `/Forecast/cac:SenderParty/cbc:IndustryClassificationCode` = `1312`: a weaving mill buying raw lint — refuted: an integrated mill spins and weaves; plausible main activity. (from broad)
- `/Forecast/cac:ReceiverParty/cac:Contact/cbc:Name` = `Cotton sales`: the ginnery's sales contact receives a forecast of what its customer will buy — fits the role. (from parties)
- `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`: logistics refuted (a recognised growing region); the merge kept the inconsistency with the farm's `District` as F9 (from broad, context). (from logistics)
- `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`: one subunit per item as a filler — refuted: states that the item is sold by the bale. (from context; broad saw it as adding nothing, folded into F8's options)
- `/Forecast/cbc:Note` = `Depends on clothing orders from the store.`: unrelated — refuted: explains why the forecast may change, which 07 then does. (from context)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined, all evidence kept.
- context/F2 → F2: kept Medium/yes; broad's partial refutation added; references to `SCG-SEASON-2026` verified over the flow.
- broad/F2, parties/F1 → F3: combined; count verified.
- broad/F7 (Low), logistics/F2, context/F3 (Medium) → F8: Low with needs decision yes (parts: no), because a per-kilogram reading (item = 1 kg; raised by merger B of this flow) fits the definition and cannot be excluded; aligned with merger B.
- broad/F8, money/F1, parties/F5 → F4: grouped (tax registration + customs-trader numbers).
- broad/F3, parties/F2 → F6: combined.
- broad/F4, parties/F3 → F7: combined (legal form and item name added as places); needs decision changed from no to yes, to align with the earlier flows' merges (tag following the issuer is a defensible reading; no convention recorded).
- broad/F6, context/F4 → F9: combined, logistics' counter-argument added.
