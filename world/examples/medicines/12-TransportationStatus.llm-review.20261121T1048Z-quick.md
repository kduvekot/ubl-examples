# LLM review: 12-TransportationStatus.xml

Flow: medicines (BYF-TX-26-3169) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/12-TransportationStatus.xml`, Git blob `d55467b1d42e617504afb34ac2ee0e7230855c3e` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### medicines/12#F1 · Low · An indicator set to true without saying what it indicates
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:IndicationIndicator` = `true`
- Why: `Status/IndicationIndicator` "specifies an indicator relevant to a specific status"; its meaning comes only from the context. Nothing in the status (condition code, descriptions) says what is true: that a temperature log is attached, that the cold chain held, or something else. A true indicator whose meaning must be guessed is a value without a stated business reason (IND5).
- Condition: either the meaning of the indicator is stated in the status (for example in its description or reason), or the indicator is absent.
- Options: (a, preferred) leave it out; the attached log and the condition already say that the cold chain held; (b) state in `CurrentStatus/cbc:StatusReason` what the indicator means.
- Needs decision: no

### medicines/12#F2 · Low · "Reply only if the delivery slot must change" with no delivery slot in the report
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: as in `10-TransportationStatus.xml` (medicines/10#F1): the arrival report names no delivery slot to the hospital that the forwarder could change.
- Condition: the instruction, if present, refers to something the report states (e.g. a planned delivery time to the consignee).
- Options: (a, preferred) leave it out; (b) state the planned delivery slot at the hospital in the report.
- Needs decision: no

## Checked and consistent
- Temperature log: 25 readings at 15-minute intervals from 05:00 to 11:00 UTC; minimum 4.4, maximum 5.8, last 5.6 °C, as in the condition; within 2 to 8 °C; 5.6 °C at 06:30 UTC matches the acceptance report `10-TransportationStatus.xml`; the log starts at 04:00 −01:00, before collection at the wholesaler at 04:15 (`06-ForwardingInstructions.xml`).
- Arrival at 10:45 +00:00 = the waybill's planned arrival; report issued 11:05, after the last reading.
- `/TransportationStatus/cac:DocumentReference/cbc:ID` resolves to `11-Waybill.xml`; the attachment's file name carries the container number `RKN20871K0` of the waybill.
