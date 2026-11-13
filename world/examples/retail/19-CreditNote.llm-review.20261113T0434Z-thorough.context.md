# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/19#F1 · High · Emission factor times base does not give the emission
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F4).
- Options: drop the emission from the credit note (preferred), or correct the factor.
- Needs decision: no

### retail/19#F2 · Medium · The factor as the party that receives the payment of a credit
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: in a credit note, PayeeParty is "The Party who receives the Payment". A credit note states
  "credits due to the Debtor from the Creditor"; if anything is paid under it, the buyer Brightmarket
  receives it (a refund), or it is set off against Brightmarket's next payment, as the note says. The
  factor Harbourline receives the payments of the factored invoice (18-Invoice.xml), not those of the
  credit. The payee copied from the invoice says the factor is paid the credit.
- Condition: the credit note names no payee, or names the party that receives the refund.
- Options: (a) preferred: drop PayeeParty; the factor's involvement can stay in a note (the credit
  reduces the receivable assigned to it); (b) name Brightmarket as the refund's payee if a refund is
  intended.
- Needs decision: no

### retail/19#F3 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples). LocaleCode is "A
  code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is a language
  code (213 examples; both counted with `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/19#F4 · Low · The credit note carries the item's full catalogue description and the parties' master data
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: crediting one damaged bench uses its identification and price; its footprint, circularity
  profile, load test and customs codes, the seller's customs trader number and the buyer's social
  media play no part (IND5/IND6).
- Condition: item and parties carry what the credit note uses.
- Options: reduce them.
- Needs decision: no

## Checked and consistent
- BillingReference `LD-INV-26-0236` (issue date 2026-04-30) and BillingReferenceLine `1` resolve to
  18-Invoice.xml; order, despatch and receipt references and their line references resolve to 08, 12
  and 17.
- One bench credited, the one refused in 17-ReceiptAdvice.xml; DiscrepancyResponse code 17
  "Transport damage" and the notes ("armrest bent, carton torn") agree with 17.
- 520.00 − 26.00 (5 % promotion support of 520.00) = 494.00, the invoice's net price per bench
  (11856.00 / 24 = 494.00).
- The line's ActualDeliveryDate 2026-04-30 is the receipt date of 17.

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine/cbc:PaymentPurposeCode`: a payment purpose on a credit that is set
  off — refuted because the code describes the underlying transaction (sale of goods), which holds for
  a refund or a set-off alike.
- `/CreditNote/cac:CreditNoteLine/cbc:AccountingCost`: repeats the header's cost centre — refuted
  because a line-level cost centre identical to the header is harmless and common.
