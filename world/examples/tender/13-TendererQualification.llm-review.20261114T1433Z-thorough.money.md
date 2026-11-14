# LLM review: 13-TendererQualification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/13-TendererQualification.xml`, Git blob `fbf9d6ddac8eb891f81b7a2f593f1db23d28b8d1` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/13#F1 · Medium · Participation 80 % / 20 %, but the subcontractor's part is 3.5 % of the tender
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `80`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `20`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:TendererRoleCode` = `SUBCONTRACTOR`
- Why: `ParticipationPercent` is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage." Saltmere Engineering's part is the installation, which the tender made the same morning prices at `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00` out of `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`, that is 3.48 %; the award documents state it so: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`. The qualification gives no basis on which the subcontractor's share would be 20 %. The share matters because the terms limit subcontracting (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`). Medium rather than High because the definition does not fix the base of the percentage.
- Condition: the participation percentages are the parties' shares of the tender on a stated or evident base and agree with the tender's amounts and the award's subcontract rate (96.5 and 3.5 by value).
- Options: (a, preferred) 96.5 and 3.5; (b) keep 80/20 and say in the note on which base (for example working hours) it is counted, with the award documents using the same base.
- Needs decision: no

### tender/13#F2 · Medium · The financial capability is an amount without a statement of what it is
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ID` = `FC-1`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: the document's purpose is to show that the tenderer meets the published criteria, of which the financial one is a yearly turnover above the threshold (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`). The capability has neither a type code ("Turnover" is one of the examples the definition of `CapabilityTypeCode` gives) nor a description, period or evidence, unlike the technical capability next to it, which at least has a description. 9200000.00 lume could be turnover, equity or a credit line, of any year. The buyer cannot evaluate the criterion from it.
- Condition: the financial capability says that it is the yearly turnover, for which year(s), and names its evidence.
- Options: (a, preferred) add type code, a description such as "Turnover 2025" (or the three years), the period and the accounts as evidence; (b) none seen without these.
- Needs decision: no

### tender/13#F3 · Low · Capability figures differ from the register extract sent to the same buyer
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: two days later the information service's extract on the same company gives a production capability of `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000` pieces and `12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`, for "Steel frame benches…". If the quantities are both the yearly output of benches they contradict each other (4,000 against 6,000); neither document says enough to tell, hence Low.
- Condition: figures for the same measure agree between this qualification and the extract of example 12, or each says what it measures so that the difference is explained.
- Options: (a, preferred) one set of figures, each with its meaning and year, used in both documents; (b) keep both and describe them (benches against all products; turnover against production value).
- Needs decision: yes

### tender/13#F4 · Low · The party's capacity amount repeats the task's total
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:PartyCapacityAmount` = `540000.00`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:TotalTaskAmount` = `540000.00`
- Why: `PartyCapacityAmount` is "A monetary amount corresponding to the financial capacity of the party that carried out this completed task", `TotalTaskAmount` "The actual total monetary amount of this completed task". The capacity of the party (what it could finance or turn over at the time) is a different thing from the value of the task; the same figure in both says nothing about the party and reads as a copy.
- Condition: `PartyCapacityAmount`, if present, is a figure about the party's capacity during the task, with a recognisable source, and not the task's own amount.
- Options: (a, preferred) drop it; the financial capability already describes the party; (b) give the party's turnover in the years of the task.
- Needs decision: no

## Checked and consistent
- Completed task: 540000.00 over 2023-01-01 to 2025-12-31 (three years) gives the annual average of 180000.00.
- 9200000.00 lume, if it is the yearly turnover, is far above the threshold of 250000.00; 4000 benches a year cover the 240 benches of the contract and the 120 of the renewal.
- Amounts are in lume, the currency of the criteria, although the company's capital is in ferra (250000000 XUF; 2.5 million lume at the invoice's rate of 100 to 1).
- 80 + 20 = 100.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:AnnualAverageAmount`: suspected a misuse, since the definition speaks of "The average monetary amount of a task such as this completed task" rather than a yearly average — refuted because the element's name says annual average and the value is exactly the total divided by the three years of the period.
