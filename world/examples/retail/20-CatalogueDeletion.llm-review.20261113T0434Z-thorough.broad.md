# LLM review: 20-CatalogueDeletion.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/20-CatalogueDeletion.xml`, Git blob `9caf2f1c11c43a13594e547d7c6d563b86a59b49` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 31131c2 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### retail/20#F1 · High · Reference to the deleted catalogue disagrees with the catalogue and its updates
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:VersionID` = `1.2`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:PreviousVersionID` = `0.9`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:VersionID` = `1.1`
- Why: the reference resolves to 02-Catalogue (ID, UUID), now at version 1.2 after 03 (1.1) and 04 (1.2). But its issue time is not 02's (17:28 against 09:00); its last revision (2026-05-21 14:00) is neither that of version 1.2 as given by 04 (2026-05-20 14:00) nor before 04's issue (2026-05-21 09:01); and for version 1.2 the previous version is 1.1, not 0.9, which was the predecessor of version 1.0. The same reference block, with its wrong times, occurs in 03 and 04.
- Condition: the reference describes the catalogue as it stands (version 1.2) consistently with 02, 03 and 04: issue date and time of 02, revision date and time of version 1.2, previous version 1.1.
- Options: (a, preferred) correct the values; (b) keep only ID, UUID and version.
- Needs decision: no

### retail/20#F2 · High · The deletion's validity ends before the catalogue expires
- XPath: `/CatalogueDeletion/cac:ValidityPeriod/cbc:EndDate` = `2026-06-19`
- XPath: `/CatalogueDeletion/cbc:EffectiveDate` = `2026-06-20`
- XPath: `/CatalogueDeletion/cbc:EffectiveTime` = `00:00:00`
- Why: `ValidityPeriod` is "The period during which the Deletion of the catalogue becomes effective. This may be given as start (after date) and end dates (before date)"; `EffectiveDate`/`Time` is "The effective date, assigned by the seller, on which the Catalogue expires". The catalogue expires at 2026-06-20 00:00, but the period in which the deletion becomes effective ends on 2026-06-19, so by its own validity the deletion would have to take effect before the expiry it announces. The two express the same moment differently and disagree.
- Condition: the validity period and the effective date and time describe the same moment (or only one of them is given).
- Options: (a, preferred) drop the validity period and keep the effective date and time; (b) a validity period starting on 2026-06-20.
- Needs decision: no

### retail/20#F3 · Medium · Language codes in LocaleCode
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/20#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/20#F5 · Low · Brightmarket's contact: buying office, customer service officer and sales at once
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. As the receiver of a catalogue withdrawal the buying office fits the role. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail (compared by script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of the contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office, or a contact fitting this role; (b) different contacts per role, if the world gives Brightmarket several.
- Needs decision: no

## Checked and consistent
- The deleted catalogue `LD-CAT-26-0218` (ID and UUID) is 02-Catalogue; contract `LD-BM-SUPPLY-2026`, provider, receiver, seller and contractor customer agree with 02.
- The withdrawal on 2026-06-20 lies before the catalogue's own end of validity (2026-07-19), explained by the note ("Replaced by the summer catalogue."); the summer catalogue lies outside the flow.
- `VersionID` `1.2` is the version left by 04-CatalogueItemSpecificationUpdate.
