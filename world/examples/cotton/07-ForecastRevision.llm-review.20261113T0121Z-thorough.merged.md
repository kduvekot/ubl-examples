# LLM review: 07-ForecastRevision.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/07-ForecastRevision.xml`, Git blob `fc49267ef8416292c4c72e5eb19588b0cdccd24f` (committed)
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

### cotton/07#F1 · High · "Twenty per cent more" is twenty-five per cent, and more than that per day
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Note` = `Twenty per cent more.`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cbc:Quantity` = `30000`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:StartDate` = `2026-04-03`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `24000`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- Why: the line revises line 1 of 02 (`RevisedForecastLineID` 1), 24 000 kg for 2026-02-16 to 2026-06-02. Recomputed: 24 000 × 1.20 = 28 800 kg; 30 000 / 24 000 = 1.25, i.e. 25 % more. Read as the second-half quantity (line period 2026-04-03 to 2026-06-02, 61 days), 30 000 kg is about 492 kg a day against 24 000 kg over 107 days, 224 kg a day, more than twice the original rate. The note and the structured values contradict each other whichever way the line is read. (Whether the revised line covers the whole period is F8.)
- Condition: the note, the revised quantity and the period it applies to describe the same change, consistent with line 1 of 02.
- Options: (a, preferred) quantity 28 800 kg as the season total with the whole period (the note's "twenty per cent" is the stated business change); (b) keep 30 000 kg and write "Twenty-five per cent more", with a matching period; (c) two revision lines (first half unchanged, second half raised) with a note per line.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### cotton/07#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (`ISO 639`) is a language code and repeats `Language/ID`. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`). Same as 02#F3.
- Condition: every `Language/LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F2), parties (F1)

### cotton/07#F3 · Low · Customs-trader numbers and a tax registration in a forecast revision
- XPath: `/ForecastRevision/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: a Forecast Revision is "a document used to revise a Forecast"; this one revises a quantity and carries no price, amount, tax or customs data. The mill's Coastal State sales-tax registration and both customs-trader numbers have no use in it and read as copied master data (IND5). Same as 02#F4.
- Condition: the forecast revision carries a tax registration or customs-trader number only if it does something with it.
- Options: (a, preferred) drop them, as for 02.
- Needs decision: no
- From: broad (F9), money (F1), parties (F5)

### cotton/07#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`); reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) dates from the companies' histories; (b) drop them; (c) record a register-wide date.
- Needs decision: yes
- From: parties (F4)

### cotton/07#F5 · Low · The mill's contact: name, job title and department contradict each other
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: as 02#F6: "Purchasing" fits the mill as buyer; the sales department and customer-service title do not. Parties counted the combination in 52 files.
- Condition: the buyer's contact has a name, job title and department that agree and fit a buyer.
- Options: (a, preferred) a purchasing department and a buyer's title; (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F4), parties (F2)

### cotton/07#F6 · Low · The ginnery's English address and the item texts tagged as Bayvarran English
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:Name[2]` = `Cotton lint, compressed bale`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: as 02#F7: the same renderings carry `en-XL` in the ginnery's own documents and `en-XB` here. Context refuted the item-text tag: the text is identical English and the tag reflects the issuer (the mill), a legitimate reading. Because both readings hold and no convention is recorded, the merge keeps it Low with a decision, as the earlier flows' merges and merger B of this flow.
- Condition: the same rendering carries the same `languageID` in every example, or the rule that the tag follows the issuer is recorded.
- Options: (a, preferred) `en-XL` for the ginnery's address and items everywhere; (b) record the issuer rule.
- Needs decision: yes
- From: broad (F5), parties (F3, address part); context (considered and refuted for the item text, argument carried)

### cotton/07#F7 · Low · The ginnery's legal form in one untagged English rendering
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: in the ginnery's own documents its legal form is given in Lisavan and English with `languageID`; here the Lisavan rendering is dropped and the English one is untagged. Split from F6, as 02#F8 (aligned with merger B and the road, rail and air merges).
- Condition: the ginnery's legal form carries the same renderings and `languageID`s in every example.
- Options: (a, preferred) both renderings with their tags, as in 01.
- Needs decision: no
- From: parties (F3, legal-form part)

### cotton/07#F8 · Low · The revised line covers only part of the forecast period
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:StartDate` = `2026-04-03`
- XPath: `/ForecastRevision/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Description` = `More bales from the second half of the season.`
- Why: line 1 of 02 forecasts 24 000 kg for the whole period 2026-02-16 to 2026-06-02. The revision line that replaces it has its own period 2026-04-03 to 2026-06-02. Read as written, it leaves 2026-02-16 to 2026-04-02 without a forecast, although the order 08 (2026-02-24) falls in it; read as the season total, the line period is wrong. The description ("more bales from the second half") supports a season total with a changed split, which one line with one period cannot express.
- Condition: the revised line(s) together cover the forecast period and state unambiguously what quantity applies to which part of it.
- Options: (a, preferred) the whole period on the revision line with the new season total; (b) two revision lines (first half unchanged, second half raised), so periods and quantities add up.
- Needs decision: no
- From: logistics (F3), broad (F1, period part)

