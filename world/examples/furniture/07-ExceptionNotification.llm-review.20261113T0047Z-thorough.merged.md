# LLM review: 07-ExceptionNotification.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/07-ExceptionNotification.xml`, Git blob `c4c9313c99d0a0d896c6b32f955b12d7b8319fcf` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/07#F1 · Medium · One notification line is an operational, a metric and a forecast exception at once
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SupplyChainActivityTypeCode` = `SALES`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:PerformanceMetricTypeCode` = `SALESUNITS`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ForecastPurposeCode` = `SALES`
- Why: On this line, `SupplyChainActivityTypeCode` "Establishes the criterion for one of the three types of exceptions: Operational, performance metric and forecast. This reports an exception notification about an operational exception." The line sets the operational type, a performance-metric type and a `ForecastException` ("A forecast accuracy or comparison exception") together. What it reports is the operational exception of criterion line 1 of `05-ExceptionCriteria.xml` (sales below 5 sets): description "Sales below the agreed threshold.", 3 against 5 sets, note "Three sets sold against five expected.". That criterion line itself sets an activity and a metric code (see the review of 05), but no forecast; the only forecast criterion (line 2 of 05) is not what the line reports.
- Condition: each notification line reports exactly one type of exception, the type of the criterion it was raised against; a forecast exception appears only when a forecast criterion was met.
- Options: (a, preferred) keep `SupplyChainActivityTypeCode` = `SALES` and remove `PerformanceMetricTypeCode` and `ForecastException`, which matches criterion line 1, the description, the note and the compared values; (b) report a forecast exception in a separate line against criterion line 2, with its own figures.
- Needs decision: no
- From: broad, context, logistics

### furniture/07#F2 · Medium · The line's reference meant for the Exception Criteria points to the Product Activity
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0572`
- XPath: `/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571`
- Why: In `ExceptionNotificationLine`, `DocumentReference` is defined as "A reference to Exception Criteria document can be provided." `BS-DOC-26-0572` is the Product Activity report `06-ProductActivity.xml`, not the Exception Criteria `05-ExceptionCriteria.xml` (`BS-DOC-26-0571`), which only the header refers to. A reference of one kind is used for another, and nothing on the line says which criterion (line 1, slow sales, or line 2, forecast deviation) was triggered. The merge tried the reading that the line points to the data it was evaluated on, which the generic element name would allow; the definition on this line names the criteria document specifically.
- Condition: the line's `DocumentReference` refers to the Exception Criteria (`BS-DOC-26-0571`), where possible identifying the triggered criterion line; the Product Activity, if referenced, is referenced at document level, with a document type or description.
- Options: (a, preferred) line reference to `BS-DOC-26-0571` (with a description "criterion line 1, slow sales"), and document-level references to both 0571 and 0572 with document types; (b) drop the line reference and keep both at document level.
- Needs decision: no
- From: broad, context, logistics

