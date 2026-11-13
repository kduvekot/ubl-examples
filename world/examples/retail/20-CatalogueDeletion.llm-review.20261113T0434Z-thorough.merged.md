# LLM review: 20-CatalogueDeletion.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/20-CatalogueDeletion.xml`, Git blob `9caf2f1c11c43a13594e547d7c6d563b86a59b49` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/20#F1 · High · The reference to the deleted catalogue gives an issue time, a last revision and a previous version that are not the catalogue's
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionTime` = `09:00:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cbc:IssueTime` = `09:01:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:VersionID` = `1.2`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:PreviousVersionID` = `0.9`
- XPath: `03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cbc:VersionID` = `1.1`
- Why: the reference resolves to 02-Catalogue by ID and UUID and names version 1.2, the version left by 03 (1.1) and 04 (1.2). In a catalogue reference `IssueTime` is "The time at which the catalogue was issued" (02: 17:28; 09:00 is 02's own revision time), and `RevisionDate`/`RevisionTime` "The date/time on which the information in the catalogue was last revised": the last revision is 04, which states a revision of 2026-05-20 14:00 and was issued on 2026-05-21 at 09:01, so 2026-05-21 14:00 is neither (and would lie after 04's issue). `PreviousVersionID` is the version superseded by this one: for 1.2 that is 1.1, not 0.9, which was 1.0's predecessor in 02. All values verified in the merge against 02, 03 and 04; no reading makes them agree. The same reference block, with the same times, occurs in 03 and 04 (merger a's examples).
- Condition: the reference describes the catalogue as it stands (version 1.2) consistently with 02, 03 and 04: 02's issue date and time, the revision date and time of version 1.2, previous version 1.1.
- Options: (a, preferred) correct the values together with 03 and 04 (IssueTime `17:28:00`, revision as stated by 04, PreviousVersionID `1.1`); (b) reduce the reference to ID, UUID, issue date and version, which is enough to identify what is deleted (context preferred this).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### retail/20#F2 · Medium · A language code in LocaleCode
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 364 occurrences in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F3), parties (F1), context (F2)

### retail/20#F3 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is a vehicle entrance, not a street name. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address; (b) record it in Bayvarra's address format (finding then dismissed).
- Needs decision: no
- From: broad (F4), parties (F2)

### retail/20#F4 · Low · Two statements of when the deletion takes effect
- XPath: `/CatalogueDeletion/cac:ValidityPeriod/cbc:EndDate` = `2026-06-19`
- XPath: `/CatalogueDeletion/cbc:EffectiveDate` = `2026-06-20`
- XPath: `/CatalogueDeletion/cbc:EffectiveTime` = `00:00:00`
- Why: `EffectiveDate`/`EffectiveTime` are "The effective date, assigned by the seller, on which the Catalogue expires": midnight at the start of 20 June. `ValidityPeriod` is "The period during which the Deletion of the catalogue becomes effective. This may be given as start (after date) and end dates (before date)": an end date of 19 June says the deletion becomes effective before or on 19 June. The broad part called this a contradiction (High). The merge tried to refute it: an end date of 19 June, taken as inclusive, ends at the instant 2026-06-20 00:00, which is exactly the effective time (the logistics part read it so and found it consistent); taken as "before date", the deletion would take effect before the expiry it announces. Both readings are possible, so the two elements are at best redundant and at worst a day apart; that is a consistency remark, not a proven contradiction, hence Low.
- Condition: the document states one moment at which the catalogue ends, or two statements that agree under any reading.
- Options: (a, preferred) keep `EffectiveDate`/`EffectiveTime` and drop the `ValidityPeriod`; (b) a validity period that starts on 2026-06-20.
- Needs decision: no
- From: broad (F2), context (F3); logistics (Checked and consistent)

### retail/20#F5 · Low · A signature without signature content
- XPath: `/CatalogueDeletion/cac:Signature/cbc:ID` = `LD-SIG-26-0619`
- Why: the signature has only an ID and a signatory party, no method, value or attachment, so it signs nothing. The earlier flows and retail a/b treat this convention (137 of 147 Signature aggregates, count by the air merge, lxml) as one decision.
- Condition: a signature carries what makes it one, or is absent.
- Options: (a, preferred) drop it; (b) complete it.
- Needs decision: yes
- From: context (F4, part)

### retail/20#F6 · Low · Brightmarket's contact: name, job title and department disagree
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: as receiver of a catalogue withdrawal the buying office fits the role (both parts agree), but its job title and department are those of a seller's customer service, which contradicts the name. The same contact is used for Brightmarket in every role in the flow (41 XML files with `<cbc:Name>Buying office</cbc:Name>`, parties part).
- Condition: name, job title and department agree with each other and with the role.
- Options: (a, preferred) a buyer's job title and purchasing department for the buying office; (b) role-specific contacts per document.
- Needs decision: no
- From: broad (F5), parties (F5)

### retail/20#F7 · Low · Party master data the catalogue deletion does nothing with
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueDeletion/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/CatalogueDeletion/cac:ProviderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: a catalogue withdrawal uses no logo, consumer web shop or social-media profile, no share capital, no customs trader number (domestic flow without customs) and no tax registrations (it has no tax content) (section 4.8, IND5/IND6). `CorporateStockAmount` is also defined as "The number of shares in the capital stock of a corporation" while its data type is an amount: a TC write-up note; the parties part's "Needs decision: yes" set to no, as retail a/b.
- Condition: the parties carry only data the deletion uses.
- Options: (a, preferred) leave them out of this document.
- Needs decision: no
- From: parties (F3, F4, F6), context (F4, part)

## Checked and consistent
- `DeletedCatalogueReference` ID `LD-CAT-26-0218` and UUID `f5163e36-0159-5b9f-b172-a86137e369e6` match 02; `VersionID` 1.2 is the version after 04 (verified).
- `ReferencedContract` `LD-BM-SUPPLY-2026`, provider, receiver, seller and contractor customer agree with 02.
- Effective on 2026-06-20 00:00, seven hours after the issue (2026-06-19 17:05) and before the catalogue's own validity end (`02-Catalogue.xml:/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2026-07-19`), explained by the note ("Replaced by the summer catalogue."); no trade order of the flow relies on the catalogue after that date (the last, 08, is from 2026-04-24; 22 is a consumer order to the store).
- GS1 keys pass `check_ids.py` (rerun); party descriptions are identical in every example of the flow (parties).

## Considered and refuted
- `/CatalogueDeletion/cbc:Note`: "Replaced by the summer catalogue", which no example carries — refuted, a note about a later catalogue outside the flow needs no example of its own (from context).
- `/CatalogueDeletion/cac:ProviderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted, the definition fits a business park (from parties).

## Changed in the merge
- broad/F2 (High), context/F3 (Low) → F4: Low; the end date read as inclusive ends at the effective instant (logistics' reading), so the contradiction is not proven; redundancy remains.
- context/F4 → F5 and F7: split (signature / master data); the signature set to "Needs decision: yes", aligned with retail a/b, air and utilities.
- parties/F3, F4, F6 and context/F4 (party part) → F7: one copied-master-data finding; the tax schemes added from context, as retail a/b; parties/F4's "yes" set to no.
- broad/F5, parties/F5 → F6: grouped.
- context/F2 option order: drop preferred.

## Outside this review
- The same wrong reference values (issue time 09:00, revision 2026-05-21 14:00, previous version 0.9) in 03 and 04, and 04's own revision time (2026-05-20 14:00) against 03's issue (2026-05-20 13:10) and 04's issue (2026-05-21 09:01), are for the reviews of 03 and 04.
