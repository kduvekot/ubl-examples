# LLM review: 17-BusinessInformation.xml

Flow: contest (PWD/2026/PROM-DC) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/contest/17-BusinessInformation.xml`, Git blob `7abfc2496c062952dd656666e2d136da73d0979c` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 829f9c48 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### contest/17#F1 · Low · The capability is typed as production, but it describes installation services
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:Description` = `Design and permits of telecom mast sites; installation of back-up power, safety equipment and ground foundations, with its own crews: the yearly value of its services in 2025, from the accounts filed for that year.`
- Why: The description gives the yearly value of Saltmere's services (design, permits, installation with its own crews), and its industry code is civil engineering (`4290`); it produces nothing. The world's BusinessCapabilityTypeCode list has `INSTALLATION` beside `PRODUCTION`; the code and the text next to it disagree. In 13-BusinessInformation.xml `PRODUCTION` fits Brackenmere, which makes furniture in its own workshop.
- Condition: the capability type code names the kind of capability the description states.
- Options: (a) preferred: `INSTALLATION`, which matches "installation … with its own crews"; (b) keep `PRODUCTION` and describe a production capability, which Saltmere does not have.
- Needs decision: no

## Checked and consistent
- Sender, receiver, notice type, subtype and the procurement-file reference `PWD/2026/PROM-DC` (also the ProfileExecutionID) agree with 13-BusinessInformation.xml, the extract for the lead member issued the same day.
- Saltmere's register number, registration date 1994-10-03, size `SMALL` and legal form agree with every other example that carries the party (counted with `grep` over `*.xml`).
- "No exclusion grounds recorded" agrees with the member's statements in 06 and 11 (no conviction; no taxes or contributions unpaid).
- Saltmere is the second member of the group "Brackenmere and Saltmere design team" in 06 and 11, which explains why the contracting authority receives an extract for it.
- The bid-office contact fits a tenderer.

## Considered and refuted
- `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `5400000.00` refers to 2025, while 13's extract of the same morning uses Brackenmere's 2024 accounts — refuted: each extract gives the latest accounts the company has filed, and companies file at different times.
- `/BusinessInformation/cbc:VersionID` absent, while 13 has version 1 — refuted: a version number is needed only when a second version follows (14 replaces 13); none follows for Saltmere.
