# LLM review: 06-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/06-Invoice.xml`, Git blob `a42ab090a50a199d6ef007b111b5c77252c9f943` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/06#F1 · High · Due date contradicts "30 days net"
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-24`
- Why: The invoice is issued on 2026-04-02 (`/Invoice/cbc:IssueDate` = `2026-04-02`); 30 days net gives 2026-05-02. The due dates and the start of the penalty period follow a 21-day term instead. The same contradiction is in 02-Invoice.xml.
- Condition: The due dates, the penalty period and the payment terms note state the same term.
- Options: (a) due date 2026-05-02 and penalty period from 2026-05-03; (b) change the note to 21 days. Preference: whichever the world's standard terms "XB-STD" say; if they say 30 days, (a).
- Needs decision: no

### utilities/06#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language itself (already in Language/ID), not a locale. 213 examples carry the same pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out; (b) a real locale (e.g. en-XB).
- Needs decision: no

### utilities/06#F3 · Low · Exemption reason given for a levy outside the scope of tax
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:ID` = `O`
- Why: TaxExemptionReasonCode is "The reason for tax being exempted, expressed as a code". Category O means the levy is outside the scope of the tax, which is not an exemption: nothing is exempted. EN 16931 requires an exemption reason for category O as well, but under UBL's definition the reason describes an exemption that does not exist here. The world's list does contain a code for this case, so the list itself mixes exemption and out-of-scope reasons.
- Condition: The out-of-scope levy carries no exemption reason, or the use of the exemption reason for out-of-scope supplies is recorded as a deliberate deviation (EN 16931 practice) among the findings.
- Options: (a) record it as an EN 16931 vs UBL finding and keep; (b) drop the exemption reason for category O. Preference: (a), since the world's list was built for this case.
- Needs decision: yes

### utilities/06#F4 · Low · Whole shop's water booked to the garden department
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". The invoice covers the water and sewage levy of the whole shop (`/Invoice/cac:InvoiceLine/cac:PurchaseReference/cbc:Description` = `Shop, Lumeport`); nothing explains why one department carries all of it.
- Condition: The accounting cost fits what is invoiced, or the story says why the garden department carries it.
- Options: (a) a building or facilities cost centre; (b) give the reason in the story. Preference: (a).
- Needs decision: yes

### utilities/06#F5 · Low · Customer master data the invoice does nothing with, and a buying office as contact
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- Why: A water bill uses neither the customer's logo, its online shop nor its social media profile. The contact is the buying office (titled "Customer service officer", department "Sales"), whereas a utility invoice goes to accounts payable or facilities.
- Condition: The customer carries only data the invoice uses; its contact handles utility invoices, with agreeing name, title and department.
- Options: (a, preferred) drop logo, web site and social media; give an accounts-payable contact.
- Needs decision: no

### utilities/06#F6 · Low · Beneficiary repeats the party the levy is collected for
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: CollectedForParty ("The Party on whose behalf this item or amount is collected") already names the department. BeneficiaryParty ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") repeats it without adding a different party; the line note speaks of "the city of Lumeport" as beneficiary, of which the department is a part. As it stands one of the two is redundant.
- Condition: BeneficiaryParty is present only if the beneficiary differs from the party collected for (e.g. the city as such, if the department only administers the levy).
- Options: (a, preferred) drop BeneficiaryParty; (b) make it the city, if the story distinguishes city and department.
- Needs decision: no

## Checked and consistent
- Lines: 86 × 2.35 = 202.10; collection line 86 × 0.42 = 36.12; total 238.22 = LineExtensionAmount = TaxExclusiveAmount = TaxInclusiveAmount = PayableAmount; tax 0.00 with taxable amounts 202.10 (E, drinking water) and 36.12 (O, levy).
- Penalty: 1.5 % of 238.22 = 3.57 = PenaltyAmount; penalty period one month from the day after the due date.
- LineCountNumeric 2 = one invoice line plus one collection line.
- Agreement with 05-UtilityStatement.xml (86 m³, 202.10, meter CSW-W-55102, contract CSW-C-260118) and with 07-RemittanceAdvice.xml's reference to CSWC-INV-26-0317.
- check_ids.py: RF03CSWCINV260317, account XB21BLUM38010004189160 and GLN 9522610900002 correct; BIC-like BLUMXBLX uses the user-assigned code XB.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: water as services — refuted, the world's tax law decides, and it is applied consistently.
- `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: supply type for a levy collected for a third party — refuted, a sewage-treatment levy is a charge for a service.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: MassPaymentNetSystem for a business customer — refuted, a retail chain paying routine bills through the mass payment system is plausible.
