# LLM review: 16-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/16-Invoice.xml`, Git blob `e1ce518ac0f84644902623e83922648f889ca0d0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/16#F1 · Medium · Language codes in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/16#F2 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/16#F3 · Low · Outbound freight booked as stock purchases
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCost` is the buyer's accounting code for the invoice. The invoice bills Lumeway for carrying goods it sold delivered duty paid to its customer (08-Order, `DDP`): an outbound distribution cost, not a purchase of stock. The same code and text are typical of a goods purchase invoice; here they look copied.
- Condition: the buyer's accounting cost describes what this invoice is for Lumeway.
- Options: (a, preferred) an accounting code and text for outbound freight or distribution costs; (b) drop both.
- Needs decision: no

### retail/16#F4 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the supplier's contact answers billing questions and the customer's contact receives and approves the invoice. Bayforth is represented by its "Export desk" (operations, for a domestic haul) and Lumeway by its customer service in sales. 08-Order shows that Lumeway has an accounts department (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`).
- Condition: the contacts fit the billing roles.
- Options: (a, preferred) Bayforth's accounts receivable and Lumeway's accounts payable; (b) use `AccountingContact` in the customer party and drop the party contacts.
- Needs decision: no

## Checked and consistent
- Arithmetic: 38 km × 2.85 = 108.30 = line extension = tax exclusive = tax inclusive = payable amount; tax 0.00 at 0 %.
- Penalty: 1.5 % × 108.30 = 1.62 (1.6245 rounded); the penalty period starts on 2026-05-31, the day after the due date; due date 2026-05-30 = issue date + 30 days, as the note says.
- The waybill reference `BF-WB-26-0231` and consignment `LD-CS-26-0228` resolve to 13-Waybill and the consignment of 11 to 15; the carrier and supplier is Bayforth, the customer Lumeway, the transport user and bill-to party of 11.
- Tax: exempt (`E`) with reason "service to a business" and supply type services fits a transport service bought by a business, under the state sales tax of both parties.
- Payment: RF reference `RF66BFINV260234` and account `XB40BLUM38020502618225` pass their check digits (check_ids.py); the account is Bayforth's, the receiving party; channel `MPNS` is a real ISO 20022 ClearingChannel2 code.

## Outside this review
- Distance: 38 km billed for the haul from Marrowdale (Upland State) to Lumeport (Coastal State); whether this matches the map's route between the two towns is a question for the map consistency review. It also bears on the timeline (truck on the Marrowdale ring road at about 11:49, expected at the store at 14:00, received the next day in 17-ReceiptAdvice).
