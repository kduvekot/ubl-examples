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
> Patterns found in many examples are described once in `world/examples/recurring.llm-review.md`.
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
- The other XML examples (`world/examples/*/*.xml`), where the example under review refers to them
  or shares a party, consignment, shipment, item, account, mandate or other object with them.
- The UBL 2.5 semantic model `UBL-Entities-2.5.gc` and the UBL 2.5 default code lists. The scripts
  download them from docs.oasis-open.org and verify the model's SHA-256.
- The code lists in `world/codelists/`, only to read what a code means.
- `world/examples/recurring.llm-review.md`, the register of recurring patterns (section 7).
- Your own knowledge of the standards involved (UBL, UN/CEFACT, ISO, IMO, IATA, ADR, IHR, ATA,
  tax practice, etc.). Say so when a finding rests on it.

Do not use:
- The companion `.md` files next to the XML, or any other documentation of the examples. Every
  search and every count is over `*.xml` only (e.g. `grep --include='*.xml'`, or Grep with
  `glob: "*.xml"`). The `.md` files repeat the XML values, so a search without that filter counts
  them twice.
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

### One example: three passes

1. **Elements.** Run `annotate.py` and `check_ids.py`. Go through the listing top to bottom and
   apply section 4 to every element and every aggregate, using the checklist in section 5 for each
   aggregate type you meet. Note candidate findings with their XPaths.
2. **References and shared objects.** For every reference in the example (`flow_index.py` lists
   them) open the referenced example and compare: does it exist, is it the kind of document the
   reference element means, do its parties, dates, quantities and amounts agree with this example?
   For every object this example shares with other examples of the flow (parties, consignments,
   containers, items, accounts, mandates, meters), compare how they describe it. Look specifically
   for statements that contradict each other (one document says paid on account, the other bills
   the full amount; one says not stamped, the other stamped).
3. **Refute.** For every candidate finding, try to prove it wrong before you keep it: re-read the
   value, the definition and the referenced example; redo the arithmetic; consider whether the
   value is a legitimate reading of the definition. Drop it if it does not survive, and lower its
   severity if it only partly does. Then compare the remaining findings with the register (section
   7): an occurrence of a registered pattern is listed under its ID, not as a finding.

Then write the review (section 8), or decide there are no findings, and run `check_xpaths.py` on it.

### One flow

Run `flow_index.py <flow>` first and keep the index in mind as the context for references. Review
the examples one at a time, in order. Do not keep the full listing of earlier examples in mind; the
index and your findings are enough.

### Several flows (`all`)

1. **Register first.** Before any review, make sure `world/examples/recurring.llm-review.md`
   exists and is current: search the XML examples for the patterns it lists and for new ones
   (section 7), recount every pattern, and update the file. This is done once, by you, not by the
   subagents.
2. **Reviews.** Run one subagent per flow. Each follows these instructions for its flow, reads the
   register but does not write it, uses the registered IDs, and reports candidate new patterns
   (with examples and a count) in its final report.
3. **Afterwards.** Add accepted new patterns to the register, add their occurrences to the reviews
   concerned, and give the user a summary per flow.

## 4. What to check

For every element in the example:

1. **The element itself.** Does the value fit the UBL definition of the element in its parent's
   context? The same element name can mean different things under different parents; use the
   definition the listing prints for that parent. Watch for definitions with conditions ("if
   different from the debtor", "assigned by the seller", "within the validity period").
2. **Parent and grandparent.** Does the value fit what the parent aggregate is (a consignee is not
   a buyer, main carriage is not pre-carriage) and the aggregate above it?
3. **The document.** Does it fit the purpose of the document type (its UBL definition) and the
   intent of this example (its type codes, notes and descriptions)? Report missing information only
   where the document's purpose depends on it (a pre-arrival report without an arrival time, a
   transport request that does not say what is to be carried).
4. **Internal consistency.** Values must not contradict each other: dates and times and their order,
   quantities, amounts and their arithmetic (including factor × base = value), units, parties and
   their roles, codes and their text equivalents, repeated renderings in several languages and their
   `languageID`, territory against tax treatment, indicators against the text that explains them.
5. **References.** See pass 2. An identifier of one kind (a consignment ID) must not be used as
   another (a document number, an order number, a shipping order).
6. **Physical plausibility within the example.** Quantities must fit their packages, packages their
   handling units, weights and dimensions their goods (e.g. stated dimensions against the stated
   pallet or container). Timelines, capacities and locations across documents and flows belong to
   the separate consistency review; note them under "Checked and consistent" or "Outside this
   review" only.
7. **Check digits and real codes.** Run `check_ids.py`. A wrong check digit is a finding.

The examples are set in a **fictional world**: invented countries, currencies, languages, parties
and identifier schemes. Accept them as given. Flag a value only when it clashes with a real
standard: a real code used with a different meaning, a real organisation, or a wrong check digit.

## 5. Checklist per aggregate type

Go through these whenever the aggregate occurs. They are the questions earlier reviews found
answers to most often; they do not replace section 4.

