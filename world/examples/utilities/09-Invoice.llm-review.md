# LLM review: 09-Invoice.xml

Reviewed file: [09-Invoice.xml](09-Invoice.xml) · Flow: `utilities` (`UTILITIES-2026-01`) · Review date: 2026-11-12

**Basis.** The semantic model of UBL 2.5 (`UBL-Entities-2.5.gc` from
<https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/>, SHA-256
`c7df070e…fe988d1`), the meaning of codes in `world/codelists`, and the other
XML documents of the flow where this document refers to them. The fictional
world (countries, currencies, languages, identifier schemes) is accepted as
given; only clashes with real standards are flagged.

**Severity.**
**High**: the value contradicts another value in this document or in a referenced document, or a reference is broken.
**Medium**: the element carries a meaning other than its UBL definition.
**Low**: plausibility, consistency or completeness remark.
**Recurring**: the same pattern occurs in many other examples.

## Summary

| # | Severity | Element(s) | Issue |
|---|---|---|---|
| 1 | High | `…/cac:PaymentMandate/cbc:MaximumPaymentInstructionsNumeric`, `…/cac:PaymentMandate/cac:ValidityPeriod` | A cap of 12 collections in an open-ended mandate used monthly since September 2024 |
| 2 | Medium | `…/cac:PaymentMandate/cac:PayerParty` | Payer given although it is the debtor |
| 3 | Low | `…/cac:CollectionInvoiceLine/cac:CollectedForParty`, `…/cac:BeneficiaryParty` | Levy collected for "the city" according to the text, but for a city department according to the parties |
| 4 | Low | `…/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` | Drinking water classified as a supply of services |
| 5 | Low | `…/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReason*` | An exemption reason on a category that is "outside the scope", not exempt |
| 6 | Low | `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent`, `cbc:PenaltyAmount` | Penalty terms that the follow-up Reminder does not apply |
| 7 | Low | `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` | A state-wide water utility as a small enterprise |
| 8 | Medium · Recurring | `…/cac:Language/cbc:LocaleCode` | A language code where a locale is defined |

## Findings

### 1. A collection cap that the mandate's own use has already exceeded (High)

- **XPaths:**
  - `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MaximumPaymentInstructionsNumeric` = `12`
  - `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:ValidityPeriod/cbc:StartDate` = `2024-09-02` (no end)
  - `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cbc:MandateTypeCode` = `RCUR` (recurring)
  - `/Invoice/cac:InvoicePeriod/cbc:DescriptionCode` = `MONTH`
- **UBL definitions:**
  - *Payment Mandate. Maximum Payment Instructions. Numeric*: "The number of maximum payment instructions allowed within the validity period."
  - *Payment Mandate. Validity_ Period*: "The period during which this mandate is valid."
- **Why it does not fit:** The cap applies to the whole validity period. That period starts
  on 2 September 2024 and has no end. Billing is monthly and collected under this
  recurring mandate. By the collection of this March 2026 bill on 23 April 2026, the
  mandate has been used about 19 times (October 2024 – April 2026), well over 12. Read
  literally, this collection is no longer allowed by the mandate it cites.
- **Suggestion:** Either drop `MaximumPaymentInstructionsNumeric` (the usual case for an
  open-ended utility mandate), or give the mandate a validity period whose length matches
  the cap (e.g. 12 months, renewed). The per-collection limit `MaximumPaidAmount` 150.00
  already gives the household the protection the statement refers to.

### 2. `PayerParty` repeats the debtor (Medium)

- **XPath:** `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty` (`PartyName/cbc:Name` = `Robin Ashdale`)
- **UBL definition:** *Payment Mandate. Payer_ Party*: "The Party, **if different from the debtor**, that makes the Payment."
- **Why it does not fit:** The debtor is the `AccountingCustomerParty`, Robin Ashdale. The
  payer named here is the same person, and the `PayerFinancialAccount` is the
  customer's own account (`XB64BLUM38010007251840`, also under
  `AccountingCustomerParty/…/Person/cac:FinancialAccount`). By its definition the element
  should only be present when a third party pays. Its presence suggests a separate payer
  that does not exist.
- **Suggestion:** Remove `PayerParty`. Keep `PayerFinancialAccount`.

### 3. The levy's beneficiary is named in two ways (Low)

- **XPaths:**
  - `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
  - `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
  - `/Invoice/cac:CollectionInvoiceLine/cbc:Note` = `Collected for the city of Lumeport and paid on to it.`
  - `/Invoice/cac:CollectionInvoiceLine/cac:Item/cbc:Name` = `Sewage levy of the city of Lumeport`
- **UBL definitions:**
  - *Invoice Line. Collected For_ Party*: "The Party on whose behalf this item or amount is collected."
  - *Invoice Line. Beneficiary_ Party*: "A Party for whom the associated transaction is ultimately intended or who derives benefit from it."
- **Why it does not fit:**
  - The text twice says the levy is the *city's* and is paid on to the city. The parties
    name a department of the city. A levy is imposed and owned by the legal person (the
    city), not by one of its departments.
  - `BeneficiaryParty` copies `CollectedForParty` and adds nothing.
