# Minimal UBL 2.5 examples

A minimal but meaningful example document for each of the 101 UBL 2.5 document types: 93 endorsed types and the 8 types deprecated in UBL 2.5. The set is independent of the rest of this repository.

## Contents

| Path | What it is |
|---|---|
| `layer1/<DocType>.xml` | the example documents (the 8 deprecated types are in `layer1/deprecated/`) |
| `layer1/<DocType>.md` | for each example: every value, why the element is present and why it has this value |
| `gen_minimal.py` | the generator; every decision and its reason is a comment in it |
| `ubl-findings.md` | findings on UBL 2.5 itself, for the OASIS UBL TC |
| `*.llm-review.*.md` | the independent reviews the set went through (three rounds and a final check) |

The examples and their `.md` files are generated. Never edit them by hand; change the generator and regenerate.

## What "minimal" means here

Each document contains:

- the elements and attributes its schema requires;
- what the document needs to fulfil its own UBL definition (UBL 2.5 §4.4, IND5 and IND6, applied to the document as a whole), for example an invoice's customer or a response's answer;
- party identification (layer 1, built on that minimal layer 0).

Nothing is added only because it would be nice to have. Each element is used according to its UBL definition (§4.7, §7.2).

## Conventions

- **Unrelated documents:** no document refers to another document in the set. References point outside it, and identifiers and party names are unique across the set.
- **Locale:** each document has one locale (country, currency, language and time zone), assigned by turns in alphabetical order: US, DE, JP, IN, BR and ZA. No document mixes countries.
- **Languages:** texts and names are in the locale's language, in Latin script, with `languageID` `en`, `de`, `pt-BR` or `ja-Latn-hepburn`. Independent human translators checked them.
- **Dates and times:** dates count from D = 2026-08-12, the publication date of the UBL 2.5 OASIS Standard, with offsets that fit each date's meaning. Times are 09:30 local time, with the locale's UTC offset.
- **Codes:** codes use UBL's default code lists where UBL has one. Otherwise they are descriptive values in UBL's own style, without `listID`; no UN/EDIFACT lists are used.
- **Amounts and quantities:** amounts and quantities are plausible for each document, round, and use the currency's minor unit. Amounts in a document add up.
- **Fictitious parties:** every party identifier is provably not a real registration:

| Scheme | Source of the value |
|---|---|
| GLN | GS1 Prefix 952, reserved for demonstrations |
| LEI | prefix 9999, not in the GLEIF register |
| D-U-N-S | Dun & Bradstreet's official test numbers ([docs.dnb.com](https://docs.dnb.com/direct/2.0/en-US/duns-testing)) |
| JP Corporate Number | not in the National Tax Agency's register |
| DE VAT | invalid in the EU's VIES register |
| BR CNPJ | not found in the Brazilian register, via BrasilAPI |
| US EIN, ZA VAT | deliberately invalid: an unassigned prefix, and a failing check digit |

  Schemes vary with the party's role, so that none dominates. `schemeID` holds the ISO/IEC 6523 code of the scheme.

## Regenerate and check

```bash
python3 minimal/gen_minimal.py
```

The generator downloads the UBL 2.5 package from OASIS into `minimal/.ubl/` (not committed). It writes the examples and their `.md` files, then checks every document:

- against the XSD (the endorsed schemas for endorsed types);
- against UBL's default code lists, with the package's own XSLT and Saxon;
- against the UBL 2.5 chapter 4 rules IND1 to IND9;
- for placeholder values;
- for references within a document that do not resolve.

It exits with status 1 and lists every violation if a check fails. To check other files:

```bash
python3 minimal/gen_minimal.py --check FILE...
```

Requirements: Python 3 with lxml, and Java for the code-list check.
