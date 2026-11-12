# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/07-Invoice.xml`, Git blob `0345a2bca9a5957f58f15a04460ca368ab893cee` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### packaging/07#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language already in `Language/ID` and names no locale. The same
  value occurs 362 times in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`,
  re-counted in the merge).
- Condition: in both parties, `LocaleCode` is absent or holds a locale (language and region) from a
  locale list named in `listID`.
- Options: (a) remove it (preferred by broad and context, and here: it needs no new code list);
  (b) a real locale such as `en-XB` from a locale list (preferred by parties).
- Needs decision: no
- From: broad F1, context F1, parties F1

### packaging/07#F2 · Low · Men's shirts charged to the buyer's "Garden department"
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Cotton shirt`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole,
  expressed as text". The invoice bills 600 men's shirts that Brightmarket sells in its clothing
  department (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`),
  but books them to the garden department, Brightmarket's cost centre for garden furniture
  (`furniture/08-Order.xml:/Order/cbc:AccountingCost` = `Garden department`), taken over from the
  order (`05-Order.xml:/Order/cbc:AccountingCost` = `Garden department`). The pair `6120` / `Garden department`
  is Brightmarket's constant in 12 XML files (`grep -rl --include='*.xml' '>Garden department<'`,
  re-counted in the merge: packaging, furniture, retail and utilities flows).
- Condition: the cost centre fits a clothing purchase and equals the order's, or is absent from
  both.
- Options: (a) preferred: a clothing-department cost centre in order and invoice; (b) drop it from
  both.
- Needs decision: no
- From: broad F3, context F2, money F1

### packaging/07#F3 · Low · The invoice is not linked to the despatch advice of the goods it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `600`
- Why: The shirts billed here were announced the same day in `06-DespatchAdvice.xml`
  (`06-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `LTM-DA-26-0526`, issued 11:35; this invoice
  14:49), but the invoice refers only to the order: no `DespatchDocumentReference` and no `Delivery`
  with a date or place. The store has to match invoice and goods receipt through the order alone,
  and the date of supply is not stated anywhere in the flow (see `06-DespatchAdvice` F2). No example
  refers to `LTM-DA-26-0526` (grep over `*.xml`). Completeness remark.
- Condition: the invoice references despatch advice `LTM-DA-26-0526`, or states the delivery (date,
  place) it bills.
- Options: (a) preferred: `cac:DespatchDocumentReference` with `LTM-DA-26-0526`, since the document
  exists in the flow and is what goods-in matches against; (b) `cac:Delivery` with the actual
  delivery date.
- Needs decision: no
- From: broad F2, logistics F1

### packaging/07#F4 · Low · Master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The customer's logo reference, online shop and photo-sharing profile play no part in a
  supplier's invoice to it, and the supplier's customs trader ID has none in a domestic supply taxed
  under the Coastal State sales tax. They are master data copied into the document (section 4.8,
  IND5); the logo reference is in 41 examples (grep over `*.xml`).
- Condition: every party detail in the invoice has a role in invoicing, payment or tax, or the
  example states one.
- Options: (a) preferred: leave them out here; (b) state why they are needed.
- Needs decision: no
- From: broad F5, context F4, parties F4

### packaging/07#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 companies in all three
  countries share exactly this date (271 occurrences in 181 examples, grep over `*.xml`, re-counted
  in the merge), which reads as a default (IND5).
