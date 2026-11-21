# LLM review: 37-GuaranteeCertificate.xml

Flow: tender (PWD/2026/PARKS) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/tender/37-GuaranteeCertificate.xml`, Git blob `28c21ac9323087164cdf852d3ec83861da4556ea` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### tender/37#F1 · Low · Guarantee effective from the day before the certificate was issued
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = `2026-02-18`
- XPath: `/GuaranteeCertificate/cbc:IssueDate` = `2026-02-19`
- Why: `ApplicablePeriod` is "The specified period in the tendering process for which this Guarantee is effective". The guarantee is said to be effective from 18 February, a day before the bank issued the certificate (19 February, 16:19). Nothing in the tendering process happened on 18 February that needed cover (Brackenmere's first tender, `17-Tender.xml`, is dated 20 February), and the other tender guarantee of the flow starts on its own issue date (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = `2026-02-23`, issued 2026-02-23). A start before issue reads as a backdated guarantee unless the story says the bonds were pledged on the 18th.
- Condition: The start of the applicable period is not before the issue date, or the document says what happened on the start date (e.g. the pledge of the bonds) that makes the guarantee effective then.
- Options: (a) preferred: start the period on the issue date, 2026-02-19, as in 14; (b) keep 18 February and state in the purpose that the bonds were deposited and pledged that day.
- Needs decision: no

### tender/37#F2 · Low · Number of bonds given as a number of shares
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `25`
- XPath: `/GuaranteeCertificate/cbc:Purpose` = `Guarantee of Brackenmere Furniture's tender in the bench procedure, given by pledging Bayvarran government bonds deposited with the bank.`
- Why: `SharesNumberQuantity` is "The number of shares immobilized". The purpose and the ISIN describe government bonds, which are debt securities, not shares. The element is the only count in `ImmobilizedSecurity`, so the value is understandable, but it states a number of shares where there are none.
- Condition: Either the count element is used for bonds by a recorded decision (and the finding is recorded for the UBL TC as a gap in the model), or the number of bonds is given elsewhere (e.g. in the purpose) and the shares element is left out.
- Options: (a) preferred: keep the element and record the gap (UBL has no neutral "number of securities" in `ImmobilizedSecurity`), since the count matters for identifying the pledged lot; (b) leave it out and rely on face and market value.
- Needs decision: no

## Checked and consistent
- Liability 2 500.00 XBL, type TENDER and the constitution by pledged government bonds agree with the requirement in `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee[1]/cbc:LiabilityAmount` = `2500.00` and its description; the note on release at contract signature repeats that description.
- The certificate (ID 3900039354) is the one referred to by both of Brackenmere's tenders, `17-Tender.xml` and `19-Tender.xml`, and was issued before either; the period end 2026-05-26 is the same as in 14.
- `FaceValueAmount` 2 632.50 is "the value of the security on the day it was immobilized" (UBL definition), market value 2 640.00 today; both exceed the liability of 2 500.
- `IssuerParty` is "the Party who issues the Immobilized Security Certificate": the guarantor bank, which holds the bonds in deposit, fits.
- ISIN XB0000260313 and the GLN of Brackenmere pass `check_ids.py`; XB is a user-assigned ISO 3166 code, so the ISIN cannot clash with a real one.

## Considered and refuted
- `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Bank of Lumeport`: government bonds issued by a bank — refuted because the definition makes this the issuer of the immobilization certificate, not of the bonds.
- `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` = `2632.50`: a face value that is not a round nominal (25 bonds) — refuted because UBL defines the element as the value on the day of immobilization, not the nominal.