### cotton/07#F9 · Low · `PackSizeNumeric` 227 for a bale "of about 227 kg"
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`
- Why: as 02#F9: `PackSizeNumeric` is "The number of items in a pack of this item". Read as the bale weight in kg it carries another meaning than a count (logistics and context: Medium); read per kilogram (the item is quantified in KGM, a bale holds about 227 one-kilogram units) it fits the definition, but only nominally ("about"). Cannot settle; Low with a decision, aligned with merger B of this flow. 7 files, all in this flow.
- Condition: `PackSizeNumeric`, where present, is a count of items in the item's unit, consistent with `PackQuantity`; a nominal weight, if meant as weight, is in an element with a weight unit.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an `AdditionalItemProperty` in KGM; (b) keep them with the per-kilogram reading documented.
- Needs decision: yes
- From: broad (F8, Low), logistics (F2, Medium), context (F2, Medium)

### cotton/07#F10 · Low · Origin area "North coast" in `Region`, in `District` in the farm's address
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: as 02#F10: the same part of Lisavu in two different address elements (logistics' reading of `Region` as a growing region is recorded there).
- Condition: the north coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in `OriginAddress`; (b) `Region` in both.
- Needs decision: no
- From: broad (F7), context (F4)

### cotton/07#F11 · Low · A forecast of future lint carries the classing certificate of one classed lot
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:EndDate` = `2026-06-02`
- Why: `Item/Certificate` is "A certificate associated with this item". The revision forecasts lint "from the second half of the season" (April to June); a classing certificate records the measured grade of a lot already ginned and classed (the same certificate goes with the 27 bales ordered in 08 and certified in 10). It cannot certify cotton still to be ginned; the wanted grade is already stated as item properties. Unlike in 02 (02#F1, High), the validation date 2026-02-20 precedes this document's issue date (2026-02-22), so no date contradiction; Low.
- Condition: the forecast revision states the wanted quality without a certificate of a specific lot, or makes clear the certificate describes a reference lot.
- Options: (a, preferred) drop the certificate and keep the grade and staple properties.
- Needs decision: no
- From: broad (F3), context (F3)

### cotton/07#F12 · Low · Classing results in the applicant's remarks
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Remarks` is "Remarks by the applicant for this certificate"; the text is the classer's result. Same as 02#F11 (and merger B's row).
- Condition: the result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark; grade and staple are item properties already.
- Needs decision: no
- From: broad (F6)

## Checked and consistent
- `OriginalDocumentReference` `LTM-FC-26-0192` resolves to 02; `SourceForecastIssueDate` 2026-02-02 and `SourceForecastIssueTime` 09:00:00 equal 02's issue date and time; `RevisedForecastLineID` 1 is 02's only line; sequence number 1 is the first revision.
- Purpose code ORDER as in 02; header forecast period unchanged (2026-02-16 to 2026-06-02); the line period lies within it.
- The note "Demand for clothing has risen" and `AdjustmentReasonCode` DEMAND agree and follow 02's note that the forecast depends on clothing orders (context).
- 30 000 kg / 227 kg = 132.2 bales (recomputed).
- Parties (mill as sender and buyer, ginnery as receiver and seller) are those of 02; certificate issuer and signatory `IC42133` as elsewhere.
- No price, amount, tax category or payment information (money).

## Considered and refuted
- `/ForecastRevision/cbc:RevisionStatusCode` = `REVISED`: redundant in a revision — refuted: it distinguishes a revision from a cancellation and states the status positively. (from broad, context)
- `/ForecastRevision/cac:ReceiverParty/cac:Contact/cbc:Name` = `Cotton sales`: the ginnery's sales contact receives a forecast of what its customer will buy — fits the role. (from parties)
- `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:Description[2]` (`languageID` `en-XB`): context refuted (tag reflects the issuer); the merge kept the tag question as F6 with that argument. (from context)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined, arithmetic redone (incl. daily rates); the period coverage split off as F8 with logistics/F3.
- broad/F2 + parties/F1 → F2.
- broad/F9 + money/F1 + parties/F5 → F3: grouped (copied tax/customs data).
- broad/F4 + parties/F2 → F5.
- broad/F5 + parties/F3 → F6 and F7: legal form split off (Low/no); F6 needs decision changed from no to yes (aligned with earlier flows and merger B).
- broad/F8 (Low), logistics/F2, context/F2 (Medium) → F9: Low/yes, aligned with merger B and 02#F9.
- broad/F3 + context/F3 → F11.
