# LLM review: 04-ExpressionOfInterestRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/04-ExpressionOfInterestRequest.xml`, Git blob `1ca94275bd6d396987ad7aa46080a104842bb2c3` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/04#F1 · Medium · A language code in `LocaleCode`
- XPath: `/ExpressionOfInterestRequest/cbc:PreferredLanguageLocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. `PreferredLanguageLocaleCode` ("a code signifying the locale in which the language in the required documents is preferred") has the same problem: `en` from "ISO 639" is a language, not a locale. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/04#F2 · Low · The sawmill is "consortium lead" with a 60 % share of a consortium that has no other member yet
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:ParticipationPercent` = `60`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Supplies the slats; a bench maker would build the benches.`
- XPath: `/ExpressionOfInterestRequest/cbc:Note` = `The sawmill considers a tender for lot 1 with a bench maker and asks to follow t…`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`
- Why: `ParticipationPercent` is "the extent to which this party is expected to participate in the tendering process, expressed as a percentage", `EconomicOperatorRole` "the role of the party in a tender consortium". The note and the role description say that the sawmill only *considers* tendering with "a bench maker" that is not named and may not exist yet. A share of 60 % and the role of lead presuppose a consortium with agreed members and shares; and 60 % for the party that supplies the slats of a steel bench, with the maker of the benches at 40 %, is not explained. The qualifying party ("the party qualifying this economic operator") is the operator itself, so the aggregate adds the operator's years and staff, which an expression of interest (a request to be registered and kept informed) does not need. No later example shows the consortium: the sawmill unsubscribes in 10.
- Condition: The expression of interest states a consortium role and share only for a consortium whose members are known; otherwise it says that the operator is interested and, in the note, what it considers.
- Options: (a) Preferred: drop `ParticipationPercent` and both role codes and keep the note. (b) Name the bench maker as a second qualifying party with its share, and make the shares plausible for slats against benches.
- Needs decision: no

### tender/04#F3 · Low · Signature ID with the prefix "HS" in a document of the sender "MS"
- XPath: `/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- XPath: `/ExpressionOfInterestRequest/cbc:ID` = `MS-DOC-26-0190`
- XPath: `10-UnsubscribeFromProcedureRequest.xml:/UnsubscribeFromProcedureRequest/cac:Signature/cbc:ID` = `HS-SIG-UNS`
- Why: Every other signature of the flow is numbered with the prefix its party uses for its documents (PWD, BF, VI, BIS, BLUM). Marrowdale Sawmill numbers its documents `MS-…` but its two signatures `HS-…`; the prefix matches no name in the document and looks left over from another party name.
- Condition: The signature ID uses the same party prefix as the sawmill's other identifiers, or the prefix is explained.
- Options: (a) Preferred: `MS-SIG-EOI` (and `MS-SIG-UNS` in 10). (b) None other seen.
- Needs decision: no

### tender/04#F4 · Low · Customs trader numbers of the parties in an expression of interest
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in an expression of interest is declared to customs, and the sawmill, which never tenders, never ships anything in this flow. They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `DocumentReference` `LPWD-DOC-26-0188` is the contract notice (02), the notice an expression of interest answers; `ContractFolderID`, contract name and lot `LOT-1` agree with 02.
- `ValidityPeriod/EndDate` 2026-02-26 is the tender submission deadline of 02/03; the interest lapses when tenders close.
- `05-ExpressionOfInterestResponse.xml` refers back to this document by its ID and names the same operator, contracting party and lot.

## Considered and refuted
- `/ExpressionOfInterestRequest/cac:ProcurementProject/cbc:Name` = "Park benches" while `ContractName` is the name of the whole project: suspected mismatch — refuted, it is the name of lot 1 in every notice and the request is for lot 1.
- An expression of interest in an open procedure, where nobody needs to be admitted: suspected not to belong — refuted, the definition covers it ("the Contracting Party registers the interest of the Economic Operator sending the relevant information for the tendering process") and the note gives that reason.
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cbc:IndustryClassificationCode` = 1610 (sawmilling) against the required class 3100 (furniture) of the notices: suspected unfit tenderer — refuted, it is exactly why the sawmill looks for a bench maker.

## Outside this review
- The contract notice (02) ends the reception of requests to participate on 2026-02-11; this expression of interest is dated 2026-02-14. Whether that period means anything in an open procedure is a finding of 02.
