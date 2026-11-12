---
name: ubl-example-review
description: Semantic review of the generated UBL 2.5 examples in world/examples against the UBL 2.5 model (UBL-Entities-2.5.gc). Checks whether each value fits the meaning of its element, its parent aggregates and the document, whether values are consistent with each other and with the documents they refer to, and writes NN-DocumentType.llm-review.md next to each example that has findings. Use when asked to review one example, a flow, or all examples. Not for fixing the examples, and not for the cross-flow consistency review (timelines, capacity, equipment locations).
argument-hint: "[<flow>/<NN-DocumentType> | <flow> | all]"
---

# Semantic review of the generated UBL examples

Arguments: `$ARGUMENTS`

## 0. Without arguments: explain and stop

If no arguments were given, do not review anything. Reply with this explanation, then the list of
flows with their number of XML examples and their number of existing `*.llm-review.md` files
(`world/examples/<flow>/`), and ask what to review:

> This skill reviews the generated UBL 2.5 examples in `world/examples/`. For each example it
> checks whether every value fits the meaning UBL 2.5 gives the element (in the context of its
> parent aggregates and the document), whether values contradict each other, and whether
> references to other examples resolve and make sense. Findings go into
> `NN-DocumentType.llm-review.md` next to the example; examples without findings get no file.
> Patterns found in many examples go into `world/examples/recurring.llm-review.md`.
>
> Usage:
> - `/ubl-example-review rail/07-TransportationStatus`: one example (e.g. to re-review after a fix)
> - `/ubl-example-review rail`: every example of one flow
> - `/ubl-example-review all`: every flow, one subagent per flow
>
> The review does not change the examples. Fixing them, and the separate consistency review across
> documents and flows (timelines, capacity, where equipment is), are separate tasks.

## 1. Inputs: what you may and may not use

Use:
- The XML example under review.
- The other XML examples (`world/examples/*/*.xml`), only where the example under review refers to
  them or shares a party, consignment, shipment, item or other object with them.
- The UBL 2.5 semantic model `UBL-Entities-2.5.gc` and the UBL 2.5 default code lists. The scripts
  download them from docs.oasis-open.org and verify the model's SHA-256.
- The code lists in `world/codelists/`, only to read what a code means.
- Your own knowledge of the standards involved (UBL, UN/CEFACT, ISO, IMO, IATA, IHR, tax practice,
  etc.). Say so when a finding rests on it.

Do not use:
- The companion `.md` files next to the XML, or any other documentation of the examples. When you
  search, restrict the search to `*.xml` (e.g. `grep --include='*.xml'`, or Grep with `glob: "*.xml"`).
- The generator (`tools/`) or the world data (`world/*.json`).

## 2. Tools

The scripts are in `.claude/skills/ubl-example-review/scripts/`. Run them with `python3 -I`; they
need `lxml`.

- `annotate.py <example.xml>`: every element, indented, with its value, the UBL 2.5 definition in
  its parent's context (printed at its first occurrence) and the meaning of codes and of
  `unitCode`/`currencyID`. `--hide-party-detail` collapses addresses, tax schemes, legal entities,
  contacts, languages and electronic addresses for a first read; read them afterwards in full.
  `--full` prints absolute XPaths on every line, to cite in the review. `!! NOT IN MODEL` and
  `?? NOT IN LIST` mark elements or codes to look at.
- `flow_index.py <flow>`: per example its type, ID, issue date and time, top-level parties, and the
  IDs it references, resolved to the example whose document ID they are (`-> ?` when none).
- `check_ids.py <example.xml>`: check digits of GS1 keys, ISIN, IBAN-like accounts, RF references
  and ISO 6346 container numbers.
- `check_xpaths.py <review.md> …`: every XPath cited in a review resolves in its example.

The scripts help you read; the judgement is yours. Read the XML itself wherever the listing is not
enough.

## 3. Method

For one flow:

1. Run `flow_index.py <flow>` and keep the index in mind: it is the context for the references.
2. Review the examples one at a time, in order. For each: run `annotate.py` and `check_ids.py`,
   read the result and the XML, open the referenced examples where needed, write the review (or
   decide there are no findings), and run `check_xpaths.py` on it. Do not keep the full listing of
   earlier examples in mind; the index and your findings are enough.
3. At the end, update `world/examples/recurring.llm-review.md` (section 6).

For `all`: run one subagent per flow, each following these instructions for its flow and given the
current recurring patterns. Subagents do not write `recurring.llm-review.md`; they report new
recurring patterns and their occurrence counts. Afterwards, update that file yourself and give the
user a summary per flow.

## 4. What to check

For every element in the example:

1. **The element itself.** Does the value fit the UBL definition of the element in its parent's
   context? The same element name can mean different things under different parents; use the
   definition the listing prints for that parent.
