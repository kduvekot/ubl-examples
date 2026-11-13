# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 44b84c0 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/19#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/19#F2 · Medium · The factor as payee of a credit that goes to the buyer
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: `PayeeParty` is the party that receives the payment. Under a credit note the money flows to Brightmarket, the customer (by refund or by set-off), not to Harbourline, which received the invoice's payment as factor. Read with UBL's definition, the credit note says Harbourline is to be paid 494.00. The note speaks of a set-off "against the next payment to the seller", while the invoice's payment goes to the factor, so it is also unclear against whose claim the credit is set off.
- Condition: the payee of the credit note is the party that receives the credited amount (or there is no payee), and the note names the claim the credit is set off against.
- Options: (a, preferred) drop the payee party and say in the note that the credit reduces the amount due to Harbourline under invoice LD-INV-26-0236; (b) keep Harbourline only if the world's factoring agreement makes the factor handle refunds, and say so.
- Needs decision: yes

### retail/19#F3 · Medium · Language codes in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/19#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/19#F5 · Low · A torn carton, but the benches travel unboxed on pallets
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:Note` = `Bench refused: armrest bent, carton torn.`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`
- Why: the item's packaging is stretch film and pallet straps, and 12-DespatchAdvice describes pallets of four benches without cartons. The credit note repeats the "carton" of 17-ReceiptAdvice.
- Condition: the note describes the packaging the goods actually have.
- Options: (a, preferred) "stretch film torn" or no packaging detail.
- Needs decision: no

### retail/19#F6 · Low · Contacts that do not fit the billing roles
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the order names the accounts contacts of both parties (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`, `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:AccountingContact/cbc:Name` = `Accounts payable`); the credit note uses customer service and the buying office, whose job title and department also contradict its name.
- Condition: the accounting parties' contacts are their accounts departments, with name, job title and department that agree.
- Options: (a, preferred) as in the order.
- Needs decision: no

### retail/19#F7 · Low · Whole item master data copied into the credit note line
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CircularityProfile`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a credit note identifies what is credited; the catalogue data (emissions, circularity, load test, dimensions, Urvania's customs tariff code in a domestic sale) is not used by it.
- Condition: the credited item carries its identifiers and tax category.
- Options: (a, preferred) drop the catalogue data.
- Needs decision: no

## Checked and consistent
- Arithmetic: 1 × 520.00 = 520.00; promotion support 5 % × 520.00 = 26.00, the same rate as the invoice's allowance, so the credit returns exactly the net price of one bench (11856.00 / 24 = 494.00); taxable = payable = 494.00; tax 0.00.
- References: invoice `LD-INV-26-0236` (issue date 2026-04-30, line 1), order line 1, despatch line 1 and receipt line 1 resolve to 18, 08, 12 and 17; the discrepancy (transport damage, one bench refused) and the delivery date 2026-04-30 agree with 17-ReceiptAdvice, which requested the credit.
- Tax category `E` "sale for resale" and supply type goods agree with the invoice.

## Considered and refuted
- `/CreditNote/cac:DiscrepancyResponse/cbc:ReferenceID` = `1`: suspected an unclear reference — refuted: it points to line 1, the only line of the credit note and of the invoice, and the line repeats the response.