- Condition: Lumeport Textile Mill's RegistrationDate is its own date in the story, or absent.
- Options: (a) preferred: a date from the company history; (b) remove; (c) confirm as a story fact.
- Needs decision: yes (dates are part of the companies' histories)
- From: broad F7, parties F3

### packaging/07#F6 · Low · The contacts of the accounting parties are a purchasing mailbox and a buying office
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party". The invoicing supplier gives its
  purchasing mailbox for queries on its own sales invoice; the accounting customer gives its buying
  office, filed in Sales as customer service officer. Neither is an invoicing contact (accounts
  receivable / payable), neither handles the payment this invoice requests, and the names contradict
  the departments. Both are the parties' single contacts used in every role (89 examples with a
  `Purchasing` or `Buying office` contact in Sales, context's XPath count).
- Condition: each accounting party's contact belongs to billing or payment, with agreeing name, job
  title and department.
- Options: (a) preferred: accounts receivable for the mill, accounts payable for the store;
  (b) leave the contacts out.
- Needs decision: no
- From: broad F4, context F3, parties F2

### packaging/07#F7 · Low · A penalty period of one month against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: `PenaltyPeriod` is "The period during which penalties may apply"; a duration of one month
  from 2026-06-12 limits penalties to that month, while the note makes the surcharge recur monthly.
  `PenaltyAmount` 130.50 is one month's surcharge (1.5 % × 8700.00, recomputed in the merge). Same
  pattern in `02-Invoice.xml` and `04-Invoice.xml` (both carry a `PenaltyPeriod`, grep over `*.xml`).
- Condition: the penalty period does not end before the terms say penalties stop.
- Options: (a) preferred: start date only, with the note stating 130.50 as the surcharge per month;
  (b) a stated cap, with the duration kept.
- Needs decision: no
- From: money F2

### packaging/07#F8 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: `StandardItemIdentification` is "Identifying information for this item, assigned according
  to a standard system", in the world's own scheme `urn:ubl-examples:world:item`. The value is a
  well-formed GTIN-12 (UPC-A; mod-10 check digit 0, recomputed in the merge) whose GTIN-13 prefix 077
  lies in the range GS1 US allocates (060–139, own knowledge), so it can be taken for a real UPC; the
  agreed rule is that fictional values must not be mistaken for real ones. 8 distinct values of the
  scheme, all valid, in 64 examples (logistics, grep over `*.xml`).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1
  allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN; (b) GTINs in GS1's demonstration
  prefix 952; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes (world-wide identifier convention)
- From: broad F6, logistics F2

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml` (same buyer and
  seller; the accounting supplier and customer blocks are identical to the seller and buyer blocks
  there, parties compared line by line); issued after the order and after the despatch advice.
- Quantity: 600 EA invoiced = 600 ordered = 600 delivered
  (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`); item,
  seller's ID `LT-SH-01`, HS `620520`, CPC `28232` and properties agree.
- Arithmetic (redone in the merge): `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `600` ×
  `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `14.5` = 8700.00 =
  `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `8700.00`; tax 0.00, category E, reason
  RESALE, scheme STT, as in the order.
- Payment terms: 2026-05-12 + 30 days = `/Invoice/cbc:DueDate` = `2026-06-11`, equal in
  `PaymentMeans` and `PaymentTerms`; `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `130.50` =
  1.5 % × 8700.00; penalty start 2026-06-12.
- Payment means: domestic credit transfer (`MPNS`, `LUMEPAY`) to the mill's own account
  `XB35BLUM38020504608076` (named Lumeport Textile Mill Ltd, Harbour branch `380205`, which is also
  in the account number); `check_ids.py` (rerun in the merge): account, GLN and RF reference
  `RF18LTMINV260529` pass.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LT-SH-01`: the buyer's
  item ID `BM-778120` of the order and despatch advice is missing — refuted because leaving out an
  optional identifier contradicts nothing; the item is still identified by the seller's ID and the
  world item number (from broad, context, logistics).

## Changed in the merge
- money F2 → F7: kept unchanged (Low, no); listed because the same pattern recurs in `02-Invoice.xml`
  and `04-Invoice.xml` of the other half of this flow and is recorded in
  `packaging-merge-decisions-b.md`.
- parties F4 / broad F5 / context F4 → F4: grouped, with the supplier's customs trader ID (parties)
  as an XPath line of its own.
- F1 (LocaleCode): both options kept; preference stated as removal (broad, context) against
  parties' `en-XB`.
- Findings renumbered by severity and position.
