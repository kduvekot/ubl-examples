# Consistency review: index

Run: `20261114T2143Z-consistency` · Review dates: 2026-11-14 and 2026-11-15
Examples: 250 in 18 flows. The topic files name the commit they reviewed (e8ff272 to 9bdf89a; no example
changed between those commits).

This is the cross-flow consistency review that the per-example reviews
(`world/examples/<flow>/*.llm-review.*.merged.md`) left open: questions that need all examples at
once. It used only the XML examples, the tables built from them
(`.claude/skills/ubl-example-review/scripts/extract_tables.py`), the mechanical checks
(`check_consistency.py`) and the merged per-example reviews. No world data, generators or companion
documentation were read, so every statement can be checked against the documents alone.

Each topic file starts with the world as the documents state it (the rules, timelines and registers),
then its findings, what it checked and found consistent, what it refuted, what became of the
"Outside this review" notes of the per-example reviews, and the questions the documents cannot answer.

## Topics

| Topic | File | High | Medium | Low | Needs decision |
|---|---|---:|---:|---:|---:|
| conditions | `consistency-review.20261114T2143Z-consistency.conditions.md` | 3 | 4 | 5 | 9 |
| timelines | `consistency-review.20261114T2143Z-consistency.timelines.md` | 3 | 2 | 3 | 3 |
| equipment | `consistency-review.20261114T2143Z-consistency.equipment.md` | 0 | 1 | 0 | 1 |
| parties | `consistency-review.20261114T2143Z-consistency.parties.md` | 0 | 1 | 1 | 2 |
| items | `consistency-review.20261114T2143Z-consistency.items.md` | 1 | 0 | 3 | 3 |
| identifiers | `consistency-review.20261114T2143Z-consistency.identifiers.md` | 0 | 3 | 2 | 3 |
| **Total** | | **7** | **11** | **14** | **21** |

All cited XPaths resolve and all 302 quoted values match (`check_xpaths.py`, `check_values.py`).

## Findings

| Finding | Severity | Decision | Title |
|---|---|---|---|
| conditions#F1 | High | no | One price list for Bayvarra, two tax treatments; catalogue territory is always the seller's country |
| conditions#F2 | High | yes | The standard terms IDs do not mean the same number of days everywhere |
| conditions#F3 | High | no | Contract-specific payment terms are never applied |
| timelines#F1 | High | yes | The coordinates put the three countries inside 35 km, against stated distances and travel times |
| timelines#F2 | High | no | One melt of steel is cast on three dates; serial numbers run against manufacture dates |
| timelines#F3 | High | no | Documents report as done what happens after their issue time, or cite documents not yet issued, in ten flows |
| items#F1 | High | yes | The sea export names the March road import as previous declaration for goods made in May |
| conditions#F4 | Medium | yes | The tender contract's tax treatment follows two countries' rules |
| conditions#F5 | Medium | yes | The customs value is built on a different basis in each flow |
| conditions#F6 | Medium | yes | Duties, import taxes and Trade Accord preference are stated nowhere, and claimed once |
| conditions#F7 | Medium | yes | The working week is stated and not kept: 48 documents dated at a weekend |
| timelines#F4 | Medium | yes | Goods "from the distributor's stock" are made days before they leave, and no document moves them |
| timelines#F5 | Medium | yes | The crossing Lumeport to Selanu takes two days, 64 hours or 84 hours |
| equipment#F1 | Medium | yes | 24 bench pallets and a castings pallet are "one full truck" and "one 40-foot container", but fit neither |
| parties#F1 | Medium | yes | Lisavu's capital is "Port Wrenfield" in English addresses and "Selanu" in every other English text |
| identifiers#F1 | Medium | yes | Two parties share the prefix `BF` |
| identifiers#F2 | Medium | yes | Document numbers are one counter per flow shared by all issuers |
| identifiers#F3 | Medium | yes | `ProfileExecutionID` is the flow name in all 250 documents |
| conditions#F8 | Low | yes | Urvania's "service to a business abroad" used for a foreign public body |
| conditions#F9 | Low | no | The XB-STD surcharge is encoded as one month only in all 18 places |
| conditions#F10 | Low | yes | Only Urvania's national tariff appears, also in Bayvarran and Lisavan declarations |
| conditions#F11 | Low | yes | Valdara's distributor price equals its public contract price; a frame price below cost |
| conditions#F12 | Low | yes | Valdara's size class against its headcount and capability |
| timelines#F6 | Low | no | Two flows lodge the export declaration after the goods have left |
| timelines#F7 | Low | no | Sea flow: nothing covers 19 to 21 May |
| timelines#F8 | Low | no | A gas bill cites a metering report issued four hours later |
| parties#F2 | Low | yes | `SMALL` is the default size of every party without its own founding data |
| items#F2 | Low | yes | The bench and its side frame have a different "standard" identity depending on the seller |
| items#F3 | Low | yes | The bench weighs less than its parts as other flows ship them |
| items#F4 | Low | no | `VI-C180-2026` replaces the side frame in one catalogue and the whole bench in a tender |
| identifiers#F4 | Low | no | Identifiers built from file numbers, flow names and other identifiers |
| identifiers#F5 | Low | no | One party, several prefixes; one prefix, several kinds of document |

## Findings that belong together

- **Where the goods are and how far apart places are**: timelines#F1 (map scale), timelines#F4 (stock that
  never arrives), timelines#F5 (crossing time), items#F1 (previous declaration), equipment#F1 (what fits a
  truck and a container), items#F3 (weight of the bench against its parts).
- **Payment terms**: conditions#F2 and conditions#F3, with conditions#F9.
- **Customs**: conditions#F5, conditions#F6, conditions#F10, timelines#F6.
- **Numbering and identity of documents**: identifiers#F1, identifiers#F2, identifiers#F3, identifiers#F4,
  identifiers#F5, timelines#F3.
- **Party master data**: parties#F1, parties#F2, conditions#F12.

## Found consistent

Exchange rates and every amount given in two currencies; tax rates per country; payment rails and
account formats per country; the description of every party (51) and every item apart from language
tags; every party identifier, address ID and account (none shared between parties); all check digits
(502 checks); weights per unit across flows; meter readings in sequence; the gas pipeline's balance;
every vehicle, vessel, wagon and container in one place at a time.

## The "Outside this review" notes

The 250 merged per-example reviews hold 221 such notes. Each has an outcome in a topic file (finding,
refuted, cannot be told, or already a per-example finding): about 100 in timelines, 31 in equipment, 25
in conditions and about 52 in parties, items and identifiers. The identifiers file lists the remaining
notes by number with the reason they are not consistency questions (money, customs, flow composition
or the tender story inside one flow).

## Reproducing the tables and checks

    python3 -I .claude/skills/ubl-example-review/scripts/extract_tables.py --check   # are the tables current?
    python3 -I .claude/skills/ubl-example-review/scripts/extract_tables.py           # build .review/tables/ (not committed)
    python3 -I .claude/skills/ubl-example-review/scripts/check_consistency.py        # mechanical hits
