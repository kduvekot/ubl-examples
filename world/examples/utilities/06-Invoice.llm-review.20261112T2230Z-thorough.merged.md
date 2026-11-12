# LLM review: 06-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/06-Invoice.xml`, Git blob `a42ab090a50a199d6ef007b111b5c77252c9f943` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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


### utilities/06#F1 · High · Due date and penalty start contradict "30 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-24`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-02`
- Why: Redone by the merge: 2026-04-02 + 30 days = 2026-05-02; the three due dates are 2026-04-23 (+21 days) and the penalty period starts on 2026-04-24, so a surcharge would apply to a payment the note says is not yet due. Refutation attempted: counting 30 days from the end of the invoice period gives 2026-04-30, not 2026-04-23 either. Same in 02 ("30 days net") and 13 ("45 days net"). The remittance 07 pays on 2026-04-19, within both terms.
- Condition: Note, due dates and penalty period start state the same term.
- Options: (a, preferred) note "21 days net", matching the penalty period and the flow's other invoices (money, context), unless the XB-STD terms are 30 days; (b) due dates 2026-05-02 and penalty period from 2026-05-03 (broad's preference if XB-STD says 30 days).
- Needs decision: no
- From: broad (F1), money (F1), context (F1)

### utilities/06#F2 · Medium · Drinking water classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture." The world's SupplyTypeCode list (`world/codelists/gc/SupplyTypeCode.gc`, verified by the merge) defines GOODS as "A supply of goods, including energy and water delivered through a network." Water through the mains is GOODS by the list's own definition. The broad part refuted it ("the world's tax law decides"); the world's list is that law's code list, so the refutation does not hold. Same as utilities/02#F4.
- Condition: The supply type of the drinking water line is GOODS.
- Options: (a, preferred) GOODS.
- Needs decision: no
- From: money (F2); broad refuted it

### utilities/06#F3 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language itself, repeating Language/ID. Recounted: 364 occurrences in 213 files over `*.xml` (parts: 362).
- Condition: LocaleCode holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) remove; (b) a locale such as en-XB with a fitting list.
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### utilities/06#F4 · Low · A tax rate of 0 % on a levy outside the scope of tax
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: Percent is "The tax rate for this category, expressed as a percentage". Category O (outside the scope of tax) has no rate; 0 % describes it as zero-rated, which is category Z. EN 16931 forbids a rate for O (BR-O-05, own knowledge); the point here is the UBL meaning. For category E the 0 % is equally a rate that does not apply, though less misleading.
- Condition: The category O of the levy carries no Percent.
- Options: (a, preferred) leave Percent out for O (and consider the same for E).
- Needs decision: no
- From: money (F4)

### utilities/06#F5 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:ID` = `O`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted, expressed as a code". Category O means outside the scope of the tax, which is not an exemption. EN 16931 requires an exemption reason for O as well (own knowledge), but under UBL's definition the reason describes an exemption that does not exist here; the world's list has a code for this case, so the list itself mixes exemption and out-of-scope reasons.
- Condition: The out-of-scope levy carries no exemption reason, or its use for out-of-scope supplies is recorded as an EN 16931 vs UBL finding.
- Options: (a, preferred) record it as an EN 16931 vs UBL finding and keep, since the world's list was built for this case; (b) drop the exemption reason for O.
- Needs decision: yes
- From: broad (F3)

### utilities/06#F6 · Low · Supply type "services" on a levy that is no supply
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: SupplyTypeCode is "A code signifying the type of supply to which this tax category applies". The sewage levy is collected for the city under category O ("Levy collected for a public body"); it is not a supply of the water company, so a type of supply has nothing to describe (context). Against it (broad): a sewage-treatment levy is a charge for a service (of the city). Kept Low.
- Condition: The levy line carries no supply type, or one the world's tax rules define for collected levies.
- Options: (a, preferred) remove SupplyTypeCode from the collection line.
- Needs decision: no
- From: context (F3); broad refuted it

### utilities/06#F7 · Low · Penalty period of one month for a surcharge "per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `3.57`
- Why: PenaltyPeriod is "The period during which penalties may apply". One month limits the surcharge to the first month of delay, while the note says 1.5 % per month late, i.e. recurring; PenaltyAmount 3.57 = 1.5 % × 238.22 (3.5733, redone) is one month's surcharge. Same decision as the packaging merges.
- Condition: The penalty period and the note describe the same rule.
- Options: (a, preferred) a penalty period with a start date only, the amount stated as per month; (b) keep one month and say "1.5 % surcharge if paid late".
- Needs decision: no
- From: money (F3)

### utilities/06#F8 · Low · Whole shop's water booked to the garden department
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- XPath: `/Invoice/cac:InvoiceLine/cac:PurchaseReference/cbc:Description` = `Shop, Lumeport`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". The invoice covers the drinking water and sewage levy of the whole shop; nothing explains why the garden department carries all of it. 16 occurrences in 12 files (recount), Brightmarket's purchasing default. Money (05) argued that a garden department is a plausible water user; aligned with utilities/05#F11 and the packaging merges (Low, no).
- Condition: The cost centre fits what is invoiced (the same as in 05), or is absent, or the story gives the reason.
- Options: (a, preferred) a facilities or building cost centre; (b) keep it with a stated reason.
- Needs decision: no
- From: broad (F4, yes), context (F4)