- **Party in a role** (Sender, Receiver, Buyer, Seller, Consignee, Carrier, Authority, Payer, …):
  is this the right party for the role in this document? Does its `Contact` fit the role (a
  consignee's contact receives goods, a buyer's contact buys, a carrier's contact handles
  transport, an authority's contact is reachable when ships or goods arrive)? Do job title,
  department and name agree with each other?
- **Party legal entity and tax scheme**: does the description fit the kind of party (a public body
  or a department is not a company in a commercial register and has no liquidation status; size
  fits what the party is)? Is a tax exemption reason the party's own status, not a transaction?
- **Address**: each part in its element (a province in `CountrySubentity`, not `Region`; a gate or
  dock is not a street name; a postal address holds nothing that only matters for vehicles); each
  repeated rendering in the language its `languageID` names; the same address of the same party
  described the same way as in the other examples.
- **Location**: the name is the place, not the company; identifiers (UN/LOCODE, GLN) where the same
  place is identified elsewhere.
- **Identifiers and references**: every ID is the kind of identifier its element names; every
  document reference points to a document that exists, of the right kind; a reference with only an
  ID says what it refers to where that is not obvious.
- **Transport events and stages**: each event is in the stage it belongs to (pre-carriage, main
  carriage, on-carriage), uses the dedicated element where one exists (loading, departure, arrival,
  pickup, delivery), is placed correctly in time relative to the issue time (an "actual" event is
  in the past, an estimate is not stale), and has a location or type where it would otherwise be
  meaningless.
- **Goods, packages, handling units, equipment**: description, counts, weights and dimensions agree
  with each other and with the referenced documents.
- **Amounts, prices, taxes, allowances**: arithmetic; tax category against exemption reason and
  territory; allowance or charge conditions that can actually be met.
- **Payment means, mandates, terms**: the parties' accounts are the right ones; mandate limits
  against validity period and frequency; payer only if different from the debtor; terms against
  what follow-up documents do; payments on account against amounts billed.
- **Codes**: the code's meaning (from the listing) fits the element; a code from a list meant for
  another element is a finding.
- **Free text**: notes and descriptions agree with the structured values next to them.

## 6. Severity, condition, options, decision

- **High**: a contradiction with another value in this example or in a referenced example, or a
  broken reference. Examples: a referenced document that does not exist; arithmetic that does not
  hold; an indicator that contradicts the text that explains it; a statement in one example that
  another example of the flow contradicts.
- **Medium**: the element carries a meaning other than its UBL definition. Examples: a province in
  `Region`; a consignment ID in `ShippingOrderID`; a code from another element's list; `PayerParty`
  equal to the debtor; a language code in `LocaleCode`.
- **Low**: plausibility, consistency or completeness remark. Examples: a contact that does not fit
  the role; a party described with an implausible size; missing details the document could carry.

Do not prescribe one fix as the only right one. State:
- **Condition**: what must be true after the fix, phrased so it can be checked against the XML.
- **Options**: the directions you see, with your preference and the reason. The fixing session
  decides how to get there (it may find a better way).
- **Needs decision: yes** when resolving the finding changes the story of the example, not only its
  encoding: adding or removing a document in a flow, changing who a party is, a judgment on tax
  treatment or the like. Otherwise **no**.

## 7. Recurring patterns

`world/examples/recurring.llm-review.md` is the register of patterns that occur in several
examples. Each is described once there, with an ID that never changes or gets reused:

```
### R<n> · <severity> · <name>
- Element: <element and parent aggregate, e.g. Language/cbc:LocaleCode>
- Typical value: `<value>`; occurrences: <count> in <number> examples, counted <date>
- How counted: <the exact search over *.xml, so it can be repeated>
- Why: <as for a finding>
- Condition / Options / Needs decision: <as for a finding>
```

A pattern goes into the register when the same problem occurs in at least three examples. A
document review lists only its own occurrences under the pattern's ID. When reviewing one example
or one flow, do not add patterns to the register; report candidates to the user instead.

## 8. Review file

Write a review only for an example with findings or occurrences of registered patterns. Name it
after the XML, in the same folder: `NN-DocumentType.xml` → `NN-DocumentType.llm-review.md`.
Re-reviewing replaces the file.

XPaths are absolute, with `cac:`/`cbc:` prefixes, the root element without prefix, and position
predicates (`[2]`) where an element repeats. A finding may cite elements of another example by its
file name and XPath. Cite values exactly.

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

## Outside this review
- <problems noticed in other examples or across documents and flows, for the consistency review>
```

Number findings in order of severity, then of position in the document. Keep "Why" to what a reader
needs to understand the problem.

## 9. Before you finish

- `check_xpaths.py` passes for every review you wrote; paths into other examples are checked
  against those examples.
- Every referenced example you name exists, and every value you quote is in the XML.
- Every count is over `*.xml` only and states how it was made.
- Report to the user: the examples reviewed, how many got a review, the number of findings by
  severity, candidate new patterns, and anything you could not check.
