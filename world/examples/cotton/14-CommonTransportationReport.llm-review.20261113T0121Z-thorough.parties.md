# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/14-CommonTransportationReport.xml`, Git blob `081267759b51366ff3d8aad9d0f0d1d2385f1b91` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/14#F1 · Medium · Language code in `LocaleCode`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/14#F2 · Low · The port authority described as a small private limited company
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Port of Lumeport Ltd`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Limited company (private)`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlExemptionDocumentReference/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: `cac:AuthorityParty` is "The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator." The Port of Lumeport receives the pre-arrival report with its security and health declarations, and issued the ship's sanitation control exemption certificate, which under the International Health Regulations (Art. 39, Annex 3; my own knowledge) is issued by the competent health authority of an authorised port. It is described as a private limited company of small size with a commercial registration. A port authority run as a company exists in practice, but a small private company acting as health and security authority for a container port is hard to reconcile with those roles; whether the world's ports are public authorities or companies is a question of the story.
- Condition: The party receiving the report and issuing the sanitation certificate is described as the kind of body that has those powers in the world (a port or port health authority), with a size that fits a container port.
- Options: (a, preferred) decide in the story whether the Port of Lumeport is a public port authority; if so describe it like the other authorities, if not name the authority (e.g. a port health authority) that receives the report and issued the certificate; (b) keep the company and give it a size that fits.
- Needs decision: yes

### cotton/14#F3 · Low · Arrival contacts reachable only on weekday office hours
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The checklist: an authority's contact is reachable when ships arrive. A contact `Note` is "a textual description of the circumstances under which this contact can be used"; port control is given as reachable on weekdays from 08:00 to 17:00 only, and the reporting carrier's contact is its bookings desk with the same hours, although the report announces an arrival and asks for a veterinary visit on arrival. Ships arrive at any hour; neither contact fits the purpose of a pre-arrival report.
- Condition: The authority's and the reporter's contacts in a pre-arrival report are ones that can be reached around the ship's arrival (e.g. a 24-hour port control and the carrier's operations or the ship's agent).
- Options: (a, preferred) port control around the clock and the carrier's operations desk; (b) drop the hours note if the hours are not known.
- Needs decision: no

### cotton/14#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- Reporter and sender are the carrier Tidewell Ocean Lines; authority and receiver are the Port of Lumeport, whose physical location carries UN/LOCODE `XBLMP`; Tidewell's full description is identical to 12, 13 and 17 (compared block by block).
- The ISSC issuer is the Maritime Administration of Bayvarra, the flag state's administration for a Bayvarran-flagged ship, which fits ISPS A/19.4 (interim certificate by the administration).
- The reporting person is the master, which fits the role code `MASTER`.

## Outside this review
- The Port of Lumeport's coordinates (40°1.20'S 15°12.60'W) and the Port of Selanu's in 12-WeightStatement.xml (40°1.20'S 15°8.40'W) put the two ports about 6 km apart on the same parallel, although one is on the island and the voyage is a sea leg; a map question across documents.
