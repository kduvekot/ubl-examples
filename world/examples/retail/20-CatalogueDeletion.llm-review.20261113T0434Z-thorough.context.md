# LLM review: 20-CatalogueDeletion.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/20-CatalogueDeletion.xml`, Git blob `9caf2f1c11c43a13594e547d7c6d563b86a59b49` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### retail/20#F1 · High · Reference to the deleted catalogue gives an issue time and a last revision that are not the catalogue's
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- Why: in CatalogueReference, IssueTime is "The time at which the catalogue was issued" (17:28, not
  09:00, which is the catalogue's own revision time) and RevisionDate/Time "The date/time on which the
  information in the catalogue was last revised". The last revision, version 1.2, is
  04-CatalogueItemSpecificationUpdate.xml, which gives 2026-05-20 14:00 as its revision and was issued
  on 2026-05-21 at 09:01; 2026-05-21 14:00 is neither. The same wrong values appear in 03 and 04.
- Condition: the reference gives the catalogue's issue time and the revision date/time that the
  1.2 update states (with that update's own revision time consistent with its issue).
- Options: correct the values together with 03 and 04, or reduce the reference to ID, UUID, issue date
  and version (preferred, enough to identify what is deleted).
- Needs decision: no

### retail/20#F2 · Medium · A language code in LocaleCode
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID
  `ISO 639` is a language code (213 examples, `grep -l` over `*.xml`).
- Condition: a locale code, or none.
- Options: `en-XB` (preferred), or drop it.
- Needs decision: no

### retail/20#F3 · Low · Two statements of when the deletion takes effect
- XPath: `/CatalogueDeletion/cac:ValidityPeriod/cbc:EndDate` = `2026-06-19`
- XPath: `/CatalogueDeletion/cbc:EffectiveDate` = `2026-06-20`
- XPath: `/CatalogueDeletion/cbc:EffectiveTime` = `00:00:00`
- Why: EffectiveDate/Time are "The effective date/time, assigned by the seller, on which the Catalogue
  expires": midnight at the start of 20 June. ValidityPeriod is "The period during which the Deletion
  of the catalogue becomes effective … start (after date) and end dates (before date)": an end date of
  19 June says the deletion takes effect before 19 June. Read by the definitions, the two differ by a
  day; one of them is redundant at best.
- Condition: the document states one moment at which the catalogue ends, or two statements that agree.
- Options: keep EffectiveDate/Time and drop the ValidityPeriod (preferred).
- Needs decision: no

### retail/20#F4 · Low · Signature and master data the deletion does nothing with
- XPath: `/CatalogueDeletion/cac:Signature/cbc:ID` = `LD-SIG-26-0619`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the signature has only an ID and a signatory; a catalogue withdrawal uses no customs trader
  number, share capital, tax schemes or social media (IND5/IND6).
- Condition: everything present has a use.
- Options: drop them.
- Needs decision: no

## Checked and consistent
- DeletedCatalogueReference ID, UUID, issue date and version `1.2` match 02 and the last update 04;
  ReferencedContract and the parties match 02.
- The deletion takes effect (2026-06-20) before the catalogue's own validity ends (2026-07-19) and
  after the orders placed on it.

## Considered and refuted
- `/CatalogueDeletion/cbc:Note`: "Replaced by the summer catalogue", which no example carries —
  refuted because a note about a later catalogue outside the flow needs no example of its own.
