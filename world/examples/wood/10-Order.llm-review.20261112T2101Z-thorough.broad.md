# LLM review: 10-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/10-Order.xml`, Git blob `9ace6d42e7deb8a74ae8c2e901f90885e501c883` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/10#F1 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/10#F2 · Low · Ex-works order without a pickup date
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Marrowdale Sawmill, timber yard`
- Why: Under EXW the buyer collects at the seller's yard; the order says where but not when the timber is to be ready or collected (no Delivery/RequestedDeliveryPeriod or Despatch/RequestedDespatchPeriod), although the Delivery/Despatch aggregate is present.
- Condition: The order states when the goods are to be ready for collection (or delivered).
- Options: (a, preferred) Add Delivery/Despatch/RequestedDespatchPeriod (or RequestedDeliveryPeriod).
- Needs decision: no

### wood/10#F3 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact on the purchase order is Brackenmere's trade sales desk in its Sales department (customer service officer), i.e. the function that sells Brackenmere's furniture, not the one that buys timber.
- Condition: The buyer's contact on the order is a purchasing contact.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/10#F4 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day). Here both buyer and seller, two different companies in the same register, have it.
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 12 m³ × 540 XBL/m³ = 6480.00 = LineExtensionAmount = PayableAmount.
- Tax: category E with reason RESALE (sale for resale or manufacture) under the Upland State sales tax fits a sale of timber to a furniture manufacturer in the same state (Brackenmere, ISIC 3100, Marrowdale).
- GLN 9523710900008 passes its check digit (check_ids.py); prefix 952 is the range GS1 reserves for examples and demonstrations (own knowledge), so it cannot be mistaken for a real GLN.
- The invoice 11-Invoice.xml refers to this order and repeats quantity, price and tax.
- Price plausibility: 540 XBL/m³ for boards against about 1108 XBL/m³ for the planed, cut-to-size slats of the Valdara order (7.2 / 0.006498 m³) is a credible difference.

## Considered and refuted
- `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty`: the seller as despatch party — refuted: under EXW the seller makes the goods available at its yard.
