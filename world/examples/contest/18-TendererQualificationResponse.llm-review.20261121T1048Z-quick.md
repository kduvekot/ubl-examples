# LLM review: 18-TendererQualificationResponse.xml

Flow: contest (PWD/2026/PROM-DC) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/contest/18-TendererQualificationResponse.xml`, Git blob `894c5b61347c57212d252456d21e457655cde66d` (committed)
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

### contest/18#F1 · Low · The exclusion does not say which request to participate it decides on
- XPath: `/TendererQualificationResponse/cbc:Note` = `Your request to participate in the design contest cannot be admitted.`
- XPath: `/TendererQualificationResponse/cac:QualificationResolution/cbc:Resolution` = `Excluded at the selection of the participants.`
- Why: A TendererQualificationResponse notifies "an economic operator whether it has been admitted to or excluded from the tendering process". Fernhollow Studio appears in no other example of the flow (`grep -l` over `*.xml`: this file only), and the response carries no reference to Fernhollow's request to participate (its number or date) or to the evidence it rests on (the social security certificate). The contracting folder identifies the contest, but not the application being rejected; for an exclusion that can be appealed within ten days, the operator and the review board need to know which submission and which certificate are meant.
- Condition: the response identifies the request to participate it decides on (by reference or by date), and preferably the certificate cited in the exclusion reason.
- Options: (a) preferred: an AdditionalDocumentReference to Fernhollow's request to participate (and one to the certificate), without adding an example; (b) name the request's date of receipt in the resolution text.
- Needs decision: no

## Checked and consistent
- ContractFolderID and ProfileExecutionID `PWD/2026/PROM-DC` and the contract name "Design of the harbour promenade bench" agree with the contract notices 03 and 08 and with 17.
- Timing: excluded on 2026-05-12, after the closing date for requests in 08 (2026-04-30) and after the register extracts of 2026-05-05 (13, 17), before the design deadline (2026-06-12) and the award (16, AwardDate 2026-06-26); ResolutionDate equals the issue date.
- The appeal period: DurationMeasure 10 days and the text "within ten days of this notice" agree; the appeal body is a public body distinct from the contracting authority, with its own address and registry contact.
- The exclusion reason is a ground the flow's other documents test (06 and 11: "no taxes or social security contributions due and unpaid").
- Sender's party data agree with the other documents of the contracting authority.

## Considered and refuted
- `/TendererQualificationResponse/cac:QualificationResolution/cbc:AdmissionCode` = `REJECTED` while the definition speaks of an indicator "(true)/(false)" — refuted: the element is a code in UBL 2.5, and the definition text is a leftover from an indicator; the world list's `REJECTED` is the right kind of value.
- `/TendererQualificationResponse/cac:QualificationResolution/cbc:ExclusionReason`: "Public Procurement Act, art. 57" has the article number of the exclusion grounds in a real procurement directive — refuted as a finding: it is cited as an act of the world, and an article number alone is not a real reference.

## Outside this review
- Whether Fernhollow's request belongs among the requests counted in 15/16 (four designs received) is a question of the flow's numbers across documents.