### furniture/07#F3 · Medium · The ForecastException names a forecast the flow does not have and matches no forecast criterion
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueDate` = `2026-03-16`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:IssueTime` = `10:00:00`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:DataSourceCode` = `SELLER`
- XPath: `05-ExceptionCriteria.xml:/ExceptionCriteria/cac:ExceptionCriteriaLine[2]/cac:ForecastExceptionCriterionLine/cbc:ComparisonDataSourceCode` = `BUYER`
- Why: Apart from F1, the content of the `ForecastException` has no counterpart in the flow. It names a seller's sales forecast "issued" on 2026-03-16 at 10:00 ("The date on which the forecast was issued"); no Forecast document exists in the flow (searched over `world/examples/furniture/*.xml`; Forecasts exist only in other flows). The only forecast criterion, line 2 of `05-ExceptionCriteria.xml`, compares the seller's forecast with the buyer's plan and is met by a deviation of more than 30 %, while this forecast exception compares a seller forecast with actual sales and gives no forecast figure or percentage at all. The aggregate is filled with values that neither the definitions nor the other documents support.
- Condition: either the `ForecastException` is absent (see F1), or the flow contains the forecast it names, and the exception matches a forecast criterion of `05-ExceptionCriteria.xml` (data source, comparison source, threshold) with its figures.
- Options: (a, preferred) remove the `ForecastException` together with F1; (b) add a forecast to the story and align criterion, comparison source, figures and times.
- Needs decision: no
- From: context, logistics

### furniture/07#F4 · Medium · ComparisonDataCode holds a kind of data, not a partner
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonDataCode` = `ACTUAL`
- Why: `ComparisonDataCode` is defined as "A code signifying the partner providing the information in this forecast exception". `ACTUAL` ("Actual sales" in the world's ComparisonDataCode list) says what kind of data was compared, not which partner provided it; the partner list used elsewhere is the DataSourceCode list, with BUYER and SELLER (as in `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:DataSourceCode` = `SELLER`). The code carries a meaning other than the element's definition.
- Condition: `ComparisonDataCode`, where present, names the partner providing the comparison information, from a list of partners.
- Options: (a, preferred) it disappears with the forecast exception (F1, F3); (b) if kept, `BUYER` from the data-source list, since the actual sales came from the store.
- Needs decision: no
- From: broad (context mentioned it within its F3)

### furniture/07#F5 · Medium · Comparison "forecast" issue time on actual sales, not that of the activity report
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueDate` = `2026-04-20`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:ForecastException/cbc:ComparisonForecastIssueTime` = `18:00:00`
- XPath: `06-ProductActivity.xml:/ProductActivity/cbc:IssueTime` = `16:35:00`
- Why: `ComparisonForecastIssueDate`/`Time` are "The date/time on which this comparison forecast was issued". The comparison data are actual sales (`ComparisonDataCode` ACTUAL), not a forecast, so the elements describe something their definition does not cover. Read as the issue time of the compared data, they point to the only actual figures of the flow, the Product Activity report `06-ProductActivity.xml`, which the line references (F2) and which was issued on 2026-04-20 (the same date) at 16:35, not 18:00. The logistics part rated this High as a contradiction with a referenced document. The merge tried to refute it: the notification never says that the 18:00 belongs to 06 (18:00 could be the close of business on the last day of the period), and the element meant for that link is itself misused (F2), so the contradiction rests on an inference; on the other hand, no other source of actual sales exists, and the 3 sets compared are 06's figure. The merge keeps it as Medium: the element is used outside its definition, and under the only reading the flow supports its value does not match 06.
- Condition: if a comparison issue date and time are given, they belong to a comparison forecast, or (if the forecast exception is kept for actual data) they are those of the document the comparison data come from (2026-04-20 16:35 for 06); otherwise they are absent with the forecast exception.
- Options: (a, preferred) resolved by removing the forecast exception (F1, F3); (b) if it stays, set the time to 16:35:00 and say which document the data come from.
- Needs decision: no
- From: logistics, broad, context

### furniture/07#F6 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/ExceptionNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode` (context, parties, earlier flows); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/07#F7 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/ExceptionNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/ExceptionNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/07#F8 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores receives the notification as the buyer and is asked to review the line. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact for supplier collaboration. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying or planning contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/07#F9 · Low · Party master data copied into the notification
- XPath: `/ExceptionNotification/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/ExceptionNotification/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/ExceptionNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo reference, online-shop website, photo-sharing profile, share capital (with the fully-paid-shares indicator) and both parties' state-sales-tax registrations are master data. An exception notification carries no amounts, tax treatment, payment or label and does nothing with any of them (section 4.8). The store's four marketing and capital elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only in documents that have a reason to carry them.
- Options: (a, preferred) remove them here, keeping identification, name, address, contact and electronic address; (b) keep any of them only with a reason the document states (none is apparent).
- Needs decision: no
- From: context, parties

### furniture/07#F10 · Low · ExceptionStatusCode, defined for shipment exceptions, used for a sales exception
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ExceptionStatusCode` = `OPEN`
- Why: UBL 2.5 defines `ExceptionNotificationLine/ExceptionStatusCode` as "A code signifying status specific to a shipment exception". The exception here is about sales, not a shipment. The value "Not resolved" is a sensible status for a notification that asks for a joint review, and the definition looks like a copying error in UBL, but under semantic conformance the value does not meet it as written. The same question arises in `05-ExceptionCriteria.xml` (where the broad part refuted it as a carried-over word).
- Condition: either `ExceptionStatusCode` is absent, or the use is kept consciously and the definition problem is recorded for the UBL TC write-up.
- Options: (a, preferred) keep it and record the definition for the TC: an open status is useful for a notification asking for review; (b) remove it.
- Needs decision: yes
- From: context

### furniture/07#F11 · Low · Source and compared values may be swapped
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SourceValueMeasure` = `3`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ComparedValueMeasure` = `5`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:VarianceQuantity` = `-2`
- Why: `SourceValueMeasure` is "The value used as the basis of comparison" and `ComparedValueMeasure` "The value that was compared with the source value that resulted in the exception". The basis of comparison is the agreed threshold of 5 sets from the criteria; the value compared with it, which resulted in the exception, is the observed 3 sets. The example has them the other way round. With the current assignment the variance is "source minus compared" (3 − 5 = −2); with the values swapped it is "compared minus basis", the more natural reading of "The variance of a data item from an expected value". The context part read the values as they are (compared 5 = the threshold, source 3 = the sales of 06) and found them consistent; the definitions are terse enough that this reading cannot be excluded, so this needs a decision.
- Condition: `SourceValueMeasure` holds the basis of comparison and `ComparedValueMeasure` the value compared with it, under one documented reading, with `VarianceQuantity` consistent with it.
- Options: (a, preferred) source 5 SET (threshold), compared 3 SET (observed), variance −2; (b) keep as is and record the reading that the source is the observed data.
- Needs decision: yes
- From: broad, logistics (context checked the opposite reading as consistent)

### furniture/07#F12 · Low · Maker's brand on an item for the store's own line
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:SupplyItem/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/ExceptionNotification/cac:ExceptionNotificationLine/cac:SupplyItem/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The description says the set is made for the store's own line, sold under the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`): a private-label product, normally sold under the retailer's brand. The maker's brand points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line.
- Needs decision: yes
- From: context

## Checked and consistent
- Arithmetic: `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:VarianceQuantity` = `-2` = 3 − 5 sets; 3 sets is less than the threshold 5 of criterion line 1, so the criterion is met; the note "Three sets sold against five expected" agrees with the values.
- Periods: the observation periods of header and line (2026-03-23 to 2026-04-20) equal the activity period of `06-ProductActivity.xml` and start on the effective date of criterion line 1 of `05-ExceptionCriteria.xml`; the notification (2026-04-21 17:49) follows the report (2026-04-20 16:35).
- References: the header's `/ExceptionNotification/cac:DocumentReference/cbc:ID` = `BS-DOC-26-0571` resolves to `05-ExceptionCriteria.xml`; the line's `BS-DOC-26-0572` resolves to `06-ProductActivity.xml` (corrected by the merge: the logistics part listed both as document-level references; 0572 is referenced on the line only). `11-OrderCancellation.xml` and `12-InstructionForReturns.xml` reference this notification.
- Priority HIGH and resolution REVIEW agree with criterion line 1 of 05 and with the note "Please review the line with us."; codes OPEN, HIGH, REVIEW, SALES resolve in the world's lists.
- Item identification matches the flow; GS1 check digits pass (`check_ids.py`, re-run by the merge); party data are identical to the other examples of the flow (parties part).

## Considered and refuted
- `/ExceptionNotification/cac:ExceptionNotificationLine/cbc:Note` = `Three sets sold against five expected.`: "expected" for a minimum threshold suspected to misstate the criterion — refuted because in plain language the agreed minimum is what the partners expected to sell at least; the description states it correctly as a threshold (from context, logistics).
- Sender = the maker: the notification comes from Brackenmere although the criteria were set by the store — refuted because `05-ExceptionCriteria.xml` says "Both sides are told when a criterion is met", and the maker evaluating the store's figures is plausible (from context).
- `/ExceptionNotification/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat receiver and sender — refuted because sender and receiver are the message parties while buyer and seller state the trade relationship, as UBL designs these documents (from parties).
- `/ExceptionNotification/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge) (from parties).
- `/ExceptionNotification/cac:SenderParty/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/ExceptionNotification/cac:SenderParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact as sender of a planning document — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/ExceptionNotification/cac:SenderParty/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/ExceptionNotification/cac:ReceiverParty/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F9 (from parties).
- `/ExceptionNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F7 by the merge.

## Changed in the merge
- broad/F2, context/F2, logistics/F3 (type part) → F1: combined.
- broad/F1, context/F1, logistics/F2 → F2: combined.
- context/F3, logistics/F3 (forecast part) → F3: combined; needs decision changed from yes (context) to no, because the preferred fix is the same removal as F1, which changes no document of the flow; the comparison times, which context included, are F5, and the comparison code is F4.
- broad/F3 → F4: kept Medium/no.
- logistics/F1, broad/F5, and the time part of context/F3 → F5: combined; severity lowered from High (logistics) to Medium, raised from Low (broad): the link of the 18:00 to `06-ProductActivity.xml` is an inference through a misused reference (F2), so the contradiction only partly survives, while the use of a forecast's issue time for actual data is a meaning other than the definition.
- broad/F4, context/F4, parties/F1 → F6: combined; preferred option set to removal, broad's `en-XB` kept as option (b).
- parties' refuted RegistrationDate → F7: made a finding (Low, needs decision) for alignment with the earlier flows.
- broad/F7, parties/F2 → F8: combined.
- context/F7, parties/F3, parties/F4 → F9: grouped as one problem (master data in a document that does not use it).
- context/F5 → F10: kept Low/yes.
- broad/F6, logistics/F4 → F11: combined; context's opposite reading (from its "Checked and consistent") added.
- context/F6 → F12: kept.
