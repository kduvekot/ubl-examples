# LLM review: 03-CataloguePricingUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/03-CataloguePricingUpdate.xml`, Git blob `fa746f7555ca2bc6ffeef41cf02e3ca5ac1ffe9d` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/03#F1 · High · The update line points to the bench line, but the document updates the side frame
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cbc:ID` = `1`
- XPath: `/CataloguePricingUpdate/cbc:Name` = `Price change of the side frame`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:Item/cbc:Name` = `Bench side frame casting`
- Why: `CataloguePricingUpdateLine/ID` is "An identifier for the catalogue line to be updated", and the line carries no item, so the ID is the only link to what is repriced. Line 1 of the related catalogue is the bench (520 per each); the side frame is line 2 (64 per each). As encoded, the update sets the bench's price to 58, while name and description say the side frame's price changes. The new price of 58 only makes sense for the side frame.
- Condition: the pricing update line's ID is the ID of the side frame's line in 02-Catalogue.
- Options: (a, preferred) line ID `2`; (b) if the bench was meant, change name, description and price accordingly; the price of 58 makes (a) the likely intent.
- Needs decision: no

### retail/03#F2 · High · Revision time after the issue time
- XPath: `/CataloguePricingUpdate/cbc:IssueTime` = `13:10:00`
- XPath: `/CataloguePricingUpdate/cbc:RevisionDate` = `2026-05-20`
- XPath: `/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- Why: `RevisionDate`/`RevisionTime` are "The date/time, assigned by the seller, on which the Catalogue was revised". The document is issued on 2026-05-20 at 13:10 and states a revision at 14:00 the same day, i.e. after it was issued.
- Condition: the revision date and time are not later than the issue date and time.
- Options: (a, preferred) a revision time before 13:10 (or drop the revision time); (b) a later issue time.
- Needs decision: no

### retail/03#F3 · High · Reference to the catalogue disagrees with the catalogue and lies in the future
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionDate` = `2026-04-20`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionTime` = `09:00:00`
- Why: the reference resolves to 02-Catalogue (same ID and UUID), but gives its issue time as 09:00 (02 was issued at 17:28; 09:00 is 02's revision time) and its last revision as 2026-05-21 14:00, which is neither 02's revision (2026-04-20 09:00) nor possible: it is the day after this document was issued (2026-05-20 13:10).
- Condition: issue and revision date and time in the reference equal those of 02-Catalogue (or of the catalogue version as it stood before this update), and none lies after this document's issue.
- Options: (a, preferred) copy them from 02-Catalogue; (b) drop the dates and keep ID, UUID and version.
- Needs decision: no

### retail/03#F4 · Medium · Language codes in LocaleCode
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats the language code of `Language/cbc:ID`. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it.
- Needs decision: no

### retail/03#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CataloguePricingUpdate/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a business park gate is a vehicle access detail, not a street name. The value occurs in 76 examples.
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give it where vehicles need it; (b) record it in Bayvarra's address format if it is really part of the postal address.
- Needs decision: no

### retail/03#F6 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CataloguePricingUpdate/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: name, job title and department contradict each other; a buyer's contact is not a seller's customer service. The same contact is used for Brightmarket in all 19 retail examples that describe it.
- Condition: name, job title and department agree with each other and with the buying role.
- Options: (a, preferred) buyer's job title and purchasing department.
- Needs decision: no

### retail/03#F7 · Low · Header parties repeated on the line
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:ContractorCustomerParty`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:SellerSupplierParty`
- Why: the line's parties are the header's; on a line they are only informative where they differ (no-filler rule).
- Condition: line-level parties are present only where they differ from the header.
- Options: (a, preferred) drop them.
- Needs decision: no

### retail/03#F8 · Low · The bench's price list is replaced, but only the side frame gets a new price
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cac:PreviousPriceList/cbc:StatusCode` = `REPLACED`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`
- Why: the update marks price list `LD-PL-2026` as replaced by `LD-PL-2026-2`. In 02-Catalogue that list also holds the bench's price, which this update does not touch; after the update the bench's price sits in a list that is said to be replaced, and nothing says it carries over to the new list.
- Condition: after the update, every price in force belongs to a price list that is active.
- Options: (a, preferred) mark the previous list as superseded only for this line (e.g. a status meaning "partly replaced") or describe in a note that the other prices carry over; (b) give the side frame's new price without a new price list.
- Needs decision: no

## Checked and consistent
- The related catalogue reference resolves to 02-Catalogue: ID `LD-CAT-26-0218`, UUID, issue date, version `1.0` and previous version `0.9` agree.
- Contract `LD-BM-SUPPLY-2026` and the parties agree with 02-Catalogue; Brightmarket and Lumeway are described as in every retail example.
- Validity 2026-05-20 to 2026-07-19 lies within the catalogue's validity (to 2026-07-19); the new price list has the same validity.
- `VersionID` `1.1` follows the catalogue's `1.0`, and 04-CatalogueItemSpecificationUpdate continues with `1.2`.
- `LineCountNumeric` `1` matches the single line.

## Considered and refuted
- `/CataloguePricingUpdate/cac:TradingTerms/cbc:Information` = `Unchanged.`: suspected filler — refuted because stating that the terms stay as they are is information (and avoids implying it by absence).
- `/CataloguePricingUpdate/cbc:Description` = `Price change of the side frame`: suspected duplicate of the name without information — refuted: harmless repetition of a short name; no meaning conflict.
- `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`: suspected to conflict with the dependent price of 02 (12.31 % of the bench) — refuted: a pricing update may replace a dependent price by a fixed one.