### utilities/06#F9 · Low · Customer's marketing data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Brightmarket's logo, online shop and social media profile have no use in a water invoice it receives; they are part of the block repeated in all 41 examples with its full data. Copied master data.
- Condition: They appear only with a use in this invoice.
- Options: (a, preferred) drop them; (b) keep them only with a stated reason.
- Needs decision: no
- From: broad (F5, part), parties (F3), context (F5, part)

### utilities/06#F10 · Low · Customer's contact: buying office with a sales job title and department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name (buying office) and job title and department (customer service, Sales) contradict each other, and the accounting customer's contact should be the one who receives and settles the invoice (accounts payable) or buys utilities.
- Condition: Name, job title and department agree, and the function deals with incoming invoices or utilities purchasing.
- Options: (a, preferred) an accounts payable contact, or a purchasing title and department for the buying office; (b) drop title and department.
- Needs decision: no
- From: broad (F5, part), parties (F4), context (F5, part)

### utilities/06#F11 · Low · The water company described as a small enterprise registered on the world's default date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: A water utility serving a state's capital is not plausibly a small enterprise (parties; broad refuted it in 05: a small company serving one city is plausible). The registration date is shared by 25 companies of the world (271 occurrences in 181 files, recount). Same as utilities/05#F8 and the earlier flows' merges.
- Condition: Size and registration date are values of the company's own story, the same in every example, or absent.
- Options: (a, preferred) a fitting size and a registration date of its own; (b) drop them where unused; (c) record a 1996 event in the story.
- Needs decision: yes
- From: parties (F2)

## Checked and consistent
- Lines: 86 × 2.35 = 202.10; collection line 86 × 0.42 = 36.12; total 238.22 = LineExtensionAmount = TaxExclusiveAmount = TaxInclusiveAmount = PayableAmount; tax subtotals 202.10 (E, WATER) and 36.12 (O, LEVY), tax 0.00; LineCountNumeric 2.
- Penalty 1.5 % × 238.22 = 3.57.
- Agreement with `05-UtilityStatement.xml` (86 m³, 202.10, meter CSW-W-55102, contract CSW-C-260118); `07-RemittanceAdvice.xml` pays 238.22 on 2026-04-19, before the due date.
- check_ids.py: RF03CSWCINV260317, account XB21BLUM38010004189160 and GLN 9522610900002 correct; BLUMXBLX uses the user-assigned country code XB. Payee account named after the supplier's registration name, branch 380100 matching the account digits, the same in 07, 09 and 10.
- Parties as in 05 and 07; BuyerCustomerParty and SellerSupplierParty have no "if different" condition. The collection line names Lumeport Public Works Department (20410548), the same as in 09, 11 and the contest flow.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: water as services — refuted by broad (the world's tax law decides). The merge disagrees: the world's own list defines GOODS to include water through a network; made F2 (from broad).
- `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: supply type for a levy — refuted by broad (a charge for a service). Kept as context's F6, Low, with this argument (from broad).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: MPNS with rail LUMEPAY for a business customer's monthly bill — plausible, contradicts nothing (from broad, money).
- `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`: including the collected levy — refuted, UBL 2.5 has no separate total for collection lines, and the levy is part of what the customer pays (from money).
- `/Invoice/cac:CollectionInvoiceLine/cbc:Note`: names the city while the party is its works department — refuted, the department is the city's body charging the levy (from parties).
- `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyIdentification/cbc:ID`: a public department in a business register scheme — refuted for this review: the world identifies it this way everywhere; a question for the world's identifier rules (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: a real GLN — refuted, GS1 prefix 952 is reserved for demonstrations and examples; check digit valid (from parties).
- `/Invoice/cac:BuyerCustomerParty`: repeats the accounting customer — refuted, "The buyer." has no condition (from context).
- `/Invoice/cac:PurchaseReference/cbc:ID`: the supply contract as purchase reference — refuted, "a subscription number" is a named example (from context).

## Refuted in the merge
### broad/F6 · Low · Beneficiary repeats the party the levy is collected for
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why (broad): CollectedForParty ("The Party on whose behalf this item or amount is collected") already names the department; BeneficiaryParty ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") repeats it without adding a different party; the line note speaks of "the city of Lumeport". One of the two is redundant.
- Condition (broad): BeneficiaryParty is present only if the beneficiary differs from the party collected for (e.g. the city as such, if the department only administers the levy). Options: drop BeneficiaryParty, or make it the city.
- Refuted because: the two definitions state two different facts, and both are true of the city's works department here (parties, context). UBL has no "if different" condition on either; under the agreed rule that nothing is implied by absence, leaving the beneficiary out would not say that it is the same party. The note's "city" is consistent, since the department is the city's body that charges and receives the levy.

## Changed in the merge
- broad/F5 and context/F5 → F9 and F10: marketing data and contact split, as parties had them.
- broad/F4 (yes) → F8, Needs decision: no: aligned with utilities/05#F11 and the packaging merges.
- F1: preference set to the note "21 days net" (money, context); broad's option kept.
- F3: count corrected to 364 occurrences in 213 files.
- broad/F6 moved to "Refuted in the merge".
