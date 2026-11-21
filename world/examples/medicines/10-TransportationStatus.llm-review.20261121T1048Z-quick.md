# LLM review: 10-TransportationStatus.xml

Flow: medicines (BYF-TX-26-3169) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/10-TransportationStatus.xml`, Git blob `bab549e6084dd103c311f7df971d54c7bf4674f9` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
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

### medicines/10#F1 · Low · "Reply only if the delivery slot must change" in an acceptance report to the carrier
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: `OtherInstruction` is "an instruction regarding this message". The terminal operator reports to the airline that it has accepted the consignment for the flight; there is no delivery slot between them in this report, and the airline's reply would be about loading the flight, not a delivery slot. The same text is in `12-TransportationStatus.xml`, from another terminal to the forwarder, which suggests a fixed text.
- Condition: the instruction, if present, is one the receiver of this report can act on.
- Options: (a, preferred) leave it out; (b) an instruction that fits acceptance (e.g. to report a different loading position).
- Needs decision: no

## Checked and consistent
- Times: acceptance at 05:30 −01:00 (06:30 UTC), report at 05:40; the van was to arrive by 05:30 (`06-ForwardingInstructions.xml`); the container log in `12-TransportationStatus.xml` shows 5.6 °C at 06:30 UTC, as reported here.
- Consignment `QLM-CS-26-3980` and carrier Kelaro Air Cargo agree with `11-Waybill.xml`; the waybill is issued after the acceptance (06:45 +00:00 = 05:45 −01:00).
- Location `XBLMA` and the terminal operator's physical location are the same airport.

## Considered and refuted
- `/TransportationStatus/cbc:ShippingOrderID` = `QLM-FI-26-2388`: the consignor's forwarding instructions quoted as a shipping order — refuted, the forwarding instructions are the shipping order of this consignment, and the waybill quotes the same reference.
