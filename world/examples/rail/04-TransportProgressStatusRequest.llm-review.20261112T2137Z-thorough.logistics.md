# LLM review: 04-TransportProgressStatusRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/04-TransportProgressStatusRequest.xml`, Git blob `1fc0afc119b31bbce07b12c53077e4e7f9cd7e51` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### rail/04#F1 · Low · The train asked about is identified only by its timetable service
- XPath: `/TransportProgressStatusRequest/cac:TransportMeans/cbc:JourneyID` = `CT 4471`
- Why: TransportMeans here is "the transport means by which the current transport service is effectuated and for which status is requested", but JourneyID is "an identifier for the regular service schedule of this means of transport" — the timetable service, which runs on other days too. The train itself is identified elsewhere in the flow (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RailTransport/cbc:TrainID` = `FRC 4417`). The request only works because its issue date happens to be the departure day; it names neither the train nor the day.
- Condition: The request identifies the specific train run, by TrainID (in `cac:RailTransport`) or by the journey together with its date.
- Options: (a) preferred: add `cac:RailTransport/cbc:TrainID` = FRC 4417 next to the JourneyID, as the waybill does; (b) add a status period or reference to the plan FRC-TEP-26-0328.
- Needs decision: no

## Checked and consistent
- The response rail/05 references this request (FRC-DOC-26-0329) and answers for the same journey CT 4471 and status location.
- Issue time 06:30 lies before the planned departure 06:45 (rail/03) and before the response at 06:45.
- Status location Ferrano Intermodal Hub is the departure point of the train (rail/08 actual departure location).

## Considered and refuted
- `/TransportProgressStatusRequest/cbc:Note[2]` = `Has the container train left?`: asked at 06:30, a quarter of an hour before the planned departure, the question seemed premature — refuted: a carrier may ask for the status shortly before departure, and the answer is dated later; the problems with that answer are in rail/05.
- `/TransportProgressStatusRequest/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`: a status location without an identifier — refuted: the name is unambiguous in the flow, and no other example identifies the hub by UN/LOCODE or GLN as a status location.