- **Suggestion:** Name the city as `CollectedForParty`, with the department as
  `Contact`/`Department` if needed. Drop `BeneficiaryParty`, or use it only for a
  different party.

### 4. Drinking water as a supply of services (Low)

- **XPath:** `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`
- **Value:** `SERVICES`
- **UBL definition:** *Tax Category. Supply Type Code*: "A code signifying the type of supply to which this tax category applies, such as goods, services, or a mixture."
- **Why it does not fit:** The line sells 14 m³ of drinking water, a metered, tangible
  commodity priced per cubic metre. In common sales-tax and VAT practice, the supply of
  water is a supply of goods (e.g. EU VAT Directive 2006/112/EC, Annex III point 2,
  "supply of water"). The sewage levy on the collection line is a service, so `SERVICES`
  fits there.
- **Suggestion:** `GOODS` for the drinking-water line, unless the world's tax rules
  deliberately treat water as a service. In that case, say so in the tax-category
  text.

### 5. Exemption reason on an "outside scope" category (Low)

- **XPaths:**
  - `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:ID` = `O` ("Services outside scope of tax")
  - `/Invoice/cac:TaxTotal/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `LEVY`, `…/cbc:TaxExemptionReason` = `Levy collected for a public body`
  - The same pair on `/Invoice/cac:CollectionInvoiceLine/cac:Item/cac:ClassifiedTaxCategory`
- **UBL definition:** *Tax Category. Tax Exemption Reason*: "The reason for tax being exempted, expressed as text."
- **Why it does not fit:** Category `O` means the amount is outside the scope of the tax,
  which is a different legal situation from an exemption (category `E`, used correctly on
  the water line). The text itself gives a scope reason (a levy collected for a public
  body), not an exemption.
- **Suggestion:** Keep the category `O`. Phrase the reason as a scope reason ("Not a
  supply by the seller: levy collected for the city"). A code list with separate
  out-of-scope codes would make the difference explicit.

### 6. Penalty terms that the follow-up does not use (Low, cross-document)

- **XPaths:**
  - `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
  - `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `0.58`
  - `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod` (from `2026-04-24`, 1 month)
- **UBL definitions:**
  - *Payment Terms. Penalty Surcharge Percent*: "The penalty for payment after the settlement period, expressed as a percentage of the payment."
  - *Penalty_ Amount*: "The monetary amount of the penalty for payment after the settlement period."
- **Why it does not fit:** The amounts are correct (1.5 % of 38.78 = 0.58). But when this
  invoice is in fact paid late (the direct debit of 23 April is returned),
  [10-Reminder](10-Reminder.xml) charges a flat returned-debit fee of 5.00 and no 0.58
  penalty. The terms announced here are not the ones applied in the same flow.
- **Suggestion:** Either add the 0.58 penalty to the Reminder next to the fee, or state
  the returned-debit fee in these payment terms instead of, or in addition to, the
  percentage.

### 7. A state water utility as a small enterprise (Low)

- **XPath:** `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode`
- **Value:** `SMALL` ("Small enterprise")
- **UBL definition:** *Party Legal Entity. Entity Size Code*: "A code signifying the size category of the legal entity (e.g., micro, small, medium, large)."
- **Why it does not fit:** The supplier is "Coastal State Water Company", the drinking-water
  supplier of a whole state that also collects the capital's sewage levy. That is
  hardly a small enterprise.
- **Suggestion:** `LARGE` (or `MEDIUM`).

### 8. `LocaleCode` holds a language, not a locale (Medium, recurring)

- **XPath:** `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode`
- **Value:** `en` with `@listID="ISO 639"`
- **UBL definition:** *Language. Locale Code*: "A code signifying the locale in which this language is used."
- **Why it does not fit:** The value repeats `Language/cbc:ID`. A locale is a language
  plus a region (e.g. `en-XB`), and ISO 639 is a list of languages.
- **Recurring:** 362 occurrences in 213 examples.

## References checked and consistent

- Arithmetic: 14 m³ × 2.35 = 32.90; 14 m³ × 0.42 = 5.88; line total 38.78 = tax-exclusive
  = tax-inclusive = payable; tax 0.00 in both subtotals.
- The due date 2026-04-23 is the issue date + 21 days, as the payment-terms note says. The
  `PaymentDueDate` values agree.
- [08-UtilityStatement](08-UtilityStatement.xml) refers to this invoice (`CSWC-INV-26-0319`)
  and to meter `CSW-W-71844`. Its readings 1830 → 1844 give the 14 m³ invoiced for
  March 2026. [10-Reminder](10-Reminder.xml) and [11-CreditNote](11-CreditNote.xml)
  refer to this invoice with matching amounts.
- The IBAN check digits of both accounts and the ISO 11649 creditor reference
  `RF46CSWCINV260319` are valid.
- The payee account (water company) and the payer account (customer) are at the same
  bank and branch, which is consistent.
