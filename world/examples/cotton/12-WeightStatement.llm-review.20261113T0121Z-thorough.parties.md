# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/12-WeightStatement.xml`, Git blob `63cbeb9c6ff2202636e981ef15d7262f47f2a1a5` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### cotton/12#F1 · Medium · The shipper named as the party signing the VGM on its own behalf
- XPath: `/WeightStatement/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/WeightStatement/cac:ShipperParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- Why: `cac:ResponsibleParty` is "The Party who signs the Verified Gross Mass (VGM) on behalf of the Shipper." The definition presupposes someone other than the shipper (SOLAS VI/2 allows a person duly authorised by the shipper to sign, my own knowledge). Here it is the shipper itself, so the role says nothing the `ShipperParty` and the signature (`/WeightStatement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`) do not already say; it is the same pattern as a payer equal to the debtor.
- Condition: `cac:ResponsibleParty` is absent, or names a party other than the shipper that signs the VGM for it.
- Options: (a, preferred) drop `cac:ResponsibleParty`, since the ginnery signs its own VGM; (b) if someone signs for it (e.g. the forwarder Bayforth or the port's weighing station), name that party.
- Needs decision: no

### cotton/12#F2 · Medium · Language code in `LocaleCode`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/12#F3 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the shipper declaring the verified gross mass of a packed container to the carrier; the contact the carrier needs is the shipping or despatch desk, not cotton sales.
- Condition: The ginnery's contact in this role is shipping or despatch, or the contact is left out.
- Options: (a, preferred) use a contact for shipping or despatch; (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/12#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/WeightStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/12#F5 · Low · Party master data the document does not use
- XPath: `/WeightStatement/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: Section 4.8 (presence): the ginnery's customs trader number is present. A VGM declaration to the carrier is not a customs filing, and it does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- Sender and shipper are the ginnery, which packed the container; receiver is the carrier Tidewell Ocean Lines, as in 13; weighing party is the Port of Selanu, whose physical location carries UN/LOCODE `XLSEL`.
- Tidewell's full description is identical in 12, 13, 14 and 17 (compared block by block); the ginnery's is identical to 01 and 11.

## Considered and refuted
- `/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Port of Selanu Ltd`: suspected because a port operator described as a small limited company — refuted, a port operated by a company is common and a weighing station needs no public status.