2. **Parent and grandparent.** Does the value fit what the parent aggregate is (a consignee is not
   a buyer, main carriage is not pre-carriage, a payer is "if different from the debtor") and the
   aggregate above it?
3. **The document.** Does it fit the purpose of the document type (its UBL definition) and the
   intent of this example (its type codes, notes and descriptions)? Report missing information only
   where the document's purpose depends on it (e.g. a pre-arrival report without an arrival time).
4. **Internal consistency.** Values must not contradict each other: dates and times and their order,
   quantities, amounts and their arithmetic, units, parties and their roles, codes and their text
   equivalents, repeated renderings in several languages and their `languageID`.
5. **References.** A reference to another document must resolve to an existing example, with
   matching ID, parties and content, and that example must make sense as the thing referred to. An
   identifier of one kind (e.g. a consignment ID) must not be used as another (a document or order
   number). The same object (party, consignment, container, vehicle, item) must be described the
   same way as in the other examples of the flow.
6. **Physical plausibility within the example.** Quantities must fit their packages, packages their
   handling units, weights and dimensions their goods. Timelines, capacities and locations across
   documents and flows belong to the separate consistency review; note them under "Checked and
   consistent" only if you happen to verify them.
7. **Check digits and real codes.** Run `check_ids.py`. A wrong check digit is a finding.

The examples are set in a **fictional world**: invented countries, currencies, languages, parties
and identifier schemes. Accept them as given. Flag a value only when it clashes with a real
standard: a real code used with a different meaning, a real organisation, or a wrong check digit.

Verify every claim before you write it: look the value up, do the arithmetic, open the referenced
example. If you are unsure, say so in the finding.

## 5. Severity, condition, options, decision

- **High**: a contradiction with another value in this example or in a referenced example, or a
  broken reference.
- **Medium**: the element carries a meaning other than its UBL definition.
- **Low**: plausibility, consistency or completeness remark.

Do not prescribe one fix as the only right one. State:
- **Condition**: what must be true after the fix, phrased so it can be checked against the XML.
- **Options**: the directions you see, with your preference and the reason. The fixing session
  decides how to get there (it may find a better way).
- **Needs decision: yes** when resolving the finding changes the story of the example, not only its
  encoding: adding or removing a document in a flow, changing who a party is, a judgment on tax
  treatment or the like. Otherwise **no**.

## 6. Output

Write a review only for an example with findings. Name it after the XML, in the same folder:
`NN-DocumentType.xml` → `NN-DocumentType.llm-review.md`. Re-reviewing replaces the file.

XPaths are absolute, with `cac:`/`cbc:` prefixes, the root element without prefix, and position
predicates (`[2]`) where an element repeats. A finding may cite elements of another example by its
file name and XPath. Cite values exactly.

### Document review

```
# LLM review: NN-DocumentType.xml

Flow: <flow> (<ProfileExecutionID>) · Review date: <YYYY-MM-DD> · Basis: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
Resolve each finding so that its condition holds. Findings marked "Needs decision: yes" are
confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the
world's code lists. This review only describes what is wrong; it does not say where or how the
example is produced.

## Findings

### <flow>/<NN>#F<n> · <High|Medium|Low> · <short title>
- XPath: `<absolute XPath>` = `<current value>`   (one line per element involved)
- Why: <one paragraph: the UBL definition, quoted, and why the value does not fit; references to
  other examples by file name and XPath>
- Condition: <what must be true afterwards>
- Options: <directions; preferred one marked, with the reason>
- Needs decision: yes | no

## Recurring patterns
- R<n> <name>: `<absolute XPath>`   (one line per occurrence in this example)

## Checked and consistent
- <what you verified and found correct, especially references, arithmetic and check digits>
```

Number findings in order of severity, then of position in the document. Keep "Why" to what a reader
needs to understand the problem.

### Recurring patterns

`world/examples/recurring.llm-review.md` describes each pattern found in several examples once:

```
### R<n> · <severity> · <name>
- Element: <element and parent aggregate, e.g. Language/cbc:LocaleCode>
- Typical value: `<value>`; occurrences: <count> in <number> examples (<how you counted>)
- Why: <as for a finding>
- Condition / Options / Needs decision: <as for a finding>
```

Before creating a new pattern, check the existing ones. Count occurrences over all `*.xml` examples.
A document review lists only its own occurrences under the pattern's ID.

## 7. Before you finish

- `check_xpaths.py` passes for every review you wrote.
- Every referenced example you name exists, and every value you quote is in the XML.
- Report to the user: the examples reviewed, how many got a review, the number of findings by
  severity, new recurring patterns, and anything you could not check.
